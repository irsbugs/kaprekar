#!/usr/bin/env python3
#
# kaprekar_constant.py
#
# Constants are 495 for 3 digits and 6174 for 4 digits.
# E.g. 2060 is 6200 - 0026 = 6174. Achieved in one interation.
#
# Examples of launching the program...
# $ python kaprekar_constant.py 105
# $ python kaprekar_constant.py 1963
# $ python kaprekar_constant.py
#
# Ian Stewart 2022-10-22
#
import sys
VERBOSE = True
MAX_ITERATIONS = 10

def main(integer_str):
    """
    Recieve integer as string from command line interface
    Call functions to rearrange in desending and assending orders
    Call function to subtract descending from assending.
    Loop if it's not repeating.
    """

    if VERBOSE: print("Initial integer:        {:>8}".format(integer_str))
    
    count = 0
    previous_str = integer_str
    
    while True:
        count += 1
        if VERBOSE: print("\nIteration count:        {:>8}".format(count))

        integer_large_str = sort_integer_in_descending_order(integer_str)
        if VERBOSE: print("Rearranged decending:   {:>8}".format(integer_large_str))

        integer_small_str = sort_integer_in_asscending_order(integer_large_str)
        if VERBOSE: print("Rearranged accending:   {:>8}".format(integer_small_str))

        integer_str = subtract_large_from_small(integer_large_str, integer_small_str)
        if VERBOSE: print("Sutraction result:      {:>8}".format(integer_str))

        # Exit if repeating sequence s not found by MAX_ITERATIONS.
        if count == MAX_ITERATIONS:
            break

        # If  iteration happens twice in sequence, then exit
        if integer_str == previous_str:   
            if VERBOSE: print("Repeating sequence was reached...")
            break
                                
        else:
            previous_str = integer_str
            continue
            
    return count, integer_str


def sort_integer_in_descending_order(int_str):
    """
    Convert string into a list
    Sort list descending order. E.g. 4557 becomes 7554
    Convert list to string
    """
    int_list = []
    int_list[:0] = int_str
    int_list.sort(reverse=True)
    int_large_str = "".join(int_list)
    return int_large_str


def sort_integer_in_asscending_order(integer_large_str):
    """
    Convert string into a list
    Sort list asscending order. E.g. 7554 becomes 4557
    Convert list to string
    """
    int_list = []
    int_list[:0] = integer_large_str
    int_list.reverse()
    int_small_str = "".join(int_list)
    return int_small_str


def subtract_large_from_small(integer_large_str, integer_small_str):
    """
    Subtract small integer from large integer
    If subtraction result is zero then integer contains the same digits, so exit.
    Else return integer as a zero filled string.
    """
    integer = (int(integer_large_str) - int(integer_small_str))
    if integer == 0:
        print("Initial integer can not be all the same digit.")
        #sys.exit("Initial integer can not be all the same digit.")
         
    int_str = str(integer)
    length = len(integer_large_str)
    return int_str.zfill(length)


def check_argument(int_str):
    """
    Check if string is a series of digits that make a positive integer.
    """
    try:
        integer = int(int_str)
    except:
        print("Must be an integer")
        sys.exit("Exiting...")

    if integer < 1:
        print("Number must be positive")
        sys.exit("Exiting...")

    return int_str


if __name__=="__main__":

    print("\nKaprekar Constant")
    
    # All 3 x digit and 4 x digit analysis
    if len(sys.argv) == 1:
        VERBOSE = False
        for i in range(100, 10000):        
            i_str = str(i)
            int_str = check_argument(i_str)
            #int_str = int_str.zfill(4)
            counter, integer_str = main(int_str)
            print(str(i).zfill(len(i_str)), counter -1, integer_str)        
        
    # Use the sys.argv[1] argument as the data and provide verbose analysis
    if len(sys.argv) >  1:
        int_str = check_argument(sys.argv[1])
        counter, integer_str = main(int_str)
        
        if counter == MAX_ITERATIONS:
            print("After {} iterations there is no repeating sequence"
                    .format(MAX_ITERATIONS))
        
        else:
            print("\n{} took {} iterations to reach a repeating {}"
                    .format(int_str, counter -1, integer_str ))


"""
Reference: 
https://en.wikipedia.org/wiki/Kaprekar%27s_routine
https://en.wikipedia.org/wiki/6174_(number)
"""
