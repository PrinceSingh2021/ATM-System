import streamlit as st

class Atm:
    def __init__(self):
        self.pin = ''
        self.balance = 0

    def create_pin(self, pin):
        self.pin = pin
        return "PIN set successfully"

    def deposit(self, pin, amount):
        if pin == self.pin:
            self.balance += amount
            return "Deposit successful"
        else:
            return "Invalid PIN"

    def withdraw(self, pin, amount):
        if pin == self.pin:
            if amount <= self.balance:
                self.balance -= amount
                return "Withdrawal successful"
            else:
                return "Insufficient funds"
        else:
            return "Invalid PIN"

    def check_balance(self, pin):
        if pin == self.pin:
            return f"Your balance is Rs.{self.balance:.2f}"
        else:
            return "Invalid PIN"

# Initialize or load user data
def get_user_data(user_id):
    if user_id not in st.session_state:
        st.session_state[user_id] = Atm()

# Streamlit app
st.set_page_config(page_title="ATM System", page_icon=":atm:", layout="wide")

st.title("ATM System")
st.sidebar.title("ATM Menu")

user_id = st.sidebar.text_input("Enter your User ID")

if user_id:
    get_user_data(user_id)
    atm = st.session_state[user_id]
else:
    st.error("Please enter a User ID")

if user_id:
    menu = st.sidebar.radio("Choose an option", ["Create PIN", "Deposit", "Withdraw", "Check Balance"])

    if menu == "Create PIN":
        st.subheader("Set Your PIN")
        new_pin = st.text_input("Enter your new PIN", type="password")
        if st.button("Set PIN"):
            if new_pin:
                result = atm.create_pin(new_pin)
                st.success(result)
            else:
                st.error("PIN cannot be empty")

    elif menu == "Deposit":
        st.subheader("Deposit Funds")
        pin = st.text_input("Enter your PIN", type="password")
        amount = st.number_input("Enter the amount to deposit", min_value=0.0, format="%.2f")
        if st.button("Deposit"):
            result = atm.deposit(pin, amount)
            if result == "Deposit successful":
                st.success(result)
            else:
                st.error(result)

    elif menu == "Withdraw":
        st.subheader("Withdraw Funds")
        pin = st.text_input("Enter your PIN", type="password")
        amount = st.number_input("Enter the amount to withdraw", min_value=0.0, format="%.2f")
        if st.button("Withdraw"):
            result = atm.withdraw(pin, amount)
            if result == "Withdrawal successful":
                st.success(result)
            else:
                st.error(result)

    elif menu == "Check Balance":
        st.subheader("Check Your Balance")
        pin = st.text_input("Enter your PIN", type="password")
        if st.button("Check Balance"):
            result = atm.check_balance(pin)
            if "Invalid PIN" in result:
                st.error(result)
            else:
                st.info(result)
else:
    st.error("Please enter a User ID")
