import streamlit as st

st.title("Simple Spending Calculator")

income = st.number_input("Monthly income:", min_value=0.0)
food = st.number_input("Food spending:", min_value=0.0)
shopping = st.number_input("Shopping spending:", min_value=0.0)
entertainment = st.number_input("Entertainment spending:", min_value=0.0)

total_spending = food + shopping + entertainment
saving = income - total_spending

st.subheader("Result")
st.write("Total spending:", total_spending)
st.write("Money left:", saving)

if income == 0:
    st.info("Enter your income to start.")
elif saving < 0:
    st.error("You are spending more than your income.")
elif saving < income * 0.2:
    st.warning("You are saving less than 20% of your income.")
else:
    st.success("Good job! Your saving looks healthy.")