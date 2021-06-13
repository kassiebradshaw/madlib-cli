import re

# GLOBAL VARIABLES
small_template = "assets/dark_and_stormy_night_template.txt"
template = "assets/template.txt"
# saved_content = ""
stripped = ""
parts = ()

string = "It was a {Adjective} and {Adjective} {Noun}."

# Required test functions
def read_template(str):
    """
    If the file exists, this function opens the file.
    Then it reads the file and appends its content to
    a global variable called saved contents
    If the file doesn't exist, an exception is raised
    notifying user that file doesn't exist. 
    Then the file closes.
    """
    with open(str, "r") as file:
        try:
            contents = file.read()
            print(contents)
            return contents
        except FileNotFoundError:
            return 'This file does not exist'

def parse_template(string):
    """
    This function takes an incoming string and strips everything
    inside curly brackets out, and puts them into a "parts" tuple.
    Then it replaces the original string with a "stripped"
    version of the string.
    """

    stripped = string

    parts = tuple(re.findall(r"\{(.*?)\}", stripped))

    string = re.sub(r"\{(.*?)\}", "{}", stripped)

    print(string, parts)
    return (string, parts)

    

def merge(str, tuple):
    """
    Function takes a string and a tuple as parameters.
    The string is formatted with the tuple to fill in the blanks.
    """

    return str.format(*tuple)