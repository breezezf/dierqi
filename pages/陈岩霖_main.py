import streamlit as st

page = st.sidebar.radio("我的首页",["我的兴趣推荐","我的图片处理工具","我的词典","我的留言"])

with open("烧脑小曲.m4a","rb") as f:
    a4 = f.read()
def page1():
    st.write("数学启动")
    st.image("首页图片.jpg")
    st.audio(a4,format="auido/m4a",start_time=0)
def page2():
    pass
def page3():
    pass
def page4():
    pass

if page == "我的兴趣推荐":
    page1()
elif page == "我的图片处理工具":
    page2()
elif page == "我的词典":
    page3()
elif page == "我的留言":
    page4()