# 1.countdown

def countdown(num):
    list = []
    for a in range (num, -1, -1):
        list.append(a)
    print(list)
    return list

countdown(9)


# 2 Print and Return 

def print_and_return(list):
    print(list[0])
    A = list[1]
    return A

print(print_and_return([1,2]))

# 3 First Plus Length

def first_plus_length(list):
    sum = list[0] + len(list)
    return sum

print(first_plus_length([1,2,3,4,5,6,7,8,9]))

# 4 Values Greater than Second 

def values_greater_than_second(list):
    if (len(list)< 2):
        return False
    else:
        final_list = []
        for i in range (0 , len(list)):
            if list[i] > list [1]:
                final_list.append(list[i])
        print(len(final_list))
        return final_list

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

# 5 This length, that value

def length_and_value(size, value):
    list = []
    for size in range(size):
        list.append(value)
    return list

print(length_and_value(4,7))
print(length_and_value(6,2))
