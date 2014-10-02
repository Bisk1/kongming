import random


def get_random(model):
    """
    Gets a random object from any of the objects for given model. It uses all records specified
    for this model in the database. If there is not even one object of given model, exception occurs.
    :param model: model of the objects to be randomized
    :return: single object of given model
    """
    count = model.objects.all().count()
    assert count > 0
    random_index = random.randint(0, count - 1)
    return model.objects.all()[random_index]


def get_random_list(model, number):
    """
    Gets a list of random object from any of the objects for given model. It uses all records specified
    for this model in the database. If there are less objects of given model than required, exception occurs.
    :param model: model of the objects to be randomized
    :param number: number of the objects to be randomized
    :return: list of objects of given model
    """
    count = model.objects.all().count()
    assert count > number
    return random.sample(model.objects.all(), number)
