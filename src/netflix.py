# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# filter for movies released between 1991 and 1998

filtered = netflix_df[np.logical_and(netflix_df["release_year"] > 1990 ,netflix_df["release_year"] < 1999)]

# filter for action movies
action_movies = filtered[filtered["genre"] == "Action"]
# count how many action movies are shorter than 90 minutes
short_movie_count = 0
for index, row in action_movies.iterrows():
    if row["duration"] < 90:
        short_movie_count += 1


# Set style 
plt.style.use('seaborn-v0_8-darkgrid')
plt.figure(figsize=(12, 8))

# Create histogram 
plt.hist(filtered["duration"], bins=20, color="#1D4C75", alpha=0.8, 
         edgecolor='white', linewidth=1.2)

# vertical line at x = 100
plt.axvline(x=100, color='#4ECDC4', linestyle='--', linewidth=3, alpha=0.9)

# Styled labels and title
plt.xlabel("Duration (minutes)", fontsize=14, fontweight='bold', color='#2C3E50')
plt.ylabel("Number of Movies", fontsize=14, fontweight='bold', color='#2C3E50')
plt.title(" Distribution of Movie Durations (1991-1998)", 
          fontsize=18, fontweight='bold', color='#E74C3C', pad=20)

# Styled legend
plt.legend(["100 minute mark"], fontsize=12, frameon=True, 
           fancybox=True, shadow=True, framealpha=0.9)

# styled grid
plt.grid(True, alpha=0.3, color='gray', linestyle='-', linewidth=0.5)

# Set background color
plt.gca().set_facecolor('#F8F9FA')

plt.tight_layout()
plt.show()
