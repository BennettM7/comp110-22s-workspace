"""Demonstrations of dictionary capabilities."""

# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dicitionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19_400
schools["Dook"] = 0
schools["NCSU"] = 26_150

# Print a dictionary literal representation
print(schools)

# Access a value by its key -- "lookup"
print(schools["UNC"])

# Remove a key-value pair from a dictionary
# by its key.
schools.pop("Dook")

# Test for exisitence of a key
is_duke_present: bool = "Dook" in schools
print(is_duke_present)

print(schools)

# Update / Reassign a key-value pair
schools["UNC"] = 20_000
schools["NCSU"] += 200

print(schools)

# Demonstration of dictionary literals

# Empty dictionary literal
schools = {}  # same as dict()
print(schools)

# Alternatively, intitalize key-value pairs
schools = {
    "UNC": 19400, 
    "Dukie": 6717
}
print(schools)

# Example looping over the keys of a dict
for key in schools:
    print(f"Key: {key} - Value: {schools[key]}")