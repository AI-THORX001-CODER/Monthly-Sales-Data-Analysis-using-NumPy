import numpy as np 
print("monthly sales data analysis:")


months =np.array(["jan","feb","march","april","may","jun","july"])

sales= np.array([10000,30899,40000,90000,560000,120000,90800])

average_sales= np. mean(sales)
max_sales =np. max(sales)

best_month_index= np . argmax(sales)
best_month= months[best_month_index]

growth= (sales[-1] -sales[0] / sales[0])*100

print("\nMonths :", months)
print("Sales :", sales)

print("\n📈 Average Sales :", average_sales)

print("🏆 Best Month :", best_month)
print("💰 Highest Sales :", max_sales)

print("🚀 Sales Growth :", round(growth, 2), "%")