#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '01-Recruitment-Trials-Bootcamp-Python-Basics'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Python Strings
# 
# Welcome back recruit! It is time for you to learn about one of most basic fundamental data types in Python, the string. What is a string? Formally, **a string is an ordered sequence of characters**. Two key words here, **ordered** and **characters.** Ordered means that we will be able to use *indexing* and *slicing* to grab elements from the string. Characters hints at the fact that strings are more flexible than just using the alphabet, we'll see they can also hold other types of characters.
#%% [markdown]
# ## Creating strings.

#%%
# Comment. Won't show up when you run a script.


#%%
# Single or double quotes are okay.
'hello'


#%%
"hello"


#%%
# Keep in mind potential errors
#'I'm not a spy!


#%%
# Use another set of quotes to capture that inside single quote
" I'm not a spy! "

#%% [markdown]
# ## Basic Printing of Strings
# 
# In the jupyter notebook, a single string in a cell is automatically returned back. However, this is different than printing a string. Printing a string allows us to have multiple outputs. Let's see some useful examples:

#%%
'one'
'two'


#%%
print('one')
print('two')


#%%
print("Special Codes")
print('this is a new line \n notice how this prints')
print('this is a tab \t notice how this prints')
print("Notice how they both follow the general escape character of backslash ")

#%% [markdown]
# ## Indexing and Slicing
# 
# Recall that strings are *ordered sequences* of characters in order. This means we can "grab" single characters (indexing) or grab sub-sections of the string (slicing).
#%% [markdown]
# ### Indexing
# 
# Indexing starts a 0, so the string hello:
# 
#     character:    h    e    l   l   o
#     index:        0    1    2   3   4
#     
# You can use square brackets to grab single characters

#%%
word = "hello"


#%%
word[0]


#%%
word[3]

#%% [markdown]
# Python also supports reverse indexing:
# 
#     character:        h     e     l    l    o
#     index:            0     1     2    3    4
#     reverse index:    0    -4    -3   -2   -1  
#     
# Reverse indexing is used commonly to grab the last "chunk" of a sequence.

#%%
word[-1]

#%% [markdown]
# ### Slicing
# 
# We can grab entire subsections of a string with *slice* notation.
# 
# This is the notation:
# 
#     [start:stop:step]
# 
# Key things to note:
# 
# 1. The starting index direclty corresponds to where your slice will start
# 2. The stop index corresponds to where you slice will go up to. **It does not include this index character!**
# 3. The step size is how many characters you skip as you go grab the next one.
# 
# Let's see some examples

#%%
alpha = 'abcdef'


#%%
# NOTICE HOW d IS NOT INCLUDED!
alpha[0:3]


#%%
alpha[0:4]


#%%
alpha[2:4]


#%%
alpha[2:]


#%%
alpha[:2]


#%%
alpha[0:6:2]

#%% [markdown]
# ## Basic String Methods
# 
# Methods are actions you can call off an object usually in the form .method_name() notice the closed parenthesis at the end. Strings have many, many methods which you can check with the Tab functionality in jupyter notebooks, let's go over some of the more useful ones!

#%%
basic = "Hello world I am still a recruit"


#%%
basic.upper()


#%%
basic.lower()


#%%
# Preview, we'll learn about lists later on!
basic.split()


#%%
basic.split('I')

#%% [markdown]
# # Print Formatting
# 
# You can use the .format() method off a string, to perform what is formally known as **string interpolation**, essentially inserting variables when printing a string.

#%%
user_name = "Recruit"


#%%
print("Welcome {}".format(user_name))


#%%
action = 'run'


#%%
print("The {} needs to {}".format(user_name,action))


#%%
print("The {a} needs to {b}".format(a=user_name,b=action))


#%%
print("The {b} needs to {a}".format(a=user_name,b=action))

#%% [markdown]
# ### Formatting Numbers

#%%
num = 123.6789
print("The code is: {}".format(num))


#%%
print("The code is: {:.1f}".format(num))


#%%
print("The code is: {:.2f}".format(num))


#%%
print("The code is: {:.3f}".format(num))


#%%
print("The code is: {:.4f}".format(num))

#%% [markdown]
# Excellent work recruit!

