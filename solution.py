# Fantasy Quest Inventory Management System
# This program creates a character inventory system for a fantasy RPG game

# Part 1: Character Profile (Using Dictionaries and Basic Types)
print("PART 1: CHARACTER PROFILE")
print("-----------------------")

# Creating the character profile dictionary with basic information
character_profile = {
    'name': "Alistair the Brave",
    'level': 1,
    'health': 100,
    'mana': 50,
    'gold': 50.75,
    'is_alive': True
}

# Printing character's name and level
print(f"Character Name: {character_profile['name']}")
print(f"Character Level: {character_profile['level']}")

# Updating character's health
character_profile['health'] = 85
print(f"Updated health: {character_profile['health']}")

# Adding experience to the character profile
character_profile['experience'] = 0
print(f"Added experience: {character_profile['experience']}")

# Printing the final character profile
print("\nFinal Character Profile:")
print(character_profile)

# Part 2: Inventory System (Using Lists)
print("\nPART 2: INVENTORY SYSTEM")
print("-----------------------")

# Creating inventory list with initial items
inventory = ['sword', 'shield', 'health potion']
print(f"Initial inventory: {inventory}")

# Adding a new item to the inventory
inventory.append('mana potion')
print(f"After adding mana potion: {inventory}")

# Removing an item from the inventory
inventory.remove('shield')
print(f"After removing shield: {inventory}")

# Iterating through inventory and printing each item
print("\nInventory items:")
for item in inventory:
    print(f"- {item}")

# Part 3: Character Stats (Using Tuples)
print("\nPART 3: CHARACTER STATS")
print("-----------------------")

# Creating a tuple for base stats (strength, dexterity, intelligence)
base_stats = (10, 8, 12)
print(f"Base stats (strength, dexterity, intelligence): {base_stats}")

# Explaining why tuple is a good choice for base stats
print("\nWhy tuples are good for base stats:")
print("Tuples are immutable, meaning they cannot be changed after creation.")
print("This is perfect for base stats which should remain constant.")

# Accessing and printing the intelligence value
print(f"\nIntelligence value: {base_stats[2]}")

# Trying to change a value in the tuple (will cause an error)
print("\nTrying to change a tuple value:")
try:
    base_stats[0] = 15
except TypeError as e:
    print(f"Error occurred: {e}")
    print("This proves tuples are immutable!")

# Part 4: Quest Log (Using Sets)
print("\nPART 4: QUEST LOG")
print("-----------------------")

# Creating a quest log using a set
quest_log = {'Defeat the Goblin King', 'Find the Lost Amulet'}
print(f"Initial quest log: {quest_log}")

# Adding a new quest
quest_log.add('Deliver the Old Scroll')
print(f"After adding new quest: {quest_log}")

# Trying to add a duplicate quest
print("\nTrying to add a duplicate quest:")
quest_log.add('Defeat the Goblin King')
print(f"Quest log after adding duplicate: {quest_log}")
print("Notice the quest wasn't added twice because sets only store unique items!")

# Removing a completed quest
quest_log.remove('Find the Lost Amulet')
print(f"\nAfter removing completed quest: {quest_log}")

# Part 5: Putting it all together
print("\nPART 5: COMPLETE CHARACTER SHEET")
print("-----------------------")

# Creating the character sheet dictionary
character_sheet = {
    'profile': character_profile,
    'inventory': inventory,
    'stats': base_stats,
    'quests': quest_log
}

# Printing the entire character sheet
print("Complete Character Sheet:")
print(character_sheet)

# To make it more readable, let's print it nicely
print("\nCharacter Sheet (Formatted):")
print(f"Name: {character_sheet['profile']['name']}")
print(f"Level: {character_sheet['profile']['level']}")
print(f"Health: {character_sheet['profile']['health']}")
print(f"Mana: {character_sheet['profile']['mana']}")
print(f"Gold: {character_sheet['profile']['gold']}")
print(f"Is Alive: {character_sheet['profile']['is_alive']}")
print(f"Experience: {character_sheet['profile']['experience']}")
print(f"Inventory: {character_sheet['inventory']}")
print(f"Base Stats: {character_sheet['stats']}")
print(f"Active Quests: {character_sheet['quests']}")