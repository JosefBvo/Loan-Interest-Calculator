totalpaid = 0 #initialized for later for loop

print("\nInterest Calculator\n")

print("Enter the amount of the loan: ")
loan = float(input())
initial_loan = loan

print("Enter the interest rate: ")
interest = float(input())
interest = interest / 100 / 12 #this gets monthly interest

print("Enter the length of the loan (in months): ")
months = int(input())

min_payment = (loan * interest * (1 + interest) ** months) / ((1 + interest) ** months -1) #calculates the minimum payment

for i in range(months): #for loop to calculate the total amount paid over life of loan
    loan = (loan - min_payment)
    loan = (loan * interest)
    totalpaid = totalpaid + min_payment 
    if months == 0: break

interest_paid = totalpaid - initial_loan

print("The minimum payment is: $", round(min_payment, 2))
print("The amount paid in interest would be: $",round(interest_paid, 2))
print("The total amount that would be paid is: $", round(totalpaid, 2))





