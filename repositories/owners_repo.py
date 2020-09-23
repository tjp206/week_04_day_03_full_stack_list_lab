from db.run_sql import run_sql
from models.owners import Owners
from models.animals import Animals

def save(owner):
    sql = "INSERT INTO owners (name, age) VALUES (%s, %s) RETURNING *"
    values = [owner.name, owner.age]
    results = run_sql(sql, values)
    id = results[0]['id']
    owner.id = id
    return owner

def select_all():
    owners = []

    sql = "SELECT * FROM owners"
    results = run_sql(sql)
    for row in results:
        owner = Owners(row['name'], row['age'], row['id'])
        owners.append(owner)
    return owners

def select(id):
    owner = None
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        owner = Owners(result['name'], result['age'], result['id'])
    return owner

def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM owners WHERE id = %s"
    values = [id]
    run_sql(sql, values)