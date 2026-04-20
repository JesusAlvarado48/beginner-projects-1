"""
Beginner Python Project - Binary Search Implementation by Kylie Ying

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

import random
import time

# Implementation of binary search algorithm!!

# We will prove that binary search is faster than naive search!


# Essence of binary search:
# If you have a sorted list and you want to search this array for something,
# You could go through each item in the list and ask, is this equal to what we're looking for?
# But we can make this *faster* by leveraging the fact that our array is sorted!
# Binary search ~ O(log(n)), naive search ~ O(n)

def get_valid_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

# In these two examples, l is a list in ascending order, and target is something that we're looking for
# Return -1 if not found


# naive search: scan entire list and ask if its equal to the target
# if yes, return the index
# if no, then return -1
def naive_search(l, target):
    # example l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


# binary search uses divide and conquer!
# we will leverage the fact that our list is SORTED
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    # example l = [1, 3, 5, 10, 12]  # should return 3
    midpoint = (low + high) // 2  # 2

    # we'll check if l[midpoint] == target, and if not, we can find out if
    # target will be to the left or right of midpoint
    # we know everything to the left of midpoint is smaller than the midpoint
    # and everything to the right is larger
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        # target > l[midpoint]
        return binary_search(l, target, midpoint+1, high)

if __name__=='__main__':
    try:
        length = 10000
        # build a sorted list of length 10000
        sorted_list = sorted(random.sample(range(-3*length, 3*length), length))
        
        print("Search conducted in repository: kying18/beginner-projects\n")
        print("A sorted list of random integers has been generated.")
        print("You will continue entering numbers until one is found in the list.\n")
        while True:
            target = get_valid_integer("Enter a number to search for: ")
            result = binary_search(sorted_list, target)

            if result != -1:
                print(f"Target {target} found at index {result}.")

                # Time comparison between naive and binary search
                start = time.time()
                naive_search(sorted_list, target)
                end = time.time()
                naive_time = end - start

                start = time.time()
                binary_search(sorted_list, target)
                end = time.time()
                binary_time = end - start

                print(f"Naive search time: {naive_time:.8f} seconds")
                print(f"Binary search time: {binary_time:.8f} seconds")
                print("Binary search is faster due to its O(log n) complexity.\n")
            else:
                print(f"Target {target} not found in the list.")

            # Ask if the user wants to continue comparing searches
            while True:
                choice = input("\nWould you like to continue comparing searches? (y/n): ").strip().lower()
                if choice in ['y', 'yes']:
                    print("\nContinuing search...\n")
                    break # exit inner loop, continue outer loop
                elif choice in ['n', 'no']:
                    print("\nExiting program. Thank you for using the search comparison tool.")
                    raise SystemExit
                else:
                    print("Invalid input. Please enter 'Y' or 'N'.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

