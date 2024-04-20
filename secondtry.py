#Private gsheet

import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("Read Google Sheet as DataFrame")

conn = st.experimental_connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet="americas")

st.dataframe(df)

if st.button("Update worksheet"):
  df = conn.update(worksheet="hoja 3",
            data=df)
  st.cache_data.clear()
  st.experimental_rerun()
# Display our Spreadsheet as st.dataframe
st.dataframe(df.head(10))
