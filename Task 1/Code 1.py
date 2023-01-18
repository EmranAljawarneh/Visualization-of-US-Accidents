import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

read_US_dataset = pd.read_csv('US_Accidents_Dec20.csv')
US_accident_data_frame = pd.DataFrame(read_US_dataset)

plt.figure(figsize=(18, 8))
sns.scatterplot(x ='Start_Lng',y='Start_Lat', data=US_accident_data_frame, hue='State')