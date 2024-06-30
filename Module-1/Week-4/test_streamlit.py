import streamlit as st

st.text("Hi")
multi_select = st.multiselect("Your favortie colour: ", ["Green", "Yellow", "Red"])
select_box = st.selectbox("Your favortie colour: ", ["Green", "Yellow", "Red"])
if multi_select is not None:
    st.write("You selected: ", multi_select)

text_input = st.text_input("Please enter your input")
if text_input is not None:
    st.write("You input is", text_input)

st.image("./cat.jpeg", caption="A cat", channels="RGB")

# Create a form
with st.form("user_form"):
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)
    
    # Submit button in the form
    submitted = st.form_submit_button("Submit")

# Handle the form submission
if submitted:
    st.write(f"Hello {name}, you are {age} years old!")