
# coding: utf-8

import pickle

def write_to_file(problem_id):
    no_matching_cluster = pickle.load(open('Week2_'+problem_id+'_no_match_cluster.pkl', 'rb'))

    ### Print in nice format
    file_name = 'Week2_' + problem_id + '_' + 'no_match.txt'
    to_file = open(file_name, 'w')
    
    for part_id in no_matching_cluster:
        to_file.write('============= Part ')
        to_file.write(str(part_id))
        to_file.write(' =============')
        to_file.write('\n\n')
        
        i=0
        for a in no_matching_cluster[part_id]:
            to_file.write(str(i))
            to_file.write(' Student ID:')
            to_file.write(str(a))
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
                    to_file.write('\n\t\t\t\t')
                    to_file.write('\n\t\t\t\t'.join(str(b) for b in L))
                else:
                    to_file.write('\n\t')
                    to_file.write(str(key))
                    to_file.write('\t')
                    to_file.write(str(L))
            to_file.write('\n\n')
        to_file.write('\n\n\n\n\n')

if __name__ == '__main__':
    print 'Write Week2 no_match_cluster into file, please enter the following'
    problem_id = raw_input('problem_id:') 
    write_to_file(problem_id)