import matplotlib.pyplot as plt

# =====================================================================
# 1. THE DATA (Our Information)
# =====================================================================

# Level 1: Bird Species
species = ["Sparrow", "Pigeon", "Crow", "Parrot", "Myna"]
sightings = [120, 95, 80, 60, 45]

# Level 2: Time vs Activity
time_of_day = ["6AM", "8AM", "10AM", "12PM", "2PM", "4PM", "6PM"]
bird_activity = [90, 85, 70, 50, 40, 60, 80]
human_traffic = [10, 30, 60, 90, 100, 70, 30]

# Level 3: Park Zones Data
tree_density = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115]
species_diversity = [3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 9, 10, 11, 11, 4, 5, 3]
tree_age = [30, 25, 20, 18, 35, 28, 40, 38, 32, 30, 45, 42, 50, 48, 55, 52, 60, 58, 65, 70]


# =====================================================================
# 2. THE LAYOUT (Creating a 2x2 Grid Window)
# =====================================================================
# This creates 1 big window (fig) with 4 smaller boxes (axes) arranged in 2 rows and 2 columns
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Urban Ecology Dashboard", fontsize=14, fontweight="bold")


# =====================================================================
# 3. DRAWING THE CHARTS
# =====================================================================

# Box 1 (Top Left): Bar Chart
axes[0, 0].bar(species, sightings, color="skyblue")
axes[0, 0].set_title("Bird Sightings (Bar Chart)")
axes[0, 0].set_xlabel("Species")
axes[0, 0].set_ylabel("Count")

# Box 2 (Top Right): Line Graph
axes[0, 1].plot(time_of_day, bird_activity, marker="o", label="Birds", color="green")
axes[0, 1].plot(time_of_day, human_traffic, marker="s", label="Humans", color="red")
axes[0, 1].set_title("Activity Trends (Line Graph)")
axes[0, 1].set_xlabel("Time")
axes[0, 1].set_ylabel("Level")
axes[0, 1].legend() # Shows the small color guide box

# Box 3 (Bottom Left): Scatter Plot
axes[1, 0].scatter(tree_density, species_diversity, color="teal")
axes[1, 0].set_title("Trees vs Bird Diversity (Scatter Plot)")
axes[1, 0].set_xlabel("Tree Density")
axes[1, 0].set_ylabel("Diversity Index")

# Box 4 (Bottom Right): Bubble Chart
# 's' sets the size of the dots using the tree age multiplied by 10
axes[1, 1].scatter(tree_density, species_diversity, s=[age * 10 for age in tree_age], color="orange", alpha=0.6)
axes[1, 1].set_title("Trees vs Diversity (Bubble Size = Tree Age)")
axes[1, 1].set_xlabel("Tree Density")
axes[1, 1].set_ylabel("Diversity Index")


# =====================================================================
# 4. SHOW EVERYTHING AT ONCE
# =====================================================================
plt.tight_layout() # Cleans up spacing so text doesn't overlap
plt.show()         # Python opens the window HERE, and waits until you close it.
print("Finished running successfully!")