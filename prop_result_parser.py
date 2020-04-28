import sys

filename = sys.argv[1]

with open(filename) as file:
    text = file.read()

    new_text = ""

    for line in text.split("\n"):
        if line.find("Command line:") != -1:
            new_text += line + "\n"
        if line.find("Simulating:") != -1:
            new_text += line + "\n"
        if line.find("Result") != -1:
            new_text += line + "\n"

    print(new_text)
