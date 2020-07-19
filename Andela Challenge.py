# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 11:10:46 2020

@author: KAMALDEEN
"""
   
def groupSort(arr):
    # The function is expected to return a 2D_INTEGER_ARRAY.
    # The function accepts INTEGER_ARRAY arr as parameter

    def my_dict(arr):
        freq = {}
        for x in arr:
            freq[x] = freq.get(x,0) + 1
        return freq
    my_list = []
    for key,value in my_dict(arr).items():
        my_list.append((key,value))
    my_list = [list(ele) for ele in my_list]
    # my_list = list(map(list,my_dict(arr).items()))       
    for i in range(len(my_list)):
        for j in range(i+1,len(my_list)):
            if my_list[i][1] < my_list[j][1]:
                my_list[i],my_list[j] = my_list[j],my_list[i]
            elif my_list[i][1] == my_list[j][1]:
                if my_list[i][0] > my_list[j][0]:
                    my_list[i],my_list[j] = my_list[j],my_list[i]
    return my_list
                    
# arr = [2,2,7,12,3,3,3,3]
# print(groupSort(arr))


