# metodo para leer un archivo txt en python  
from students.models import Ciudad


with open('ciudades.txt','r', encoding='utf-8') as c:
    cities = c.readlines()
    cities = list(map(lambda l: l.strip('\n'), cities))
    for city in cities:
        Ciudad.objects.create(ciudad = city)



