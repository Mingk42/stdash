import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

from stdash.data import load_data


data = load_data()
df = pd.DataFrame(data)
df

### 한글 폰트 적용 #######
import matplotlib.font_manager as fm  # 폰트 관리
import os

home_path=os.path.expanduser("~")

fe = fm.FontEntry(fname=f'{home_path}/font/NanumSeongsil.ttf', name='NanumSeongsil') #파일 저장되어있는 경로와 이름 설정
fm.fontManager.ttflist.insert(0, fe)  # Matplotlib에 폰트 추가
plt.rcParams.update({'font.size': 10, 'font.family': 'NanumSeongsil'}) #폰트설정
### 한글 폰트 적용  끝 ###



st.title("Request User")

r_gbc = df.groupby(df['request_user']).count()

fig, ax = plt.subplots()

ax.pie(r_gbc["num"], labels=r_gbc.index)
plt.legend(ncol=3)

st.pyplot(fig)



# from sklearn.metrics import confusion_matrix