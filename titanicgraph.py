import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("C:/Users/SPTINT-04/Documents/titanic11_12.csv")
df=pd.DataFrame(data)
print(df.head(10))
plt.hist(df['Age'])
plt.title("frequency distribution of Age")
plt.show()
print(df['Sex'].value_counts().plot(kind="bar"))
plt.show()
c=df[df['Pclass']==3]
f=c[c['Sex']=='female']
f['Survived'].value_counts().plot(kind='bar')
plt.show()
plt.scatter(df['Age'], df['Fare'])
plt.show()
df['Fare'].quantile([.25,.50,.75]).plot(kind='hist')
plt.title("Quantile function")
plt.show()


