import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

from stdash.data import load_data


data = load_data()
df = pd.DataFrame(data)
##################################################################

df["request_time"] = pd.to_datetime(df["request_time"])
df["prediction_time"] = pd.to_datetime(df["prediction_time"])
df["request_yyyymmddhh"] = df["request_time"].dt.strftime("%Y-%m-%d %H시")
df["prediction_yyyymmddhh"] = df["prediction_time"].dt.strftime("%Y-%m-%d %H시")
r_gbc = df.groupby(df['request_yyyymmddhh']).count()
p_gbc = df.groupby(df['prediction_yyyymmddhh']).count()

##################################################################
st.title("요청 / 처리건수(h)")


r_gbcn = r_gbc["num"]
########################################
# r_gbcn.loc[len(r_gbcn)]=0
# idx=list(r_gbcn.index)
# idx.pop()
# idx.append("2024-09-25 03시")

# r_gbcn.index=idx
########################################
#r_gbcn
p_gbcn = p_gbc["num"]
#p_gbcn
############################################
m_gbcn = pd.DataFrame( [r_gbcn,p_gbcn] ).T
m_gbcn.reset_index(inplace=True)
m_gbcn.columns = ["Date/Time", "# of reqs", "# of preds"]
m_gbcn.set_index("Date/Time", inplace=True)
m_gbcn = m_gbcn.sort_index()
m_gbcn
############################################
p_gbcn = m_gbcn["# of preds"]
r_gbcn = m_gbcn["# of reqs"]
############################################


### 한글 폰트 적용 #######
import matplotlib.font_manager as fm  # 폰트 관리
import os

home_path=os.path.expanduser("~")

fe = fm.FontEntry(fname=f'{home_path}/font/NanumSeongsil.ttf', name='NanumSeongsil') #파일 저장되어있는 경로와 이름 설정
fm.fontManager.ttflist.insert(0, fe)  # Matplotlib에 폰트 추가
plt.rcParams.update({'font.size': 10, 'font.family': 'NanumSeongsil'}) #폰트설정
### 한글 폰트 적용  끝 ###

fig, ax = plt.subplots()

ax.plot(list(p_gbcn.index), p_gbcn.values, color="#f49292", label="# of preds", marker="*")
ax.bar(r_gbcn.index, r_gbcn.values, color="#99ffff", label="# of reqs")

plt.title("Prediction time by Request time")
plt.xticks(rotation = 25)
plt.xlabel("Date/Time")
plt.ylabel("# of Reqs / Pred")
plt.legend()

st.pyplot(fig)
##################################################################
#st.bar_chart(r_gbcn, x_label="Date/Time", y_label="# of Requests", height=450)
#st.line_chart(p_gbcn, x_label="Date/Time", y_label="# of Requests", height=450)

