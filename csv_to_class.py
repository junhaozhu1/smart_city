import pandas as pd
import matplotlib.pyplot as plt
import classes
ROAD = ["Street", 'Subway']
CAPATABLE = ['Hospital', 'School']
RESIDENT = ['Residential_building']


def csv_to_classes(csv_path):
    df = pd.read_csv(csv_path, index_col=False)
    # print(df)
    roads = []
    facilities = []
    residents = []

    for i, entries in df.iterrows():
        if entries['Type'] in ROAD:
            try:
                class_obj = getattr(classes, entries['Type'])
                instance = class_obj(entries['Name'], (entries['Start_X'], entries['Start_Y']),
                                     (entries['End_X'], entries['End_Y']), entries['Name'][0:2]+str(i))

                roads.append(instance)
            except AttributeError:
                print(f"No class named {entries['Type']} found. Skipping...")

        elif entries['Type'] in CAPATABLE:
            try:
                class_obj = getattr(classes, entries['Type'])
                instance = class_obj(entries['Name'], (entries['Start_X'], entries['Start_Y']),
                                     entries['nearbyStreet'], entries['capacity'], entries['Name'][0:2]+str(i))

                facilities.append(instance)
            except AttributeError:
                print(f"No class named {entries['Type']} found. Skipping...")

        elif entries['Type'] in RESIDENT:
            try:
                class_obj = getattr(classes, entries['Type'])
                instance = class_obj(entries['Name'], (entries['Start_X'], entries['Start_Y']),
                                     entries['nearbyStreet'], entries['capacity'], entries['Name'][0:2]+str(i))

                residents.append(instance)
            except AttributeError:
                print(f"No class named {entries['Type']} found. Skipping...")

        else:
            try:
                class_obj = getattr(classes, entries['Type'])
                instance = class_obj(entries['Name'], (entries['Start_X'], entries['Start_Y']),
                                     entries['nearbyStreet'], entries['Name'][0:2]+str(i))

                facilities.append(instance)
            except AttributeError:
                print(f"No class named {entries['Type']} found. Skipping...")

    # add road to facilities list
    for facility in facilities:
        for road in roads:
            if facility.street == road.name:
                road.add_facilities(facility)

    for facility in residents:
        for road in roads:
            if facility.street == road.name:
                road.add_facilities(facility)

    return residents, facilities, roads
