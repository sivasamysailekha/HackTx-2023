import streamlit as st
import plotly.express as px
import requests
from bs4 import BeautifulSoup

# Function to scrape student discounts from a sample website
def scrape_student_discounts():
    url = "https://collegeinfogeek.com/student-discounts/"  
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        discounts = []

       
        discount_elements = soup.find_all("div", class_="student-discount")
        for element in discount_elements:
            discount_name = element.find("h2").text
            discount_description = element.find("p").text
            discounts.append({"Name": discount_name, "Description": discount_description})

        return discounts
    else:
        return []


st.title("Budget U")
st.markdown('<style>h1{color: #3366FF;}</style>', unsafe_allow_html=True)

menu = st.sidebar.selectbox("Select Module", ["Budgeting", "Credit Cards", "Credit Score", "Taxes", "Scholarships", "Financial Aid", "Banking"])
st.sidebar.markdown('<style>.sidebar .selectbox {background-color: #3366FF; color: white;}</style>', unsafe_allow_html=True)

if menu == "Budgeting":
    st.header("Budgeting")
    st.write("This module helps you manage your finances and track your income and expenses. It also provides visualizations of your budget.")
    
    #dictionaries to store income and expenses 
    if 'income' not in st.session_state:
        st.session_state.income = {}
    if 'expenses' not in st.session_state:
        st.session_state.expenses = {}
    
    #input section for monthly income
    st.header("Monthly Income")
    monthly_income = st.number_input("Monthly Income", step=0.01)
    st.session_state.income["Monthly Income"] = monthly_income

    # two input sections for additional income and expenses
    st.header("Additional Income")
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
    
    #pie chart to visualize expenses by category
    expense_categories = list(st.session_state.expenses.keys())
    expense_sums = [sum(v for _, v in data) for data in st.session_state.expenses.values()]
    
    fig = px.pie(names=expense_categories, values=expense_sums, title="Expense Categories")
    st.plotly_chart(fig)
    
    #pie chart to visualize money saved versus money available for spending
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
    st.markdown("[Click here for more information on Credit Cards](https://www.example.com/credit-cards)")
    

elif menu == "Credit Score":
    st.header("Credit Score")
    st.write("Discover the importance of your credit score, how it is calculated, and how to improve it for better financial opportunities.")
    st.markdown("[Click here for more information on Credit Scores](https://www.example.com/credit-scores)")
    

elif menu == "Taxes":
    st.header("Taxes")
    st.write("Understand tax regulations, deductions, and credits. Get tips on how to file your taxes and maximize your returns.")
    st.markdown("[Click here for more information on Taxes](https://www.example.com/taxes)")
    

elif menu == "Scholarships":
    st.header("Scholarships")
    st.write("Explore opportunities for scholarships, grants and other forms of income for students")
    st.markdown("[Click here for more information on Scholarships](https://www.example.com/scholarships)")
    

elif menu == "Financial Aid":
    st.header("Financial Aid")
    st.write("Learn about financial aid options, including grants, loans, and work-study programs, to fund your education.")
    st.markdown("[Click here for more information on Financial Aid](https://www.example.com/financial-aid)")
    
elif menu == "Banking":
    st.header("Banking")
    st.write("Explore banking-related features and services.")

    
    st.subheader("Banking Information")
    bank_name = st.text_input("Bank Name")
    account_type = st.selectbox("Account Type", ["Savings", "Checking", "Credit Card"])
    account_number = st.text_input("Account Number")
    initial_balance = st.number_input("Initial Balance", step=0.01)

    if st.button("Add Banking Info"):
        pass
      

    
    st.subheader("Track Amounts")
    transaction_description = st.text_input("Transaction Description")
    transaction_amount = st.number_input("Transaction Amount", step=0.01)
    transaction_type = st.selectbox("Transaction Type", ["Deposit", "Withdrawal"])

    if st.button("Add Transaction"):
        pass

discounts = scrape_student_discounts()

if discounts:
    st.subheader("Available Student Discounts")
    for discount in discounts:
        st.write(f"**{discount['Name']}**: {discount['Description']}")
else:
    st.write("No student discounts available at the moment. Check back later!")


st.markdown('<style>body {background-color: #F5F5F5;}</style>', unsafe_allow_html=True)


st.markdown('<p style="text-align:center; color: #3366FF;">© 2023 Financial Toolkit</p>', unsafe_allow_html=True)