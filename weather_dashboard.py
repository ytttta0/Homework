import requests
import streamlit as st
import pandas as pd

st.title("⛅ 台灣氣象資料 Dashboard")

API_KEY = "CWA-7539DAF4-828A-4271-9F98-CCE621362C83"
LOCATION = st.selectbox("選擇城市",["臺北市","臺中市","高雄市"])

url = f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization={API_KEY}&locationName={LOCATION}"
res = requests.get(url, verify=False)
data = res.json()

location = data["records"]["location"][0]
st.subheader(f"📍 {location['locationName']} 36小時預報")

for element in location["weatherElement"]:
    name = element["elementName"]
    value = element["time"][0]["parameter"]["parameterName"]
    st.write(f"{name}:{value}")







