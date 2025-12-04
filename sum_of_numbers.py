#!/usr/bin/env python3
# Created By: Brandon
# Date: 12/01/2025
# Program shows all the multiples of 3 and 5 from 0 to 1000


def main():

    # import constants.py file
    import constants

    # initialize counters
    counter = 0
    counter2 = 0
    # for loop to calculate the multiples of 3
    for counter in range(0, 334):
        sum1 = constants.MULTIPLE3 * counter
        counter = counter + 1
        print("{} * {} = {}".format(constants.MULTIPLE3, counter, sum1))
    # for loop to calculate the multiples of 3
    for counter2 in range(0, 200):
        sum2 = constants.MULTIPLE5 * counter2
        print("{} * {} = {}".format(constants.MULTIPLE5, counter2, sum2))
        counter2 = counter2 + 1


if __name__ == "__main__":
    main()
