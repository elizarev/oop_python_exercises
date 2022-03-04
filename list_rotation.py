# Write a function rotate(), with the parameters my_list and num_rotations.
# rotate() should return the input list rotated num_rotations forward.
# rotate list
# no time/space requirements
# return "rotated" version of input list


def rotate(my_list, num_rotations):
    for i in range(num_rotations):
        removed = my_list.pop()
        my_list.insert(0, removed)
    return my_list
