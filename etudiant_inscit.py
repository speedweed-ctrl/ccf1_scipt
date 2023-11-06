import matplotlib.pyplot as plt

# Data
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]  # Remove 2019 as it's missing in the data

categories = [
    "Droit",
    "Sciences sociales et du comportement",
    "Mathématiques et statistiques",
    "Sciences informatiques et télécommunications",
    "Sciences de la vie",
    "Architecture et bâtiment",
    "Ingénierie and techniques apparentées",
    "Santé"
]

data = [
    [19319, 18793, 17688, 16889, 15615, 14594, 13869, 14583, 14449],
    [16607, 16208, 17911, 18328, 16284, 16540, 16446, 16307, 15842],
    [5451, 4982, 4720, 4113, 3468, 3189, 2628, 2570, 2237],
    [48275, 43493, 39930, 37149, 30993, 28490, 27150, 26173, 26889],
    [8427, 8497, 8487, 7872, 7335, 7309, 6775, 6108, 5957],
    [7442, 7188, 7167, 7006, 6363, 6105, 5986, 5823, 5684],
    [47635, 45576, 44932, 45331, 40664, 37216, 35114, 34435, 35950],
    [22308, 20958, 20989, 20529, 20610, 19480, 19482, 19177, 0]  # Remove 0 for 2019
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
ax.set_title('Number of Regular Enrolled Students by Year and Category')
ax.set_xticks([pos + width * (len(categories) / 2) for pos in x])
ax.set_xticklabels(years)
ax.legend()

# Save the plot to a file
plt.savefig('enrolled_students_bar.png', bbox_inches='tight')

# Optionally, you can also display the file path
print("Bar plot saved as 'enrolled_students_bar.png'")
