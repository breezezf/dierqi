import streamlit as st
page=st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区'])
def page_1():
    '''我的兴趣推荐'''
    st.write("原神,启动")
    a=":blue[收到]"
    st.write(a)
    with open("bullet2.mp3","rb") as f:
        b=f.read()
    st.audio(b,format="audio/mp3",start_time=0)
def page_2():
    '''我的图片处理工具'''
    st.image("bg.png")
def page_3():
    '''我的智慧词典'''
    pass
def page_4():
    '''我的留言区'''
    pass
if page=='我的兴趣推荐':
    page_1()
elif page=='我的图片处理工具':
    page_2()
elif page=='我的智慧词典':
    page_3()
elif page=='我的留言区':
    page_4()