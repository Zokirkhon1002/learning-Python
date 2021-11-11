# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 01:54:52 2021

@author: Zokirkhon
"""

###1
### Ruchnoy
# def get_full_name(firstName, secondName):
#     return f"{firstName} {secondName}".title();

# print(get_full_name("zokirkhon","kotibkhonov"))





###2
def get_full_name(firstName, secondName, otasiningIsmi=""):
    if otasiningIsmi:
        return f"{firstName} {otasiningIsmi} {secondName}".title();
    else:
        return f"{firstName} {secondName}".title();












































