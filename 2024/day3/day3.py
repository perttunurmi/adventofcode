from ast import pattern
from functools import total_ordering
from os import read
import re


file = open("day3.txt","r")
data = file.read()
file.close

pattern = r'mul\(\d{1,3},\d{1,3}\)'
instructions = re.findall(pattern, data, flags=0)

total = 0
for string in instructions:
   pattern = r'\d{1,3}'
   nums = re.findall(pattern,string, flags=0)
   total += int(nums[0]) * int(nums[1])

print("part1", total)


pattern = r'don\'t\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\)'
instructions = re.findall(pattern, data, flags=0)


do = True
total = 0
for string in instructions:
   print(string)
   if ('don' in string):
      do = False
   if ("do()" in string):
      do = True
   if (do == True and not "do()" in string):
      pattern = r'\d{1,3}'
      nums = re.findall(pattern,string, flags=0)
      total += int(nums[0]) * int(nums[1])

print(total)
