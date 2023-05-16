# -*- coding:utf-8 -*-
import streamlit as st 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np 

# 한글폰트 적용
# 폰트 적용
import os
import matplotlib.font_manager as fm  # 폰트 관련 용도 as fm



# fpath = os.path.join(os.getcwd(), "customFonts/NanumGothic-Bold.ttf")
# prop = fm.FontProperties(fname=fpath)

font_dirs = [os.getcwd() + '\customFonts']
st.write(font_dirs)
font_files = fm.findSystemFonts(fontpaths=font_dirs)

names = []
for font_file in font_files:
    st.write(font_file)
    font_name = fm.FontProperties(fname=font_file, size=10).get_name()
    names.append(font_name)

fm._load_fontmanager(try_read_cache=False)

for f in fm.fontManager.ttflist:
   st.write(f.name)

def main():
    st.write(names)
    fontname = st.selectbox("폰트 선택", names)

    plt.rcParams['font.family']=str(fontname)
    tips = sns.load_dataset("tips")
    fig, ax = plt.subplots()
    sns.scatterplot(data=tips, x = 'total_bill', y = 'tip', hue='day')
    ax.set_title("한글 테스트")
    st.pyplot(fig)
    
    st.dataframe(tips)
    

if __name__ == "__main__":
    main()