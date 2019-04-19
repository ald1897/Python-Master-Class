#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '01-Recruitment-Trials-Bootcamp-Python-Basics'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Working with Simple Text Files
# 
# In the field as an agent, you will need to be able to open files and work with them programmatically. Python can easily handle working with .txt files (later on you will be trained in working with other file formats, such as .csv or .pdf). Let's go over best practices for working with simple text files in Python.
# 
# ## Opening a File
# 
# Let's being by opening the file test.txt that is located in the same directory as this notebook. For now we will work with files located in the **same directory as the notebook or .py script** you are using. 
# 
# It is very easy to get an error on this step:

#%%
errorfile = open('wrong_name.txt')

#%% [markdown]
# This means two possible things occured, either the name of the file is wrong, or you didn't provide the correct file path (more on that later).
# 
# Let's now provide the correct file name:

#%%
myfile = open('test_file.txt')

#%% [markdown]
# Now we can call various read methods off this text file:
# 
# .read() returns the entire contents as a string:

#%%
myfile.read()

#%% [markdown]
# If you run this again, you will recieve a blank:

#%%
myfile.read()

#%% [markdown]
# That is because the "cursor" is at the end of the file. You can reset the cursor to the start using seek:

#%%
myfile.seek(0)


#%%
myfile.read()

#%% [markdown]
# **readlines()**
# 
# Because so many files often have line breaks (\n) often people want to use these as separators and read in the entire text file as list, where each item in the list is a string representing a line in the text file.

#%%
myfile.seek(0)


#%%
myfile.readlines()

#%% [markdown]
# ____
#%% [markdown]
# ### File Locations
# 
# 
# 
# If want to open files at another location on your computer, simply pass in the entire file path.
# 
# For Windows you need to use double \\ so python doesn't treat the second \ as an escape character, a file path is in the form:
# 
#     myfile = open("C:\\Users\\YourUserName\\Home\\Folder\\myfile.txt")
#     
# For MacOS and Linux you use slashes in the opposite direction:
# 
#     myfile = open("/Users/YouUserName/Folder/myfile.txt")
#%% [markdown]
# Let's see a full example

#%%
myfile = open('G:\\Projects\\Python-Master-Class\\02-Field-Readiness-Exam-1\\exam.txt','r')
lines = myfile.read()
print(lines)
myfile.close()
linelist = [lines.split('\n')]
print(linelist)
#%% [markdown]
# ### Best Practice
# 
# Often best practice is to use the **with** statement for opening files, this allows you to not worry about closing the file after you open it. Here is the syntax:

#%%
with open('test_file.txt') as myfile:
    # Notice the indentation!
    # We'll discuss this a lot more later on
    lines = myfile.read()
    
    
# File auto closed after this with statment


#%%
print(lines)

#%% [markdown]
# ## Read and Write Options
# 
# The open() function has a second parameter that allows you to specify whether you only want to be able to read the file, or write to it as well, or do both.
# 
# Here is a table of some of the important options:
#%% [markdown]
# <table>
# <tr>
# <th style="text-align:center;">Modes &amp; Description</th>
# </tr>
# <tr>
# <td><p><b>r</b></p>
# <p>Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.</p></td>
# </tr>
# 
# <tr>
# <td><p><b>r+</b></p>
# <p>Opens a file for both reading and writing. The file pointer placed at the beginning of the file.</p></td>
# </tr>
# <tr>
# <td><p><b>w</b></p>
# <p>Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.</p></td>
# </tr>
# <tr>
# <td><p><b>w+</b></p>
# <p>Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.</p></td>
# </tr> 
# <tr>
# <td><p><b>a</b></p>
# <p>Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.</p></td>
# </tr> 
# <tr>
# <td><p><b>ab</b></p>
# <p>Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.</p></td>
# </tr> 
# <tr>
# <td><p><b>a+</b></p>
# <p>Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.</p></td>
# </tr> 
# </table>

#%%
f = open('second_file.txt')
f.read()


#%%
f = open('second_file.txt')
f.write("new line")

#%% [markdown]
# Now let's add in the 'w' code

#%%
f = open('test_file.txt','w')
# Returns the number of characters written
f.write('new line')


#%%
f.close()


#%%
f = open('test_file.txt')
f.read()

#%% [markdown]
# Notice how the entire file has been overwritten! If you want to add to the file, you need to use the **'a'** append mode for writing to it.

#%%
f = open('totally_new_file.txt','w+')
f.write("I Created a new file")
f.close()

#%% [markdown]
# Okay recruit! Time to see if any of that stuck with you! Let's get you going on your first field readiness exam!

