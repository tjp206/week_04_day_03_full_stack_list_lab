import pdb
from models.animals import Animals
from models.owners import Owners

import repositories.animals_repo as animals_repo
import repositories.owners_repo as owners_repo


animals_repo.delete_all()
owners_repo.delete_all()

owner_1 = Owners('Ally', 25)
owners_repo.save(owner_1)
owner_2 = Owners('Maddie', 31)
owners_repo.save(owner_2)

animal_1 = Animals('Oscar', 'Shih Tzu', owner_1)
animals_repo.save(animal_1)
animal_2 = Animals('Peach', 'Cat', owner_2)
animals_repo.save(animal_2)


