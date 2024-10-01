paragragh = "i had a good experience in improve my skills throw Tuwaiq Academy in Riyadh"
city = "Riyadh"

print("Length:", len(paragragh))

occurrence = paragragh.lower().find(city.lower())
print("occurrence:", occurrence)

count_C = paragragh.lower().count(city.lower())
print("appears:", count_C)

print("uppercase:", paragragh.upper())
print("lowercase:", paragragh.lower())

NewCity = "jeddah"
NewParagragh = paragragh.replace(city, NewCity, 1)
print("New Paragragh:", NewParagragh)
print("Last char:", paragragh[-1])
