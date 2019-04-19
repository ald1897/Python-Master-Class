#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '01-Recruitment-Trials-Bootcamp-Python-Basics'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Python Lists
# 
# We've learned that strings are sequences of characters. Similarly, lists are sequences of objects, they can hold a variety of data types in order, and they follow the same sequence and indexing bracket rules that strings do. They can also take in mixed data types. 
# 
# Let's explore some useful examples:

#%%
my_list = [1,2,3]


#%%
my_list


#%%
my_list2 = ['a','b','c']


#%%
my_list2


#%%
a = 100
b = 200
c = 300
my_list3 = [a,b,c]


#%%
my_list

#%% [markdown]
# ## Indexing and Slicing
# 
# This works the same as in a string!

#%%
mylist = ['a','b','c','d']


#%%
mylist[0]


#%%
mylist[0:3]

#%% [markdown]
# ### The len function
# 
# Python has built in functions that you can call. We'll slowly introduce more of them as we need them. One useful built in function is the **len** function which returns back the length of an object. Notice how its syntax highlighted, indicating that its a built in function. If you see this auto-highlighting occur when choosing your own variable name, then you should choose a different variable name, so you don't accidentally overwrite the function.

#%%
len('string')


#%%
len(my_list)

#%% [markdown]
# ## Useful List Methods
# 
# Methods are actions you can call off a function. Their typical format is:
# 
#     mylist = [1,2,3]
#     mylist.some_method()
#     
# You must call the parenthesis to execute the method! Let's go through a few useful ones pertaining to lists.

#%%
mylist = [1,2,3]


#%%
mylist.append(4)


#%%
mylist


#%%
mylist.pop()


#%%
mylist


#%%
mylist.append


#%%
mylist.append(4)


#%%
mylist


#%%
item = mylist.pop()


#%%
item


#%%
mylist


#%%
first_item = mylist.pop(0)


#%%
first_item


#%%
mylist


#%%
mylist = [1,2,3]


#%%
# This method doesn't return anything.
# Instead it performs the action "in-place" , or on the list itself without returning anything.
mylist.reverse()


#%%
mylist


#%%
# Also in place
mylist.sort()


#%%
mylist


#%%
# THIS WON'T WORK!
result = mylist.reverse()


#%%
# Doesn't return anything
result


#%%
print(result)


#%%
mylist = [1,2,3]
mylist.insert(0,'NEW')


#%%
mylist

#%% [markdown]
# ## Nested Lists
# 
# Lists can hold other lists! This is called a nested list. Let's see some examples.

#%%
new_list = [1,2,3,['a','b','c']]


#%%
type(new_list)


#%%
new_list[3]


#%%
new_list[3][0]

#%% [markdown]
# That is all for now, we'll be using lists a lot throughout your training!

