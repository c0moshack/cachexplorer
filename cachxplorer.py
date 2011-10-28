#!/usr/bin/python
import sys
import os

def directory_parser():
## Search firefox cache directory for files
  

def mime_extractor(files):
## Determine mime type and add to dictionary
  mimedict = {}
  for f in files:
    data = os.popen("file -z " + files)
    string = data.readlines()
    string = splitter(string)
    key = string[0]
    value = string[1]
    mimedict[key] = value 
  return mimedict    

def splitter(string):
## Split value returned from file command 
  for s in string:
    res = s.split(",")
    res = res[0]
    res = res.split(": ")
    return res

def main():
  if len(sys.argv) == 2 :
    print "Usage: firecache.py -f <path to file>"
  elif sys.argv[1] == "--help":
    print "Usage: firecache.py <option> <file>\
    Valid Options:\
    --help\
    --file\
    --full"
  elif sys.argv[1] == "--file":
    print "Checking file for MIME type"
  elif sys.argv[1] == "--full":
    print "Scanning cache diretory"
    mimedict = mime_extractor(sys.argv[2])
    for k in mimedict.keys():
      print "File at",k ,"is of type", mimedict[k]
  else:
    print "Invalid option"

if __name__ == '__main__':
  main()