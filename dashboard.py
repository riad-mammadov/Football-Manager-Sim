from setup import dashboard
def getDashboard():
    for i, opt in enumerate(dashboard, 1):
        print(f"{i}: {opt}")

    while True:
        try:
            choice = int(input())
            if i <= choice <= len(dashboard):
                if choice == 1:
                    return viewSquad()
                elif choice == 2:
                    return viewFixtures()
                elif choice == 3:
                    return playNext()
                elif choice == 4:
                    return handleQuit
            else:
                print("Enter a number within the range ")
        except ValueError:
            print("Please enter a valid number ")

def viewSquad():
    pass

def viewFixtures():
    pass

def playNext():
    pass

def handleQuit():
    pass