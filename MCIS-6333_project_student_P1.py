# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load only the Birthrate column
usecols = ["Birthrate"]
cd_birthrate = pd.read_csv('country_data.csv', usecols=usecols)

# Distribution of Birthrate
birthrate = cd_birthrate['Birthrate']
plt.hist(birthrate, bins=10, color='dodgerblue', alpha=0.7, edgecolor='black')
plt.title('Distribution of Birthrate')
plt.xlabel('Birthrate')
plt.ylabel('Frequency')
plt.show()

# Load only the Literacy column
usecols=["Literacy"]
cd_literacy = pd.read_csv('country_data.csv', usecols=usecols)

# Distribution of Literacy Rate
literacy_rate = cd_literacy['Literacy']
counts, bins, _ = plt.hist(literacy_rate, bins=10, color='forestgreen', alpha=0.7, edgecolor='black')
plt.title('Distribution of Literacy Rate')
plt.xlabel('Literacy Rate (%)')
plt.ylabel('Frequency')
plt.show()

# Tallest bar range
print(f"Lower value of tallest bar: {bins[counts.argmax()]:.2f}")
print(f"Upper value of tallest bar: {bins[counts.argmax()+1]:.2f}")
