import streamlit as st

st.set_page_config(page_title="Finance Advisor", layout="wide")

st.sidebar.title("Navigation")

st.sidebar.markdown("---")
st.sidebar.caption("Source: Forbes")

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
        "High school completion":3,
        "Some college, no degree":4,
        "Associate's degree": 5,
        "Bachelor's degree": 6,
        "Doctor's degree": 7,
        "Professional degree": 8
    }

    average_salary_data = {
    "Less than 9th grade": {
        "16 to 19 years old": 24248,
        "20 to 24 years old": 24248,
        "25 to 34 years old": 30310,
        "35 to 44 years old": 30310,
        "45 to 54 years old": 30310,
        "55 to 64 years old": 24268,
        "65 years and older": 24248
    },
    "Some high school, no completion": {
        "16 to 19 years old": 27990,
        "20 to 24 years old": 27990,
        "25 to 34 years old": 31650,
        "35 to 44 years old": 31650,
        "45 to 54 years old": 31650,
        "55 to 64 years old": 27990,
        "65 years and older": 27990
    },
     "High school completion": {
        "16 to 19 years old": 32400,
        "20 to 24 years old": 32400,
        "25 to 34 years old": 40500,
        "35 to 44 years old": 40500,
        "45 to 54 years old": 48600,
        "55 to 64 years old": 32400,
        "65 years and older": 32400
    },
    "Some college, no degree": {
        "16 to 19 years old": 36664,
        "20 to 24 years old": 36664,
        "25 to 34 years old": 45830,
        "35 to 44 years old": 54996,
        "45 to 54 years old": 54996,
        "55 to 64 years old": 45830,
        "65 years and older": 36664
    },
  "Associate's degree": {
        "16 to 19 years old": 39888,
        "20 to 24 years old": 39888,
        "25 to 34 years old": 49860,
        "35 to 44 years old": 49860,
        "45 to 54 years old": 59832,
        "55 to 64 years old": 39888,
        "65 years and older": 39888
    },
    "Bachelor's degree": {
        "16 to 19 years old": 53808,
        "20 to 24 years old": 53808,
        "25 to 34 years old": 67260,
        "35 to 44 years old": 67260,
        "45 to 54 years old": 80712,
        "55 to 64 years old": 80712,
        "65 years and older": 53808
    },
    "Master's degree": {
        "16 to 19 years old": 65000,
        "20 to 24 years old": 65000,
        "25 to 34 years old": 81250,
        "35 to 44 years old": 81250,
        "45 to 54 years old": 97500,
        "55 to 64 years old": 97500,
        "65 years and older": 65000
    },
    "Professional degree": {
        "16 to 19 years old": 84120,
        "20 to 24 years old": 84120,
        "25 to 34 years old": 105150,
        "35 to 44 years old": 105150,
        "45 to 54 years old": 126180,
        "55 to 64 years old": 126180,
        "65 years and older": 126180
    },
    "Doctor's degree": {
        "16 to 19 years old": 81800,
        "20 to 24 years old": 81800,
        "25 to 34 years old": 102250,
        "35 to 44 years old": 102250,
        "45 to 54 years old": 122700,
        "55 to 64 years old": 122700,
        "65 years and older": 122700
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

    average_salary = average_salary_data[education_group][age_group]

    st.success(f"You selected: {age_group}")
    st.success(f"You selected: {education_group}")

    st.subheader("Estimated Average Salary")

    estimated_monthly_salary = average_salary / 12
    ideal_monthly_saving = estimated_monthly_salary * 0.20


    col1, = st.columns(1)

    with col1:
        st.metric("Estimated Annual Salary", f"${average_salary:,.2f}")



    st.markdown("---")

    st.subheader("Ideal Monthly Saving")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Estimated Monthly Salary", f"${estimated_monthly_salary:,.2f}")

    with col2:
        st.metric("Ideal Monthly Saving 20%", f"${ideal_monthly_saving:,.2f}")


 