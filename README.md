# **Mad Lib CLI**

Lab 03 - File IO and Exceptions

* **Author**: Kassie Bradshaw
* **Version**: 1.0.0
* [Link to current PR](https://github.com/kassiebradshaw/madlib-cli/pull/1)

---

## **Overview**

In this assignment you will be creating a command line application which takes advantage of Python's built in capabilities for reading and writing files.

---

## **Feature Tasks**

[x] Create a file called `madlib.py` at the root of `madlib_cli` folder, which will contain all of the Python code that you will write relating to your Madlib game.

[ ] Keeping in mind the concept of [Single Responsibility Principle](https://en.wikipedia.org/wiki/Single_responsibility_principle), build a command line tool which will perform the following:

    [ ] Print a welcome message to the user, explaining the Madlib process and command line interactions
    [x] Read a template Madlib file, and parse that file into usable parts.
    [ ] Prompt the user to submit a series of words to fit each of the required components of the Madlib template
    [ ] With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template.
    [ ] After the resulting Madlib has been completed, provide the completed response back to the user in the command line.
    [ ] Write the completed text to a new file on your file system (in the repo). 
    [ ] Note: A smaller example file is included as well which can be handy when developing/testing.

## **Stretch Goals**

[ ] Figure out / research a way to verify terminal input/output

[ ] Test that completed madlib is properly written to disk with correct content.

---

## **Resources**

* Starter test script is supplied and should be moved into your application's tests folder.
  * [ ] *NOTE:* All included tests must pass as written
  * [ ] You can add more tests if you like

* [Python String format() Method](https://www.w3schools.com/python/ref_string_format.asp)
* [Unpacking Arrays](https://realpython.com/python-kwargs-and-args/#unpacking-with-the-asterisk-operators)

---

## **Getting Started**

* Use `Poetry` to create project named `madlib-cli`
* Create repository on GitHub with name `madlib-cli`

---

## **Change Log**

06-12-2021:

---

## **Collaboration & Credit**

Got help from TA Anthony Beaver

Collaborated with:

* Michael Hendricks
* Garfield Grant
* Marie Marcos

* [Used for help with regex expression to get back ONLY text BETWEEN brackets in a string](https://stackoverflow.com/a/48916501)

* [Used for help with regex expression to replace string with empty brackets](https://appdividend.com/2020/06/10/python-regex-replace-how-to-replace-string-in-python/)
