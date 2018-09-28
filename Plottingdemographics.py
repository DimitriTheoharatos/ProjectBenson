import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
from difflib import SequenceMatcher

sns.set()
df = pd.read_csv('stationdemographic.csv')
print(df.columns)
sns.scatterplot(x='avg_age', y='Rich Women', data=df)
plt.show()