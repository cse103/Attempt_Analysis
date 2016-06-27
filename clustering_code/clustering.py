
# coding: utf-8

# In[1]:

from parsetrees.expr_parser import webwork_parser
from parsetrees.expr_parser import Eval_parsed
import pickle
from collections import defaultdict
import cluster_functions
from itertools import combinations

def cluster(Week, problem_id):
    ### Load data ###
    data = pickle.load(open('../2015data/'+Week+'_data.pkl','rb'))

    ### Make params as inputs to function find_matches ###
    params = defaultdict(list)
    for (pro, par) in data.keys():
        if pro == problem_id and \
        data[(pro,par)][0]['answer'] != '<pre style="text-align:left; padding-left:.2em">yes</pre>' and \
        data[(pro,par)][0]['answer'] != '<pre style="text-align:left; padding-left:.2em">no</pre>':
            params[par] = cluster_functions.make_params(pro, par, data)

    ### Create clusters, if no hits, clustered as 'Nothing' ###
    problem_clusters={}
    for part in params:
        problem_clusters[part]=defaultdict(list)
        for p in params[part]:
            final_pairs = cluster_functions.find_matches(p)
            if len(final_pairs)>0:
                sorted_final = sorted(final_pairs,key=lambda x: x[0])
                sorted_node = [s[0] for s in sorted_final]
                problem_clusters[part][str(sorted_node)] += [(p['answer'], p['attempt'], sorted_final)]
            else:
                if p['attempt'].isdigit():
                    problem_clusters[part]['Digits'] += [(p['answer'], p['attempt'], 'digit')]
                else:
                    problem_clusters[part]['Nothing'] += [(p['answer'], p['attempt'], p['att_tree'], p['user_id'])]

        # Cluster Nothing
        nothing_clusters = defaultdict(list)
        initial_nothing = problem_clusters[part]['Nothing'][:]
        for (i, j) in combinations(problem_clusters[part]['Nothing'], 2):
            tmp = {'user_id':j[3], 'answer':i[1], 'attempt':j[1],
                                'ans_tree':i[2][:], 'att_tree':j[2][:]}
            matches = cluster_functions.find_matches(tmp)
            if len(matches) > 0:
                sorted_final = sorted(matches,key=lambda x: x[0])
                sorted_node = [s[0] for s in sorted_final]
                if not (i[1], i[3]) in nothing_clusters[str(sorted_node)]:
                    nothing_clusters[str(sorted_node)] += [(i[1], i[3])]
                    if i in initial_nothing:
                        initial_nothing.remove(i)
                if not (j[1], j[3]) in nothing_clusters[str(sorted_node)]:
                    nothing_clusters[str(sorted_node)] += [(j[1], j[3])]
                    if j in initial_nothing:
                        initial_nothing.remove(j)
        problem_clusters[part]['Nothing_clusters'] = nothing_clusters
        problem_clusters[part]['Nothing'] = initial_nothing

    return problem_clusters



if __name__ == '__main__':
    Week = raw_input('Assignment Name:')
    problem_id = raw_input('Problem ID:')
    problem_clusters = cluster(Week, problem_id)
    pkl_dir = 'clusters/' + Week + '/'
    pickle.dump(problem_clusters, open(pkl_dir + Week + '_' + problem_id + '_cluster.pkl','wb'))
    print 'pickel file for ', Week, ' ', problem_id, ' is generated in ', pkl_dir



