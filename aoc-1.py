"""--- Day 1: Trebuchet?! ---

Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

Your puzzle answer was 55172.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?

"""
with open('aoc-1.txt', 'r') as f:
    content = f.readlines()
    content = [x.strip() for x in content]
number_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
result: list[dict] = []
for line in content:
    i = 0
    numbers = {}
    #We first iterate over every line and save the numbers that are in every line along with their index
    for i in range(len(line)):
        if line[i].isdigit():
            numbers[i] = line[i]
    #We then iterate over the dictionary of numbers and save the numbers that are represented with their word equivalent and save their index
    for key, value in number_dict.items():
        index = -len(key)
        while index != -1:
            index = line.find(key, index+len(key), len(line))
            if index != -1:
                numbers[index] = value
    result.append(numbers)
#After we have a list of dictionaries with the numbers and their index we sort the numbers and add the first and last number if there is no last number we duplicate the first one
i = 0
for i in range(len(result)):
    sorted_numbers = dict(sorted(result[i].items()))
    sorted_numbers = list(sorted_numbers.values())
    if len(sorted_numbers) > 1:
        result[i] = sorted_numbers[0] + sorted_numbers[-1]
    else:
        result[i] = sorted_numbers[0] * 2
result = [int(x) for x in result]
print(sum(result))




