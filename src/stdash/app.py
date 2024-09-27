import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

from stdash.data import load_data


data = load_data()

st.title("CNN JOB MON")
df = pd.DataFrame(data)

df
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
p_gbcn = p_gbc["num"]
##################################################################
# st.bar_chart(r_gbcn, x_label="Date/Time", y_label="# of Requests", height=450)
# st.line_chart(p_gbcn, x_label="Date/Time", y_label="# of Requests", height=450)

