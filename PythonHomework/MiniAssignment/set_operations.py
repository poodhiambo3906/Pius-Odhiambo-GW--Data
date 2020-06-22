
"""Set Operations."""

hero1 = {"smart", "rich", "armored", "martial_artist", "strong"}
hero2 = {"smart", "fast", "strong", "invulnerable", "antigravity"}

print(hero1)
print(hero2)

# Attributes for both heros (union)
hero1 | hero2
hero1.union(hero2)
print(hero1.union(hero2))
print('- - - - - - - - -')

# Attributes common to both heros (intersection)
hero1 & hero2
hero1.intersection(hero2)
print(hero1.intersection(hero2))
print('- - - - - - - - -')

# Attributes in hero1 that are not in hero2 (difference)
hero1 - hero2
hero1.difference(hero2)
print(hero1 - hero2)
print('- - - - - - - - -')

# Attributes in hero2 that are not in hero1 (difference)
hero2 - hero1
hero2.difference(hero1)
print(hero2 - hero1)
print('- - - - - - - - -')

# Attributes for hero1 or hero2 but not both (symmetric difference)
hero1 ^ hero2
hero1.symmetric_difference(hero2)
print(hero1 ^ hero2)
