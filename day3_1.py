puzzle = open("puzzle_input.txt", "r")
data = puzzle.readlines()
sum = 0

for bag in data:
    for j in range(0, int(len(bag)/2)):

        for k in range(int(len(bag)/2), int(len(bag))):

            if (bag[j] == bag[k] and bag[j] != "_"):

                if (64 < ord(bag[j]) < 91):
                    sum += ord(bag[j])-38

                else:
                    sum += ord(bag[j])-96

                bag = bag.replace(str(bag[j]), "_")

print(sum)
