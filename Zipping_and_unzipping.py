'''Develop a script that zips a folder containing multiple text files into a single compressed
file. Include a function to unzip the compressed file and restore the original folder
structure.'''
from zipfile import *
def zipfolder():
  zipname=input("Enter zip file name:")
  f=ZipFile(zipname, "w", ZIP_DEFLATED)
  n=int(input("Enter number of files:"))
  for i in range(n):
    name=input("Enter file name:")
    f.write(name)
  f.close()
  print("Folder Zipped Successfully")
def unzipfolder():
  zipname=input("Enter zip file to extract:")
  outf=input("Enter folder to unzip:")
  f=ZipFile(zipname, "r")
  files=f.namelist()
  for file in files:
    f.extract(file, outf)
  f.close()
  print("Folder Unzipped Successfully")
zipfolder()
unzipfolder()
