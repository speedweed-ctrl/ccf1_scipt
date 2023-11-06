import matplotlib.pyplot as plt

# Data
categories = ['Taux de chômage', 'Masculin', 'Féminin']
values = [23.7, 14.9, 31]  # Adjust the values accordingly

# Create a donut chart
fig, ax = plt.subplots()
ax.pie(values, labels=categories, autopct='%1.1f%%', startangle=90, pctdistance=0.85)

# Draw a circle in the center (donut hole)
center_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(center_circle)

# Equal aspect ratio ensures that the pie chart is drawn as a circle.
ax.axis('equal')

# Title
plt.title('Taux de chômage des diplômés de l’enseignement supérieur par genre')

# Save the chart to a file
plt.savefig('donut_chart.png', bbox_inches='tight')

