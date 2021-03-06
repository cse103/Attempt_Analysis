
# coding: utf-8

# In[1]:
import sys
sys.path.append('..')
from parsetrees.expr_parser import webwork_parser
from parsetrees.expr_parser import Eval_parsed
import pickle
from collections import defaultdict
import cluster_functions
from itertools import combinations
from datetime import datetime as dt
from datetime import timedelta as td

def format_cluster(n, part):
    time = dt.strptime(n[-1], "%Y-%m-%d %H:%M:%S")
    # we create one signature 'redirect'
    # that the hints should redirect students to previous parts
    if part == '1' and user_id != n[3]:
        user_id = n[3]
        ini_time_str = n[-1]
    if part != '1':
        user_id = n[3]
        ## Some students didn't complete part 1, need to check all parts before the current part
        k = 1
        while str(k) != part and not data_timestamp[user_id][(problem_id, str(k))]:
            k += 1
        if str(k) == part:
            ini_time_str = n[-1]
        else:
            ini_time_str = data_timestamp[user_id][(problem_id, str(k))][1]
    ini_time = dt.strptime(ini_time_str, "%Y-%m-%d %H:%M:%S")

    dependency_timestamp = [dt.strptime(data_timestamp[user_id][(problem_id, d)][1], "%Y-%m-%d %H:%M:%S") for d in dependency_list if data_timestamp[user_id][(problem_id, d)]]
    if any(time < t for t in dependency_timestamp):
        problem_clusters[part]['redirect'].append((n[0],n[1]))
    else:
        if not user_id in no_match_cluster:
            no_match_cluster[user_id] = {'first_attempt':ini_time_str}
            for d in dependency_list+[part]:
                if data_timestamp[user_id][(problem_id, d)]:
                    correct_attempt = data_timestamp[user_id][(problem_id, d)][0]
                    t = dt.strptime(data_timestamp[user_id][(problem_id, d)][1], "%Y-%m-%d %H:%M:%S")
                    key = 'part' + str(d) + '_correct_attempt'
                    no_match_cluster[user_id][key] = [str(t-ini_time), correct_attempt]
            t = dt.strptime(n[-1], "%Y-%m-%d %H:%M:%S")
            no_match_cluster[user_id]['part'+str(part)+'_incorrect_attempt'] = [(str(t-ini_time), n[1])]
        else:
            t = dt.strptime(n[-1], "%Y-%m-%d %H:%M:%S")
            no_match_cluster[user_id]['part'+str(part)+'_incorrect_attempt'] += [(str(t-ini_time), n[1])]

