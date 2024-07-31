"""Singly Linked List"""
 

class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class SLL:
    def __init__(self, start=None):
        self.start = start
        
    def is_empty(self):
        return self.start is None
    def insert_at_start(self, data):
        
    
#driver Code
mylist=SLL()    
    
