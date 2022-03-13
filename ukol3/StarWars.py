from turtle import home


data = [
    {
        "name": "Luke Skywalker",
        "height": "172",
        "mass": "77",
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": "19BBY",
        "gender": "male",
        "homeworld": {
            "name": "Tatooine",
            "rotation_period": "23",
            "orbital_period": "304",
            "diameter": "10465",
            "climate": "arid",
            "gravity": "1 standard",
            "terrain": "desert",
            "surface_water": "1",
            "population": "200000"},
    },
    {
        "name": "Obi-Wan Kenobi",
        "height": "182",
        "mass": "77",
        "hair_color": "auburn, white",
        "skin_color": "fair",
        "eye_color": "blue-gray",
        "birth_year": "57BBY",
        "gender": "male",
        "homeworld": {
            "name": "Stewjon",
            "rotation_period": "unknown",
            "orbital_period": "unknown",
            "diameter": "0",
            "climate": "temperate",
            "gravity": "1 standard",
            "terrain": "grass",
            "surface_water": "unknown",
            "population": "unknown"}
    },
    {
        "name": "R2-D2",
        "height": "96",
        "mass": "32",
        "hair_color": "n/a",
        "skin_color": "white, blue",
        "eye_color": "red",
        "birth_year": "33BBY",
        "gender": "n/a",
        "homeworld": {
            "name": "Naboo",
            "rotation_period": "26",
            "orbital_period": "312",
            "diameter": "12120",
            "climate": "temperate",
            "gravity": "1 standard",
            "terrain": "grassy hills, swamps, forests, mountains",
            "surface_water": "12",
            "population": "4500000000"}
    },
    {
        "name": "Darth Vader",
        "height": "202",
        "mass": "136",
        "hair_color": "none",
        "skin_color": "white",
        "eye_color": "yellow",
        "birth_year": "41.9BBY",
        "gender": "male",
        "homeworld": {
            "name": "Tatooine",
            "rotation_period": "23",
            "orbital_period": "304",
            "diameter": "10465",
            "climate": "arid",
            "gravity": "1 standard",
            "terrain": "desert",
            "surface_water": "1",
            "population": "200000"}
    },
    {
        "name": "Chewbacca",
        "height": "228",
        "mass": "112",
        "hair_color": "brown",
        "skin_color": "unknown",
        "eye_color": "blue",
        "birth_year": "200BBY",
        "gender": "male",
        "homeworld": {
            "name": "Kashyyyk",
            "rotation_period": "26",
            "orbital_period": "381",
            "diameter": "12765",
            "climate": "tropical",
            "gravity": "1 standard",
            "terrain": "jungle, forests, lakes, rivers",
            "surface_water": "60",
            "population": "45000000"}
    },
    {
        "name": "Yoda",
        "height": "66",
        "mass": "17",
        "hair_color": "white",
        "skin_color": "green",
        "eye_color": "brown",
        "birth_year": "896BBY",
        "gender": "male",
        "homeworld": {
            "name": "unknown",
            "rotation_period": "0",
            "orbital_period": "0",
            "diameter": "0",
            "climate": "unknown",
            "gravity": "unknown",
            "terrain": "unknown",
            "surface_water": "unknown",
            "population": "unknown", }
    },
    {
        "name": "Leia Organa",
        "height": "150",
        "mass": "49",
        "hair_color": "brown",
        "skin_color": "light",
        "eye_color": "brown",
        "birth_year": "19BBY",
        "gender": "female",
        "homeworld": {
                "name": "Alderaan",
                "rotation_period": "24",
                "orbital_period": "364",
                "diameter": "12500",
                "climate": "temperate",
                "gravity": "1 standard",
                "terrain": "grasslands, mountains",
                "surface_water": "40",
                "population": "2000000000"}
    },
]

for person in data:
  person["height"] = int(person["height"])
  person["mass"] = int(person["mass"])
  planet = person["homeworld"]
  if planet["rotation_period"].isdigit():
    planet["rotation_period"] = int(planet["rotation_period"])
  if planet["orbital_period"].isdigit():
    planet["orbital_period"] = int(planet["orbital_period"])
  if planet["diameter"].isdigit():
    planet["diameter"] = int(planet["diameter"])
  if planet["surface_water"].isdigit():
    planet["surface_water"] = int(planet["surface_water"])
  if planet["population"].isdigit():
    planet["population"] = int(planet["population"])
  person["homeworld"] = planet

total_height = 0
for person in data:
  total_height += person["height"]

print (f'Prumerna vyska postav je {round(total_height/len(data))}')

gender_values = set([person["gender"] for person in data])

print (gender_values)

male = [person["name"] for person in data if person["gender"]=="male"]
female = [person["name"] for person in data if person["gender"]=="female"]
rest = [person["name"] for person in data if person["gender"]!="female" and person["gender"]!="male"]

gender = [female,male,rest]

print(gender)

gender2 = {"male": male, "female": female, "n/a": rest}
print(gender2)

print ("Postavy s bilymi vlasy nebo kuzi:")
for person in data:
  if "white" in person["hair_color"] or "white" in person["skin_color"]:
    print(person["name"])

planets = []
for person in data:
  if person["homeworld"] not in planets:
    planets.append(person["homeworld"])
namesPlanets = [planet["name"]for planet in planets]
print(namesPlanets)
