import re

# -------------------- GLOBAL VARIABLES ----------------------

small_template = "assets/dark_and_stormy_night_template.txt"
large_template = "assets/template.txt"

string = "It was a {Adjective} and {Adjective} {Noun}."

# --------------------MY PROGRAM FUNCTIONS -------------------

def welcome():
    """
    This is the "header" of the program
    """

    print("""                                                    
    *************************************************
    ****                                         ****  
    ***                  WELCOME                  *** 
    **                      TO                     **
    ***                 MAD LIBS!                 ***
    ****                                         ****
    *************************************************""")

def intro():
    """
    This is the piece that explains the "Mad Libs" game
    """

    print("""    *                                               *
     *              A game that takes              *         
      *      that takes user input to fill in     *  
       *        category-specific blanks,        *   
      *            in order to create a           *  
     *                 silly story.                * 
    *                                               *
    *************************************************""")

def instructions():
    """
    This tells the user how to interact with the program
    """

    print("""    **                                             **
    **     Please fill in a response for each      **
    **           prompt, and hit enter.            **
    **                                             **
    **            To exit, type 'QUIT'             **
    **                                             **
    *************************************************""")

def print_game():
        welcome()
        intro()
        instructions()



# --------------- REQUIRED FOR TESTS TO PASS -----------------

def read_template(str):
    """
    If the file exists, this function opens it & reads it.
    Appends its content to a global variable called contents.
    If the file doesn't exist, an exception is raised notifying user.
    """

    with open(str, "r") as file:
        try:
            contents = file.read()
            # print(contents)
            return contents
        except FileNotFoundError:
            return "This file does not exist"


def parse_template(str):
    """
    This function takes an incoming string and strips everything
    inside curly brackets out, and puts it into a "parts" tuple.
    Then it replaces the original string with a "stripped"
    version of the string.
    """
    

    stripped = str

    parts = tuple(re.findall(r"\{(.*?)\}", stripped))

    str = re.sub(r"\{(.*?)\}", "{}", stripped)

    print(str, parts)
    return (str, parts)

    

def merge(str, tuple):
    """
    Function takes a string and a tuple as parameters.
    The string is formatted with the tuple to fill in the blanks.
    """

    return str.format(*tuple)

# --------------- MY OTHER FUNCTIONS -----------------


if __name__ == "__main__":
    
    print_game()
    read_template(large_template)
    parse_template(contents)
