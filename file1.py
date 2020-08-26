#!/bin/python3

def hello():
  print('hi from hello')
  

def parsefile(filename):
    fh = open(filename)
    print(fh.read())
