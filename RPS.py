
import sys
import random
choises=["R","P","S"]

def display(x,y,z):
    if z == "tie":
        print(f"You:{x} and ai:{y}\n It's a 'tie!!'")
      
    elif z == "user_win":
        print(f"You:{x} and ai:{y}\n 'ai lose!!'")
      

    elif z == "ai_win":
        print(f"You:{x} and ai:{y}\n 'ai win!!'")
        
    else:
        #just for fun
        print("You do sometink whit the code right because\n '''you not supose to read this!!!'''")
        sys.exit()


def main():
    
    while True:
        user_input=input("[R,P,S]:").upper()
        if user_input not in choises:
            continue
        ai_input=random.choice(["R","P","S"])
        
        if user_input == ai_input:
            display(x=user_input,y=ai_input,z="tie")
          
        elif user_input.startswith("R") and ai_input == "S":
            display(x=user_input,y=ai_input,z="user_win")
          
        elif user_input.startswith("P") and ai_input == "R":
            display(x=user_input,y=ai_input,z="user_win")
            
        elif user_input.startswith("S") and ai_input =="P":
            display(x=user_input,y=ai_input,z="user_win")
            
        else:
            display(x=user_input,y=ai_input,z="ai_win")
        agian()
        
def agian():
    while True:
        user_choise = input("You wish you play again [Y/N]: ").upper()
        if user_choise .startswith("Y"):
            return
        elif user_choise.startswith("N"):
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice, try again.")
   
if __name__ =="__main__":
    print("----------------------")
    print("----------RPS---------")
    print("----------------------")
    main()

