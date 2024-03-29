#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """

  f = open(filename, 'rU')
  text = f.read()

  #regular expression to find year
  match = re.search(r'Popularity in (\d\d\d\d)', text)
  year = match.group(1)

  #extract names and rank number into tuples
  touples = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)

  #use touples to create name and rank key value pairs
  namedict = {}
  for t in touples:
    namedict[t[1]] = t[0]
    namedict[t[2]] = t[0]

  #create a single string of all the "name year" ranks and put the year up front
  text = []
  for k, v in sorted(namedict.items()):
    text.append(k+' '+v)
  text.insert(0, year)
  #for key in sorted(namedict.keys()):
  #  print key,':',namedict[key]
  return text


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  #print summaries to screen
  if not summary:
    for a in args:
      text = '\n'.join(extract_names(a)) + '\n'
      print text

  #print summaries to files
  if summary:
    for a in args:
      text = '\n'.join(extract_names(a)) + '\n'
      f = open(a+'.summary', 'w')
      f.write(text)

if __name__ == '__main__':
  main()

