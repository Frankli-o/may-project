import streamlit as st

st.set_page_config(page_title="Finance Advisor", layout="wide")

st.sidebar.title("Navigation")

mode = st.sidebar.radio(
    "Select a tool:",
    ["Spending Calculator", "Risk Management Advisor"]
)

st.title("Personal Finance Advisor")

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
    personal_insurance = st.number_input(f"{period} personal insurance spending:", min_value=0.0)

    total_spending = (
        rent
        + food
        + transportation
        + entertainment
        + healthcare
        + education
        + personal_insurance
    )

    saving = income - total_spending

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

    else:
        daily_income = income / 365
        daily_spending = total_spending / 365
        daily_saving = saving / 365

        monthly_income = income / 12
        monthly_spending = total_spending / 12
        monthly_saving = saving / 12

        yearly_income = income
        yearly_spending = total_spending
        yearly_saving = saving

    st.subheader("Your Financial Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### Daily")
        st.metric("Income", f"${daily_income:.2f}")
        st.metric("Spending", f"${daily_spending:.2f}")
        st.metric("Saving", f"${daily_saving:.2f}")

    with col2:
        st.markdown("### Monthly")
        st.metric("Income", f"${monthly_income:.2f}")
        st.metric("Spending", f"${monthly_spending:.2f}")
        st.metric("Saving", f"${monthly_saving:.2f}")

    with col3:
        st.markdown("### Yearly")
        st.metric("Income", f"${yearly_income:.2f}")
        st.metric("Spending", f"${yearly_spending:.2f}")
        st.metric("Saving", f"${yearly_saving:.2f}")

   
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

    age_scores = {
        "16 to 19 years old": 1,
        "20 to 24 years old": 2,
        "25 to 34 years old": 3,
        "35 to 44 years old": 4,
        "45 to 54 years old": 5,
        "55 to 64 years old": 6,
        "65 years and older": 7
    }

    education_scores = {
        "Less than 9th grade": 1,
        "Some high school, no completion": 2,
        "Some college, no degree": 3,
        "Associate's degree": 4,
        "Bachelor's degree": 5,
        "Doctor's degree": 6,
        "Professional degree": 7
    }

    average_salary_data = {
        "16 to 19 years old": {
            "Less than 9th grade": 30130,
            "Some high school, no completion": 20000,
            "Some college, no degree": 22000,
            "Associate's degree": 24000,
            "Bachelor's degree": 26000,
            "Doctor's degree": 28000,
            "Professional degree": 30000
        },
        "20 to 24 years old": {
            "Less than 9th grade": 22000,
            "Some high school, no completion": 25000,
            "Some college, no degree": 30000,
            "Associate's degree": 35000,
            "Bachelor's degree": 45000,
            "Doctor's degree": 55000,
            "Professional degree": 60000
        },
        "25 to 34 years old": {
            "Less than 9th grade": 28000,
            "Some high school, no completion": 32000,
            "Some college, no degree": 42000,
            "Associate's degree": 50000,
            "Bachelor's degree": 68000,
            "Doctor's degree": 90000,
            "Professional degree": 105000
        },
        "35 to 44 years old": {
            "Less than 9th grade": 32000,
            "Some high school, no completion": 38000,
            "Some college, no degree": 48000,
            "Associate's degree": 58000,
            "Bachelor's degree": 80000,
            "Doctor's degree": 110000,
            "Professional degree": 130000
        },
        "45 to 54 years old": {
            "Less than 9th grade": 34000,
            "Some high school, no completion": 40000,
            "Some college, no degree": 52000,
            "Associate's degree": 62000,
            "Bachelor's degree": 85000,
            "Doctor's degree": 115000,
            "Professional degree": 140000
        },
        "55 to 64 years old": {
            "Less than 9th grade": 33000,
            "Some high school, no completion": 39000,
            "Some college, no degree": 50000,
            "Associate's degree": 60000,
            "Bachelor's degree": 82000,
            "Doctor's degree": 112000,
            "Professional degree": 135000
        },
        "65 years and older": {
            "Less than 9th grade": 25000,
            "Some high school, no completion": 30000,
            "Some college, no degree": 38000,
            "Associate's degree": 45000,
            "Bachelor's degree": 65000,
            "Doctor's degree": 90000,
            "Professional degree": 110000
        }
    }

    age_group = st.radio(
        "Choose your age group:",
        list(age_scores.keys()),
        horizontal=True
    )

    education_group = st.radio(
        "Choose your education level:",
        list(education_scores.keys()),
        horizontal=True
    )

    age_score = age_scores[age_group]
    education_score = education_scores[education_group]

    average_salary = average_salary_data[age_group][education_group]

    st.success(f"You selected: {age_group}")
    st.success(f"You selected: {education_group}")

    st.subheader("Estimated Average Salary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Estimated Annual Salary", f"${average_salary:,.2f}")

    with col2:
        st.metric("Estimated Monthly Salary", f"${average_salary / 12:,.2f}")

    st.markdown("---")
   



    income = st.number_input("Monthly income:", min_value=0.0)
    savings = st.number_input("Current total savings:", min_value=0.0)
    debt = st.number_input("Current total debt:", min_value=0.0)
    emergency_fund = st.number_input("Emergency fund:", min_value=0.0)

    debt_ratio = debt / income if income > 0 else 0
    emergency_ratio = emergency_fund / income if income > 0 else 0
    savings_ratio = savings / income if income > 0 else 0

    st.subheader("Your Risk Analysis")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Debt / Monthly Income", f"{debt_ratio:.2f}")

    with col2:
        st.metric("Emergency Fund Months", f"{emergency_ratio:.2f}")

    with col3:
        st.metric("Savings Months", f"{savings_ratio:.2f}")

    st.markdown("---")

    if income == 0:
        st.info("Enter your income to begin.")
    elif debt_ratio > 6:
        st.error("High risk: Your debt is more than six months of income.")
    elif emergency_fund < income:
        st.warning("Medium risk: Your emergency fund is less than one month of income.")
    else:
        st.success("Low risk: Your financial position looks stable.")