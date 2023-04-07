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

def find_word(word, search):
    global count
    elements = []
    with open("puzzle.txt", "r") as rf:
        for line in rf:

            elements.append(line.replace("\n","").split(")"))

            if(word == elements[0][0]):
                count+=1
                line_search.append(word)
                result = find_word(elements[0][1], search)
                if(result!=None):
                    return line_search
            elements = [] 

        if(count != 0 and word!=search):
            line_search.remove(line_search[count-1])
            count-=1

        if(word==search):
            return word
        
def orbital_transfers(you, san):
    temp = len(you)
    if(len(san) < len(you)):
        temp = len(san)
    for i in range(temp):
        if(san[0] == you[0]):
            san.remove(san[0])
            you.remove(you[0])  

    return len(you) + len(san)
    

if __name__ == "__main__":   

    count = 0
    line_search=[]
    
    rf = open ("puzzle.txt", "r")
    line = rf.readline().replace("\n","").split(")")
    root = find_root(line[0])

    you = find_word(root,"YOU")
    line_search = []
    count = 0
    san = find_word(root,"SAN")

    number = orbital_transfers(you, san)

    print(number)
