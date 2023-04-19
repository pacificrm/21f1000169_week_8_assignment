import streamlit as st
st.title("Find the largest number among the given 3 numbers")


# num1 = st.number_input("Enter first number: ")
# num2 = st.number_input("Enter second number: ")
# num3 = st.number_input("Enter third number: ")
num1 = st.text_input("Enter first number: ")
num2 = st.text_input("Enter second number: ")
num3 = st.text_input("Enter third number: ")

calculate=st.button("Find the largest number")

if calculate:
   lrg=max(float(num1),float(num2),float(num3))
   st.write("The largest Number is:",lrg)
