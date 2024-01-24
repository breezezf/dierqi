import streamlit as st

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '图片处理工具', '我的智能词典', '我的评论区'])

def page_1():
    '''我的兴趣推荐'''
    
    a = ":red[我的电影推荐]"
    st.write(a)
    st.write("《泰坦尼克号》《盗梦空间》《这个杀手不太冷》《海上钢琴师》《忠犬八公的故事》《辛德勒的名单》《哈利波特》")
    b = ":blue[我的书籍推荐]"
    st.write(b)
    st.write("《梦的解析》《孤岛之鬼》《西游记》《天才在左，疯子在右》《红楼梦》")
    c = ":green[我的歌曲推荐]"
    st.write(c)
    st.write("《一路生花》《叹》")
    st.write("  ")
    st.write("《盗梦空间》")
    st.image("盗梦空间.jpg")
    st.write("《海上钢琴师》")
    st.image("海上钢琴师.jpg")
    st.write("《忠犬八公的故事》")
    st.image("忠犬八公的故事.jpg")
    st.write("《哈利波特》")
    st.image("哈利波特.jpg")
    #with open('.mp3', 'rb') as f:
        #mymp3 = f.read()
    
def page_2():
    '''图片处理工具'''
    pass
def page_3():
    '''我的智能词典'''
    pass
def page_4():
    '''我的评论区'''
    pass

if page == '我的兴趣推荐':
    page_1()
elif page == '图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的评论区':
    page_4()