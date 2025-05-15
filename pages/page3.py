import streamlit as st


value = st.radio("",["男","女"],index=None)

value


st.divider()

st.selectbox("",["微信","手机号"],index=None)
st.divider()

foods = st.multiselect("",["面","米饭","粥"])

foods

st.divider()
sliderValue = st.slider("滑块",value=170,min_value=1,max_value=300,step=1)
sliderValue

uploader = st.file_uploader("文件上传",type=["pdf","jpeg"])
uploader.name