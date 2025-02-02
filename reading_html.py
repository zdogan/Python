# download mbox.txt from  http://www.py4inf.com/code/mbox.txt and show the path  
fhand = open((r"C:\Users\SEVGI\Desktop\mbox.txt"))
count = 0
for line in fhand:
    count = count + 1
    print ('Line Count:', count)

#7.4 reading files
# Our for loop simply counts the number of lines in the ﬁle and prints them out
