import streamlit as st


userName = st.text_input("请输入姓名：")

password = st.text_input("请输入密码：",type="password")

st.divider()

age = st.number_input("请输入年龄：",step=1)

describe = st.text_area("请输入自我介绍：")
st.divider()

check = st.checkbox("我同意以上条款")
if check:
    st.radio("111",options=["1","2"])


st.divider()
success= st.button("提交")
if success:
    st.write("提交成功！")
