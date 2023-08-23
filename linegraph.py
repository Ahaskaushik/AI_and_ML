import pandas as pd
import matplotlib.pyplot  as plt

data = pd.read_csv(r"C:\Users\SPTINT-04\Downloads\tips.csv")
df=pd.DataFrame(data)
print(df)
plt.plot(df['tip'])
plt.plot(df['day'])
plt.xlabel("days")
plt.ylabel("tip")
plt.show()

