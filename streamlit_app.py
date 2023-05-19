import streamlit as st

def calculate_zakat(weight_gold_24, weight_gold_22, weight_gold_18, value_other_gold, value_precious_stones,
                    weight_silver, value_cash, value_loans_investments, value_landed_property, value_business_stock,
                    value_partnership_firms):
    zakat_percentage = 2.5
    zakat_payable_gold_24 = (weight_gold_24 * zakat_percentage) / 100
    zakat_payable_gold_22 = (weight_gold_22 * zakat_percentage) / 100
    zakat_payable_gold_18 = (weight_gold_18 * zakat_percentage) / 100
    zakat_payable_other_gold = (value_other_gold * zakat_percentage) / 100
    zakat_payable_precious_stones = (value_precious_stones * zakat_percentage) / 100
    zakat_payable_silver = (weight_silver * zakat_percentage) / 100
    zakat_payable_cash = (value_cash * zakat_percentage) / 100
    zakat_payable_loans_investments = (value_loans_investments * zakat_percentage) / 100
    zakat_payable_landed_property = (value_landed_property * zakat_percentage) / 100
    zakat_payable_business_stock = (value_business_stock * zakat_percentage) / 100
    zakat_payable_partnership_firms = (value_partnership_firms * zakat_percentage) / 100

    return (zakat_payable_gold_24, zakat_payable_gold_22, zakat_payable_gold_18, zakat_payable_other_gold,
            zakat_payable_precious_stones, zakat_payable_silver, zakat_payable_cash, zakat_payable_loans_investments,
            zakat_payable_landed_property, zakat_payable_business_stock, zakat_payable_partnership_firms)


