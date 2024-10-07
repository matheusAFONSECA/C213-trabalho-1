import streamlit as st

def main():
    st.title("Streamlit App")
    st.header("Welcome to my Streamlit application!")
    st.text("This is a basic example of a Streamlit app.")

    if st.button("Click me"):
        st.write("Button clicked!")

    st.sidebar.title("Sidebar")
    st.sidebar.text("This is the sidebar.")

if __name__ == "__main__":
    main()