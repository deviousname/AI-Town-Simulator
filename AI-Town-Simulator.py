#coded with OpenAI Playground through prompt guidance with additional bug fixes and coding by deviousname
"""
### Here is what this code does... ###
1. It creates a list of first names and a list of last names.
2. It creates a list of full names by combining a random first name and a random last name.
3. It creates a list of ages by generating a random number between 18 and 100.
4. It creates a dictionary of full names and ages by combining the full names list and the ages list.
5. It finds the oldest person in the dictionary and stores their name and age.
6. It creates a list of jobs.
7. It creates a dictionary of full names, ages, and jobs by combining the full names dictionary and the jobs list.
8. It finds the youngest person in the dictionary and stores their name, age, and job.
9. It creates a list of hobbies.
10. It creates a dictionary of full names, ages, jobs, and hobbies by combining the full names/ages/jobs dictionary and the hobbies list.
11. It finds the person with the most hobbies in the dictionary and stores their name, age, job, and hobbies.
12. It creates a dictionary of full names, ages, jobs, hobbies, and synopses by combining the full names/ages/jobs/hobbies dictionary and a synopsis generator.
13. It finds the most positive person in the dictionary and stores their name, age, job, hobbies, and synopsis.
14. It creates a dictionary of people by combining the full names/ages/jobs/hobbies/synopses dictionary and adding some extra information.
15. It creates a dictionary of towns by combining a town name generator and a town stuff generator.
16. It creates a dictionary of worlds by combining a world name generator and a world stuff generator.
17. It creates a list of dialogue.
18. It creates a while loop that generates random events and dialogue.
"""

import random
import time

first_names = ['John', 'Jane', 'Leroy', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James',
               'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara',
               'Elizabeth', 'Laura', 'Jennifer', 'Maria']

last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson',
              'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore',
              'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']

full_names = []

for i in range(100):
    first = random.choice(first_names)
    last = random.choice(last_names)
    full_names.append(f"{first} {last}")

ages = []
for i in range(100):
    ages.append(random.randint(18, 100))
    
full_names_ages = dict(zip(full_names, ages))
oldest = 0
for name, age in full_names_ages.items():
    if age > oldest:
        oldest = age
        oldest_name = name

jobs = ['Teacher', 'Doctor', 'Lawyer', 'Programmer', 'Scientist', 'Engineer', 'Accountant', 'Janitor', 'Chef',
        'Bartender', 'Waiter', 'Waitress', 'Carpenter', 'Plumber', 'Electrician', 'Mechanic', 'Farmer', 'Rancher',
        'Police Officer', 'Firefighter', 'Nurse']

full_names_ages_jobs = {}
for name, age in full_names_ages.items():
    full_names_ages_jobs[name] = [age, random.choice(jobs)]
    
youngest = 100
for name, age_job in full_names_ages_jobs.items():
    if age_job[0] < youngest:
        youngest = age_job[0]
        youngest_name = name
        youngest_job = age_job[1]

hobbies = ['Fishing', 'Hunting', 'Golfing', 'Hiking', 'Camping', 'Swimming', 'Dancing', 'Singing',
           'Playing an instrument', 'Painting', 'Drawing', 'Sculpting', 'Writing', 'Reading', 'Coding',
           'Programming', 'Sewing']

full_names_ages_jobs_hobbies = {}
for name, age_job in full_names_ages_jobs.items():
    full_names_ages_jobs_hobbies[name] = [age_job[0], age_job[1], []]
    for i in range(random.randint(1, 5)):
        full_names_ages_jobs_hobbies[name][2].append(random.choice(hobbies))
        
most_hobbies = 0
for name, age_job_hobbies in full_names_ages_jobs_hobbies.items():
    if len(age_job_hobbies[2]) > most_hobbies:
        most_hobbies = len(age_job_hobbies[2])
        most_hobbies_name = name
        most_hobbies_list = age_job_hobbies[2]

