import pandas as pd
import matplotlib.pyplot as plt
import classes
ROAD = ["Street", 'Subway']
CAPATABLE = ['Hospital', 'School']
RESIDENT = ['Residential_building']

def csv_to_classes(csv_path):
    df = pd.read_csv(csv_path, index_col=False)
    print(df)
    roads = []
    facilities = []
    residents = []

    for i, entries in df.iterrows():
        if entries['Type'] in ROAD:
            try:
                class_obj = getattr(classes, entries['Type'])
                instance = class_obj(entries['Name'], (entries['Start_X'], entries['Start_Y']),
                                     (entries['End_X'], entries['End_Y']))

                roads.append(instance)
            except AttributeError:
                print(f"No class named {entries['Type']} found. Skipping...")

        elif entries['Type'] in CAPATABLE:
            try:
                class_obj = getattr(classes, entries['Type'])
                instance = class_obj(entries['Name'], (entries['Start_X'], entries['Start_Y']),
                                     entries['nearbyStreet'], entries['capacity'])

                facilities.append(instance)
            except AttributeError:
                print(f"No class named {entries['Type']} found. Skipping...")

        elif entries['Type'] in RESIDENT:
            try:
                class_obj = getattr(classes, entries['Type'])
                instance = class_obj(entries['Name'], (entries['Start_X'], entries['Start_Y']),
                                     entries['nearbyStreet'], entries['capacity'])

                residents.append(instance)
            except AttributeError:
                print(f"No class named {entries['Type']} found. Skipping...")

        else:
            try:
                class_obj = getattr(classes, entries['Type'])
                instance = class_obj(entries['Name'], (entries['Start_X'], entries['Start_Y']),
                                     entries['nearbyStreet'])

                facilities.append(instance)
            except AttributeError:
                print(f"No class named {entries['Type']} found. Skipping...")

    # print(str(facilities[0].street) == (roads[0].name))
    # print(roads[0].name)
    # print(roads)
    # print(resident)

    # add road to facilities list
    for facility in facilities:
        for road in roads:
            if facility.street == road.name:
                print(road, facility)
                road.add_facilities(facility)

    # print(roads[0].depending_facilities[0])
    return resident, facilities, roads
