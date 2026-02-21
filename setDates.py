#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 08:33:02 2026

@author: sidperkins
"""

import re
from datetime import date, timedelta
import random

# define helper functions
def create_date_strings_from_today(num_days):
  """
  Creates a list of strings of dates, starting from today, for a specified number of days.
  Args:
    num_days: The number of consecutive days to include in the list.
  Returns:
    A list of date strings in 'YYYY-MM-DD' format.
  """
  today = date.today()
  date_strings = []

  for day_offset in range(num_days):
    # Calculate the next date
    next_date = today + timedelta(days=day_offset)
    # Convert the date object to a string in 'YYYY-MM-DD' format (ISO 8601 format)
    date_str = '"' + next_date.isoformat() +'"' # or use strftime('%Y-%m-%d')
    date_strings.append(date_str)

  return date_strings

def savefile(outfile, outText):
    out = open(outfile,'w')
    out.write(outText)

def openfile(infile):
    inf = open(infile,'r')
    return inf.read()

# define main function
def main():
    # solicit input from user
    pref = input("\nWelcome to JOURNLE Date Setter!\n\n>>Please choose 1 to replace all blank dates, 8 to clear dates, or 9 to replace ALL dates.\n\n>>")
    print(pref)
    # open the HTML file for journ.le as text
    text = openfile('./index.html')

    if pref == '1':
        # use regular expressions to find the desired text
        re.findall(r'(?<=releaseDate: )""',text)
        
        # compile a regular expression that pulls every releaseDate field
        p = re.compile(r'(?<=releaseDate: )""')
    
        dateN = len(p.findall(text)) # provides number of dates required for assignment
        dateArray = create_date_strings_from_today(dateN)
        
        random.shuffle(dateArray)
        repl_iter = iter(dateArray)
        textNew = re.sub(p, lambda match: next(repl_iter,match.group(0)), text)
        print(textNew)

    elif pref == '8':
    	warn = input('\n\n>> !Proceed with clearing dates (1=proceed)?\n>>')
    	if warn == '1':
            # use regular expressions to find the desired text
            re.findall(r'(?<=releaseDate: )"([^"]*)"',text)
        
            # compile a regular expression that pulls every releaseDate field
            p = re.compile(r'(?<=releaseDate: )"([^"]*)"')

            textNew = re.sub(p,'""',text)
            print(textNew)

    elif pref == '9':
        warn = input('\n\n>> !Proceed with replacing all  dates (1=proceed)?\n>>')
        if warn == '1':
            # use regular expressions to find the desired text
            re.findall(r'(?<=releaseDate: )"([^"]*)"',text)
        
            # compile a regular expression that pulls every releaseDate field
            p = re.compile(r'(?<=releaseDate: )"([^"]*)"')
        
            dateN = len(p.findall(text)) # provides number of dates required for assignment
            dateArray = create_date_strings_from_today(dateN)
            
            random.shuffle(dateArray)
            repl_iter = iter(dateArray)
            textNew = re.sub(p, lambda match: next(repl_iter,match.group(0)), text)
            print(textNew)
    else:
        print ('>> !Invalid selection. Quitting.')
    
    savefile('./indexNew.html',textNew)
    
main()