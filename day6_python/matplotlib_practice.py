import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import pandas as pd

df = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May","Jun"],
    "Sales":[120,150,180,170,210,250],
    "Profit":[20,25,35,30,45,55],
    "Customers":[100,120,150,130,180,220],
    "Category":["A","B","A","B","A","B"]
})
#plt.plot(df["Month"], df["Sales"])

#plt.title("Monthly Sales")
#plt.xlabel("Month")
#plt.ylabel("Sales")

#plt.show()
#plt.bar(df["Month"], df["Sales"])

#plt.title("Monthly Sales")
#plt.show()

#plt.hist(df["Sales"], bins=5)

#plt.show()

sales = [40,30,20,10]
labels = ["A","B","C","D"]

plt.pie(
    sales,
    labels=labels,
    autopct="%1.1f%%"
)

plt.show()