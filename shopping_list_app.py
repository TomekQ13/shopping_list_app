# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 13:06:59 2020

@author: kucza
"""

import streamlit as st
import shopping_list as sl
import os

st.title('Shopping list')

@st.cache(allow_output_mutation=True)
def init_class():
    shopping_list = sl.ShoppingList()
    return shopping_list

shop_list = init_class()

name = st.text_input("Name")
price = st.text_input("Price")
room = st.text_input("Room")
category = st.text_input("Category")
shop = st.text_input("Shop")
url = st.text_input("URL")
comments = st.text_input("Comments")

dict_to_append = {
    'Name' : name,
    'Price' : price,
    'Room' : room,
    'Category' : category,
    'Shop': shop,
    'URL' : url,
    'Comments': comments    
}

#adding item button
if st.button('Add item to the list'):
    #if price or name are empty then print an error
    if len(price) == 0 or len(name) == 0:
        st.error('Name or price cannot be empty')
    else:
        if dict_to_append['Name'] in shop_list.data['Name'].tolist():
            st.write('An item with the same name already exists')
        else:
            shop_list.add_item(dict_to_append)
            st.write('Item '+ name + ' has been added to the list')

    
if st.button('Delete last added item'):
    shop_list.delete_item(last_added = 'yes')
    
if st.button('New list'):
    shop_list.new_list()
    
st.dataframe(shop_list.data)    

st.dataframe(shop_list.data.pivot_table(values = 'Price', index = ['Room', 'Category'], aggfunc='sum'))
    
st.write('Total price ' + str(shop_list.data['Price'].sum()))

st.sidebar.header('Load')

file = st.sidebar.file_uploader('Select the file')
if file != None:
    shop_list.read_list(file)
    st.sidebar.info('File loaded')
        

st.sidebar.header('Save')
    
save_file_name = st.sidebar.text_input('Specify a name for the file')
if st.sidebar.button('Save the list'):
    if len(save_file_name) == 0:
        st.sidebar.error('Specify a name')
    else:
        shop_list.save_list(str(save_file_name)+'.csv')
        path = os.getcwd()
        st.info('List saved in '+str(path)+"\\"+str(save_file_name)+'.csv')


        