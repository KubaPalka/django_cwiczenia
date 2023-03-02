from random import randint, choice

def add_data(model):
    activity = ['True', 'False']
    names = ['Scorpions', 'Metallica', 'Muse', 'Kiss', 'Carcass']
    name = choice(names)
    g = randint(0, 6)
    genre = g
    year = '1979-01-01'
    still_active = choice(activity)
    for i in range(0, 5):
        model.objects.create(name=name, year=year, still_active=still_active, genre=genre)

def find_without(model):
    model.objects.get(name='null')

def find_with_text(model):
    return model.objects.filter(name__icontains="corp")


def find_categories(model):
    return model.objects.all()






