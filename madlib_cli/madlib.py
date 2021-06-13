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
            # saved_content = contents
            return contents
        except FileNotFoundError:
            return 'This file does not exist'
        # finally:
        #     print(saved_content)

def parse_template(string):
    """
    This function strips the file's
    contents and breaks it into a "stripped" string
    and a "parts" tuple
    """

    incoming_string = string

    parts = tuple(re.findall(r"\{(.*?)\}", incoming_string))

    string = re.sub(r"\{(.*?)\}", "{}", incoming_string)

    print(string, parts)
    return (string, parts)

    

def test_merge(str, tuple):
    pass