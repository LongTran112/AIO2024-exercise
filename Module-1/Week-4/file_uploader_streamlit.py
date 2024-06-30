import streamlit as st

# Single file uploader
uploaded_file = st.file_uploader("Choose a file")

# Handle file upload
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write("File uploaded successfully!")
    st.write(f"Filename: {uploaded_file.name}")
    st.write(f"File type: {uploaded_file.type}")
    st.write(f"File size: {uploaded_file.size} bytes")
    
    # Optionally, process the file here (e.g., read its content, display it, etc.)
    # Example for reading a CSV file (uncomment if needed):
    # import pandas as pd
    # df = pd.read_csv(uploaded_file)
    # st.write(df)

# Multiple files uploader
uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)

# Handle multiple file upload
if uploaded_files is not None:
    for uploaded_file in uploaded_files:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.write("File uploaded successfully!")
        st.write(f"Filename: {uploaded_file.name}")
        st.write(f"File type: {uploaded_file.type}")
        st.write(f"File size: {uploaded_file.size} bytes")
        
        # Optionally, process the files here (e.g., read their content, display them, etc.)
        # Example for reading a CSV file (uncomment if needed):
        # import pandas as pd
        # df = pd.read_csv(uploaded_file)
        # st.write(df)