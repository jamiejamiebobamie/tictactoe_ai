#!python

from strings import contains, find_index, find_all_indexes
import unittest


class StringsTest(unittest.TestCase):

    def test_contains_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert contains('abc', '') is True  # all strings contain empty string
        assert contains('abc', 'a') is True  # single letters are easy
        assert contains('abc', 'b') is True
        assert contains('abc', 'c') is True
        assert contains('abc', 'ab') is True  # multiple letters are harder
        assert contains('abc', 'bc') is True
        assert contains('abc', 'abc') is True  # all strings contain themselves
        assert contains('aaa', 'a') is True  # multiple occurrences
        assert contains('aaa', 'aa') is True  # overlapping pattern

        assert contains('ABC', 'ABC') is True
        assert contains('abc', 'abc') is True  # multiple letters are harder
        assert contains('111', '11') is True
        assert contains('c', 'c') is True  # all strings contain themselves
        assert contains('a', 'a') is True  # multiple occurrences
        assert contains('aaaB', 'aB') is True  # overlapping pattern


    def test_contains_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert contains('abc', 'z') is False  # remember to test other letters
        assert contains('abc', 'ac') is False  # important to test close cases
        assert contains('abc', 'az') is False  # first letter, but not last
        assert contains('abc', 'abz') is False  # first 2 letters, but not last
        assert contains('abc', '1') is False  # remember to test other letters
        assert contains('abc', 'aC') is False  # important to test close cases
        assert contains('abZ', 'az') is False  # first letter, but not last
        assert contains('bbc', 'abz') is False  # first 2 letters, but not last

        assert contains('fer', 'ref') is False  # reversed order
        assert contains('f e r', 'fer') is False  # spaces between characters
        assert contains('Z', 'z') is False  # upper vs lowercase
        assert contains('bbq', 'bqb') is False  # jumbled word order




    def test_contains_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert contains('ababc', 'ab') is True  # multiple occurrences
        assert contains('banana', 'na') is True  # multiple occurrences
        assert contains('ababc', 'abc') is True  # overlapping prefix
        assert contains('bananas', 'nas') is True  # overlapping prefix

        assert contains('Ababc', 'ab') is True  # uppercase letters
        assert contains('henry', 'enry') is True  # the last letter is a part of match
        assert contains('poop', 'p') is True  # the first and last letters are a match

    def test_find_index_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert find_index('abc', '') == 0  # all strings contain empty string
        assert find_index('abc', 'a') == 0  # single letters are easy
        assert find_index('abc', 'b') == 1
        assert find_index('abc', 'c') == 2
        assert find_index('abc', 'ab') == 0  # multiple letters are harder
        assert find_index('abc', 'bc') == 1
        assert find_index('abc', 'abc') == 0  # all strings contain themselves
        assert find_index('aaa', 'a') == 0  # multiple occurrences
        assert find_index('aaa', 'aa') == 0  # overlapping pattern

        assert find_index('aab', 'b') == 2  # match on the last letter

    def test_find_index_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert find_index('abc', 'z') is None  # remember to test other letters
        assert find_index('abc', 'ac') is None  # important to test close cases
        assert find_index('abc', 'az') is None  # first letter, but not last
        assert find_index('abc', 'abz') is None  # first 2 letters, but not last

        assert find_index('A', 'B') is None  # upperace letters
        assert find_index('1', '2') is None  # numbers as strings

    def test_find_index_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert find_index('ababc', 'abc') == 2  # overlapping prefix
        assert find_index('bananas', 'nas') == 4  # overlapping prefix
        assert find_index('abcabcabc', 'abc') == 0  # multiple occurrences
        assert find_index('abcabcab', 'abc') == 0  # multiple occurrences
        assert find_index('abcabcdef', 'abcd') == 3  # overlapping prefix
        assert find_index('abcabcdef', 'abcdef') == 3  # overlapping prefix
        assert find_index('abcabcdabcde', 'abcde') == 7  # overlapping prefix
        assert find_index('abcabcdabcde', 'abcd') == 3  # multiple occurrences, overlapping prefix
        assert find_index('abra cadabra', 'abra') == 0  # multiple occurrences
        assert find_index('abra cadabra', 'adab') == 6  # overlapping prefix

        assert find_index('abcabcdef', 'f') == 8  # last letter
        assert find_index('abcabcdabcde', 'a') == 0  # first letter

    def test_find_all_indexes_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert find_all_indexes('abc', '') == [0, 1, 2]  # all strings contain empty string
        assert find_all_indexes('abc', 'a') == [0]  # single letters are easy
        assert find_all_indexes('abc', 'b') == [1]
        assert find_all_indexes('abc', 'c') == [2]
        assert find_all_indexes('abc', 'ab') == [0]  # multiple letters are harder
        assert find_all_indexes('abc', 'bc') == [1]
        assert find_all_indexes('abc', 'abc') == [0]  # all strings contain themselves
        assert find_all_indexes('aaa', 'a') == [0, 1, 2]  # multiple occurrences
        assert find_all_indexes('aaa', 'aa') == [0, 1]  # overlapping pattern

        assert find_all_indexes('aaaa', 'a') == [0,1,2,3]  # all letters are a match
        assert find_all_indexes('aaab', 'b') == [3]  # last letter is a match



    def test_find_all_indexes_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert find_all_indexes('abc', 'z') == []  # remember to test other letters
        assert find_all_indexes('abc', 'ac') == []  # important to test close cases
        assert find_all_indexes('abc', 'az') == []  # first letter, but not last
        assert find_all_indexes('abc', 'abz') == []  # first 2 letters, but not last

        assert find_all_indexes('10', '2') == []  # numbers as strings


    def test_find_all_indexes_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert find_all_indexes('ababc', 'abc') == [2]  # overlapping prefix
        assert find_all_indexes('bananas', 'nas') == [4]  # overlapping prefix
        assert find_all_indexes('abcabcabc', 'abc') == [0, 3, 6]  # multiple occurrences
        assert find_all_indexes('abcabcab', 'abc') == [0, 3]  # multiple occurrences
        assert find_all_indexes('abcabcdef', 'abcd') == [3]  # overlapping prefix
        assert find_all_indexes('abcabcdef', 'abcdef') == [3]  # overlapping prefix
        assert find_all_indexes('abcabcdabcde', 'abcde') == [7]  # overlapping prefix
        assert find_all_indexes('abcabcdabcde', 'abcd') == [3, 7]  # multiple occurrences, overlapping prefix
        assert find_all_indexes('abra cadabra', 'abra') == [0, 8]  # multiple occurrences
        assert find_all_indexes('abra cadabra', 'adab') == [6]  # overlapping prefix

        assert find_all_indexes('abra cadabra', ' ') == [4]  # testing for spaces

if __name__ == '__main__':
    unittest.main()