def main():
    st.title("Zakat Calculator")

    st.subheader("Assets")

    weight_gold_24 = st.number_input("Weight of 24 Carat Gold/Jewelry (grams):", min_value=0.0, step=0.01)
    weight_gold_22 = st.number_input("Weight of 22 Carat Gold/Jewelry (grams):", min_value=0.0, step=0.01)
    weight_gold_18 = st.number_input("Weight of 18 Carat Gold/Jewelry (grams):", min_value=0.0, step=0.01)
    value_other_gold = st.number_input("Value of Other Gold Valuables:", min_value=0.0)
    value_precious_stones = st.number_input("Value of Precious Stones:", min_value=0.0)
    weight_silver = st.number_input("Weight of Silver (grams):", min_value=0.0, step=0.01)

    st.subheader("Cash and Bank Balances")

    value_cash = st.number_input("Cash in Hand:", min_value=0.0)
    value_savings_accounts = st.number_input("Cash in Bank (Savings Accounts):", min_value=0.0)
    value_current_accounts = st.number_input("Cash in Bank (Current Accounts):", min_value=0.0)
    value_fixed_deposits = st.number_input("Cash in Bank (Fixed Deposits):", min_value=0.0)

    st.subheader("Loans,investments, and Funds")
    value_loans_investments = st.number_input("Loans, Investments, and Funds:", min_value=0.0)

    st.subheader("Landed Property")

    value_landed_property = st.number_input("Value of Landed Property:", min_value=0.0)

    st.subheader("Business (Stock-in-Trade)")

    value_business_stock = st.number_input("Value of Saleable Stock:", min_value=0.0)
    value_damaged_stock = st.number_input("Value of Damaged/Dead Stock:", min_value=0.0)
    value_credit_sales = st.number_input("Amount Receivable from Credit Sales:", min_value=0.0)
    value_payable_suppliers = st.number_input("Amount Payable to Suppliers:", min_value=0.0)
    value_bad_debts = st.number_input("Bad Debts:", min_value=0.0)

    st.subheader("Share in Partnership Firms")

    value_capital_balance = st.number_input("Capital Balance as per Last Balance Sheet:", min_value=0.0)
    value_loans_advanced = st.number_input("Loans Advanced to the Firm:", min_value=0.0)
    value_withdrawals = st.number_input("Withdrawals made during the current Year:", min_value=0.0)
    value_accumulated_profit = st.number_input("Accumulated Profit from the date of Balance Sheet to this Date:",
                                               min_value=0.0)

    if st.button("Calculate Zakat"):
        (zakat_payable_gold_24, zakat_payable_gold_22, zakat_payable_gold_18, zakat_payable_other_gold,
         zakat_payable_precious_stones, zakat_payable_silver, zakat_payable_cash, zakat_payable_loans_investments,
         zakat_payable_landed_property, zakat_payable_business_stock, zakat_payable_partnership_firms) = calculate_zakat(
            weight_gold_24, weight_gold_22, weight_gold_18, value_other_gold, value_precious_stones,
            weight_silver, value_cash, value_loans_investments, value_landed_property, value_business_stock,
            value_partnership_firms)

        st.subheader("Zakat Payable")
        st.write("Weight in Grams\tPrice/Gm\tEstimated Value\tZakat Payable")
        st.write(f"1. ZAKAT ON GOLD (2.5%)")
        st.write(f"1a. 24 Carat Gold/Jewelry\t{weight_gold_24}\t\t\t\t\t\t\t{zakat_payable_gold_24}")
        st.write(f"1b. 22 Carat Gold/Jewelry\t{weight_gold_22}\t\t\t\t\t\t\t{zakat_payable_gold_22}")
        st.write(f"1c. 18 Carat Gold/Jewelry\t{weight_gold_18}\t\t\t\t\t\t\t{zakat_payable_gold_18}")
        st.write(f"1d. Other Gold Valuables\t\t\t\t{value_other_gold}\t\t\t\t{zakat_payable_other_gold}")

        st.write(f"2. ZAKAT ON PRECIOUS STONES (2.5%)")
        st.write(f"Calculate the nett Market Value of the Precious stones like Diamonds, Rubies, Etc.")
        st.write(f"and add them to the Estimated Value Column if they are purchased for commercial purpose.")
                st.write(f"3. ZAKAT ON SILVER (2.5%)")
        st.write(f"Include Household Silver Utensils, Artefacts, and Jewelry.")
        st.write(f"For Utensils, usually the silver is 90% pure so take 90% of the total weight.")
        st.write(f"Weight in Grams\tPrice/Gm\tEstimated Value\tZakat Payable")
        st.write(f"\t\t\t\t\t\t{weight_silver}\t\t\t\t\t\t\t{zakat_payable_silver}")

        st.write(f"4. ZAKAT ON CASH IN HAND/BANK (2.5%)")
        st.write(f"Weight in Grams\tPrice/Gm\tEstimated Value\tZakat Payable")
        st.write(f"4a. Cash in Hand\t\t\t\t\t\t{value_cash}\t\t\t\t\t\t{zakat_payable_cash}")

        st.write(f"4b. Cash in Bank (Savings Accounts)\t\t\t\t{value_savings_accounts}\t\t\t\t\t\t{zakat_payable_cash}")
        st.write(f"4c. Cash in Bank (Current Accounts)\t\t\t\t{value_current_accounts}\t\t\t\t\t\t{zakat_payable_cash}")
        st.write(f"4d. Cash held in Fixed Deposits\t\t\t\t{value_fixed_deposits}\t\t\t\t\t\t{zakat_payable_cash}")

        st.write(f"5. ZAKAT ON LOANS/INVESTMENTS/FUNDS/SHARES, ETC (2.5%)")
        st.write(f"Weight in Grams\tPrice/Gm\tEstimated Value\tZakat Payable")
        st.write(f"5a. Loans Receivable from Friends and Relatives\t\t\t{zakat_payable_loans_investments}")
        st.write(f"5b. Investment in Govt Bonds/Mutual Funds/etc\t\t\t{zakat_payable_loans_investments}")
        st.write(f"5c. Optional Provident Fund balance\t\t\t\t\t{zakat_payable_loans_investments}")
        st.write(f"5d. Cash Value of Takaful Policies\t\t\t\t\t{zakat_payable_loans_investments}")
        st.write(f"5e. Value of Shares (stocks) including Dividends\t\t\t{zakat_payable_loans_investments}")
        st.write(f"5f. Government Security Deposits, ADRs, etc\t\t\t\t{zakat_payable_loans_investments}")
        st.write(f"5g. Investment in Private Chits, Funds, etc\t\t\t\t{zakat_payable_loans_investments}")
        st.write(f"5h. Investment in Cars Business etc\t\t\t\t\t{zakat_payable_loans_investments}")

        st.write(f"6. ZAKAT ON LANDED PROPERTY (2.5%)")
        st.write(f"Weight in Grams\tPrice/Gm\tEstimated Value\tZakat Payable")
        st.write(f"6a. Landed Property held as an Investment/Business\t\t{value_landed_property}\t\t\t{zakat_payable_landed_property}")
        st.write(f"6b. Zakat on Rentals Coming from Property\t\t\t\t{zakat_payable_landed_property}")

        st.write(f"7. ZAKAT ON BUSINESS (2.5%)")
                st.write(f"7a. Value of Saleable Stock\t\t\t\t\t\t{value_business_stock}\t\t\t\t\t\t{zakat_payable_business_stock}")
        st.write(f"7b. Value of Damaged/Dead Stock\t\t\t\t\t\t{value_damaged_stock}\t\t\t\t\t\t{zakat_payable_business_stock}")
        st.write(f"7c. Amount Receivable from Credit Sales\t\t\t\t{value_credit_sales}\t\t\t\t\t\t{zakat_payable_business_stock}")
        st.write(f"7d. LESS: Amount Payable to Suppliers\t\t\t\t\t{value_payable_suppliers}\t\t\t\t\t\t{zakat_payable_business_stock}")
        st.write(f"7e. LESS: Bad Debts\t\t\t\t\t\t\t\t\t{value_bad_debts}\t\t\t\t\t\t\t{zakat_payable_business_stock}")

        st.write(f"8. ZAKAT ON SHARE IN PARTNERSHIP FIRMS (2.5%)")
        st.write(f"Weight in Grams\tPrice/Gm\tEstimated Value\tZakat Payable")
        st.write(f"8a. Capital Balance as per Last Balance Sheet\t\t\t{value_capital_balance}\t\t\t\t\t\t{zakat_payable_partnership_firms}")
        st.write(f"8b. Loans Advanced by you to the Firm as of Date\t\t\t{value_loans_advanced}\t\t\t\t\t\t{zakat_payable_partnership_firms}")
        st.write(f"8c. LESS: Withdrawals made by you during the current Year\t\t{value_withdrawals}\t\t\t\t\t\t{zakat_payable_partnership_firms}")
        st.write(f"8d. Accumulated Profit from the date of Balance Sheet to this Date\t{value_accumulated_profit}\t\t\t\t\t\t{zakat_payable_partnership_firms}")

        st.write("NETT TOTAL WORTH CALCULATED")

        st.write("11. GENERAL LIABILITIES")
        st.write("You need to deduct your direct Payables or Liabilities which have not been deducted earlier.")
        st.write("Usage of the loan should have been on Zakatable Wealth only.")

        value_loans_to_pay = st.number_input("Loans/Debts which are to be paid back:", min_value=0.0)
        value_income_tax = st.number_input("Income Tax/Wealth Tax Payable:", min_value=0.0)

        total_liabilities = value_loans_to_pay + value_income_tax

        st.write("TOTAL LIABILITIES")
        st.write(total_liabilities)

        total_zakat_payable = (zakat_payable_gold_24 + zakat_payable_gold_22 + zakat_payable_gold_18 +
                               zakat_payable_other_gold + zakat_payable_precious_stones + zakat_payable_silver +
                               zakat_payable_cash + zakat_payable_loans_investments + zakat_payable_landed_property +
                               zakat_payable_business_stock + zakat_payable_partnership_firms) - total_liabilities

        st.write("TOTAL ZAKAT PAYABLE")
        st.write(total_zakat_payable)


if __name__ == "__main__":
    main()


