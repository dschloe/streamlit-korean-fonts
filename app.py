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

font_dirs = [os.getcwd() + '/customFonts']
font_files = fm.findSystemFonts(fontpaths=font_dirs)

for font_file in font_files:
    fm.fontManager.addfont(font_file)

fm._load_fontmanager(try_read_cache=False)

fontNames = [f.name for f in fm.fontManager.ttflist]
st.write(fontNames)

def main():
    # st.write(font_files)
    # fontname = st.selectbox("폰트 선택", fontNames)

    plt.rc('font', family="KoPubWorldBatang")
    tips = sns.load_dataset("tips")
    fig, ax = plt.subplots()
    sns.scatterplot(data=tips, x = 'total_bill', y = 'tip', hue='day')
    ax.set_title("한글 테스트")
    st.pyplot(fig)
    
    st.dataframe(tips)
    

if __name__ == "__main__":
    main()