full_names_ages_jobs_hobbies_synopsis = {}
for name, age_job_hobbies in full_names_ages_jobs_hobbies.items():
    
    full_names_ages_jobs_hobbies_synopsis[name] = [age_job_hobbies[0], age_job_hobbies[1], age_job_hobbies[2], '']
    
    if age_job_hobbies[0] < 30:
        full_names_ages_jobs_hobbies_synopsis[name][3] += 'Young '
    elif age_job_hobbies[0] < 60:
        full_names_ages_jobs_hobbies_synopsis[name][3] += 'Middle-aged '
    else:
        full_names_ages_jobs_hobbies_synopsis[name][3] += 'Old '
        
    if age_job_hobbies[1] in ['Teacher', 'Doctor', 'Lawyer', 'Programmer', 'Scientist', 'Engineer', 'Accountant']:
        full_names_ages_jobs_hobbies_synopsis[name][3] += 'Professional '        
    elif age_job_hobbies[1] in ['Janitor', 'Chef', 'Bartender', 'Waiter', 'Waitress', 'Carpenter', 'Plumber',
                                'Electrician', 'Mechanic', 'Farmer', 'Rancher']:
        
        full_names_ages_jobs_hobbies_synopsis[name][3] += 'Blue-collar '
    else:
        full_names_ages_jobs_hobbies_synopsis[name][3] += 'Service '
        
    if 'Fishing' in age_job_hobbies[2] or 'Hunting' in age_job_hobbies[2] or 'Golfing' in age_job_hobbies[2] or 'Hiking' in age_job_hobbies[2] or 'Camping' in age_job_hobbies[2] or 'Swimming' in age_job_hobbies[2]:
        full_names_ages_jobs_hobbies_synopsis[name][3] += 'Outdoorsy '
    elif 'Dancing' in age_job_hobbies[2] or 'Singing' in age_job_hobbies[2] or 'Playing an instrument' in age_job_hobbies[2] or 'Painting' in age_job_hobbies[2] or 'Drawing' in age_job_hobbies[2] or 'Sculpting' in age_job_hobbies[2]:
        full_names_ages_jobs_hobbies_synopsis[name][3] += 'Artistic '
    elif 'Writing' in age_job_hobbies[2] or 'Reading' in age_job_hobbies[2] or 'Coding' in age_job_hobbies[2] or 'Programming' in age_job_hobbies[2] or 'Sewing' in age_job_hobbies[2]:
        full_names_ages_jobs_hobbies_synopsis[name][3] += 'Intellectual '
    else:
        full_names_ages_jobs_hobbies_synopsis[name][3] += 'Normal '
        
    full_names_ages_jobs_hobbies_synopsis[name][3] += 'Person'
    
most_positive = 0
for name, age_job_hobbies_synopsis in full_names_ages_jobs_hobbies_synopsis.items():
    if age_job_hobbies_synopsis[3].count('Young') + age_job_hobbies_synopsis[3].count('Professional') + age_job_hobbies_synopsis[3].count('Outdoorsy') + age_job_hobbies_synopsis[3].count('Artistic') + age_job_hobbies_synopsis[3].count('Intellectual') > most_positive:
        most_positive = age_job_hobbies_synopsis[3].count('Young') + age_job_hobbies_synopsis[3].count('Professional') + age_job_hobbies_synopsis[3].count('Outdoorsy') + age_job_hobbies_synopsis[3].count('Artistic') + age_job_hobbies_synopsis[3].count('Intellectual')
        most_positive_name = name
        most_positive_synopsis = age_job_hobbies_synopsis[3]

People_Dictionary = {}
for name, age_job_hobbies_synopsis in full_names_ages_jobs_hobbies_synopsis.items():
    People_Dictionary[name] = {'Age': age_job_hobbies_synopsis[0], 'Job': age_job_hobbies_synopsis[1], 'Hobbies': age_job_hobbies_synopsis[2], 'Synopsis': age_job_hobbies_synopsis[3]}

People_Dictionary[oldest_name]['Village Elder'] = True
People_Dictionary[youngest_name]['Player Character'] = True
People_Dictionary[most_hobbies_name]['Merchant'] = True
People_Dictionary[most_positive_name]['Town Mayor'] = True

lover_1 = random.choice(list(People_Dictionary.keys()))
lover_2 = random.choice(list(People_Dictionary.keys()))

while lover_1 == lover_2:
    lover_2 = random.choice(list(People_Dictionary.keys()))
    
People_Dictionary[lover_1]['Lover'] = lover_2
People_Dictionary[lover_2]['Lover'] = lover_1
People_Dictionary[lover_1]['Children'] = []
People_Dictionary[lover_2]['Children'] = []

for i in range(random.randint(1, 5)):
    child_name = random.choice(first_names) + ' ' + random.choice(last_names)
    People_Dictionary[lover_1]['Children'].append(child_name)
    People_Dictionary[lover_2]['Children'].append(child_name)
    People_Dictionary[child_name] = {'Age': random.randint(0, 18), 'Job': 'Child', 'Hobbies': [], 'Synopsis': 'Child'}
    for i in range(random.randint(1, 5)):
        People_Dictionary[child_name]['Hobbies'].append(random.choice(hobbies))
        
