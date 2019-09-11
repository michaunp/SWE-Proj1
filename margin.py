#!/usr/bin/env python3
import argparse
import math
import re
import tokenize

parser = argparse.ArgumentParser(description="Process text file with given margins.")
parser.add_argument('-i', dest='input_file', type=str, nargs=1, help='Text input file.')
parser.add_argument('-o', dest='output_file', type=str, nargs=1, help='Text output file.')
parser.add_argument('-l', dest='l_margin', type=int, nargs=1, help='Width of left margin in inches.')
parser.add_argument('-r', dest='r_margin', type=int, nargs=1, help='Width of left margin in inches.')

IN_TO_PT = 64/11
punctuation = ['?', '.', '!']

def main():
  args = parser.parse_args()
  for i in range(1, 81):
    if i == 80:
      print('c')
    else: 
      print('c', end= "")
      
  file_content = open(args.input_file[0], 'r')
  output_file = open(args.output_file[0], 'w')
  lines = file_content.readlines()

  tokens = []
  for line in lines:
    line_tokens = re.split("(?<=\\S) ", line)
    for token in line_tokens:
      tokens.append(token)
  l_characters = math.floor(args.l_margin[0] * IN_TO_PT)
  r_characters = math.floor(args.r_margin[0] * IN_TO_PT)
  margin_space = l_characters + r_characters
  text_space = 80 - margin_space
  curr_text_space = text_space
  
  for i in range(l_characters):
      print(' ', end='')
      output_file.write(' ')
  for token in tokens:
    sentence_end = token[-1] in punctuation and len(token) > 1
    word_len = len(token)
    rem_space = curr_text_space - word_len
      
    if sentence_end:
      if rem_space >= 2:
        print(token, end='  ')
        output_file.write(token + '  ')
        curr_text_space -= (word_len + 2)
      else:
        for i in range(r_characters):
          print(' ', end='')
          output_file.write(' ')
        print('\n')
        output_file.write('\n')
        for i in range(l_characters):
          print(' ', end='')
          output_file.write(' ')
        print(token, end='  ')
        output_file.write(token + '  ')
        curr_text_space = text_space - (word_len + 2)
        
    else:
      if rem_space >= 1:
        print(token, end=' ')
        output_file.write(token + ' ')
        curr_text_space -= (word_len + 1)
      else:
        for i in range(r_characters):
          print(' ', end='')
          output_file.write(' ')
        print('\n')
        output_file.write('\n')
        for i in range(l_characters):
          print(' ', end='')
          output_file.write(' ')
        print(token, end=' ')
        output_file.write(token + ' ')
        curr_text_space = text_space - (word_len + 1)

if __name__== "__main__":
  main()