# Write a python program that, given an input list, will filter the input above a user defined threshold. # This is to be done with a standard function.
# That is, given a list [1,2,3,4,5,6,7,8,9], and an argument (6), it should return [1,2,3,4,5,6]

list_before = [1,5,7,9,6,1,0,12]

# Input list should be a list of integers. Threshold value to keep values at or below the threshold.
def filter(int_list, threshold):                            # define function with list and threshold as arguments
    list_after = [x for x in int_list if x <= threshold]    # list comprehension - add index if < or = to threshold
    return list_after                                       # return so available in global scope
    
print(filter(list_before, 6))                               # print called function with threshold 6. should print return value from function