

if __name__ == "__main__":                                                                                                  # main method
    print("Part - 1")                                                                                                       # Part - 1
    print("1.a) Python Lists are mutable.")                                                                                 # print about lists
    print("1.b) Python Tuples are immutable.")                                                                              # print about tuples
    print("1.c) Python Dictionaries are mutable.")                                                                          # print about dictionaries
    print("1.d) Python Strings are immutable.")                                                                             # print about strings
    print()
    print()

    # Part - 2
    print("Part - 2")                                                                                                       # Part - 2
    print("2.a) No error, because lists are mutable and the index number does not exceed the number of elements minus 1.")  # print about 2.a)
    print("2.b) Error, because strings are immutable.")                                                                     # print about 2.b)
    print("2.c) Error, because strings are immutable.")                                                                     # print about 2.c)
    print("2.d) No error, because dictonaries are mutable we can delete keys from dictionaries.")                           # print about 2.d)
    print()
    print()

    # Part - 3
    print("Part - 3")                                                                                                       # Part - 3
    start = int(input("Enter the start point: "))                                                                           # scan start
    end = int(input("Enter the end point: "))                                                                               # scan end
    while end - start <= 10:                                                                                                # repeat scan condition
        end = int(input("End must be at least 10 more than the start. Enter the end point: "))                              # scan end
    l, s = [], 0                                                                                                            # initialize list and sum
    for i in range(start, end + 1, 2):                                                                                      # start for with condition
        l.append(i ** 2)                                                                                                    # append list
        s += (i**2)                                                                                                         # calculate running sum
    print(f"The squares of the alternating elements are {l}")                                                               # print list
    print(f"The sum of the squares of alternating elements is {s}")                                                         # print total sum

    print()
    print()

