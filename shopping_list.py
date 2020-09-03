# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 12:09:48 2020

@author: kucza
"""

import pandas as pd


class ShoppingList:
    
    last_added = -1
    total_price = -1
    
    def __init__(self, columns = ['Name', 'Price', 'Room', 'Category', 'Shop', 'URL', 'Comments'], name = '_'):
        
        if name != '_':
            self.data = pd.read_csv(name, sep = ';')
        else:
            self.data = pd.DataFrame(columns = columns)

    
    def add_item(self, dict_to_append):
        
        #prints an error if a name already exists in the df
        if  dict_to_append['Name'] in self.data['Name'].tolist():
            print('An item with the same name already exists')
            return
        
        #appends the dict to the df
        self.data = self.data.append(dict_to_append, ignore_index = True)
        
        #saves last added item
        self.last_added = self.data.index[self.data['Name'] == dict_to_append['Name']]
        
        #updates total price
        self.total_price = self.data['Price'].sum()
        
        return self
    
    def delete_item(self, last_added = 'no', delete_index = []):
        
        #deletes last added item
        if last_added == 'yes':
            
            #checks if the last_added attribute is updated
            if self.last_added == -1:
                print('Last added item has been deleted or no items have been added yet')
                return
            
            self.data = self.data.drop(self.last_added)

            #update last_added attribute
            self.last_added = -1
            
            return self       
        
        #delete item by index
        for item in enumerate(delete_index):
            self.data = self.data.drop(item[1])
            
        #update total price
        self.total_price = self.data['Price'].sum()
        
        return self
        
    def pivot_price(self, variables):
        
        #check if there is some data
        if len(self.data) == 0:
            print('The list does not contain any items. Add some items to the list first.')
            return
        
        pivot = self.data.pivot_table(values = 'Price', index = variables, aggfunc='sum')
        return pivot
        
    def save_list(self, name):
        self.data.to_csv(name, sep = ';')
        
    def read_list(self, name):
        self.data = pd.read_csv(name, sep = ';')
    
    def new_list(self):
        #deletes all rows and resets the attributes
        self.data = self.data[0:0]
        self.last_added = -1
        self.total_price = -1
        
        return self
        
        
        
        
        
        