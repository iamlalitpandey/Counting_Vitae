# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 12:58:12 2017

@author: Lalit
"""
import re,pandas as pd
import matplotlib.pyplot as plt
file = open('Resume.txt', 'r')
text = re.sub('[^a-zA-Z]+', "", file.read().lower())
chlist={}
for ch in text: 
    if ch not in chlist:
        chlist[ch]=1
    else:
        chlist[ch]+=1
#print chlist
YfreqSeries = pd.Series.from_array(chlist.values())
plt.figure(figsize=(15, 8))
sp = YfreqSeries.plot(kind='bar')
sp.set_xlabel("Characters")
sp.set_ylabel("Character Counts")
sp.set_title("Counting Vitae Chart")

plt.xticks(range(len(chlist)), chlist.keys(),rotation=0)
file.close()
