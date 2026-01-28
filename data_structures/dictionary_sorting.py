scores = {
    "Aman": 85,
    "Riya": 92,
    "Karan": 78
}

# Sort by marks (descending)
sorted_scores = dict(
    sorted(scores.items(), key=lambda x: x[1], reverse=True)
)

print(sorted_scores)
