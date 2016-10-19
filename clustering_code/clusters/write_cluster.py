
# coding: utf-8

# In[11]:

import pickle
import pandas as pd
from collections import defaultdict
from StringIO import StringIO
import prettytable

def write_to_file(path, problem_id, set_id):
    cluster = pickle.load(open(path + set_id + '/pkl_files/' + set_id+'_'+problem_id+'_cluster.pkl', 'rb'))
    no_matching_cluster = pickle.load(open(path + set_id + '/pkl_files/' + set_id+'_'+problem_id+'_no_match_cluster.pkl', 'rb'))

    file_name = path + set_id + '/md_files/' + set_id + '_' + problem_id + '_' + 'clusters.md'
    to_file = open(file_name, 'w')

    for part_id in sorted(cluster.keys()):
        to_file.write('## Part ')
        to_file.write(str(part_id))
        to_file.write('\n\n')


        types_of_mistakes=cluster[part_id].keys()

        cluster_size = {}
        for t in types_of_mistakes:
            cluster_size[t] = len(cluster[part_id][t])
        sorted_cluster_keys = sorted(cluster_size, key=lambda x:cluster_size[x], reverse=True)

        for mistake in sorted_cluster_keys:
            if mistake == "['R']":
                continue
            to_file.write('### (')
            to_file.write(str(cluster_size[mistake]))
            to_file.write(') Mistake Group ')
            to_file.write(mistake)
            to_file.write(' of size ')
            to_file.write(str(cluster_size[mistake]))
            to_file.write('\n')

            if len(cluster[part_id][mistake][0]) > 2:
                to_file.write('""" Please write hint here """\n\n')
                to_file.write('|ID\t|Author\t|Condition\t|Hint Text|\n')
                to_file.write('|---|---|---|---|\n')
                to_file.write('|0|\t|')
                to_file.write(str(mistake))
                to_file.write('\t|"hint"\t|\n\n')
                group = cluster[part_id][mistake]
            	to_file.write('|\t|Answer\t|Attempt\t|Matching sub-exp|\n')
                to_file.write('|---|---|---|---|\n')
                count = 0
                avoid_duplicate = defaultdict(int)
                for p in group:
                    if avoid_duplicate[p[1]]:
                        continue
                    to_file.write('|')
                    to_file.write(str(count))
                    to_file.write('\t|')
                    to_file.write(str(p[0]))
                    to_file.write('\t|')
                    to_file.write(str(p[1]))
                    to_file.write('\t|')
                    to_file.write(str(p[2]))
                    to_file.write('\t|')
                    to_file.write('\n')
                    count += 1
                    avoid_duplicate[p[1]] = 1

            to_file.write('\n\n\n\n')

        to_file.write('### (')
        to_file.write(str(len(no_matching_cluster[part_id])))
        to_file.write(') No Match Group \n')
        to_file.write('""" Please write hint here """\n\n')
        to_file.write('|ID\t|Author\t|Condition\t|Hint Text|\n')
        to_file.write('|---|---|---|---|\n')
        to_file.write('|0|\t|\t|"hint"\t|\n\n')
        i=0
        for a in no_matching_cluster[part_id]:
            to_file.write(str(i))
            to_file.write(' Student ID:')
            to_file.write(str(a))
            to_file.write('\n')
            i+=1
            record=no_matching_cluster[part_id][a]

            key_list = ['first_attempt']
            for p_id in xrange(1, int(part_id)+1):
                s1 = 'part' + str(p_id) + '_incorrect_attempt'
                s2 = 'part' + str(p_id) + '_correct_attempt'
                key_list += [s1, s2]

            for key in key_list:
                if key in record:
                    L=record[key]
                else:
                    continue
                if key == 'first_attemp':
                    to_file.write('\n\t')
                    to_file.write(str(key))
                    to_file.write('\t\t\t')
                    to_file.write(str(L))
                elif '_incorrect_attempt' in key:
                    to_file.write('\n\t')
                    to_file.write(str(key))
                    to_file.write('\n\t\t\t\t\t')
                    to_file.write('\n\t\t\t\t\t'.join(str(b) for b in L))
                else:
                    to_file.write('\n\t')
                    to_file.write(str(key))
                    to_file.write('\n\t\t\t\t\t')
                    to_file.write(str(L))
            to_file.write('\n\n')
        to_file.write('\n\n\n\n\n')

        to_file.write('\n\n\n\n\n\n')

if __name__ == '__main__':
    path = '2016_clusters/'
    print 'Write cluster into file, please enter the following'
    set_id = raw_input('week_id:')
    problem_ids = raw_input('problem_ids(seperate with space):')
    ids = [i for i in problem_ids.split()]
    for pid in ids:
        write_to_file(path, pid, set_id)
