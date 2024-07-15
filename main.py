import time
import os
import platform
import sqlite3
import datetime

def main():
    print("Welcome! What would you like to do?")
    menuStart()


def menuStart():
    print("Menu")
    print("1: Start today's review.")
    print("2: Add new belief.")
    print("3: Show all beliefs.")
    print("4: Quit.")
    options = ["1", "2", "3", "4"]    
    choice = input("Your Input: ")

    if choice not in options:
        print("Your choice was not in the options, please try again.")
    
    match choice: 
        case "1":
            dailyShiftingReview()
        case "2":
            addBelief()
        case "3":
            showAllBeliefs()
        case "4":
            return
    print("An error has occured... returning to start menu...")
    menuStart()

def dailyShiftingReview():
    # select all beliefs ready for a review
    print("")
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")

    # get all beliefs that haven't been reviewed yet
    cur.execute("select * where ")

    con.commit()
    con.close()
    

def addBelief():
    belief = input("Your belief: ")

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("insert into beliefs (description, createdDate, lastInteractDate)" + 
                "values(?, ?, ?)", 
                (belief, 
                    datetime.datetime.today().strftime("%Y-%m-%d"),
                    datetime.datetime.today().strftime("%Y-%m-%d")))
    con.commit()
    con.close()

    print("Belief added.")
    response = input("Would you like to record a shift on this belief now? (y/n)").lower()
    
    if response == "y":
        # do a shift for a single belief
        print("here be some stuff")
    elif response != "n":
        print("Error in response. Returning to main menu...")
    menuStart()

def showAllBeliefs():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("select * from beliefs;")
    rows = cur.fetchall()

    for row in rows: 
        print("Id: " + str(row[0]))
        print("Description: " + row[1])
        print("Create Date: " + row[2])
        print("Last InteractDate: " + row[3])

    con.commit()
    con.close()

    print("Returning to main menu...")
    menuStart()







# Test methods used in development
def printTest():
    isWindows = None

    isWindows = platform.system() == "Windows"
    clearScreen = "clear"

    (columns, rows) = os.get_terminal_size()

    print(columns)
    print(rows)
    print("-" * columns)

    res = ""
    for i in range(columns):
        if i % 10 == 0:
            res += "|"
        else:    
            res += " " 

    print(res + "\n" + res + "\n" + res)
    #print("\033[2J\033[H", end="", flush=True)
    end2 = time.time()
    #print("\033c", end="", flush=True)
    return

def sqlTest():
    print("sql test")

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    #cur.execute("""
    #    create table beliefs (
    #            beliefId integer primary key,
    #            description text not null,
    #            createdDate text not null,
    #            lastReviewDate text null,
    #            nextReviewDate text null
                
    #            );
    #""")

   # cur.execute(""",,
   #     create table reviews (
   #             reviewId integer primary key,
   #             fkBeliefId integer key,
   #             createdDate text,
   #             startLevel integer, 
   #             endLevel integer,
   #             change integer, 
   #             foreign key(fkBeliefId) references beliefs(beliefId)
   #             );
   #     """)
    con.commit()
    con.close()
    # TODO fix the foreign key error above    

if __name__ == "__main__":
    main()