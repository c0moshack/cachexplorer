#!/usr/bin/python
import os
import argparse
import fnmatch

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

def mime_extractor(f):
## Determine MIME type and add to dictionary
  data = os.popen("file -z " + f)
  string = data.readlines()
  string = splitter(string)
  #key = string[0]
  value = string[1]
  return value    

def splitter(string):
## Split value returned from file command 
  for s in string:
    res = s.split(",")
    res = res[0]
    res = res.split(": ")
  return res

def fullScan(path):
  mimedict = {}
  #Get file types
  for f in directory_parser(path):
    mimedict[f] = mime_extractor(f) 
  #print output
  for k in mimedict.keys():
    print "----"
    print "File:", k 
    print "Type:", mimedict[k].strip()
    
def filescan(userfile):
  return mime_extractor(userfile)
  

def getfirefoxprofile():
  path = os.path.expandvars("/home/$USER/.mozilla/firefox/")
  for profile in os.listdir(path):
    if fnmatch.fnmatch(profile, '*.default'):
      return path + profile + "/Cache/"  
  
def main():
  # Define available options
  oparser = argparse.ArgumentParser(prog='cachexplorer.py', usage='%(prog)s [options]')
  oparser.add_argument("-f", "--file", dest="file", help = "scan single file", metavar="<file>")
  oparser.add_argument("-F", "--full", dest="full", help = "recursively scan a directory", metavar="<full>")
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
    print "Type:", filescan(args.file)
  
  #Check if scanning directory
  if args.full != None:
    print "Scanning cache directory of: %s" % args.full
    if args.full == "firefox":
      fullScan(getfirefoxprofile())  
    

if __name__ == '__main__':
  main()  
