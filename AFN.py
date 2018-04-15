# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 15:47:07 2018

@author: Teo
"""
from Node import Node

class AFN:
    def __init__(self, nodes=[], edges=[]):
        self.nodes=nodes
        self.edges=edges
    def add_node(self):
        node =Node(len(self.nodes)+1)
        self.nodes.append(node)
        return node.info
    
    def add_edge(self,first,second):
        self.edges.append((first,second))
        
    def get_nodes(self):
        return self.nodes
    
    def get_edges(self):
        return self.edges