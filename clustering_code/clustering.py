
# coding: utf-8

# In[1]:

from parsetrees.expr_parser import webwork_parser
from parsetrees.expr_parser import Eval_parsed
import pickle
from collections import defaultdict
import cluster_functions
from itertools import combinations
from datetime import datetime as dt

def cluster(Week, problem_id):
    ### Load data ###
    data = pickle.load(open('../2015data/'+Week+'_data.pkl','rb'))
    data_timestamp = pickle.load(open('../2015data/'+Week+'_correct_timestamp.pkl','rb'))


    ### Make params as inputs to function find_matches ###
    params = defaultdict(list)
    for (pro, par) in data.keys():
        if pro == problem_id and \
        data[(pro,par)][0]['answer'] != '<pre style="text-align:left; padding-left:.2em">yes</pre>' and \
        data[(pro,par)][0]['answer'] != '<pre style="text-align:left; padding-left:.2em">no</pre>':
            params[par] = cluster_functions.make_params(pro, par, data)

    ### Create clusters, if no hits, clustered as 'Nothing' ###
    problem_clusters = {}
    no_match_clusters = {}
    for part in params:
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
                if att * ans < 0:
                    problem_clusters[part]['Wrong_Sign'] += [(p['answer'], p['attempt'])]
                    continue
                elif float(ans).is_integer() and not float(att).is_integer():
                    problem_clusters[part]['Fraction'] += [(p['answer'], p['attempt'])]
                    continue
            final_pairs = cluster_functions.find_matches(p)
            if len(final_pairs)>0:
                sorted_final = sorted(final_pairs,key=lambda x: x[0])
                sorted_node = [s[0] for s in sorted_final]
                problem_clusters[part][str(sorted_node)] += [(p['answer'], p['attempt'], sorted_final)]
            else:
                if p['attempt'].isdigit() or len(p['att_tree']) == 1:
                    problem_clusters[part]['Digits'] += [(p['answer'], p['attempt'])]
                else:
                    no_match += [(p['answer'], p['attempt'], p['att_tree'], p['user_id'], p['user_var'], p['timestamp'])]

        ## Cluster no match
        no_match_cluster = {}
        dependency_list_input = raw_input('What parts are prerequisite for part' + str(part) + ':')
        dependency_list = [i for i in dependency_list_input.split()]
        print 'part' + str(part) + ' depends on ', dependency_list
        user_id = ''
        for n in no_match:
            time = dt.strptime(n[-1], "%Y-%m-%d %H:%M:%S")
            # we create one signature 'redirect'
            # that the hints should redirect students to previous parts
            if part == '1' and user_id != n[3]:
                user_id = n[3]
                ini_time_str = n[-1]
            if part != '1':
                user_id = n[3]
                ## Some students didn't complete part 1, need to check all the way to the current part
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
                problem_clusters[part]['redirect'].append(n)
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
        no_match_clusters[part] = no_match_cluster
    return problem_clusters, no_match_clusters



if __name__ == '__main__':
    Week = raw_input('Assignment Name:')
    problem_id = raw_input('Problem ID:')
    problem_clusters, no_match_clusters = cluster(Week, problem_id)
    pkl_dir = 'clusters/' + Week + '/'
    pickle.dump(problem_clusters, open(pkl_dir + Week + '_' + problem_id + '_cluster.pkl','wb'))
    print 'clusters pickel file for ', Week, ' ', problem_id, ' is generated in ', pkl_dir
    pickle.dump(no_match_clusters, open(pkl_dir + Week + '_' + problem_id + '_no_match_cluster.pkl','wb'))
    print 'no_match_cluster pickel file for ', Week, ' ', problem_id, ' is generated in ', pkl_dir
