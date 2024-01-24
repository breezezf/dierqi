'''我的首页'''
import streamlit as st

page = st.sidebar.radio('我的首页', ['中野三玖', '我的图片处理工具', '我的智慧词典', '我的留言区'])

def page_1():
    '''中野三玖'''
    st.write("中野三玖")
    a = ":red[三玖天下第一]"
    st.write(a)
    st.image('三玖1.png')
    
def page_2():
    '''我的图片处理工具'''
    st.image('三玖2.png')

def page_3():
    '''我的智慧词典'''
    pass

def page_4():
    '''我的留言区'''
    pass
    
if page == '中野三玖':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()