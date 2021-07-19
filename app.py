import streamlit as st
st.title(":sparkles:Taylor Swift Lyrics Word Cloud Generator:sparkles:")
import time
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
df = pd.read_csv("taylor_swift_lyrics.csv",sep='|', encoding='latin-1')

option=st.selectbox('What album do you want to create a Word Cloud for ?',
	('folklore','evermore'))
if option=='folklore': 
	song=st.selectbox('Choose your song', ('cardigan','the 1','the last great american dynasty','exile','my tears ricochet','mirrorball','seven','august','this is me trying','illicit affairs','invisible strings','mad woman','epiphany','betty','peace','hoax','the lakes'))
else:
	song=st.selectbox('Choose your song', ('willow','champagne problems','gold rush',"'tis the damn season",'tolerate it','no body, no crime (ft. HAIM)','happiness', 'dorothea','coney island (ft. The National)','ivy','cowboy like me','long story short','marjorie','closure','evermore(ft. Bon Iver)','right where you left me',"It's time to go"))


title=['cardigan','the 1','the last great american dynasty','exile','my tears ricochet','mirrorball','seven','august','this is me trying','illicit affairs','invisible strings','mad woman','epiphany','betty','peace','hoax','the lakes','willow','champagne problems','gold rush',"'tis the damn season",'tolerate it','no body, no crime (ft. HAIM)','happiness', 'dorothea','coney island (ft. The National)','ivy','cowboy like me','long story short','marjorie','closure','evermore(ft. Bon Iver)','right where you left me',"It's time to go"]
X=title.index(song)
print(X)

words=df.lyric[X]
with st.spinner('Wait for it...'):
	time.sleep(4)
st.success('Done!')
st.balloons()

if option=='folklore': 
	mask2 = np.array(Image.open('jwsmcwo2opc51-removebg-preview.jpg'))
	hue=112
	sat=13
	li=26
	bc="#7f7f7f"
else: 
	mask2 = np.array(Image.open('3a-removebg-preview.jpg'))
	hue=0
	sat=92
	li=31
	bc="#bb8358"



def one_color_func(word=None, font_size=None,
                       position=None, orientation=None,
                       font_path=None, random_state=None):
    h = hue
    s = sat 
    l = li
    return "hsl({}, {}%, {}%)".format(h, s, l)

wc = WordCloud(background_color=bc, max_words=2000,
               stopwords=STOPWORDS, max_font_size=256,mask=mask2
               ,color_func=one_color_func)
wc.generate(words)
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
fig=plt.show()
st.pyplot(fig)
