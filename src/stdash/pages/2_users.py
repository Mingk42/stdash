import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from stdash.data import load_data, font_path


data = load_data()
df = pd.DataFrame(data)
#df

### 한글 폰트 적용 #######
import matplotlib.font_manager as fm  # 폰트 관리


fe = fm.FontEntry(fname=font_path(), name='NanumSeongsil') #파일 저장되어있는 경로와 이름 설정
fm.fontManager.ttflist.insert(0, fe)  # Matplotlib에 폰트 추가
plt.rcParams.update({'font.size': 10, 'font.family': 'NanumSeongsil'}) #폰트설정
### 한글 폰트 적용  끝 ###


r_gbc = df.groupby(df['request_user']).count()
p_gbc = df.groupby(df['prediction_model']).count()
p_gbc.reset_index(inplace=True)
n00 = p_gbc["prediction_model"].str.contains(r"^n\d\d")
p_gbc = p_gbc[n00]
p_gbc.set_index("prediction_model", inplace=True)


st.title("Request User")

fig, ax = plt.subplots()

ax.pie(r_gbc["num"], labels=r_gbc.index)
plt.legend(ncol=3)

st.pyplot(fig)

# from sklearn.metrics import confusion_matrix

st.title("# of Reqs / Preds By Users")

df["prediction_model"] = df["prediction_model"].map(lambda x:x.replace("mnist240924.keras.n11","n11"))

r_gbc=df.groupby(["request_user"]).count()
p_gbc=df.groupby(["prediction_model"]).count()

p_gbc.reset_index(inplace=True)
p_gbc["prediction_model"] = p_gbc["prediction_model"].map(lambda x:x.replace("mnist240924.keras.n11","n11"))
n00 = p_gbc["prediction_model"].str.contains(r"^n\d\d")
p_gbc=p_gbc[n00]
p_gbc.set_index("prediction_model", inplace=True)

rn_gbc = r_gbc["num"]
pn_gbc = p_gbc["num"]
########################################
rp_gbc = df[df["request_user"]==df["prediction_model"]].groupby("request_user").count()

rpn_gbc = rp_gbc["num"]
########################################



for i in rn_gbc.index:
    if i not in pn_gbc.index:
        pn_gbc[i]=0
    if i not in rpn_gbc.index:
        rpn_gbc[i]=0

for i in pn_gbc.index:
    if i not in rpn_gbc.index:
        rpn_gbc[i]=0


rn_gbc.sort_index(inplace=True)
pn_gbc.sort_index(inplace=True)
rpn_gbc.sort_index(inplace=True)

x_range = np.arange(len(rn_gbc))

fig, ax = plt.subplots(figsize=(12,7))

ax.bar(x_range-0.3, rn_gbc.values, 0.3, label="# of reqs")
ax.bar(x_range, pn_gbc.values, 0.3, label="# of preds")
ax.bar(x_range+0.3, rpn_gbc.values, 0.3, label="# of reqs=preds")

ax.set_title("# of Reqs / Preds By Users")
ax.set_xlabel("Users")
ax.set_ylabel("# of reqs / preds")
ax.set_xticks(x_range, rn_gbc.index)
ax.legend()

st.pyplot(fig)