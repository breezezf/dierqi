'''原来你也用编程'''
import streamlit as st

page = st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区'])

def page_1():
    '''我的兴趣推荐'''
    st.write("h")
    a = ":blue[原神]"
    st.write(a)

def page_2():
    '''我的图片处理工具'''
    pass
    
def page_3():
    '''我的智能词典'''
    pass

def page_4():
    '''我的留言区'''
    pass

if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()