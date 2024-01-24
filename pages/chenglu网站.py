import streamlit as st

page = st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理','我的智慧词典','我的留言区'])

def page_1():
    '''我的兴趣推荐'''
    pass
def page_2():
    '''我的图片处理'''
    pass
def page_3():
    '''我的智慧词典'''
    pass
def page_4():
    '''我的留言区'''
    pass
if page == '我的兴趣推荐':
    page_1()
    st.image("kun.jpg")
    with open('你干嘛剪切.mp3','rb') as f:
        mymp3 = f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    a=":red[话说这东汉末年闹了一场鸡瘟,诞生一男子 名叫坤坤 曹操将其列为不祥之兆,将其怒劈,几千年后,一男子诞生也叫坤坤 爱打篮球 练习时间长达两年半 还爱唱跳rap 放我们欣赏他的成名绝句 和帅气容颜]"
    st.write(a)    
    
elif page == '我的图片处理':
    page_2()
     
elif page =='我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()
    a=":red[请畅所欲言]"
    st.write(a)