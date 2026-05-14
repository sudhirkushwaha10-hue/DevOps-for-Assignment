Base_salary=int(50000)
Bonus=int(5000)
Other_Charges=int(2000)
Gross_Salary=float(Base_salary+Bonus)
Tax=(1/10*(Base_salary+Bonus))
Net_Salary=Gross_Salary-Tax-Other_Charges
print("Gross Salary:", Gross_Salary)
print("Net_Salary:",Net_Salary )