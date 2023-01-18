import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

read_US_dataset = pd.read_csv('US_Accidents_Dec20.csv')
numberOfAccidents = read_US_dataset[['ID', 'State']].groupby('State').count().sort_values('ID', ascending=False)

warnings.simplefilter(action='ignore', category=FutureWarning)

sns.barplot(numberOfAccidents['ID'], numberOfAccidents.index)
sns.set(rc={"figure.figsize":(10, 8)})

x = numberOfAccidents["ID"]
y = numberOfAccidents.index

plt.figure(figsize=(15, 5))
display(plt.plot(y,x))
plt.xlabel('states')
plt.ylabel('Number of accidents')

plt.show()