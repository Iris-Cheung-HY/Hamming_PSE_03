# Hamming_PSE_03
## Problem Statment
Imagine working on software that analyzes mutations in DNA.

Create a function named hamming_distance that calculates the number of differences between two DNA strands (aka two strings). This method should take in two different DNA strands as inputs and the return value should be the number of differences between each string.

Input strings are guaranteed to be non-empty and only contain the characters “G”, “A”, “T”, & “C”.
A hamming distance can only be calculated if the inputs are the same length.
For example, given these two DNA strands (strings), hamming_distance should return 7 because there are 7 differences:

### Example Input	            Expected Ouput
strand1 = "GAGCCTACTAACGGGAT"
strand2 = "CATCGTAATGACGGCCT"	       7

### Explanation:
Strand #1:   GAGCCTACTAACGGGAT
Strand #2:   CATCGTAATGACGGCCT
Differences: ^ ^ ^  ^ ^    ^^
             7 in total
(This problem is sourced from http://rosalind.info/problems/hamm/)



