def find_root(word):

    flag = 0
    with open("puzzle.txt", "r") as rf:
        for line in rf:

            elements = line.replace("\n","").split(")")

            if(word == elements[1]):
                flag = 1
                return find_root(elements[0]) 
        
        if(flag == 0):
            return word

def find_word(word):
    global count
    global final_sum

    with open ("puzzle.txt", "r") as rf:
        for line in rf:
            out = line.replace("\n","").split(")")
            if(word == out[0]):
                count+=1
                find_word(out[1])
         
        if(count != 0):
            count-=1
            final_sum+=(count+1)

if __name__ == "__main__":
    count = 0
    final_sum=0

    rf = open ("puzzle.txt", "r")
    line = rf.readline().replace("\n","").split(")")
    root = find_root(line[0])

    find_word(root)

    print(final_sum)