import streamlit as st

st.title("Simple Calculator 🧮")

# Input numbers
num1 = st.number_input("Enter First Number:", value=0.0)
num2 = st.number_input("Enter Second Number:", value=0.0)

# Operation selection
operation = st.selectbox(
    "Select Operation:",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# Calculate button
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"Result: {result}")

    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"Result: {result}")

    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"Result: {result}")

    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Result: {result}")
        else:
            st.error("Division by zero is not allowed ❌")
