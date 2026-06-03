import streamlit as st

st.set_page_config(page_title="Finance Advisor", layout="wide")

st.sidebar.title("Navigation")

mode = st.sidebar.radio(
    "Select a tool:",
    ["Spending Calculator", "Risk Management Advisor"]
)

st.title("Finance Advisor Website")

if mode == "Spending Calculator":
    st.header("Spending Calculator")

    income = st.number_input("Monthly income:", min_value=0.0)
    rent = st.number_input("Rent / housing cost:", min_value=0.0)
    food = st.number_input("Food spending:", min_value=0.0)
    transportation = st.number_input("Transportation spending:", min_value=0.0)
    entertainment = st.number_input("Entertainment spending:", min_value=0.0)

    total_spending = rent + food + transportation + entertainment
    saving = income - total_spending

    st.subheader("Your Result")
    st.write(f"Total spending: ${total_spending:.2f}")
    st.write(f"Money left: ${saving:.2f}")

    if income == 0:
        st.info("Enter your income to begin.")
    elif saving < 0:
        st.error("You are spending more than your monthly income.")
    elif saving < income * 0.2:
        st.warning("You are saving less than 20% of your income.")
    else:
        st.success("Your saving level looks healthy.")

elif mode == "Risk Management Advisor":
    st.header("Risk Management Advisor")

    income = st.number_input("Monthly income:", min_value=0.0)
    savings = st.number_input("Current total savings:", min_value=0.0)
    debt = st.number_input("Current total debt:", min_value=0.0)
    emergency_fund = st.number_input("Emergency fund:", min_value=0.0)

    debt_ratio = debt / income if income > 0 else 0

    st.subheader("Your Risk Analysis")

    st.write(f"Debt-to-monthly-income ratio: {debt_ratio:.2f}")

    if income == 0:
        st.info("Enter your income to begin.")
    elif debt_ratio > 6:
        st.error("High risk: Your debt is more than six months of income.")
    elif emergency_fund < income:
        st.warning("Medium risk: Your emergency fund is less than one month of income.")
    else:
        st.success("Low risk: Your financial position looks stable.")