def cluster(Week, problem_id, part_id='', var=False):
    ## We only care about attempts after 3 minutes in nothing cluster
    min_diff = 3
    ### Load data ###
    data = pickle.load(open('../../2016data/'+Week+'_data.pkl','rb'))
    data_timestamp = pickle.load(open('../../2016data/'+Week+'_correct_timestamp.pkl','rb'))


    ### Make params as inputs to function find_matches ###
    params = defaultdict(list)
    for (pro, par) in data.keys():
        if part_id != '' and par != part_id:
            continue
        if pro == problem_id and \
        data[(pro,par)][0]['answer'] != '<pre style="text-align:left; padding-left:.2em">yes</pre>' and \
        data[(pro,par)][0]['answer'] != '<pre style="text-align:left; padding-left:.2em">no</pre>':
            params[par] = cluster_functions.make_params(pro, par, data)

    ### Create clusters, if no hits, clustered as 'Nothing' ###
    problem_clusters = {}
    no_match_clusters = {}
    for part in params:
        if len(params[part]) == 0:
            continue
        problem_clusters[part]=defaultdict(list)
        no_match = []
        for p in params[part]:
            if len(p['att_tree']) > 1:
                if p['att_tree'][0] == 'X':
                    att = p['att_tree'][1]
                else:
                    att = p['att_tree'][0][1]
                if p['ans_tree'][0] == 'X':
                    ans = p['ans_tree'][1]
                else:
                    ans = p['ans_tree'][0][1]
                convert_fail = False
                if att == None:
                    print "Not correct type"
                    continue
                try:
                    float(att)
                except OverflowError:
                    print "Can't convert to float"
                    convert_fail = True
                if not convert_fail and att * ans < 0:
                    problem_clusters[part]['Wrong_Sign'] += [(p['answer'], p['attempt'])]
                    continue
                elif not convert_fail and float(ans).is_integer() and not float(att).is_integer():
                    problem_clusters[part]['Fraction'] += [(p['answer'], p['attempt'])]
                    continue
            if var:
                final_pairs = cluster_functions.find_matches_w_variables(p['answer'], p['attempt'], var)
            else:
                final_pairs = cluster_functions.find_matches(p)
            if len(final_pairs)>0:
                sorted_final = sorted(final_pairs,key=lambda x: x[0])
                sorted_node = [s[0] for s in sorted_final]
                if var:
                    err = cluster_functions.show_matching_group_w_variables(p['answer'], p['attempt'], var)
                    problem_clusters[part][str(sorted_node)] += [(p['answer'], p['attempt'], err, p['user_id'], p['user_var'], p['timestamp'])]
                else:
                    problem_clusters[part][str(sorted_node)] += [(p['answer'], p['attempt'], sorted_final, p['user_id'], p['user_var'], p['timestamp'])]
            else:
                if p['attempt'].isdigit() or len(p['att_tree']) == 1:
                    problem_clusters[part]['Digits'] += [(p['answer'], p['attempt'])]
                else:
                    no_match += [(p['answer'], p['attempt'], p['att_tree'], p['user_id'], p['user_var'], p['timestamp'])]

        ## Cluster no match
        no_match_cluster = {}
        #dependency_list_input = raw_input('What parts are prerequisite for part' + str(part) + ':(seperate with space)')
        dependency_list = []#[i for i in dependency_list_input.split()]
        #print 'part' + str(part) + ' depends on ', dependency_list
        user_id = ''
        for n in no_match:
            if n[-1] != 'null':
                time = dt.strptime(n[-1], "%Y-%m-%d %H:%M:%S")
            else:
                continue
            # we create one signature 'redirect'
            # that the hints should redirect students to previous parts
            if part == '1' and user_id != n[3]:
                user_id = n[3]
                ini_time_str = n[-1]
            if part != '1':
                user_id = n[3]
                if user_id not in data_timestamp.keys():
                    continue
                ## Some students didn't complete part 1, need to check all the way to the current part
                k = 1
                while str(k) != part and (problem_id, str(k)) not in data_timestamp[user_id].keys():
                    k += 1
                if str(k) == part:
                    ini_time_str = n[-1]
                else:
                    ini_time_str = data_timestamp[user_id][(problem_id, str(k))][1]
            ini_time = dt.strptime(ini_time_str, "%Y-%m-%d %H:%M:%S")

            dependency_timestamp = [dt.strptime(data_timestamp[user_id][(problem_id, d)][1], "%Y-%m-%d %H:%M:%S") for d in dependency_list if data_timestamp[user_id][(problem_id, d)]]
            if any(time < t for t in dependency_timestamp):
                problem_clusters[part]['redirect'].append((n[0],n[1]))
            else:
                if not user_id in no_match_cluster:
                    no_match_cluster[user_id] = {'first_attempt':ini_time_str}
                    for d in dependency_list+[part]:
                        if user_id in data_timestamp.keys() and (problem_id, d) in data_timestamp[user_id].keys():
                            correct_attempt = data_timestamp[user_id][(problem_id, d)][0]
                            t = dt.strptime(data_timestamp[user_id][(problem_id, d)][1], "%Y-%m-%d %H:%M:%S")
                            key = 'part' + str(d) + '_correct_attempt'
                            no_match_cluster[user_id][key] = [str(t-ini_time), correct_attempt]
                    t = dt.strptime(n[-1], "%Y-%m-%d %H:%M:%S")
                    no_match_cluster[user_id]['part'+str(part)+'_incorrect_attempt'] = [(str(t-ini_time), n[1])]
                else:
                    t = dt.strptime(n[-1], "%Y-%m-%d %H:%M:%S")
                    no_match_cluster[user_id]['part'+str(part)+'_incorrect_attempt'] += [(str(t-ini_time), n[1])]

        ## Remove attempts within min_diff defined at the top
        updated_cluster = {}
        for user in no_match_cluster:
            last_att_time = no_match_cluster[user]['part'+str(part)+'_incorrect_attempt'][-1][0]
            if 'day' not in last_att_time:
                t = dt.strptime(last_att_time, "%H:%M:%S")
                time_diff = td(hours=t.hour, minutes=t.minute, seconds=t.second)
                if time_diff.total_seconds() < 60 * min_diff:
                    print 'remove user:', no_match_cluster[user]
                    continue
            updated_cluster[user] = no_match_cluster[user]
        no_match_clusters[part] = no_match_cluster
    return problem_clusters, no_match_clusters



if __name__ == '__main__':
    Week = raw_input('Assignment Name:')
    problem_ids = raw_input('Problem ID(seperate with space):')
    problem_ids = [i for i in problem_ids.split()]
    for problem_id in problem_ids:
        #part_id = raw_input('Part ID:')
        #if part_id:
        #    print 'selected part ', part_id
        #    problem_clusters, no_match_clusters = cluster(Week, problem_id, part_id)
        #else:
        problem_clusters, no_match_clusters = cluster(Week, problem_id)
        pkl_dir = '2016_clusters/{0}/pkl_files/'.format(Week)
        pickle.dump(problem_clusters, open(pkl_dir + Week + '_' + problem_id + '_cluster.pkl','wb'))
        print 'clusters pickel file for ', Week, ' ', problem_id, ' is generated in ', pkl_dir
        pickle.dump(no_match_clusters, open(pkl_dir + Week + '_' + problem_id + '_no_match_cluster.pkl','wb'))
        print 'no_match_cluster pickel file for ', Week, ' ', problem_id, ' is generated in ', pkl_dir
