import random
import sys
Politics = {
    "India": "Democracy",
    "Leader": "Prime Minister",
    
    "Prime Minister": "Narendra Modi",
    
    "Soldiers": 980000,
    "Friends": ["Usa", "Russia","Israel"],
    "Enemies": ["Pakistan", "China","Canada"]
}
def Nuke(Nation):
    if Nation in Politics["Enemies"]:
        random_number = random.randint(1,2)
        if random_number == 1:
         print("Nuked", Nation)
         ran = random.randint(1000,500000)
         Politics["Enemies"].remove(Nation)
         Politics["Soldiers"] += ran
         print("Your Army has increased by", ran)
        else:
            random_number = random.randint(250000,1000000)
            print("Failed to Nuke", Nation)
            print("Your Army has decreased by", random_number)
            Politics["Soldiers"] -= random_number 
    elif Nation in Politics["Friends"]:
        print("Nuked your friend", Nation," You have lost your allies and your army")
        Politics["Friends"].remove(Nation)
        Politics["Soldiers"] = 0
        sys.exit()
    else:
        print("Nuked a neutral nation", Nation," Your army has decreased by 50000")
        Politics["Soldiers"] -= 50000

    if(Politics["Soldiers"] < 0):
     print("Your Army has been defeated. You have lost the game.")
     sys.exit()

def Ally(Nation):
    if Nation in Politics["Friends"]:
        print("Already an ally", Nation)
    else:
        random_number = random.randint(1,2)
        if random_number == 1:
            print("Ally", Nation)
            Politics["Friends"].append(Nation)
            inc = random.randint(1000,100000)
            Politics["Soldiers"] += inc
            print("Your Army has increased by", inc)
        else:
            print("Failed to Ally", Nation)
            print("Your Army has decreased by 10000")
            Politics["Soldiers"] -= 10000
    if(Politics["Soldiers"] < 0):
     print("Your Army has been defeated. You have lost the game.")
     sys.exit()


def elections():
    Rahul_Gandhi = random.randint(1,100)
    Narendra_Modi = random.randint(1,100)
    Arvind_Kejriwal = random.randint(1,100)
    if Rahul_Gandhi > Narendra_Modi and Rahul_Gandhi > Arvind_Kejriwal:
        print("Rahul Gandhi wins the elections")
        Politics["Prime Minister"] = "Rahul Gandhi"
    elif Narendra_Modi > Rahul_Gandhi and Narendra_Modi > Arvind_Kejriwal:
        print("Narendra Modi wins the elections")
        Politics["Prime Minister"] = "Narendra Modi"
    else:
        print("Arvind Kejriwal wins the elections")
        Politics["Prime Minister"] = "Arvind Kejriwal"

    pop = random.randint(1,3)
    if pop == 1:
            print("Population is happy with the new Prime Minister")
            Politics["Soldiers"] += 100000
            print("Your Army has increased by 100000")
    elif pop == 2:
            print("Population is unhappy with the new Prime Minister")
            Politics["Soldiers"] -= 100000
            print("Your Army has decreased by 100000")
    else:
            print("Population is neutral with the new Prime Minister")
    if(Politics["Soldiers"] < 0):
     print("Your Army has been defeated. You have lost the game.")
     sys.exit()
    
def display(): #IMP
    print("Country:", "India")
    print("Government Type:", Politics["India"])
    print("Prime Minister:", Politics["Prime Minister"])
    
    print("Soldiers:", Politics["Soldiers"])
    print("Friends:", Politics["Friends"])
    print("Enemies:", Politics["Enemies"])

def emergency():
    print("You have become like Indra Gandhi You may lose ur nation now")
    chances = random.randint(1,4)
    if chances ==1 or chances == 2 or chances == 3:
        print("You have lost your nation")
        sys.exit()
    else:
        print("You have survived the emergency and your army has increased by 50000")
        Politics["Soldiers"] += 50000

def help_menu(): #Also IMP
    print("\n=== AVAILABLE COMMANDS ===\n")
    
    print("display")
    print("  → Shows current country status (PM, army, allies, enemies)\n")
    
    print("nuke <nation>")
    print("  → Attempt to attack an enemy nation")
    print("  → Success: enemy removed, army increases")
    print("  → Fail: army decreases\n")
    
    print("ally <nation>")
    print("  → Try to form alliance with a nation")
    print("  → Success: becomes friend, army increases")
    print("  → Fail: army decreases\n")
    
    print("elections")
    print("  → Conduct elections and change Prime Minister\n")
    
    print("emergency")
    print("  → High-risk move: may lose nation or gain army\n")
    
    print("exit")
    print("  → Exit the game\n")
    
    print("help")
    print("  → Show this menu\n")


while True:
    cmd = input(">> ").lower().split()

    if not cmd:
        continue

    command = cmd[0]

    if command == "display":
        display()

    elif command == "nuke":
        if len(cmd) < 2:
            print("Enter a nation")
        else:
            Nuke(cmd[1].capitalize())

    elif command == "ally":
        if len(cmd) < 2:
            print("Enter a nation")
        else:
            Ally(cmd[1].capitalize())

    elif command == "elections":
        elections()

    elif command == "emergency":
        emergency()

    elif command == "exit":
        print("Game Over")
        break
    elif command == "help": #Most Important Command
     help_menu()

    else:
        print("Invalid command")
        #Now we run it