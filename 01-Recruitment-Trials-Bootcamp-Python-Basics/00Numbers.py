#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '01-Recruitment-Trials-Bootcamp-Python-Basics'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Python Numbers
# 
# Welcome recruit! It is time for you to begin your bootcamp by learning the basics. While these ideas may seem simple, they're fundamental enough that we should quickly go over them before tackling more complex topics. Let's begin by discussing the very basics of working with numbers in Python. This should be straight forward.
#%% [markdown]
# ## Main Types of Numbers
# 
# Integers are whole numbers. Float (floating point) numbers are numbers with a decimal point.

#%%
100


#%%
type(100)


#%%
1.2


#%%
type(1.2)


#%%
type(100.0)


#%%
type(100.)

#%% [markdown]
# ### Basic Arithmetic

#%%
#Addition
1+1


#%%
# Subtraction
2-1


#%%
# Multiplication
2*2


#%%
# Division
3/2


#%%
# Division always returns floats!
1/1


#%%
# Powers
2 ** 3


#%%
2 ** (1/2)


#%%
# Order of Operations
1 + 2 * 1000 + 1


#%%
(1 + 2) * (1000+1)

#%% [markdown]
# # Assigning Variables

#%%
a = 2


#%%
type(a)


#%%
a + 3


#%%
b = 3


#%%
a + b


#%%
# Reassignment
a = 1000


#%%
a + b

#%% [markdown]
# ### Reassignment with same variable

#%%
a


#%%
# Keep in mind, if you run this more than once, you will keep running a = a+a!
a = a + a


#%%
a


#%%
a = a + a


#%%
a

#%% [markdown]
# ## Simple Example

#%%
message = 111
hash_code = 346728236


#%%
secret_message = message * hash_code


#%%
secret_message


#%%
decrypted_message = secret_message / hash_code


#%%
decrypted_message

#%% [markdown]
# Excellent work recruit! Time to move on to the other basic data types.

