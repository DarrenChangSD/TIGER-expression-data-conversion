'''
    File name: parse_EST.py
    Author: Darren Chang
    Date created: 9/16/2019
    Date last modified: 9/18/2019
    Python Version: 3.6.8
    Created in order to convert TIGER experssion data into csv form for the Oncogenomics Lab.
'''
import csv 
import requests 
import os
import ntpath
import glob
import pandas as pd

#regex
import re

#loading
import itertools
import threading
import time
import sys

#used to search current directory for any txt file
#let user know that there should only be txt files that you want to parse
def get_file(path):
	txt_list = []
	for filename in os.listdir(path):
		if filename.endswith(".txt"):
			txt_list.append(os.path.join(path, filename))
	return txt_list

#parseTXT is used to parse the txt file
def parseTXT(txtfile): 
	#open and read text file
	text_file = open(txtfile, "r")

	#read each line and save it in lines
	lines = text_file.readlines()

	#initialize full and temp list
	full_list = []
	temp_list = []

	#header row assignments
	temp_list.append("gene_ID")
	temp_list.append("tissue_ID")
	temp_list.append("#_of_tags")
	temp_list.append("total_tissue_tags")
	temp_list.append("tissue_name")
	temp_list.append("enrichment_score")
	temp_list.append("-log10(P)_value")

	#add to full list and reset temp list
	full_list.append(temp_list)
	temp_list = []

	#for loop running through each line of the txt file
	for line in lines:
		#regex command to split line elements by white space
		#Example:
		#line 1: r = ['>', '2', 'Tissue', '19', '']
		#line 2: r = ['2', '1', '3.26345', 'bone', '55055', '0.575507', '']
		# '' is a \n (new line) this creates a 7th column we don't want I remove this later
		r = re.split(r"\s", line)

		#case for start of an EST profile indicated by '>'
		#we perform a regex command for each line allowing us to pull data from the r list
		if(r[0]) == '>':
			header_r = r
			gene_ID = r[1]
			temp_list.append(gene_ID)  #add gene ID
			temp_list.append(r[2]) 	   #add Tissue ID
			temp_list.append(r[3])     #add total tags
			temp_list.append('None')   #add total # of tags
			temp_list.append('None')   #add tissue name
			temp_list.append('None')   #add enrichment score
			temp_list.append('None')   #add - log10(P) value
		else:
			temp_list.append(gene_ID)  #add gene ID
			temp_list.append(r[0])	   #add tissue ID
			temp_list.append(r[1])     #add # of tags
			temp_list.append(r[4])     #add total # of tags
			temp_list.append(r[3])     #add tissue name
			temp_list.append(r[2])     #add enrichment score
			temp_list.append(r[5])     #add -log10(P) value		

		#before moving onto the next line we append that line to the full list and reset the temp list
		full_list.append(temp_list)
		temp_list = []
	return full_list
	
#savetoCSV is used to take the output of parseTXT and convert into a csv file
def savetoCSV(full_list, filename): 
  
	#specifying the fields for csv file 
	fields = ['gene_ID', 'tissue_ID', '#_of_tags', 'total_tissue_tags',\
			  'total_tissue_tags', 'enrichment_score', '-log10(P)_value']

	#create the desired csv file name
	filename = filename + '.csv'

	#writing to csv file 
	#double for loop to access individual elements and commma them
	with open(filename, 'w') as csvfile: 
  		for small_list in full_list:
  			for item in small_list:
  				csvfile.write(item + ",")
  			csvfile.write("\n")
	
	#use a little bit of pandas to drop the empty 7th column
	df = pd.read_csv(filename)
	df.drop(df.columns[len(df.columns)-1], axis = 1, inplace = True)
	df.to_csv(filename, index = False)
		
#here is the animation


#main function is used to run the code
def main(): 
	print("start")
	#start of the main get current directory and txt file path
	dir_path = os.getcwd()
	txt_files = get_file(dir_path)

	#start little animation for laoding and user interaction
	done = False
	def animate():
   		for c in itertools.cycle(['|', '/', '-', '\\']):
   			if done:
   				break
   			sys.stdout.write('\rloading ' + c)
   			sys.stdout.flush()
   			time.sleep(0.1)
   		print('\nYour csv file should be in your current directory: ' + os.getcwd())
   		sys.stdout.write('Done!\n')
	t = threading.Thread(target=animate)
	t.start()

	#after looking for all txt files parses that file
	"""WIP have not tried multiple txt file will not work WIP"""
	for file in txt_files:
		full_list = parseTXT(file)
		name = os.path.splitext(ntpath.basename(file))[0]
		
		#store new items in a csv file 
		savetoCSV(full_list, name) 
		done = True
	  
#call to main function here
if __name__ == "__main__": 
	# calling main function 
	main() 

