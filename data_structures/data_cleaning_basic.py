data = [10, None, 20, "", 30, None, 40]

cleaned = []
for item in data:
    if item not in (None, ""):
        cleaned.append(item)

print("Cleaned data:", cleaned)
