#Dictionary in List example

travel_log = [
    {
        "Country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "Country" : "Germany",
        "visits" : 5,
        "cities" : ["Berlin", "Hamburg", "Stuttgart"]
    }
]

#todo : write the function that will allow new country to be added to travel_log

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["Country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)











# #Nesting
# capitals = {
#     "France" : "Paris",
#     "Germany" : "Dictionary"
# }

# #Nesting a dictionary within dictionary
# travel_log = {
#     "France" : {
#         "cities_visited" : ["Paris", "Lille", "Dijon"],
#         "total_visits" : 12 
#     },
#     "Germany" : {
#         "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits" : 15
#     }
# }


