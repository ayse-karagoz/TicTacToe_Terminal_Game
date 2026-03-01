def delete_everthing(list):# we used that 
    for i in range(0,3,1):
        for j in range(0,3,1):
            list[i][j]= "-"
def print_the_list(list):
    for i in range(0,3,1):
        print(list[i])
def control_the_list(list):
    bool_check = False
    player = ""
    list_player= []# i notice that when somethings like both player wins it detects wrong
    for i in range(0,3,1):#if there are more winner than one length of list should be more 1
        if(list[i][0]==list[i][1] and list[i][1]==list[i][2]):#we check that
            bool_check= True
            player = list[i][0]
            list_player.append(player)
    for i in range(0,3,1):
        if(list[0][i]==list[1][i] and list[1][i]==list[2][i]):
            bool_check= True
            player= list[0][i]
            list_player.append(player)
    if(list[0][0]==list[1][1] and list[1][1]==list[2][2]):
        bool_check = True
        player=list[0][0]
        list_player.append(player)
    if(list[0][2]==list[1][1] and list[2][0]==list[1][1]):
        bool_check = True
        player= list[1][1]
        list_player.append(player)
    if(len(list_player)>1):
        player = "everyone"
    if(bool_check==True):
        return player
    return None
def print_result(player:str):
    if(player != None):
        print(f"And our winner is {player}")
    else:
        print("We don't have any winner nor loser")
def game(list):
    while True:
        check = input("Do you want to play yes or no ")
        answer = check.lower()
        if(answer=="no"):
            break
        elif(answer=="yes"):
            for i in range(0,9,1):
                player = ""
                if(i%2==0):
                    player = "X"
                else:
                    player= "O"
                print(f"player {player},your turn")
                while True:
                    row = int(input("Choose row number"))
                    while(row<1 or row>3):
                        row = int(input("Invalid row number,choose again"))
                    column = int(input("Choose column number"))
                    while(column<1 or column>3):
                        column = int(input("Invalid column number,choose again"))
                    if(list[row-1][column-1]== "-"):
                        list[row-1][column-1]=player
                        break
                    else:
                        print("Invalid location,please choose free locations")
                print_the_list(list)
            player =control_the_list(list)
            print_result(player)
            delete_everthing(list)
        else:
            print("Your answer was invalid")
def main():
    my_list=[["-","-","-"],["-","-","-"],["-","-","-"]]
    game(my_list)
main()