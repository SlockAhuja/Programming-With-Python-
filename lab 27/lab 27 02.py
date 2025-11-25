# ahuja Slock
import seaborn as sns
sns.set(style="dark")
fmri = sns.load_dataset("fmri")
# Plot the responses for different\
# events and regions
sns.lineplot(x="timepoint",
             y="signal",
             hue="region",
             style="event",
             data=fmri)
