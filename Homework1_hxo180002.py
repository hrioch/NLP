import sys
import os
import re
import pickle


def checklen():  # This method checks for input filepath "data/data.csv" as a system argument.
    if len(sys.argv) > 1:
        if sys.argv[1] == "data/data.csv" and len(sys.argv) == 2:  # Verifying that path is correct
            readfile(sys.argv[1])  # Send filepath over to the function that actually parses the file.
        else:
            print("File path is not specified to data/data.csv. Please try again.")
    else:
        print("File path is not specified to data/data.csv. Please try again.")


class Person:  # Class to contain specified information about employees, and a function to print it all.
    def __init__(self, last, first, mi, id, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.id = id
        self.phone = phone

    def display(self):
        print("Employee ID: " + self.id)
        print("\t" + self.first + " " + self.mi + " " + self.last)
        print("\t" + self.phone)


def readfile(filepath):  # Function that parses through input file at specific location.
    with open(os.path.join(os.getcwd(), filepath), 'r') as f:  # Opening file
        text_in = f.read()
    lines = text_in.split("\n")  # Splitting each line into a separate entry allows for easy subdivision and looping.
    d = {}  # Creation of dictionary meant for Person objects.
    for line in lines:
        params = line.split(",") # Splitting each line by a comma.
        last = params[0].capitalize()  # Formats last name correctly.
        first = params[1].capitalize()  # Formats first name correctly.
        if params[2] == "":  # This if statement checks for existence of a middle initial. If none, X is placed.
            mi = "X"
        else:
            mi = params[2].capitalize()  # Capitalizes middle initial.
        empid = params[3]  # Preliminary placement of ID into variable, will be used to verify validity.
        match = re.match('^[A-Z]{2}\d{4}$', empid)  # Regex expression to check if formatting is valid.
        while match is None:  # While loop is used to account for multiple errors in reentry.
            print("ID " + empid + " is invalid. Please enter it correctly.")
            empid = input("Format is 2 capital letters followed by 4 digits, no spaces.")
            match = re.match('^[A-Z]{2}\d{4}$', empid)
        empnum = params[4]  # Similar to ID, phone number is placed to be matched against a regex expression.
        matchnum = re.match('^[1-9]\d{2}-\d{3}-\d{4}$', empnum)
        while matchnum is None:
            print("Phone number " + empnum + " is invalid. Please enter it correctly.")
            empnum = input("Format is 3 digits, dash, 3 digits, dash, 4 digits. No spaces.")
            matchnum = re.match('^[1-9]\d{2}-\d{3}-\d{4}$', empnum)
        person = Person(last, first, mi, empid, empnum)  # Entry of information into Person object.
        d[person.id] = person  # Person object is placed into dictionary. ID is the key, Person object is the value.
    main(d)  # Passing dictionary over to main method, which will package/unpackage and print the dictionary.


def main(dictp):  # Main method uses pickle to compress the dictionary, and then open it back up for printing.
    pickle.dump(dictp, open("dict.p", "wb"))  # Pickle file is "dict.p", written in binary.
    newdict = pickle.load(open("dict.p", "rb"))  # The same pickle file is opened back up and placed into a new dict.
    keyslist = newdict.keys()  # Keys are used for access of values in newdict.
    print("Employee list: ")
    print("")
    for key in keyslist:
        p = newdict[key]
        p.display()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    checklen()  # Program starts here, first method called is to check for number of arguments.


