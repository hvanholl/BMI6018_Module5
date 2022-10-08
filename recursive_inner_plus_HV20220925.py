# Write the a python program that, given an input list of any level of complexity/nestedness, will return the inner most list plus 1. This is to be done with recursion. Note: the input will contain only integers or lists. 

input_list_1 = [1,2,3,4,[5,6,7,[8,9]]]
input_list_2 = [5,[9,2, 1, 3, [5,6,7,[3,1,[0,1], 5, [1,2]], 5, 0]]]
input_list_3 = [[0,1,2,3,[0,1]],[0,1,2,3,[0,1]]]

def recurs(input_r):                                                    
    if all(isinstance(j, int) for j in input_r) == True:                # if all items in list are integers
        output = [i + 1 for i in input_r]                               # create output list with this sublist
        return output                                                   
    else:                                                               
        input_temp = [i for i in input_r if isinstance(i, list) == True]   # create new input list with indexes that are lists
        input_r = [int for i in input_temp for int in i]                   # flatten the list
        return recurs(input_r)                                             # recursion until everything is a list 

one = recurs(input_list_1)
two = recurs(input_list_2)
three = recurs(input_list_3)

print(one)
print(two)
print(three)


