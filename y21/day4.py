import sys

input=open("input.txt","r")
drawn=input.readline().replace("\n","").split(",")
boards=input.read().split('\n')
board=[[],[],[],[],[]]
counter=0
total_sum=[]
total=[]

def sum_number(board:list[int],bingo:int):
    sum=0
    for j in board:
        for i in j:
            if(i!="*"):
                sum+=int(i) 
    # print(int(sum),int(bingo))
    
    total_sum.append(int(sum)*int(bingo))
    total.append(drawn.index(bingo))


def column_control(board:list[list],bingo):
    counter=0
    index=0
    for j in range(5):
        for i in board:
            if(i[j]=="*"):
                counter+=1
                
            else:
                counter=0 
                break 
            
        if (counter==5):
            sum_number(board,bingo)
            return 5

            
def line_control(board:list[list],bingo):
    counter=0
    #print(board)
    for j in board:
        for i in range(len(j)):
            if(j[i]=="*"):
                counter+=1

            else:
                counter=0  
                break 

        if (counter==5):
            sum_number(board,bingo)
            return 5
           
                
def drawn_control(board:list[list]):#matrisin satır sütünlarından biri tamamen dolu mu

    a=-1
    counter=0
    for i in drawn:

        for j in board:

            if(i in j):
            
                j.insert(j.index(i),"*")
                j.remove(i)
                #print(i,board)
                counter+=1 

                if(counter>=4):
                    a=line_control(board,i)

                    if(a==5):
                        return a  
                    b=column_control(board,i) 

                    if(b==5):
                        return a    

for i in boards:

    if(i!="\n" and i!=""):
        boardNumber=i.split(" ")
        for j in boardNumber:
            if(j.isnumeric and j!=""):
                board[counter].append(j)
        #print(board)

        counter+=1    

        if(counter==5):
            value=drawn_control(board)
            if(value==5):
                
                board=[[],[],[],[],[]]
                counter=0
                continue
                
            board=[[],[],[],[],[]]
            counter=0

temp=total[0]
for i in range(len(total)):
    if(temp<total[i]):
        temp=total[i]

index=total.index(temp)
print(temp)
print(total_sum[index])  
