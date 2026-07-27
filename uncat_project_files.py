#!/usr/bin/python3

import os
import sys

NL = '\n'

inputFile = ''

def process_lines_and_uncat_files():
    outputFile = ''
    lines = []

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
                uncat_file(outputFile, lines)
                outputFile = line.rstrip(NL)
                count = -1
                lines = []

    if len(lines) > 0:
        uncat_file(outputFile, lines)    

def uncat_file(file, lines):
    os.makedirs(os.path.dirname(file), exist_ok = True)

    with open(file, 'w') as f:
        f.write(''.join(lines))

def main():
    global inputFile
    
    if len(sys.argv) == 1:
        print('usage: uncat_project_files.py <inputFile>')
        exit(1)

    inputFile = sys.argv[1]
    
    if not os.path.exists(inputFile):
        print('non-existent file: ' + inputFile)
        exit(1)

    process_lines_and_uncat_files()

if __name__=="__main__":
    main()
