# SWE-Proj1

## Requirements/Assumptions

* We are assuming English letters only, and a default 12 pt font size for the text input.
* We are assuming that a sentence is at least two characters with one of them being a question mark, exclamation point, or period.
* We are assuming that no negative integers are given as input.
* We are assuming that we can just output the adjusted text to the terminal, and not a file

Must specify input text file with -i flag
Must specify width of left margin with -l flag
Must specify width of right margin with the -r flag


## Algorithm
1.) Open the input file and tokenize all of the words in the file
2.) Iterate through each word and do the following
3.) Check the length of the word
4.) Check the last character of the word
5.) Subtract the length of the word from the available space on the line
6.) If the difference is greater than or equal to zero print the word on the line, otherwise move to the next line and print the word
7.) If the length of the word was greater than or equal to two and last character of the word was a period, exclamation point or question mark print two spaces while respecting margins. Otherwise, print one space while respecting margins.

## Test Cases
My test cases were different types of sentences that I wrote in my test file. Some sentences included multiple symbols, capitalized words, and long words.
