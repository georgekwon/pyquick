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

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_paths(dir):
  filenames = os.listdir(dir)
  special_paths = []
  for filename in filenames:
    #print filename
    if re.search(r'__\w+__', filename):
      special_paths.append(os.path.abspath(os.path.join(dir, filename)))
  return special_paths

def print_special_paths(dir):
  for special_path in get_paths(dir):
    print special_path

def copy_to(paths, dir):
  if not os.path.exists(paths):
    os.mkdir(paths)
    print 'made directory'+paths
  for special_path in get_paths(dir):
    shutil.copy(special_path, paths)

def zip_to(paths,dir):
  pathsstr = ''
  for path in get_paths(dir):
    pathsstr = pathsstr+' '+path
  #print pathsstr
  command = 'zip -j '+paths+pathsstr
  #print command
  print 'Command I\'m going to do:'+command
  os.system(command)


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
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
  for arg in args:
    if len(todir) != 0:
      copy_to(todir, arg)

    if len(tozip) != 0:
      zip_to(tozip, arg)

    if len(todir) ==0 and len(tozip) == 0:
      print_special_paths(arg)


if __name__ == "__main__":
  main()
