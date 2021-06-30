
import sys
import csv
import os

def parse(file_name, directory_path): # does initial parsing of file
  file_object = open(directory_path + '/' + file_name, 'r')
  fields = []
  for line in file_object:
    if ':' in line:
      fields.append(line)
  return fields

def get_dimensions(file_name, directory_path): # manually parse pipe size table data
  file_object = open(directory_path + '/'+ file_name, 'r')
  fields = []
  
  for line in file_object: # isolate all non-field entries
    if ':' not in line:
      fields.append(line)

  trimmed = fields  # max range of table
  rem_nl = []

  for t in trimmed: # remove new line chars
    if '\n' != t:
      rem_nl.append(t.rstrip(t[-1]))

  if (len(rem_nl) !=  0):
    first_num = rem_nl[0].strip('\n')
    while first_num.isdigit() is False:
        rem_nl.pop(0)
        if len(rem_nl) == 0:
          break
        first_num = rem_nl[0].strip('\n')

    end = 0
    for item in rem_nl: # find end of table
      if '±' in item:
        break
      else:
        end += 1
    
    rem_nl = rem_nl[:end]

  while len(rem_nl) != 24: # resize final product
    rem_nl.append(' ')

  return rem_nl

def csv_row(fields): #creates row of data in form of list to be added to csv later
  values = []
  for item in fields:
    portioned = item.split(':')
    if len(portioned) is 2:
      values.append(portioned[1].rstrip(portioned[1][-1]))
    elif len(portioned) is 1:
      values.append(' ')
    elif len(portioned) is 3:
      values.append(portioned[2].rstrip(portioned[2][-1]))
  
  return values

def get_all_rows(directory_path) : # comb through directory and extract data from each into lists
  all_rows  = []
  for item in os.listdir(directory_path):
    row = csv_row(parse(item, directory_path))
    row = row + get_dimensions(item, directory_path)
    all_rows.append(row)
  return all_rows

size_fields = ['SizeA', 'MaterialA', 'InvA', 'DropInvA',
               'SizeB', 'MaterialB', 'InvB', 'DropInvB',
               'SizeC', 'MaterialC', 'InvC', 'DropInvC',
               'SizeD', 'MaterialD', 'InvD', 'DropInvD',
               'SizeE', 'MaterialE', 'InvE', 'DropInvE',
               'SizeF', 'MaterialF', 'InvF', 'DropInvF'] # pipe size, material, invert fields from table

# Parameter directory: file path of folder of txt files
# Parameter csv_filename: intended output file
def load_all(directory, csv_filename): # build a csv file
  first = []
  for item in parse(os.listdir(directory)[0], directory): # get first row of csv for fields
    if item.split(':')[0] is not '':
      first.append(item.split(':')[0])
  
  first = first + size_fields 
  for val in first:
    val = val.replace('\n', '')
  
  with open(csv_filename, 'w', newline='') as file: # open or create new csv file
    writer = csv.writer(file) 
    writer.writerow(first) # write title row
    writer.writerows(get_all_rows(directory)) # write rest of rows
    file.close() # close file

load_all('/content/txts', 'output2.csv')
