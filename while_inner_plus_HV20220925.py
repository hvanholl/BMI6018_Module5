# Write a python program that, given an input list of any level of complexity/nestedness, will return the inner most list plus 1. This is to be done with a while loop. Note: the input will contain only integers or lists. 
#As an example:

input_list_1 = [1,2,3,4,[5,6,7,[8,9]]]
input_list_2 = [5,[9,2, 1, 3, [5,6,7,[3,1,[0,1], 5, [1,2]], 5, 0]]]
input_list_3 = [[0,1,2,3,[0,1]],[0,1,2,3,[0,1]]]

def while_list(input_list):
    i = 0                                                 # Initialize loop                                
    while i < len(input_list):                            # Loop until i is equal to the length of the list
        if all(isinstance(j, int) for j in input_list):   # If all list items are integers
            output = [i + 1 for i in input_list]          # Create output list with that index
            return output                                 # Return value to function
        i += 1                                            # increase index by 1
        if any(isinstance(j, list) for j in input_list):               # If idex is a list itself
            input_temp = [i for i in input_list if isinstance(i, list) == True] # Make the input list a list of indices that are lists
            input_list = [int for i in input_temp for int in i]                   # flatten the list
            i = 0                                         # re-initialize loop to loop through nested list


one = while_list(input_list_1)
two = while_list(input_list_2)
three = while_list(input_list_3)

print(one)
print(two)
print(three)