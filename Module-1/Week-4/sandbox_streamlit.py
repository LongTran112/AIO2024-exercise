import streamlit as st

st.write("This is an example using st.echo")

with st.echo():
    st.write("This text is inside the st.echo block")
    x = 42
    st.write(f"The value of x is {x}")

st.write("This is an example using st.slider")

# Single value slider
age = st.slider("Select your age", min_value=0, max_value=100, value=25)
st.write(f"Selected age: {age}")

# Range slider
range_values = st.slider("Select a range of values", 0, 100, (25, 75))
st.write(f"Selected range: {range_values}")