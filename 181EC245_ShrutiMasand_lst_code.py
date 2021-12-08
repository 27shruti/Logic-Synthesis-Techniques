"""
Created on Fri Oct 1 20:33:14 2020

@author: Shruti Masand & Vishal Shukla
"""

######################LST Project - SHRUTI MASAND-181EC245, VISHAL SHUKLA-171EC252#######################

#Import all libraries required for the code to function properly

#Pyeda library for implementing the data structures and algorithms 
#necessary for performing logic synthesis and verification

import pyeda
from pyeda.boolalg.boolfunc import *
from pyeda.boolalg.expr import exprvar
from pyeda.inter import *
from pyeda.boolalg.bfarray import exprvars

#Graphviz library for using the graphviz tool in order to
#visualise the constructed ROBDD

from graphviz import Source

#cofactQ1 function for calculating cofactors

def cofactQ1(expression, variable):
    tmp = Function
    t = tmp.cofactors(expression, variable)
    return t

#bdd function for calculating and displaying the ROBDD

def bdd(expression):
    # a, b, c, d = map(bddvar, 'abcd')
    #f = expression
    f = expr2bdd(expression)
    gv = Source(f.to_dot())
    gv.render('render_pdf_name',view=True)
    
#define_var function for defining the variables as boolean variables    

def define_var(var_array):
    for i in var_array:
        #r = var_array[i]
        #print(exprvar(r))
        #s = tuple(i)
        #print(s)
        r = exprvar(str(i))
        print(r)
                

f = Function()

######################################### INPUT THE FUNCTION HERE ###########################################

expression = '(a&b)|(b&c)|(a&c)'
f = expr(expression)

######################################## DEFINE THE VARIABLES HERE ##########################################

a, b, c = map(exprvar, 'abc')

#############################################################################################################

varlist = sorted(list(f.support))
print(varlist,'\n',f)           

var_new = []
var_dict = dict()
for i in varlist:
    var_new.append(str(i))
#print(var_new)

for i in var_new:
    var_dict[i] = str(i)
#print(var_dict)

var_join = ''.join(var_new)
#print(var_join)    

#varlist = map(exprvar, var_join)
#define_var(varlist)

for i in var_dict:
        #r = var_array[i]
        #print(exprvar(r))
        #s = tuple(i)
        #print(s)
        for j in var_new:
            #print(type(j))
            j = i
            #print(type(j))
        #print(type(i))
        #i = exprvar(str(i))
        #print(type(i))

########################## INPUT THE VARIABLES WRT WHICH COFACTORS HAVE TO BE CALCULATED ####################        
var_list = [a,b]

print("Cofactors need to be calculated wrt the following variables : ")
print(var_list)

############################### CALLING THE COFATQ1 FUNCTION ###############################################
u = cofactQ1(f,var_list)

############################# LAST RESULT TO GET PRINTED = COFACTORS #######################################
print("Cofactors of the given boolean expression wrt the given variables are given by : ")
print(u)

################################ CALLING THE BDD FUNCTION ##################################################
v = bdd(f)

############################################ END OF CODE ###################################################
