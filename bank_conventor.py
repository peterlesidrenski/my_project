deposit = float(input("enter a number: "))
deposit_time = float(input("enter time"))
yearly_procent = float(input("enter number: "))
procent = yearly_procent / 100
price = float(deposit + deposit_time * ((deposit * procent)/12))
print(price)