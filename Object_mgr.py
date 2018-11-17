global objects
objects = [[],[],[]]


def add_object(o, layer):
    objects[layer].append(o)


def remove_object(o):
    for i in range(len(objects)):
        for obj in objects[i]:
            if obj == o:
                objects[i].remove(obj)
                del obj


def clear():
    for o in all_objects():
        del o
    objects.clear()

def clear_and_create_new_Objects():
    clear()
    global objects
    objects = [[], [],[]]

def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o

def find_curtain_object(layer, index):
    find = 0
    for obj in objects[layer]:
        if find == index:
            return obj
        find += 1

