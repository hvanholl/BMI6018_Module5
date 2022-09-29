# Write the a python program that, given an input list of any level of complexity/nestedness, will return the inner most list plus 1. This is to be done with recursion. Note: the input will contain only integers or lists. 

input_list_1 = [1,2,3,4,[5,6,7,[8,9]]]
input_list_2 = [5,[9,2, 1, 3, [5,6,7,[3,1,[0,1], 5, [1,2]], 5, 0]]]

def recurs(input_r):                                                    # define recursive function
    if all(isinstance(j, int) for j in input_r) == True:                # if all items in list are integers
        output = [i + 1 for i in input_r]                               # create output list with this sublist
        return output                                                   # return the output
    else:                                                               # otherwise
        input_r = [i for i in input_r if isinstance(i, list) == True]   # create new input list with indexes that are lists
        input_r = input_r[0]                                            # make the first index the new list.
                                                                        # If this step isn't here it will be an infinite loop.
        return recurs(input_r)                                          # call the function on itself and return        

one = recurs(input_list_1)
two = recurs(input_list_2)
print(one)
print(two)