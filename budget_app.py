import streamlit as st
import plotly.express as px

# Create a title for your app
st.title("Financial Toolkit")

# Add a sidebar for navigation
menu = st.sidebar.selectbox("Select Module", ["Budgeting", "Credit Cards", "Credit Score", "Taxes", "Scholarships", "Financial Aid"])

if menu == "Budgeting":
    st.header("Budgeting")
    st.write("This module helps you manage your finances and track your income and expenses. It also provides visualizations of your budget.")
    
    # Initialize dictionaries to store income and expenses using st.session_state
    if 'income' not in st.session_state:
        st.session_state.income = {}
    if 'expenses' not in st.session_state:
        st.session_state.expenses = {}
    
    # Create two input sections for income and expenses
    st.header("Income")
    income_name = st.text_input("Income Source")
    income_amount = st.number_input("Amount (Income)", step=0.01)
    
    if st.button("Add Income"):
        st.session_state.income[income_name] = st.session_state.income.get(income_name, 0) + income_amount
    
    st.header("Expenses")
    expense_name = st.text_input("Expense Description")
    expense_amount = st.number_input("Amount (Expense)", step=0.01)
    expense_category = st.selectbox("Category", ["Food", "Housing", "Transportation", "Entertainment", "Other"])
    
    if st.button("Add Expense"):
        expense_data = st.session_state.expenses.get(expense_category, [])
        expense_data.append((expense_name, expense_amount))
        st.session_state.expenses[expense_category] = expense_data
    
    # Display the current budget
    total_income = sum(st.session_state.income.values())
    total_expenses = sum(sum(v for _, v in data) for data in st.session_state.expenses.values())
    balance = total_income - total_expenses
    
    st.write(f"Total Income: ${total_income:.2f}")
    st.write(f"Total Expenses: ${total_expenses:.2f}")
    st.write(f"Balance: ${balance:.2f}")
    
    # Create a pie chart to visualize expenses by category
    expense_categories = list(st.session_state.expenses.keys())
    expense_sums = [sum(v for _, v in data) for data in st.session_state.expenses.values()]
    
    fig = px.pie(names=expense_categories, values=expense_sums, title="Expense Categories")
    st.plotly_chart(fig)
    
    # Create a pie chart to visualize money saved versus money available for spending
    if balance > 0:
        savings = balance
        spending = total_income - balance
    else:
        savings = 0
        spending = total_income
    
    savings_data = [savings, spending]
    savings_labels = ["Savings", "Spending"]
    savings_fig = px.pie(names=savings_labels, values=savings_data, title="Money Saved vs. Money Available for Spending")
    st.plotly_chart(savings_fig)

elif menu == "Credit Cards":
    st.header("Credit Cards")
    st.write("Learn how to apply for credit cards, compare different card options, and understand credit card terms and benefits.")
    st.markdown("[Click here for more information on Credit Cards](https://www.investopedia.com/terms/c/creditcard.asp#:~:text=Key%20Takeaways%201%20Credit%20cards%20are%20plastic%20or,options%20for%20those%20with%20little%20or%20bad%20credit.)")
    # Add content related to credit cards
    # ...

elif menu == "Credit Score":
    st.header("Credit Score")
    st.write("Discover the importance of your credit score, how it is calculated, and how to improve it for better financial opportunities.")
    st.markdown("[Click here for more information on Credit Scores](https://www.investopedia.com/terms/c/credit_score.asp)")
    # Add content related to credit scores
    # ...

elif menu == "Taxes":
    st.header("Taxes")
    st.write("Understand tax regulations, deductions, and credits. Get tips on how to file your taxes and maximize your returns.")
    st.markdown("[Click here for more information on Taxes](https://myscholly.com/taxes-for-college-students/")
    # Add content related to taxes
    # ...

elif menu == "Scholarships":
    st.header("Scholarships")
    st.write("Explore opportunities for scholarships, grants, and financial aid to support your education.")
    st.markdown("[Click here for more information on Scholarships](https://www.usnews.com/education/best-colleges/paying-for-college/articles/how-to-find-and-secure-scholarships-for-college#:~:text=Students%20should%20review%20a%20scholarship%27s%20website%20to%20learn,or%20letters%20of%20recommendation.%205%20Meet%20posted%20deadlines.")
    # Add content related to scholarships
    # ...

elif menu == "Financial Aid":
    st.header("Financial Aid")
    st.write("Learn about financial aid options, including grants, loans, and work-study programs, to fund your education.")
    st.markdown("[Click here for more information on Financial Aid](https://studentaid.gov/")
    # Add content related to financial aid
    # ...