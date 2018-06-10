import random

def random_walk(n):
    """Return coordenates after move 'n' random blocks"""
    x,y = 0,0
    for i in range(n):
        (dx,dy)= random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x,y = x + dx, y + dy
    return(x,y)


number_of_walk = 22000
for walk_length in range(1,31):
    no_transport = 0
    for i in range(number_of_walk):
        (x,y) = random_walk(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
    no_transport_percentage = float(no_transport)/number_of_walk
    sol = "Walk size = {size}, percentage of no transport = {percentage}".format(size = walk_length, percentage = no_transport_percentage * 100)
    print(sol)
