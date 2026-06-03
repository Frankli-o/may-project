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

    period = st.radio(
        "Choose your input period:",
        ["Day", "Month", "Year"],
        horizontal=True
    )

    income = st.number_input(f"{period} income:", min_value=0.0)
    rent = st.number_input(f"{period} rent / housing cost:", min_value=0.0)
    food = st.number_input(f"{period} food spending:", min_value=0.0)
    transportation = st.number_input(f"{period} transportation spending:", min_value=0.0)
    entertainment = st.number_input(f"{period} entertainment spending:", min_value=0.0)
    healthcare = st.number_input(f"{period} healthcare spending:", min_value=0.0)
    education = st.number_input(f"{period} education spending:", min_value=0.0)
    personali = st.number_input(f"{period} personal insurance spending:", min_value=0.0)

    total_spending = rent + food + transportation + entertainment + healthcare + education + personali
    saving=income-total_spending
    if period == "Day":
        daily_income = income
        daily_spending = total_spending
        daily_saving = saving

        monthly_income = income * 30
        monthly_spending = total_spending * 30
        monthly_saving = saving * 30

        yearly_income = income * 365
        yearly_spending = total_spending * 365
        yearly_saving = saving * 365

    elif period == "Month":
        daily_income = income / 30
        daily_spending = total_spending / 30
        daily_saving = saving / 30

        monthly_income = income
        monthly_spending = total_spending
        monthly_saving = saving

        yearly_income = income * 12
        yearly_spending = total_spending * 12
        yearly_saving = saving * 12

    else:  # Year
        daily_income = income / 365
        daily_spending = total_spending / 365
        daily_saving = saving / 365

        monthly_income = income / 12
        monthly_spending = total_spending / 12
        monthly_saving = saving / 12

        yearly_income = income
        yearly_spending = total_spending
        yearly_saving = saving

    st.subheader("Your Result")

    st.write(f"Daily income: ${daily_income:.2f}")
    st.write(f"Daily spending: ${daily_spending:.2f}")
    st.write(f"Daily saving: ${daily_saving:.2f}")

    st.write(f"Monthly income: ${monthly_income:.2f}")
    st.write(f"Monthly spending: ${monthly_spending:.2f}")
    st.write(f"Monthly saving: ${monthly_saving:.2f}")

    st.write(f"Yearly income: ${yearly_income:.2f}")
    st.write(f"Yearly spending: ${yearly_spending:.2f}")
    st.write(f"Yearly saving: ${yearly_saving:.2f}")

    if income == 0:
        st.info("Enter your income to begin.")
    elif saving < 0:
        st.error("You are spending more than your income.")
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