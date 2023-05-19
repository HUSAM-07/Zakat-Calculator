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

    st.subheader("Zakat Information")
    with st.beta_expander("Click to expand Zakat information"):
        st.write("Zakat on Pure Gold and Gold Jewellery")
        st.write("Zakat should be calculated at 2.5% of the market value as on the date of valuation (Lunar date). Most Ulema favour the Market Value prevailing as on the date of Calculation and not the purchase price.")
        st.write("")
        st.write("Zakat on Precious and Semi-Precious Stones")
        st.write("If these precious stones were purchased for commercial purpose (as an inventory), only then the market value of these precious stones will be considered while calculating zakat.")
        st.write("One may calculate the Saleable Value of Items-at-hand on the date of Zakat Calculation.")
        st.write("")
        st.write("Zakat on Silver")
        st.write("Zakat is to be paid on Silver in Pure form or Jewellery, Utensils, Decorative items and all household items including crockery, cutlery made of silver at 2.5% of the prevailing market rates.")
        st.write("")
        st.write("Zakat on Cash and Bank Balances")
        st.write("Zakat should be paid at 2.5% on all cash balance and bank balances in your savings, current or FD accounts. The amount technically should be in the bank for one year. Usually it happens that the balance keeps on changing as per personal requirements.")
        st.write("You may make your best judgement and the best way is to pay on remaining amount on the day of calculation")
        st.write("")
        st.write("Zakat on Loans Given, Funds, etc")
        st.write("by you on loans you have given to your friends and relatives. It should be treated as Cash in Hand. You may deduct Loans Payable by you to arrive at the nett present value of your wealth. However, if you are in doubt, on the return of your money, then you may not calculate it as your wealth. But you can add it to your wealth retrospectively if and when you receive your money.")
        st.write("Zakat is payable on all Govt Bonds, Public Sector Bond, Cash value of Takaful policies, your paid-up portion of BC/Committee (Bachat/voluntary contribution) which is not yet received, Govt Bills receivables, etc. Please remember you need to be aware of what the sharia says about Insurance and other types of investments. It is outside the scope of this Zakath Calculator.")
        st.write("")
        st.write("Zakat on Landed Property")
        st.write("Zakat is not payable on personal residential House even if you have more than one and meant for residential purpose only. Also, Zakat is not applicable to the value of Property given on rent irrespective of how many. However, Zakat is payable on the rental income itself which remains till the date of Zakat.")
        st.write("However, if your intention of holding properties is to sell at a future date for a profit or as an investment, then Zakat is payable on the Market Value of the property on Zakat date.")
        st.write("Your paid-up portion of BC/Committee (Bachat/voluntary contribution) which is not yet received")

    st.subheader("Disclaimer")
    st.write("This Zakah Calculator is uploaded for the benefit of our customers to calculate their Zakah for the year. However, it is suggested that the Zakah calculation shall be further presented to a Sharia Scholar for his review/feedback.")

if __name__ == "__main__":
    main()

