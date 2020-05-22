import Solver

def resolve_hangman():
    Type = input("What type is the hangman? \nLocation/City/Pokemon/Item/Move/Ability/Side\n")
    solver = Solver.resolver(Type.lower())
    
    while True:
        new_input = input("What does the hangman say? \nif its over send Done, else use a . for unknown\n")
        
        # if the hangman has been found, we can terminate
        if new_input.lower() == "done":
            break

        else:   
            
            a = solver.feed(new_input.lower())

            for item in solver.active_list:
                print(f"{item} is a possibility")

if __name__ == "__main__":
    while True:
        resolve_hangman()
