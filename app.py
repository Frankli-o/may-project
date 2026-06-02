import streamlit as st

st.title("Personal Spending Advisor")

income = st.number_input("Enter your monthly income:", min_value=0.0)
spending = st.number_input("Enter your monthly spending:", min_value=0.0)

saving = income - spending

st.write("Your estimated monthly savings:", saving)

if income == 0:
    st.info("Enter your income to begin.")
elif saving < 0:
    st.warning("You are spending more than your income.")
elif saving < income * 0.2:
    st.warning("Your saving rate is low. Try to save at least 20%.")
else:
    st.success("Your saving rate looks healthy.")
