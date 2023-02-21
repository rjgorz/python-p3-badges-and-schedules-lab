def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(names):
    rooms = []
    for i in range(len(names)):
        rooms.append(f"Hello, {names[i]}! You'll be assigned to room {i + 1}!")
    return rooms

def printer(names):    
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)

    for badge in badges:
        print(badge)
    for room in rooms:
        print(room)

    return None