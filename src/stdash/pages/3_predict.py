import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import requests as reqs

from stdash.data import load_data, font_path

st.sidebar.markdown("# This page includes accuracy and reqs/preds by users")
st.markdown("# Predict")


data = load_data()

### 한글 폰트 적용 #######
import matplotlib.font_manager as fm  # 폰트 관리

fe = fm.FontEntry(fname=font_path(), name='NanumSeongsil') #파일 저장되어있는 경로와 이름 설정
fm.fontManager.ttflist.insert(0, fe)  # Matplotlib에 폰트 추가
plt.rcParams.update({'font.size': 10, 'font.family': 'NanumSeongsil'}) #폰트설정
### 한글 폰트 적용  끝 ###


st.title("### Accuracy")
df = pd.DataFrame(data)


df["correct_yn"] = df["label"] == df["prediction_result"]
correct_yn = df.groupby("correct_yn").count()
correct_yn_n = correct_yn[["num"]]

correct_yn_n.index=["틀림","맞춤"]
correct_yn_n.reset_index(inplace=True)
correct_yn_n.columns=["O/X","cnt"]
correct_yn_n.set_index("O/X", inplace=True)
correct_yn_n

fig, ax = plt.subplots()

ax.pie(correct_yn_n["cnt"], labels=["틀림","맞춤"], autopct='%1.1f%%')

corrt_preds_cnt = correct_yn_n.iloc[1].values[0]
total_preds_cnt = correct_yn_n.sum().values[0]

plt.title(f"Accuracy : {corrt_preds_cnt/total_preds_cnt *100:.1f}%")
plt.legend()
st.pyplot(fig)




################################################################################################
uploaded_files = st.file_uploader(
    "Choose a Image file", accept_multiple_files=True
)
for uploaded_file in uploaded_files:
    
    ftype,ext = uploaded_file.type.split("/")

    if ftype != "image":
        # raise Exception("")
        st.error("잘못된 형식, 이미지파일을 선택해주세요", icon="🚨")
        
        #uploaded_file.detach()
        # reqs.delete(uploaded_file._file_urls)
        # print("::::::::::::::::::::::::::::::::", uploaded_file._file_urls["file_id"])
        print("::::::::::::::::::::::::::::::::", type(uploaded_file._file_urls))

    print(uploaded_file)
    print(f"type ::::::::::: {uploaded_file.type}")
    print(f"type ::::::::::: {uploaded_file.type}")
#     bytes_data = uploaded_file.read()
#     st.write("filename:", uploaded_file.name)
#     st.write(bytes_data)
################################################################################################