plt.figure(figsize=(10, 6))
bars = df['level'].value_counts().plot(kind='bar')

# Add number labels on top of each bar
for bar in bars.patches:  # 'patches' contains the rectangles (bars)
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,  # x position at center of bar
        height,                             # y position on top of bar
        int(height),                         # label (count)
        ha='center', va='bottom'            # center horizontally, bottom vertically
    )

plt.title("Levels Distribution")
plt.xlabel("Levels")
plt.ylabel("Count")
plt.show()

# =======================================================
# Plot using the new labels
plt.figure(figsize=(10, 6))
bars = df['level'].value_counts().sort_index().plot( # sort_index ensures proper order
    kind='bar',
    rot=0  # <-- ensures horizontal x-axis labels
)

# Add number labels on top of each bar
for bar in bars.patches:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        int(height),
        ha='center', va='bottom'
    )

plt.title("Levels Distribution")
plt.xlabel("Levels")
plt.ylabel("Count")
plt.show()
