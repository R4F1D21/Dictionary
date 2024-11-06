set_1 = {'a','b','c'}
print(set_1,'\n')

# Converting a list into the set
sample_list = [1,1,2,2,3,3] 
sample_set = set(sample_list)
print(sample_set,'\n')

'''
#sets are not indexable.
print(sample_set[2])#Type error
'''

#Check if 4 exists in the sample set or not.
if 4 in sample_set:
    print('Yes.')
else:
    print('No.')

#Adding elements to the set. it sort the items in increasing order.

myset = set([])
myset.add(3)
myset.add(17)
myset.add(21)
myset.add(2)
myset.add(1)
print(myset, '\n')

# Set Operations
 # 1. Union
 # 2. intersection
 # 3. Difference
 # 4. Symmetric Difference


a = {3,1,2,4,5}
b = {4,5,6,7,8}
# Union of Sets 
print(a|b)
# OR 
#print(a.union(b))
