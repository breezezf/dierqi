import streamlit as st

page = st.sidebar.radio('我的网站',['ut详细介绍','我的工具','我的词典','网站相关'])

b = "wiki: https://undertale.fandom.com/zh/wiki/Undertale%E7%B6%AD%E5%9F%BA?variant=zh-hans"
def page1():
    st.image("Undertale.jpg")
    st.write("Undertale（或者称作UNDERTALE，中文可能译作地下传说或者传说之下）是一款托比‧福克斯在 GameMaker: Studio制作的游戏是一款独立RPG游戏，于2015年九月15日于Steam上公开。")
    st.write("游戏的主线在于玩家试图逃脱地下世界回到地表世界的旅程。这款游戏受到了令人难以置信的良好回应，Steam上有超过一万则评价，其中约有98%是正面的。")
    st.write(b)
    st.write("主题音乐：")
    with open('Toby Fox-Undertale.mp3','rb') as f:
        topicm = f.read()
    st.audio(topicm,format='audio/mp3',start_time=0)
    st.write("未完待续……")
def page2():
    pass
def page3():
    pass
def page4():
    pass

if page == 'ut详细介绍':
    page1()
elif page == '我的工具':
    page2()
elif page == '我的词典':
    page3()
elif page == '网站相关':
    page4()