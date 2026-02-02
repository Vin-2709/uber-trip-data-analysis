import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("UberDataset.csv")

dataset['PURPOSE'] = dataset['PURPOSE'].fillna("NOT")

dataset['START_DATE'] = pd.to_datetime(dataset['START_DATE'], errors='coerce')
dataset['END_DATE'] = pd.to_datetime(dataset['END_DATE'], errors='coerce')

dataset['date'] = dataset['START_DATE'].dt.date
dataset['time'] = dataset['START_DATE'].dt.hour

dataset['day-night'] = pd.cut(
    x=dataset['time'],
    bins=[0, 10, 15, 19, 24],
    labels=['Morning', 'Afternoon', 'Evening', 'Night'],
    include_lowest=True
)

dataset.dropna(inplace=True)

plt.figure(figsize=(20,5))
plt.subplot(1,2,1)
sns.countplot(x=dataset['CATEGORY'])
plt.xticks(rotation=90)

plt.subplot(1,2,2)
sns.countplot(y=dataset['PURPOSE'])

plt.show()

sns.countplot(x=dataset['day-night'])
plt.show()

dataset['MONTH'] = dataset['START_DATE'].dt.month

month_label = {
    1:'Jan',2:'Feb',3:'Mar',4:'April',5:'May',6:'June',
    7:'July',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'
}

dataset['MONTH'] = dataset['MONTH'].map(month_label)

mon = dataset['MONTH'].value_counts(sort=False)

df = pd.DataFrame({
    "MONTHS": mon.index,
    "VALUE COUNT": dataset.groupby('MONTH')['MILES'].max().values
})

sns.lineplot(data=df)
plt.xlabel("MONTHS")
plt.ylabel("VALUE COUNT")
plt.show()

dataset['DAY'] = dataset['START_DATE'].dt.weekday

day_label = {
    0:'Mon',1:'Tues',2:'Wed',3:'Thur',4:'Fri',5:'Sat',6:'Sun'
}

dataset['DAY'] = dataset['DAY'].map(day_label)

day_count = dataset['DAY'].value_counts()

sns.barplot(x=day_count.index, y=day_count.values)
plt.xlabel("DAY")
plt.ylabel("COUNT")
plt.show()

sns.boxplot(y=dataset['MILES'])
plt.show()

sns.boxplot(y=dataset[dataset['MILES']<100]['MILES'])
plt.show()

sns.boxplot(y=dataset[dataset['MILES']<40]['MILES'])
plt.show()

sns.histplot(dataset[dataset['MILES']<40]['MILES'], kde=True)
plt.show()
