import sys
import math

# Save humans, destroy zombies!


class Entity:
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
        
class Ash (Entity):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)

class Zombie (Entity):
    def __init__(self, id : int, x: int, y: int, next_x:int, next_y: int) -> None:
        super().__init__(x,y)
        self.eliminated = False
        self.id = id
        self.next_x = next_x
        self.next_y = next_y

def dist(a: Entity, b: Entity) -> int:
    return int(math.sqrt(a.x*a.x + b.y*b.y))

ash = Ash(-1, -1)
zombies = {}

# game loop
while True:
    ash.x, ash.y = [int(i) for i in input().split()]
    
    human_count = int(input())
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        
    zombie_count = int(input())
    closest_zombie = None
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        if zombie_id not in zombies:
            zombies[zombie_id] = Zombie(zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext)
        else:
            zombies[zombie_id].x, zombies[zombie_id].y = zombie_x, zombie_y,
            zombies[zombie_id].next_x, zombies[zombie_id].next_y = zombie_xnext, zombie_ynext
            
        if (closest_zombie is None) or (dist(ash, closest_zombie) > dist(ash, zombies[zombie_id])):
            closest_zombie = zombies[zombie_id]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # Your destination coordinates
    print("{x} {y}".format(x = closest_zombie.x, y = closest_zombie.y))
