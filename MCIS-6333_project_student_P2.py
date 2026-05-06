# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn
import matplotlib

# Apply a style for better visuals
matplotlib.style.use('ggplot')

# Reading the dataset
cd = pd.read_csv('country_data.csv')

# -------------------------------
# 2a. Simple Scatter Plot: Population vs Area
# -------------------------------
plt.figure(figsize=(8, 6))
scatter = plt.scatter(
    cd['Population'], 
    cd['Area'], 
    c=cd['Population'],   # color by Population values
    cmap='viridis',        # you can change to 'plasma', 'cividis', 'cool', etc.
    edgecolors='black',
    s=50,                  # marker size
    alpha=0.8              # transparency
)

plt.colorbar(scatter, label='Population')  # Add a colorbar for reference

plt.title('Population vs Area')
plt.xlabel('Population')
plt.ylabel('Area (sq miles)')
plt.grid(True)
plt.show()

# -------------------------------
# 2b. 16 Scatter Plots for Birthrate, Deathrate, Infant mortality, and GDP
# -------------------------------

# Selecting the relevant columns
selected_columns = ['Birthrate', 'Deathrate', 'Infant mortality', 'GDP', 'Region']
cd_selected = cd[selected_columns].dropna()

# Creating 16 scatter plots (pairplot)
sbn.pairplot(cd_selected, hue='Region', palette='Set1', plot_kws={'s': 20})
plt.suptitle('Pairwise Scatter Plots of Birthrate, Deathrate, Infant Mortality, and GDP', y=1.0005)
plt.show()