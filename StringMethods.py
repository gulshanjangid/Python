text = "   python programming   "

# 1. Remove spaces
text = text.strip()

# 2. First letter capital
print(text.capitalize())

# 3. Uppercase
print(text.upper())

# 4. Lowercase
print(text.lower())

# 5. Title
print(text.title())

# 6. Replace
print(text.replace("python", "FastAPI"))

# 7. Split
words = text.split()
print(words)

# 8. Join
result = "-".join(words)
print(result)

# 9. Find
print(text.find("python"))

# 10. Count
print(text.count("p"))

# 11. Starts with
print(text.startswith("python"))

# 12. Ends with
print(text.endswith("programming"))