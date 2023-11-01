################################################################################
#     ____                          __     _                          ___
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__ \
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         __/ /
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/
#
#  Question 2
################################################################################
#
# Instructions:
# Write a function that will swap a tuple of two items. For example, the function
# should change (x, y) into (y, x).
# Assign the function to `swapper` so that the function `run_swapper(..)` can use
# it. As always, there is a test suite that checks the result. It is in
# `question2_test.py.`

def exchange_tuple(tuple1):
    my_list = list(tuple1)
    my_list[0], my_list[1] = my_list[1], my_list[0]
    my_tuple = tuple(my_list)
    return my_tuple


swapper = exchange_tuple


def run_swapper(list_of_tuples):
    return list(map(swapper, list_of_tuples))
