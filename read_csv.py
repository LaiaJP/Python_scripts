#!/usr/bin/python

import csv
data = open("Fe2_pH_titration_data", "w")
with open('190722_R52A_THB1_Fe2_pH_titration_good_scans.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		data.write("%s\n" % row)	
data.close()		





#f.write((row))
#	f.close()		


#		if line_count ==0:
#			print(f'\t{row[1]}')
#			line_count +=1
#		else:
#			print(f'\t{row[0]} {row[1]} {row[2]}')
#			line_count += 1
#	print(f'Processed {line_count} lines')

