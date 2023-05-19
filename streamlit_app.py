import streamlit as st

def calculate_zakat(product_values, currency):
    zakat_percentage = 2.5
    total_product_value = sum(product_values)
    zakat_amount = (zakat_percentage / 100) * total_product_value
    return zakat_amount, currency

def main():
    st.title("Zakat Calculator")

    currencies = ['USD', 'EUR', 'GBP']  # Add more currencies as needed
    currency = st.selectbox("Select Currency:", currencies)

    asset_types = ['Gold', 'Silver', 'Cash', 'Real Estate', 'Investments']  # Add more asset types as needed

    product_values = []
    for asset_type in asset_types:
        product_value = st.number_input(f"Enter value of {asset_type} in {currency}:")
        product_values.append(product_value)

    if st.button("Calculate Zakat"):
        zakat_amount, selected_currency = calculate_zakat(product_values, currency)
        st.success(f"Total Zakat amount in {selected_currency}: {zakat_amount:.2f}")

    nisab_thresholds = {
        'USD': 4000,
        'EUR': 3000,
        'GBP': 2500
    }  # Add more thresholds for different currencies

    st.subheader("Nisab Threshold")
    st.write(f"The current Nisab threshold for {currency} is {nisab_thresholds[currency]}.")

    st.subheader("Donation Options")
    st.write("Consider donating your Zakat to these charitable organizations:")
    st.write("- Islamic Relief USA.")
    st.write("- Zakat Foundation of America.")
    st.write("- Muslim Aid USA.")

if __name__ == "__main__":
    main()