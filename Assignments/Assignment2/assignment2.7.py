countries = ["Finland", "Germany", "Sweden", "Ireland", "Turkey"]

filtered_countries = list(filter(lambda country: "and" in country, countries))
print(filtered_countries)

#without using filter()
countries = ["Finland", "Germany", "Sweden", "Ireland", "Turkey"]
filtered_countries = []

for country in countries:
    if "and" in country:
        filtered_countries.append(country)

print(filtered_countries)

