import streamlit as st
st.title("Find the largest number among the given 3 numbers")


num1 = st.number_input("Enter first number: ")
num1 = st.number_input("Enter second number: ")
num1 = st.number_input("Enter third number: ")

def largestNumber(num1,num2,num3):
   if (num1 >= num2) and (num1 >= num3):
      largest = num1
   elif (num2 >= num1) and (num2 >= num3):
      largest = num2
   else:
      largest = num3
if calculate:
   largest=largestNumber(num1,num2,num3)
   st.write("The largest Number is:",largest)
