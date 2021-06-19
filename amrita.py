import pandas as pd
import os
 
csv_file = (r"F:\SOB\mempool.csv")
txt_file = (r"F:\SOB\block.txt")

text_list = []

with open(csv_file, "r") as my_input_file:
    for line in my_input_file:
        line = line.split(",")
        text_list.append(",".join(line))

with open(txt_file, "w") as my_output_file:
    #my_output_file.write("#1\n")
   # my_output_file.write("double({},{})\n".format(len(text_list),2))
  
    for line in text_list:
        my_output_file.write("  " + line)
    print('File Successfully written.')
