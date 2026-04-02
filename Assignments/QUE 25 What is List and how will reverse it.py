# list is muteable(changeable) and orderd collection of elements 
# > element are stored in index based
# > it can store diffrent data type (int , float , string etc)
# > list can be written in square braket []

## EXAMPLE ##

a = [10, 20, "hello", 5.2]
print(a)

## how to reserve list ?
# there are many type to reserve

# 1. using sliceing (this is most cooan type)
my_list = [10, 20, 30, 40, 50]
reverse = my_list[::-1]
print("reverse")


# 2. using reverse() method. 
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)

# 3. using loop (basic method).
my_list = [1, 2, 3, 4, 5]
rev = []

for i in range(len(my_list)-1, -1, -1):
    rev.append(my_list[i])

print(rev)