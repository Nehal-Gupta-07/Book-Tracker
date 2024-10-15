import streamlit as st
import requests

backend_url = "http://127.0.0.1:5000"

# Title
st.title("Book Tracker")

# Add new book
st.sidebar.header("Add a New Book")
name = st.sidebar.text_input("Book Name")
author = st.sidebar.text_input("Author Name")
platform = st.sidebar.selectbox("Platform", ["Physical", "Digital"])


if st.sidebar.button("Add Book"):
    data = {"name": name, "author": author, "platform": platform}
    response = requests.post(f"{backend_url}/add_book", json=data)
    if response.status_code == 200:
        st.sidebar.success("Book added successfully!")
    else:
        st.sidebar.error("Failed to add book.")

# View all books
if st.sidebar.button("View All Books"):
    response = requests.get(f"{backend_url}/view")
    books = response.json()["books"]
    st.write("All Books in the Library:")
    for book in books:
        st.write(f"**Title:** {book[1]}, **Author:** {book[2]}, **Platform:** {book[3]}")

# Search books
st.sidebar.header("Search Books")
search_type = st.sidebar.selectbox("Search by", ["name", "author","platform"])
keyword = st.sidebar.text_input("Enter keyword")

if st.sidebar.button("Search"):
    data = {"search_type": search_type, "keyword": keyword}
    response = requests.post(f"{backend_url}/search", json=data)
    books = response.json()["books"]
    if books:
        st.write("Search Results:")
        for book in books:
            st.write(f"**Title:** {book[1]}, **Author:** {book[2]}, **Platform:** {book[3]}")
            
    else:
        st.warning("No matching books found.")
