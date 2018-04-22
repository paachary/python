from filecmp import cmpfiles
from filecmp import cmp
import os

d1_contents = set(os.listdir('/home/prashant/python_code/src/rnd/package'))
d2_contents = set(os.listdir('/home/prashant/python_code/src/rnd/pip_freeze'))

flag = cmp('/home/prashant/python_code/src/rnd/package/output.txt',
           '/home/prashant/python_code/src/rnd/pip_freeze/output.txt',
           shallow=False)
print(flag)

common = list(d1_contents & d2_contents)

common_files = [f
                for f in common
                if os.path.
                isfile(os.path
                         .join('/home/prashant/python_code/src/rnd/package'
                               , f))
                ]
print("PRAX common files = ", common_files)

match, mismatch, errors = cmpfiles('/home/prashant/python_code/src/rnd/package',
                                   '/home/prashant/python_code/src/rnd/pip_freeze',
                                   common_files)
print ('Match:', match)
print ('Mismatch:', mismatch)
print ('Errors:', errors)
