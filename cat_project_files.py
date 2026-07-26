#!/usr/bin/python3

import os
import glob
import sys

NL = '\n'
PATTERNS = [ './**/*.MF', './**/*.java', './**/*.properties', './**/*.xml', './**/*.yaml', './**/*.txt']

def list_files_glob(pattern = './**/*.*', recursive = True):
    files = glob.glob(pattern, recursive = True)

    for file in files:
        # files in target have strange line endings and are not necessary
        if not os.path.dirname(file).startswith('./target'):
            process_file(file)

def process_file(file):
    lines = []

    with open(file, 'r') as f:
        lines.extend(f.readlines())
        # check for missing newline at end of file
        if len(lines[-1]) == 1:
            lines[-1] += NL

    with open(outputFile, 'a') as f:
        f.write(file)
        f.write(NL)
        f.write(str(len(lines)))
        f.write(NL)
        f.write(''.join(lines))

def main():
    global outputFile

    if len(sys.argv) == 1:
        print('usage: cat_project_files.py <outputFile>')
        exit(0)

    outputFile = sys.argv[1]

    if os.path.exists(outputFile):
        os.remove(outputFile)

    for p in PATTERNS:
        list_files_glob(pattern = p)

if __name__=="__main__":
    main()
