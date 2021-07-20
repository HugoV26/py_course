"""
    * List Comprehension

     ~ [expr for val in collection]
     ~ [expr for val in collection if condition]
     ~ [expr for val in collection if condition1 and condition2]
     ~ [expr for val1 in collection1 and val2 in collection2]

"""

squares = []

for i in range(1, 101):
    squares.append(i**2)

print(squares)

squares_two = [i**2 for i in range(1, 101)]
print(squares_two)

videogames = ["Mario Kart", "Resident Evil", "The Legend of Zelda", "Mario Bros", "Silent Hill"]

mario_games = []

for game in videogames:
    if game.startswith('Mario'):
        mario_games.append(game)
print(mario_games)

m_games = [game for game in videogames if game.startswith("Mario")]
print(m_games)

consoles = [('Brow Box', 1967), ('Atari Pong', 1975), ('Nintendo Nes', 1985), ('Playstation', 1994), ('Playstation 2', 2001), ('Xbox 360', 2005)]

# antes del 2000
old_consoles = [console[0] for console in consoles if console[1] < 2000]
old_consoles = [console for (console, year) in consoles if year < 2000]
print(old_consoles)

"""
    * Cartesian Product

    A = {1, 3}
    B = {x, y}

    A x B = {(1, x), (1, y), (3, x), (3, y)}

"""

A = [1, 3, 5]
B = [2, 4, 6]
# ~ [expr for val1 in collection1 val2 in collection2]
cartesian_product = [(a, b) for a in A for b in B]
print(cartesian_product)