town_stuff = ["tavern", "general store", "blacksmith", "church", "graveyard", "school", "library", "police station", "fire station", "hospital", "bank", "post office", "train station", "bus station", "park", "lake", "river", "forest", "mountain", "farm", "ranch", "factory", "mine", "quarry", "lumber mill", "power plant", "wind farm", "solar farm", "nuclear power plant", "water treatment plant", "sewage treatment plant", "recycling center", "dump", "city hall", "courthouse", "jail", "prison", "museum", "zoo", "botanical garden", "planetarium", "aquarium", "theater", "movie theater", "concert hall", "stadium", "sports arena", "golf course", "tennis court", "basketball court", "baseball field", "football field", "soccer field", "hockey rink", "bowling alley", "skating rink", "pool hall", "billiards hall", "casino", "hotel", "motel", "bed and breakfast", "hostel", "campground", "beach", "lighthouse", "pier", "dock", "marina", "boat launch", "boat rental", "boat repair", "boat storage", "boat dealership", "car dealership"]

town_name = random.choice(first_names) + ' ' + random.choice(last_names) + ' ' + random.choice(['Town', 'City', 'Village', 'Hamlet', 'Burg', 'Borough', 'Municipality', 'County', 'Parish', 'Precinct', 'District', 'Region', 'Province', 'State', 'Territory', 'Country', 'Nation', 'Empire', 'Kingdom', 'Republic', 'Commonwealth', 'Principality', 'Duchy'])

Town_Dictionary = {town_name: {'Population': len(People_Dictionary), 'Town Stuff': []}}

for i in range(random.randint(1, 10)):
    Town_Dictionary[town_name]['Town Stuff'].append(random.choice(town_stuff))

world_stuff = ["ocean", "sea", "lake", "river", "stream", "creek", "pond", "swamp", "marsh", "wetland", "bayou", "lagoon", "fjord", "glacier", "iceberg"]

world_name = random.choice(first_names) + ' ' + random.choice(last_names) + ' ' + random.choice(['World', 'Planet', 'Moon', 'Asteroid', 'Comet', 'Star', 'Galaxy', 'Universe', 'Multiverse', 'Dimension', 'Realm', 'Plane', 'Domain', 'Sphere', 'Sphere of Influence', 'Sphere of Existence', 'Sphere of Reality', 'Sphere of Life', 'Sphere of Death', 'Sphere of Time', 'Sphere of Space', 'Sphere of Matter', 'Sphere of Energy', 'Sphere of Light', 'Sphere of Darkness', 'Sphere of Good', 'Sphere of Evil', 'Sphere of Law', 'Sphere of Chaos', 'Sphere of Order', 'Sphere of Entropy', 'Sphere of Creation', 'Sphere of Destruction', 'Sphere of Balance', 'Sphere of Imbalance'])

World_Dictionary = {world_name: {'Towns': [town_name], 'World Stuff': []}}

for i in range(random.randint(1, 10)):
    World_Dictionary[world_name]['World Stuff'].append(random.choice(world_stuff))

dialogue = [f'"I like going to the {random.choice(world_stuff)} with {random.choice(list(People_Dictionary.keys()))}."',
            f'"Sometimes I go to the {random.choice(town_stuff)} with {random.choice(list(People_Dictionary.keys()))} alone."',
            f'"My hobbies are {", ".join(People_Dictionary[random.choice(list(People_Dictionary.keys()))]["Hobbies"])}."']

while True:        
    person = random.choice(list(People_Dictionary.keys()))
    if random.randint(1, 2) == 1:
        place = random.choice(World_Dictionary[world_name]['World Stuff'])
        print(f"{person} went to the {place}.")
    else:
        place = random.choice(Town_Dictionary[town_name]['Town Stuff'])
        print(f"{person} went to the {place}.")
    time.sleep(3)
    if random.randint(1, 2) == 1:
        person2 = random.choice(list(People_Dictionary.keys()))
        print(f"{person} met {person2}.")
    else:
        print(f"{person} went home.")
    time.sleep(3)
    if random.randint(1, 2) == 1:
        print(f"{person} went to sleep.")
    else:
        print(f"{person} went to work.")
    time.sleep(3)
    if random.randint(1, 10) == 1:
        print(random.choice(dialogue))
