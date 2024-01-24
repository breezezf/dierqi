import streamlit as st

page = st.sidebar.radio('首页',['原神启动','我的图片处理工具','我的智慧词典','我的留言区'])

def page_1():
    '''原神启动'''  
    st.write('原神启动')
    st.image("OP_s.png")
    with open('OPGo.mp3','rb') as f:
        mymp3 = f.read()
    st.audio(mymp3,format='audio/mp3', start_time=0)
        
def page_2():
    '''我的图片处理工具''' 
    pass
    
def page_3():
    '''我的智慧词典'''   
    pass
    
def page_4():
    '''我的留言区'''   
    pass
    
if page == '原神启动':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()
