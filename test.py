# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 16:13:23 2018

@author: Teo
"""

from AFN import AFN

def main():
    afn = AFN()
    afn.add_node()
    afn.add_node()
    afn.add_edge("1","2")
    for i in afn.get_edges():
        print(i)
    
if __name__=="__main__":
    main()