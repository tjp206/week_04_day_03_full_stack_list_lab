from db.run_sql import run_sql
from models.animals import Animals
from repositories import owners_repo

def save(animal):
    sql = "INSERT INTO animals (name, breed, owner) VALUES (%s, %s, %s) RETURNING *"
    values = [animal.name, animal.breed, animal.owner.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal

def select_all():
    animals = []

    sql = "SELECT * FROM animals"
    results = run_sql(sql)

    for row in results:
        owner = owners_repo.select(row['owner'])
        animal = Animals(row['name'], row['breed'],owner, row['id'])
        animals.append(animal)
    return animals

def select(id):
    task = None
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        owner = owners_repo.select(result['id'])
        animal = Animals(result['name'], result['breed'], owner.id, result['id'])
    return animal

def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)