#!/usr/bin/python
#import sys
import os
#import optparse
import argparse

def directory_parser(d):
## Search Firefox cache directory for files
  flist = []
  folderCount = 0
  for top, dirs, files in os.walk(d):
    folderCount += len(dirs)
    for nm in files:      
      flist.append(os.path.join(top, nm))
  print folderCount, "directories scanned\n"
  return flist

def mime_extractor(files):
## Determine MIME type and add to dictionary
  mimedict = {}
  for f in files:
    data = os.popen("file -z " + f)
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
  # Define available options
  oparser = argparse.ArgumentParser(usage="%prog [options] arg")
  oparser.add_argument("-f", "--file", dest="file", help = "scan single file", metavar="file")
  oparser.add_argument("-F", "--full", dest="full", help = "recursively scan a directory", metavar="full")
  oparser.add_argument("-v", "--verbose", action="store_true", dest="verbose")
  oparser.add_argument("-q", "--quiet", action="store_false", dest="verbose")
  
  args = oparser.parse_args()
  
  #Check if verbose option was set
  if args.verbose == True :
    if args.file:
      print "Scanning...%s" % args.file
    if args.full:
      print "Scanning...%s" % args.full
  
  #Check if scanning single file    
  if args.file != None:
    print "Checking file for MIME type"
  
  #Check if scanning directory
  if args.full != None:
    print "Scanning cache directory", args.full
    mimedict = mime_extractor(directory_parser(args.full))
    for k in mimedict.keys():
      print "----"
      print "File:", k 
      print "Type:", mimedict[k].strip()

if __name__ == '__main__':
  main()  
