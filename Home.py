import streamlit as st
import pandas

st.set_page_config(layout="wide")

c1, c2 = st.columns(2)

with c1:
    st.image("images/photo.jpg", width=250 )

with c2:
    st.title("Sathiyanarayanan Senthil Kumar")
    content = """
    Hi, I am Sathiyanarayanan! a Master of Data Science graduate with a strong passion for leveraging data 
    to drive impactful solutions. With over 2.5 years of experience in the IT industry, I have honed my expertise 
    in data automation, cleaning, and integration, particularly in retail and e-commerce domains.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built using Python. Feel free to contact me!
"""
st.write(content2)

c3, empty_col, c4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with c3:
    for index, row in df[:10].iterrows():
        st.header(f"{int(index)+1}. {row["title"]}")
        st.write(row["description"])
        st.image(f"images/{row["image"]}")
        st.write(f"[Source Code]({row["url"]})")

with c4:
    for index, row in df[10:].iterrows():
        st.header(f"{int(index)+1}. {row["title"]}")
        st.write(row["description"])
        st.image(f"images/{row["image"]}")
        st.write(f"[Source Code]({row["url"]})")
        
