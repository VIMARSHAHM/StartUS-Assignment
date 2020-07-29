# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:42:54 2020

@author: VIMARSHA H M
"""


#Question 2 Password Validator:

# Method 1: 
# =============================================================================
import re
password= input("Enter the Password")
pattern = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[-.]).{1,20}(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])$'
for i in password:
    match = re.search(pattern,password)
if match:
    print(match.group())
else:
    print("pattern not found")

# =============================================================================



# Method 2:
# =============================================================================
# import re
# p= input("Input your password")
# x = True
# while x:  
#     if (len(p)<1 or len(p)>20):
#         break
#     elif not re.search("^[a-z]",p):
#         break
#     elif not re.search("[0-9]",p):
#         break
#     elif not re.search("[A-Z]",p):
#         break
#     elif not re.search("[.-]",p):
#         break
#     elif not re.search("[a-zA-z0-9]$",p):
#         break
#     else:
#         print("Valid Password")
#         x=False
#         break
# 
# if x:
#     print("Not a Valid Password")
# 
# =============================================================================















