# Nesting inside dictionaries

travel_log = {
    "France" : {"Cities Visited" : ["Paris", "Lille", "Dijon"] , "total_visits" : 12},
    "Germany" : {"Cities Visited" : ["Berlin", "München", "Hamburg"] , "total_visits" : 9}

}

# Nesting dictionaries inside lists

travel_log = [
    {
        "Country" : "France", 
        "Cities Visited" : ["Paris", "Lille", "Dijon"] , 
        "total_visits" : 12},

    {
        "Country" : "Germany", 
        "Cities Visited" : ["Berlin", "München", "Hamburg"] , 
        "total_visits" : 9}

]

# Adding to a list inside a dictionary

Details = {"Destination": "China", 
           "Nationality": "Italian", "Age": []}
Details["Age"] += [20, "Twenty"]
print(Details)