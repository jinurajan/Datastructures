"""
Iterator for Combination

Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.


Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false


Constraints:

1 <= combinationLength <= characters.length <= 15
There will be at most 10^4 function calls per test.
It's guaranteed that all calls of the function next are valid.

"""


class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.current_index = 0
        self.__generate_combinations(
            characters, combinationLength)
        print self.combinations

    def __format_str(self, first_char, rest_char):
        string = first_char + "".join(rest_char)
        return string

    def __generate_combinations(self, array, comb_len):
        self.combinations = []
        length = len(array)
        if length == 0:
            self.combinations = []
        elif length == comb_len:
            self.combinations = [array]
        else:
            for i in range(length):
                if comb_len == 1:
                    self.combinations.append(array[i])
                else:
                    first_char = array[i]
                    first_comb_index = i + 1
                    
                    while first_comb_index + comb_len - 1 <= length:
                        print first_char, array[first_comb_index:first_comb_index+comb_len-1]
                        self.combinations.append(
                            self.__format_str(
                                first_char,
                                array[first_comb_index:first_comb_index + comb_len-1]))
                        first_comb_index += 1

    def next(self):
        """
        :rtype: str
        """
        if not self.combinations:
            raise Exception("There are no more combinations")
        val = self.combinations.pop(self.current_index)
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.combinations:
            return False
        return True


# obj = CombinationIterator("abc", 2)
# print obj.next()
# print obj.hasNext()
# print obj.next()
# print obj.hasNext()
# print obj.next()
# print obj.hasNext()
# edge cases
# obj = CombinationIterator("ab", 2)
# print obj.next()
# print obj.hasNext()

# obj = CombinationIterator("ab", 1)
# print obj.next()
# print obj.next()
# print obj.hasNext()

obj = CombinationIterator("gkosu", 3)
print obj.hasNext()
print obj.hasNext()
print obj.hasNext()
print obj.next()
print obj.hasNext()
print obj.next()
print obj.next()
print obj.next()
print obj.hasNext()
print obj.next()
