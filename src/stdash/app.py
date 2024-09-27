import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import requests as reqs

##################################################################
def load_data():
    url = "http://43.202.66.118:8077/all"

    resp = reqs.get(url)
    data = resp.json()

    return data

data = load_data()
##################################################################
st.title("CNN JOB MON")
df = pd.DataFrame(data)

df
##################################################################

df["request_time"] = pd.to_datetime(df["request_time"])
df["request_time_t"] = df["request_time"].dt.strftime("%Y-%m-%d %H시")
gbc = df.groupby(df['request_time_t']).count()

##################################################################
st.title("요청 / 처리건수(h)")

### 한글 폰트 적용 #######
import matplotlib.font_manager as fm  # 폰트 관리
import os

home_path=os.path.expanduser("~")

fe = fm.FontEntry(fname=f'{home_path}/font/NanumSeongsil.ttf', name='NanumSeongsil') #파일 저장되어있는 경로와 이름 설정
fm.fontManager.ttflist.insert(0, fe)  # Matplotlib에 폰트 추가
plt.rcParams.update({'font.size': 10, 'font.family': 'NanumSeongsil'}) #폰트설정
### 한글 폰트 적용  끝 ###

fig, ax = plt.subplots()

ax.bar(gbc["prediction_time"].index, gbc["prediction_time"].values, color="#99ffff", label="prediction_time")
ax.plot(gbc["prediction_time"].index, gbc["prediction_time"].values, color="#f49292", label="prediction_time", marker="*")

plt.title("Prediction time by Request time")
plt.xticks(rotation = 45)
plt.xlabel("Date/Time")
plt.ylabel("# of Requests")

st.pyplot(fig)
##################################################################
st.bar_chart(gbc["request_user"])

