"""--- Day 2: Cube Conundrum ---

You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. 
You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.

The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. 
He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. 
They don't get many visitors up here; would you like to play a game in the meantime?

As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. 
Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, 
and then put them back in the bag. He'll do this a few times per game.

You play several games and record the information from each game (your puzzle input). 
Each game is listed with its ID number (like the 11 in Game 11: ...) 
followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; 
the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. 
However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; 
similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
"""

with open('aoc-2.txt', 'r') as f:
    content = f.readlines()
    content = [x.strip() for x in content]

#We separate the games for each line

games:dict = {}
for line in content:
    line = line.split(":")
    #Filter numbers only from game name
    line[0] = ''.join(filter(lambda x: x.isdigit(), line[0]))
    #Make a list[dict] with the colors of the balls for different sets of the same game
    game_history = []
    game = line[1].split(";")
    for set in game:
        blue_number = 0
        red_number = 0
        green_number = 0
        balls = set.split(",")
        for ball in balls:
            if "blue" in ball:
                blue_number = "".join(filter(lambda x: x.isdigit(), ball))
                blue_number = int(blue_number)
            elif "red" in ball:
                red_number = "".join(filter(lambda x: x.isdigit(), ball))
                red_number = int(red_number)
            elif "green" in ball:
                green_number = "".join(filter(lambda x: x.isdigit(), ball))
                green_number = int(green_number)
        game_history.append({"blue": blue_number, "red": red_number, "green": green_number})
    games[int(line[0])] = game_history
#Now that the data is correctly formatted we can start the game
#We define our real bag
real_bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}
id_sum = 0
#We go through all the games
for game_id, sets in games.items():
    flag = 0
    #We go through all the sets in every game
    for set in sets:
        #We go through each of the balls that are taken out of the bag and check if the number is possible
        for color, number in set.items():
            if number > real_bag[color]:
                #Once we find a combination that is impossible we flag the game and break the loop
                flag = 1
                break
        #If there was an impossible combination in the game we discard the game
        if flag == 1:
            break
    #if there was no possible combinations we sum the game ids
    if flag == 0:
        id_sum += game_id
print(id_sum)
"""The Elf says they've stopped producing snow because they aren't getting any water! 
He isn't sure why the water stopped; however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!

As you continue your walk, the Elf poses a second question: in each game you played, 
what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

Again consider the example games from earlier:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

    In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
    Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
    Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
    Game 4 required at least 14 red, 3 green, and 15 blue cubes.
    Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.

The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. 
The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?"""
import math

result = 0
for game_id, sets in games.items():
    ball_power = 1
    minimum_number = {
        "red" : -(math.inf),
        "green" : -(math.inf),
        "blue" : -(math.inf),
    }
    for set in sets:
        for color, number in set.items():
            minimum_number[color] = number if number > minimum_number[color] else minimum_number[color]
    print(minimum_number)
    for key, value in minimum_number.items():
        ball_power *= value
    result += ball_power
print(result)

