import time
import random
test_list1=random.sample(xrange(1000),1000)
test_list2=random.sample(xrange(1000),1000)

print(test_list1)
print(test_list2)

s=time.time()
for i in range(100):
    test_list1.sort()
print time.time()-s

s=time.time()
for i in range(100):
    test_list2=sorted(test_list2)
print time.time()-s
