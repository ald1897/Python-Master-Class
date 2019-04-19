#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '02-Field-Readiness-Exam-1'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Field Readiness Exam
# 
# ** Welcome to your first FRE - Field Readiness Exam Recruit! This is where we test your skills to see if you qualify to become a full field agent. Complete the tasks below to the best of your ability. Immediately after this we will go over the solutions and check your performance. **
# _______
#%% [markdown]
# ### Task 1
# 
# **Open the exam.txt file with Python and with only read permission and store the contents in a list called exam_lines**

#%%
# Code Here
exam_lines = []
with open('G:\\Projects\\Python-Master-Class\\02-Field-Readiness-Exam-1\\exam.txt','r') as myfile:
    # Notice the indentation!
    # We'll discuss this a lot more later on
	lines = myfile.read()
	exam_lines = [lines.split('\n')]
print(exam_lines)


#%%
# Your output should look something like this:

#%% [markdown]
# ### Task 2
# 
# How many lines does this file have?

#%%
# Your output should look something like this:

#%% [markdown]
# ### Task 3
# 
# Print out the 5th line of the text file.

#%%
# Your output should look something like this:

#%% [markdown]
# ### Task 4
# 
# Grab the last line of the text file and save it to a variable called last.

#%%
# Your output should look something like this:

#%% [markdown]
# ### Task 5
# 
# Use indexing to grab the letter 'o' from the last line of the file.

#%%
# Your output should look something like this:

#%% [markdown]
# ### Task 6
# 
# How could you use Python to count how many words there are in the last line?

#%%
# Your output should look something like this:

#%% [markdown]
# ### Task 7
# 
# What data types are returned by the following lines of code:
# 
#     1.)  2/3
#     2.)  2 + 2.0
#     3.)  1 + 1
#     4.)  "2" + "2"
#     5.)  1 > 2
#     
# Try to do these in your head before checking by running the code in python.

#%%
# No need to write down your answers, just use this cell to self check is necessary.

#%% [markdown]
# ### Task 8
# 
# Let's check how well you understand indexing and key calls. Here we present to you a set of dictionaries and lists that are nested inside a single dictionary **d**. While this is an unrealistic representation of how you would use these data types in the field, this is just for practice:

#%%
d = {"levelone":[1,2,{'leveltwo':[5,6,[1,['get me please']]]}]}

#%% [markdown]
# Your task is to retrieve the string "get me please" from the dictionary with stacked index and key calls.
# 
# Hint: Approach this step by step, slowly adding on more and more index calls. Recall that you can use .keys() to figure out what keys are in a  dictionary.

#%%
# Your output should look something like this:

#%% [markdown]
# ### Bonus Task
# 
# How many unique integers are in this list? (You will need to use a casting method we haven't shown you yet)

#%%
mylist = [1,2,3,4,5,6,4,3,2,1,2,3,4,5,6,6,7,8,5,6,7,8,9,8,9,8,9,7,10,123,1,2,2,3,1,3,2,4,1,4,4,1,2,2,22,3,4,1,4,1]


#%%
# Your output should look something like this:

#%% [markdown]
# Excellent work recruit, now that you are done with the basics of data types and storage with Python, let's move on to learning about control flow with Python.

