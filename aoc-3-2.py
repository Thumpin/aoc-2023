"""--- Day 3: Gear Ratios ---

You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; 
it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. 
If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. 
There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be 
included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). 
Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

To begin, get your puzzle input."""

with open('aoc-3.txt', 'r') as f:
    content = f.readlines()
    content = [x.strip() for x in content]

for line in content:
    print(line)

import re
regex = re.compile(r"[^\w.]")
regex_result = []
special_index = []
for line in content:
    result = regex.finditer(line)
    regex_result.append(result)
for line in regex_result:
    line_special_index = []
    for matches in line:
        line_special_index.append(matches.span()[0])
    special_index.append(line_special_index)
#We check for every adjacent number to a special character
regex = re.compile(r"\d+")
regex_result = []
number_index = []
for line in content:
    result = regex.finditer(line)
    regex_result.append(result)
for line in regex_result:
    line_number_index = []
    for matches in line:
        line_number_index.append(matches.span())
    number_index.append(line_number_index)
new_number = []
for line in number_index:
    if line:
        new_line = []
        for number in line:
            new_digit = []
            for i in range(number[0], number[1]):
                new_digit.append(i)
            new_line.append(new_digit)
        new_number.append(new_line)
    else:
        new_number.append([])
results = []
for i in range(len(special_index)):
    for j in range(len(special_index[i])):
        special_char_index = special_index[i][j]
        for x in range(len(new_number[i-1])):
            if special_char_index-1 in new_number[i-1][x] or special_char_index in new_number[i-1][x] or special_char_index+1 in new_number[i-1][x]:
                results.append(content[i-1][new_number[i-1][x][0]:new_number[i-1][x][-1]+1])
                new_number[i-1][x] = []
        for x in range(len(new_number[i])):
            if special_char_index-1 in new_number[i][x] or special_char_index in new_number[i][x] or special_char_index+1 in new_number[i][x]:
                results.append(content[i][new_number[i][x][0]:new_number[i][x][-1]+1])
                new_number[i][x] = []
        for x in range(len(new_number[i+1])):
            if special_char_index-1 in new_number[i+1][x] or special_char_index in new_number[i+1][x] or special_char_index+1 in new_number[i+1][x]:
                results.append(content[i+1][new_number[i+1][x][0]:new_number[i+1][x][-1]+1])
                new_number[i+1][x] = []
results = [int(x) for x in results]
result_sum = sum(results)
print(result_sum)

"""--- Part Two ---

The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
"""

with open('aoc-3.txt', 'r') as f:
    content = f.readlines()
    content = [x.strip() for x in content]

for line in content:
    print(line)

import re
regex = re.compile(r"\*+")
regex_result = []
special_index = []
for line in content:
    result = regex.finditer(line)
    regex_result.append(result)
for line in regex_result:
    line_special_index = []
    for matches in line:
        line_special_index.append(matches.span()[0])
    special_index.append(line_special_index)
#We check for every adjacent number to a special character
regex = re.compile(r"\d+")
regex_result = []
number_index = []
for line in content:
    result = regex.finditer(line)
    regex_result.append(result)
for line in regex_result:
    line_number_index = []
    for matches in line:
        line_number_index.append(matches.span())
    number_index.append(line_number_index)
new_number = []
for line in number_index:
    if line:
        new_line = []
        for number in line:
            new_digit = []
            for i in range(number[0], number[1]):
                new_digit.append(i)
            new_line.append(new_digit)
        new_number.append(new_line)
    else:
        new_number.append([])
results = []
for i in range(len(special_index)):
    for j in range(len(special_index[i])):
        old_values = []
        special_char_index = special_index[i][j]
        special_result = []
        for x in range(len(new_number[i-1])):
            if special_char_index-1 in new_number[i-1][x] or special_char_index in new_number[i-1][x] or special_char_index+1 in new_number[i-1][x]:
                special_result.append(content[i-1][new_number[i-1][x][0]:new_number[i-1][x][-1]+1])
                old_value = [new_number[i-1][x], i-1, x]
                old_values.append(old_value)
                new_number[i-1][x] = []
        for x in range(len(new_number[i])):
            if special_char_index-1 in new_number[i][x] or special_char_index in new_number[i][x] or special_char_index+1 in new_number[i][x]:
                special_result.append(content[i][new_number[i][x][0]:new_number[i][x][-1]+1])
                old_value = [new_number[i][x], i, x]
                old_values.append(old_value)
                new_number[i][x] = []
        for x in range(len(new_number[i+1])):
            if special_char_index-1 in new_number[i+1][x] or special_char_index in new_number[i+1][x] or special_char_index+1 in new_number[i+1][x]:
                special_result.append(content[i+1][new_number[i+1][x][0]:new_number[i+1][x][-1]+1])
                old_value = [new_number[i+1][x], i+1, x]
                old_values.append(old_value)
                new_number[i+1][x] = []
        if len(special_result) > 1:
            results.append(special_result)
        else:
            for value in old_values:
                new_number[value[1]][value[2]] = value[0]
total = 0
for result in results:
    sub_total = 1
    for value in result:
        sub_total *= int(value)
    total += sub_total
print(total)