import streamlit as st

st.title("Personal Finance Tool")

mode = st.radio(
    "Choose a mode:",
    ["Spending Calculator", "Risk Management Advisor"]
)

if mode == "Spending Calculator":
    st.header("Spending Calculator")

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

elif mode == "Risk Management Advisor":
    st.header("Risk Management Advisor")

    savings = st.number_input("Current savings:", min_value=0.0)
    debt = st.number_input("Current debt:", min_value=0.0)
    emergency_fund = st.number_input("Emergency fund:", min_value=0.0)

    st.subheader("Risk Result")

    if debt > savings:
        st.error("High risk: Your debt is greater than your savings.")
    elif emergency_fund < 1000:
        st.warning("Medium risk: Your emergency fund may be too low.")
    else:
        st.success("Low risk: Your financial risk looks manageable.")