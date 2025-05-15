import streamlit as st

with st.sidebar:
    userName = st.text_input("请输入姓名：")
column1,column2 = st.columns([1,5])
column3,column4 = st.columns([1,5])
with column1:
    "请输入密码："
with column2:
    password = st.text_input("",type="password",label_visibility="collapsed")
with column3:
    st.write("请输入年龄：")
with column4:
    age = st.number_input("",step=1)
column5,column6 = st.columns([1,2])
with column5:
    "请输入自我介绍："
with column5:
    describe = st.text_area("")
check = st.checkbox("我同意以上条款")
if check:
    st.radio("111",options=["1","2"])


st.divider()
success= st.button("提交")
if success:
    st.write("提交成功！")
