# Ahuja Slock

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# initialise data of lists
data = {
    'Name': ['Slock', 'Dhaval', 'Tosif', 'Dhamo'],
    'Age': [21, 30, 28, 25]
}

df = pd.DataFrame(data)

# Draw violin plot
sns.violinplot(y=df['Age'])
plt.show()
