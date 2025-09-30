import random
import matplotlib.pyplot as plt

rolls = [random.randint(1, 6) for _ in range(100)]

plt.hist(rolls, bins=range(1, 8), align='left', rwidth=0.8)
plt.title('Distribution of 100 Dice Rolls')
plt.xlabel('Dice Roll Outcome')
plt.ylabel('Frequency')
plt.xticks(range(1, 7))
plt.show()
