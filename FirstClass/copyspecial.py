#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

# +++your code here+++
# Write functions and modify main() to call them


def get_special_paths(dir):
    special_files = []
    paths = []
    files_in_dir = os.listdir(dir)
    for file in files_in_dir:
        if re.search(r'__\w+__', file): special_files.append(file)
    for file in special_files: paths.append(os.path.abspath(os.path.join(dir,file)))
    return paths


def copy_to(paths, to_dir):
    if os.path.exists(to_dir) != True: os.mkdir(to_dir)
    for special_file in paths: shutil.copy(special_file,to_dir)
    return


def zip_to(paths, zippath):
    zip_command = "zip -j " + os.path.abspath(zippath) + ' ' + ' '.join(paths)
    print "running zip with following command:%s" %zip_command
    (status, output) = commands.getstatusoutput(zip_command)
    if status:
        sys.stderr.write(output+'\n')
        sys.exit(1)
    else:
        print "Successful zip to %s" %os.path.abspath(zippath)
    return


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print "usage: [--todir dir][--tozip zipfile] dir [dir ...]"
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print "error: must specify one or more dirs"
        sys.exit(1)

        # +++your code here+++
        # Call your functions
    special_file_paths = get_special_paths(args[0])
    if todir != '': copy_to(special_file_paths, todir)
    elif tozip != '': zip_to(special_file_paths, tozip)
    else: print '\n'.join(special_file_paths)




if __name__ == "__main__":
    main()
