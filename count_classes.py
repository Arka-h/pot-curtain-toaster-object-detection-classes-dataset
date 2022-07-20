# 0:curtain
# 1:pot
# 2:toaster

import os
count = {}
count2 = 0  # No. of images containing class 2


def count_in(dirname):
    global count2, count
    for file in list(filter(lambda l: l.endswith('.txt'), os.listdir(dirname))):
        # for i, file in enumerate(list(filter(lambda l: l.endswith('.txt'), os.listdir(dirname)))): # testing
        # print(f'{dirname} file {i}') # testing
        with open(os.path.join(dirname, file)) as f:
            flag = 0
            for line in f:
                count[line[0]] = count.get(line[0], 0) + 1
                if line[0] == '2':
                    flag = 1
            if flag:
                count2 += 1


count_in('test')
count_in('train')
count_in('valid')

print('RESULTS:')
print(f'{5909 - count2} are curtain and pot, {count2} of them are toaster')
print(f'Distribution of annotations: {count}')
