def remove_duplicates(data):
    """
    Usuwa duplikaty z listy.
    :param data: lista dowolnych elementów
    :return: lista bez duplikatów
    """
    return list(set(data))

def flatten(nested_list):
    """
    Spłaszcza listę zagnieżdżoną o jeden poziom.
    :param nested_list: lista list
    :return: lista elementów
    """
    return [item for sublist in nested_list for item in sublist]
