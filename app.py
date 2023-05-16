# -*- coding:utf-8 -*-
import streamlit as st 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np 

# 한글폰트 적용
# 폰트 적용
import os
import matplotlib.font_manager as fm  # 폰트 관련 용도 as fm

def unique(list):
    x = np.array(list)
    return np.unique(x)

# fpath = os.path.join(os.getcwd(), "customFonts/NanumGothic-Bold.ttf")
# prop = fm.FontProperties(fname=fpath)

@st.cache_data
def fontRegistered():
    font_dirs = [os.getcwd() + '/customFonts']
    font_files = fm.findSystemFonts(fontpaths=font_dirs)

    for font_file in font_files:
        st.write(font_file)
        fm.fontManager.addfont(font_file)

    fm._load_fontmanager(try_read_cache=False)
    

def main():
    # st.write(font_files)
    fontRegistered()
    ttfFontNames = [f.name for f in fm.fontManager.ttflist]
    otfFontNames = [f.name for f in fm.fontManager.otflist]
    fontNames = ttfFontNames + otfFontNames
    # st.write(fontNames)
    fontname = st.selectbox("폰트 선택", unique(fontNames))

    plt.rc('font', family=fontname)
    tips = sns.load_dataset("tips")
    fig, ax = plt.subplots()
    sns.scatterplot(data=tips, x = 'total_bill', y = 'tip', hue='day')
    ax.set_title("한글 테스트")
    st.pyplot(fig)
    
    st.dataframe(tips)
    

if __name__ == "__main__":
    main()