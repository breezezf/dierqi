import turtle

'我的主页'

import streamlit as st

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])

def page_1():

    pass

'我的兴趣推荐'

st.write('心的旅程')
a = ':blue[心的旅程]'
st.write(a)

def page_2():

    pass

'我的图片处理工具'

st.image("bcm.png")

def page_3():

    pass

'我的智能词典'

with open('aduan_歌曲.mp3', 'rb') as f:
st.audio(mymp3, format='audio/mp3', start_time=0)

def page_4():

    pass

'我的留言区'

if (page == '我的兴趣推荐'):
    page_1()
elif (page == '我的图片处理工具') :
    page_2()
elif (page == '我的智慧词典') :
    page_3()
elif (page == '我的留言区') :
    page_4()
else :
    pass
