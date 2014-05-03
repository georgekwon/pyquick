#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
'''
1) read in the apache log file and use regex (expression btwn spaces) to find puzzle URLs
2) remove duplicates, order alphabetically, print one per line
3) write a function that retrieves all the images and saves them to an output dir
'''

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  #filename = 'animal_code.google.com'
  f = open(filename, 'rU')
  text = f.read()
  all_urls = re.findall(r'GET\ (\S*puzzle\S*)\ HTTP', text)
  img_urls = []
  for url in all_urls:
    urlfull = 'http://'+'code.google.com'+url
    if urlfull not in img_urls:
      img_urls.append(urlfull)

  img_urls.sort()
  return img_urls


def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)
  index = file(os.path.join(dest_dir, 'index.html'), 'w')
  index.write('<html><body>\n')

  img_index = 1
  for img_url in img_urls:
    print 'Retrieving image...'
    filename = 'img'+str(img_index)+'.jpg'
    urllib.urlretrieve(img_url, dest_dir+filename)
    img_index += 1
    index.write('<img src = "%s">' % filename)

  index.write('\n</body></html>\n')


def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
