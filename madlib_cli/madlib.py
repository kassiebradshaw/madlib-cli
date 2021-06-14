import re

# -------------------- GLOBAL VARIABLES ----------------------

small_template = "assets/dark_and_stormy_night_template.txt"
large_template = "assets/template.txt"

# ------------MY PROGRAM'S DECORATIVE INTRO FUNCTIONS -----------

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
      *           user input to fill in           *  
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

# ------ FUNCTIONS THAT ACTUALLY MAKE MY PROGRAM DO THINGS --------

def game(file):
    """
    Function contains the actual game play
    Opens template, parses it into blanks & empty story string
    Prompts user for input for each blank, appends input to a list
    Turns list into a tuple
    Passes user_tuple and empty_story to merge function
    Returns filled-in-the-blanks story.
    """

    user_entries = []
    content = read_template(file)
    story_pieces = parse_template(content)

    blanks = story_pieces[1]
    empty_story = story_pieces[0]

    for words_needed in blanks:
        print("    ** I need a(n):", words_needed)
        entry = input("    ** Your word: > ")
        if entry != 'QUIT':
            user_entries.append(entry)
        else:
            print("    **GAME OVER. G'bye!")
            quit()

    user_tuple = tuple(user_entries)
    
    whole_story = merge(empty_story, user_tuple)

    print("""    **
    **""", whole_story)

    save_story(whole_story)


def start_game():
    """
    Prompts user to play a short game or a long game,
    reads from a different template depending on response.
    If user types quit, they get a goodbye prompt.
    """

    print("""
    ** Do you want a short mad lib or a long one?
    ** Type 'SHORT' or 'LONG'
    """)
    entry = input("    ** > ")
    if entry != "QUIT":
        if entry.lower() == "short":
            print("    **")
            print("    ** Okay, SHORT version comin' up!")
            print("    **")
            game(small_template)
        if entry.lower() == "long":
            print("    **")
            print("    **")
            print("""  ** Okay LONG it is, get ready for lots of words!""")
            print("    **")
            game(large_template)
    else:
        print("** Come play again soon!")   


def save_story(story):
    with open("assets/saved_stories.txt", "w") as file:
        file.write(story) 

def display_game():
        welcome()
        intro()
        instructions()
        start_game()
    

# --------------- REQUIRED FOR TESTS TO PASS -----------------

def read_template(str):
    """
    If the file exists, this function opens it & reads it.
    If the file doesn't exist, an exception is raised notifying user.
    """

    with open(str, "r") as file:
        try:
            contents = file.read()
            return contents
        except FileNotFoundError as error:
            print(error, "This file does not exist")


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

    return (str, parts)

    

def merge(str, tuple):
    """
    Function takes a string and a tuple as parameters.
    The string is formatted with the tuple to fill in the blanks.
    """

    return str.format(*tuple)

# --------------- GAAAAAAME TIIIIIIME! -----------------


if __name__ == "__main__":
    display_game()
