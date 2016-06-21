
# coding: utf-8

# In[1]:

from parsetrees.expr_parser import webwork_parser
from parsetrees.expr_parser import Eval_parsed
import pickle
from collections import defaultdict
import cluster_functions


def cluster(Week, problem_id):
    ### Load data ###
    data = pickle.load(open('../2015data/'+Week+'_data.pkl','rb'))

    ### Make params as inputs to function find_matches ###
    params = defaultdict(list)
    for (pro, par) in data.keys():
        if pro == problem_id:
            params[par] = cluster_functions.make_params(pro, par, data)

    ### Create clusters, if no hits, clustered as 'Nothing' ###
    problem_clusters={}
    for part in params:
        problem_clusters[part]=defaultdict(list)
        for p in params[part]:
            final_pairs = cluster_functions.find_matches(p)
            if len(final_pairs)>0:
                sorted_final = sorted(final_pairs,key=lambda x: x[0])
                problem_clusters[part][str(sorted_final)] += [p['attempt']]
            else:
                problem_clusters[part]['Nothing'] += [p['attempt']]

    return problem_clusters



if __name__ == '__main__':
    Week = raw_input('Assignment Name:')
    problem_id = raw_input('Problem ID:')
    problem_clusters = cluster(Week, problem_id)
    pkl_dir = 'clusters/' + Week + '/'
    pickle.dump(problem_clusters, open(pkl_dir + Week + '_' + problem_id + '_cluster.pkl','wb'))
    print 'pickel file for ', Week, ' ', problem_id, ' is generated in ', pkl_dir



