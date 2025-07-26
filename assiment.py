# the total car price

total_price = 1753690.8

# the first payment
                    
down_payment = 160000.0
                     
loan_amount = total_price - down_payment
                     
                     
annual_interst_rate = 9.0
                     
monthly_interst_rate = annual_interst_rate /12/100
loan_period_years = 5
loan_period_months = loan_period_years * 12

# EMI
emi = loan_amount * monthly_interst_rate * (1 + monthly_interst_rate) ** loan_period_months / ((1 + monthly_interst_rate) ** loan_period_months - 1)

                     
# the results

print(f"Total Loan Amount: {loan_amount:,}")
print(f"Monthly EMI for {loan_period_years} years: {emi:,.2f}")