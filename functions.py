from os.path import exists
def get_todos(filepath='todos.txt'):
    if not exists(filepath):
        with open(filepath, 'x') as file:
            pass
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_write,filepath='todos.txt'):
    with open(filepath, 'w') as file:
        file.writelines(todos_write)