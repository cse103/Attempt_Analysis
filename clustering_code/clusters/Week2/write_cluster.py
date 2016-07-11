
# coding: utf-8

# In[11]:

import pickle
import pandas as pd
from collections import defaultdict
from StringIO import StringIO
import prettytable  

def write_to_file(problem_id):
    cluster = pickle.load(open('Week2_'+problem_id+'_cluster.pkl', 'rb'))
    no_matching_cluster = pickle.load(open('Week2_'+problem_id+'_no_match_cluster.pkl', 'rb'))

    file_name = 'Week2_' + problem_id + '_' + 'clusters.md'
    to_file = open(file_name, 'w')

    for part_id in cluster:
        to_file.write('## Part ')
        to_file.write(str(part_id))
        to_file.write('\n\n')
            

        types_of_mistakes=cluster[part_id].keys()

        cluster_size = {}
        for t in types_of_mistakes:
            cluster_size[t] = len(cluster[part_id][t])
        sorted_cluster_keys = sorted(cluster_size, key=lambda x:cluster_size[x], reverse=True)

        for mistake in sorted_cluster_keys:
            to_file.write('### Mistake Group ')
            to_file.write(str(mistake))
            to_file.write(' of size ')
            to_file.write(str(cluster_size[mistake]))
            to_file.write('\n')

            if len(cluster[part_id][mistake][0]) > 2:
                to_file.write('Hint = """ Please write hint here """\n\n')
                group = cluster[part_id][mistake]
            	to_file.write('|\t|Answer\t|Attempt\t|Matching sub-exp|\n')
                to_file.write('|---|---|---|---|\n')
                count = 0
                for p in group:
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

            to_file.write('\n\n\n\n')

        to_file.write('### No Match Group \n')
        to_file.write('Hint = """ Please write hint here """\n\n')
        i=0
        for a in no_matching_cluster[part_id]:
            to_file.write(str(i))
            to_file.write(' Student ID:')
            to_file.write(str(a))
            to_file.write('\n')
            i+=1
            record=no_matching_cluster[part_id][a]
            for key in ['first_attempt',
            'part1_incorrect_attempt', 'part1_correct_attempt',
            'part2_incorrect_attempt', 'part2_correct_attempt', 
            'part3_incorrect_attempt', 'part3_correct_attempt',
            'part4_incorrect_attempt', 'part4_correct_attempt', 
            'part5_incorrect_attempt', 'part5_correct_attempt']:
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
    print 'Write Week2 cluster into file, please enter the following'
    problem_id = raw_input('problem_id:') 
    write_to_file(problem_id)