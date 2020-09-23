DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS owners;


CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT
);

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    breed VARCHAR(255),
    owner INT REFERENCES owners(id)
);