import streamlit as st
page=st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理器','我的智慧词典','我的留言区'])

def page_1():
    '''我的兴趣推荐'''
    a=':red[没有天堂，只有人间。没有上帝，只有人民]'
    st.write(a)
    st.image('bcm.jpg')
def page_2():
    '''我的图片处理器'''
    pass
def page_3():
    '''我的智慧词典'''
    pass 
def page_4():
    '''我的留言区'''
    pass   
if page == '我的兴趣推荐':
    page_1()
elif page =='我的图片处理器':
    page_2()
elif page =='我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()
