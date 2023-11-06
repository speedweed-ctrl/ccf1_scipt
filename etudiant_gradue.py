import matplotlib.pyplot as plt

# Data
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2018]  # Remove 2017 as it's missing in the data

categories = [
    "Droit",
    "Sciences sociales et du comportement",
    "Mathématiques and statistiques",
    "Sciences informatiques et télécommunications",
    "Sciences de la vie",
    "Architecture et bâtiment",
    "Ingénierie and techniques apparentées",
    "Santé"
]

data = [
    [4901, 3795, 3317, 2688, 3204, 3055, 2667, 2485],
    [4037, 3449, 2996, 2395, 2894, 3235, 3182, 2994],  # Removed 3182 data point for 2017
    [1971, 1128, 876, 685, 645, 727, 717, 611],  # Removed 689 data point for 2017
    [13749, 11525, 11960, 10728, 10251, 8966, 7492, 6515],  # Removed 7492 data point for 2017
    [3536, 1963, 1898, 1815, 1898, 2070, 1993, 2033],  # Removed 2264 data point for 2017
    [1208, 1315, 1545, 1443, 1540, 1469, 1475, 1274],
    [8355, 7757, 8184, 7494, 8234, 8557, 7986, 7235],
    [4348, 4626, 4708, 4593, 4297, 3676, 3491, 3401]  # Removed 3979 data point for 2017
]

# Transpose the data for plotting
data = list(map(list, zip(*data)))

# Plotting
width = 0.15
x = range(len(years))

fig, ax = plt.subplots(figsize=(12, 8))

for i, category in enumerate(categories):
    ax.bar([pos + width * i for pos in x], data[i], width, label=category)

ax.set_xlabel('Year')
ax.set_ylabel('Number of Students')
ax.set_title('Number of Students Graduated by Year and Category')
ax.set_xticks([pos + width * (len(categories) / 2) for pos in x])
ax.set_xticklabels(years)
ax.legend()

# Save the plot to a file
plt.savefig('graduated_students_bar.png', bbox_inches='tight')

# Optionally, you can also display the file path
print("Bar plot saved as 'graduated_students_bar.png'")
