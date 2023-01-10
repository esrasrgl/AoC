puzzle = open("puzzle_input.txt", "r")
data = puzzle.readlines()
count=0
badge=[]
sum=0
for i in range(100):

    bag=data[i*3]

    for c in bag:

        if(c in data[i*3+1] and c in data[i*3+2] ):

            badge.append(c)
        
            if(64<ord(c)<91):
                sum+=ord(c)-38#-38 büyük harf -96 kücük

            else:
                sum+=ord(c)-96
            break

    count+=1
print(sum)
