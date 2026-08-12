import matplotlib.pyplot as plt
import numpy as np

# Data
scores = [4, 5, 6, 7, 8, 9, 10]
frequencies = [1, 2, 3, 5, 4, 3, 2]
total_n = sum(frequencies)  # should be 20

# 1. Print the frequency table
print("Frequency Table")
print("+" + "-" * 20 + "+")
print(f"| {'Score (x)':^10} | {'Frequency (f)':^10} |")
print("+" + "-" * 20 + "+")
for x, f in zip(scores, frequencies):
    print(f"| {x:^10} | {f:^10} |")
print("+" + "-" * 20 + "+")
print(f"| {'Total (N)':^10} | {total_n:^10} |")
print("+" + "-" * 20 + "+")
print()

# Create the vertical bar chart
plt.figure(figsize=(8, 5))
bars = plt.bar(scores, frequencies, color='skyblue', edgecolor='black', width=0.6)

# Customize the chart
plt.xlabel('Score (x)', fontsize=12)
plt.ylabel('Frequency (f)', fontsize=12)
plt.title('Frequency Distribution of Scores', fontsize=14)
plt.xticks(scores)  # ensure all score values are shown
plt.yticks(range(0, max(frequencies) + 2))  # y-axis from 0 to at least max+1
plt.ylim(0, max(frequencies) + 1)  # give a little headroom

# add frequency values on top of bars
for bar, freq in zip(bars, frequencies):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
             str(freq), ha='center', va='bottom', fontsize=10)

# Show grid for readability (optional)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()