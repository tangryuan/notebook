import streamlit as st

tabs = st.tabs(["性别","联系方式","食物"])

with tabs[0]:
    value = st.radio("",["男","女"],index=None)

    value

with tabs[1]:
    st.selectbox("",["微信","手机号"],index=None)
with tabs[2]:
    foods = st.multiselect("",["面","米饭","粥"])

    foods

with st.expander("身高信息"):
    sliderValue = st.slider("滑块",value=170,min_value=1,max_value=300,step=1)
    sliderValue

uploader = st.file_uploader("文件上传",type=["pdf","jpeg"])