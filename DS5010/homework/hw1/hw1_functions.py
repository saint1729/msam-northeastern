# Problem 1
def mean(x):
    """
    Takes an iterable and returns the mean value.

    :param x: list: An Iterable of float or int values.
    :return: float: The mean of all values in x.
    """
    # initialization
    n = 0
    result = 0
    # iterate the iterable
    for element in x:
        # check for validity
        if not isinstance(element, (float, int)):
            continue
        # increment the number of elements and running sum
        n += 1
        result += element

    # calculate mean
    return result / n if (n > 0 and len(x) > 0) else None


# Problem 2
def imax(x):
    """
    Takes an iterable and returns the index of the maximum value.

    :param x: List: An Iterable of float or int values.
    :return: Integer: The index of max value.
    """
    # initialization
    ans, max_val = None, -float('inf')
    # enumerate the iterable
    for i, element in enumerate(x):
        # check for validity
        if not isinstance(element, (float, int)):
            continue
        # update the maximum and corresponding index
        if element > max_val:
            max_val = element
            ans = i

    return ans


def value_count(x):
    """
    Takes an iterable and returns a Counter of all elements in the list.

    :param x: List: An Iterable of float or int values.
    :return: Dict: A counter of all elements in the input list.
    """
    # initialization
    d = {}
    # iterate the iterable
    for element in x:
        # increment the count for corresponding key
        d[element] = d.get(element, 0) + 1

    return d


# Problem 3
def mode(x):
    """
    Takes an iterable and returns the most common value.

    :param x: List: An Iterable of float or int values.
    :return: Any: The most common element in the input list.
    """
    # get the value count for an input iterable
    d = value_count(x)
    # initialize the values
    max_count, result = -1, None
    # iterate the dictionary
    for key, val in d.items():
        # update the result if value greater than current max
        if val > max_count:
            max_count = val
            result = key

    return result


# Problem 4
def tokenize(s):
    """
    Takes a string and tokenizes it into a list of words.

    :param s: String: Any string.
    :return: Any: The most common element in the input list.
    """
    # tokenize the given string
    s_list = s.split(" ")
    # initialize the result list
    result = []
    # iterate through every token
    for token in s_list:
        # initialize the word array
        # this is done to make the time complexity O(n),
        # as string is immutable in python
        w = []
        # iterate through every character in word
        for character in token:
            # check if character is alphanumeric and append to word array
            if character.isalnum():
                w.append(character)
        # join all characters and convert to lowercase and append to result list
        w = ("".join(w)).lower()
        result.append(w)
    return result


# Problem 5
def count_words(s):
    """
    Counts the occurrences of unique words in a string.

    :param s: String: Any string.
    :return: Dict: A counter of all alphanumeric tokens of the string.
    """
    # use above utility function to tokenize the input string
    tokens = tokenize(s)
    # return the value count as dictionary using above utility function
    return value_count(tokens)


if __name__ == "__main__":
    print(mean([1, 2, 3, 4, 5, 6]))
    print(mean([1.11, 2.22, 3.33, "abc"]))
    print(mean(["hello!", "world!", "test!"]))

    print(imax([1, 2, 3, 100, 3, 2]))
    print(imax([-999, -99, -9, -99, "abc"]))
    print(imax(["hello!", "world!", "test!"]))

    print(mode([1, 1, 2, 3, 5, 8, 13]))
    print(mode([-999, -99, -9, -99, "abc"]))
    print(mode(["a", "a", "b", "b", "b", "c"]))

    print(tokenize("Hello, world!"))
    print(tokenize("Hi! Hi! Who are you?"))

    print(count_words("I am that I am."))
    print(count_words("We are not who we are."))

