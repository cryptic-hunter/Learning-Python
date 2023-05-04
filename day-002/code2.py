#Create a program to calculate the life left if we live till 90 years
#1 year = 365 days, 52 weeks, 12 months
max_months = 1080
max_weeks = 4680
max_days = 32850
age = int(input("What is your current age? "))
age_weeks = age*52
age_months = age*12
age_days = age*365
age_months_left = max_months - age_months
age_weeks_left = max_weeks - age_weeks
age_days_left = max_days - age_days
print(f"You have {age_months_left} months, {age_weeks_left} weeks and {age_days_left} days left of your life")