import pandas
import matplotlib.pyplot as plt

with open('lesson12/kostky.txt', encoding='utf-8') as f:
  lines = f.readlines()

print(lines[2])
lines = [line.replace('\n','') for line in lines]
kostky = pandas.Series(lines)
print(kostky.head())
kostky.hist(bins=1)
plt.show()