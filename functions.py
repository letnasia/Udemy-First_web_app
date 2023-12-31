FILEPATH = './todos.txt'


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of to-do items.
    :param filepath:
    :return: list
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath=FILEPATH):
    """
    Write the to-do items list in the text file.
    :param todos_local:
    :param filepath:
    :return: None
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_local)


if __name__ == '__main__':
    print(get_todos())

