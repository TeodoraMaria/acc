# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 15:53:00 2018

@author: Teo
"""

class Node:
    def __init__(self,info="",isInitial=False,isFinal=False):
        self.info=info
        self.isInitial=isInitial
        self.isFinal=isFinal
    
    def setFinal(self,isFinal):
        self.isFinal=isFinal
    def setInitial(self,isInitial):
        self.isInitial=isInitial
    
    def setStatesTrue(self):
        self.isFinal=True
        self.isInitial=True