import streamlit as st

# Initialize session state for form validation
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

# Define a function to validate form input
def validate_form(name, age):
    if not name:
        st.error("Name is required.")
        return False
    if age < 0 or age > 120:
        st.error("Age must be between 0 and 120.")
        return False
    return True

# Create a form
with st.form("user_form"):
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)
    hobbies = st.multiselect("Select your hobbies:", ["Reading", "Traveling", "Cooking", "Sports"])

    # Submit button in the form
    submitted = st.form_submit_button("Submit")

# Handle the form submission
if submitted:
    if validate_form(name, age):
        st.session_state.form_submitted = True
        st.write(f"Hello {name}, you are {age} years old!")
        st.write(f"Your hobbies: {', '.join(hobbies)}")

# Optionally display a message if the form was successfully submitted
if st.session_state.form_submitted:
    st.success("Form submitted successfully!")
