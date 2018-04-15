# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 15:21:26 2018

@author: Teo
"""

def Expr(reg, alf):
    if len(reg)==1:
        if reg in alf:
            #deseneaza caz1
        elif reg=='λ':
            #deseneaza caz 2
        else:
            #deseneza caz 3
    elif '∪' in reg:
        prima.ultima=Expr()
        primb,ultimb=Expr()
        #deseneaza cazul 4
    elif '*' in reg:
        prim, ultim=Expr()
        #deseneaza cazul 6
        return prim,ultim
    else:
        prima,ultima=Expr()
        primb,ultimb=Expr()
        #deseneaza leg cazul 5
        return prima,ultimb
        