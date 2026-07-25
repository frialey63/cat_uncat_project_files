#!/usr/bin/python3

import os
import sys

NL = '\n'

lines = []
outputFile = ''

def uncat_file():
    os.makedirs(os.path.dirname(outputFile), exist_ok = True)

    with open(outputFile, 'w') as f:
        f.write(''.join(lines))

def main():
    global lines
    global outputFile

    if len(sys.argv) == 1:
        print('usage: uncat_project_files.py <inputFile>')
        exit(1)

    inputFile = sys.argv[1]
    
    if not os.path.exists(inputFile):
        print('non-existent file: ' + inputFile)
        exit(1)

    with open(inputFile, 'r') as f:
        count = -1

        for line in f:
            if not outputFile:
                outputFile = line.rstrip(NL)
            elif count == -1:
                count = int(line)
            elif count > 0:
                lines += line
                count -= 1
            else:
                uncat_file()
                outputFile = line.rstrip(NL)
                count = -1
                lines = []

    if len(lines) > 0:
        uncat_file()

if __name__=="__main__":
    main()
