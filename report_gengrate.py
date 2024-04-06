CMP = ["Ho", "Po", "Fi"]
WLL = ["Sc", "Ma", "Cl"]
HAP = ["Pa", "In"]

def report(buildings_dict, residents_list):
    print(f"Area Report: ")
    print("")
    for houseId, facilities in buildings_dict.items():
        for residents in residents_list:
            if houseId == residents.id:
                name = residents.name
                print(f"Resident building: {name}")

        requisite_score = 0
        for facility in facilities["neighbors"]:
            if facility[0][:2]  == "Ho":
                min_key, min_value = min(facility[4].items(), key=lambda x: x[1])
                print(f"   | The nearest Hospital is: {round(facility[2] * 10, 1)}m far, takes {round(min_value, 1)} minutes (by {min_key})")
                requisite_score += calc_score(min_value)
            if facility[0][:2]  == "Po":
                min_key, min_value = min(facility[4].items(), key=lambda x: x[1])
                print(f"   | The nearest Police Office is: {round(facility[2] * 10, 1)}m far, takes {round(min_value, 1)} minutes (by {min_key})")
                requisite_score +=calc_score(min_value)
            if facility[0][:2]  == "Fi":
                min_key, min_value = min(facility[4].items(), key=lambda x: x[1])
                print(f"   | The nearest Hospital is: {round(facility[2] * 10, 1)}m far, takes {round(min_value, 1)} minutes (by {min_key})")
                requisite_score += calc_score(min_value)
        print((f"  * The score for Requisite facilities is {round(1.5*requisite_score, 2)}"))

        will_score = 0
        for facility in facilities["neighbors"]:
            if facility[0][:2]  == "Sc":
                min_key, min_value = min(facility[4].items(), key=lambda x: x[1])
                print(f"   | The nearest School is: {round(facility[2] * 10, 1)}m far, takes {round(min_value, 1)} minutes (by {min_key})")
                will_score += calc_score(min_value)
            if facility[0][:2]  == "Ma":
                min_key, min_value = min(facility[4].items(), key=lambda x: x[1])
                print(f"   | The nearest Market is: {round(facility[2] * 10, 1)}m far, takes {round(min_value, 1)} minutes (by {min_key})")
                will_score +=calc_score(min_value)
            if facility[0][:2]  == "Cl":
                min_key, min_value = min(facility[4].items(), key=lambda x: x[1])
                print(f"   | The nearest Clinic is: {round(facility[2] * 10, 1)}m far, takes {round(min_value, 1)} minutes (by {min_key})")
                will_score += calc_score(min_value)
        print((f"  * The score for Willness facilities is {round(will_score, 2)}"))

        hap_score = 10
        for facility in facilities["neighbors"]:
            if facility[0][:2] == "Pa":
                min_key, min_value = min(facility[4].items(), key=lambda x: x[1])
                print(
                    f"   | The nearest Park is: {round(facility[2] * 10, 1)}m far, takes {round(min_value, 1)} minutes (by {min_key})")
                will_score += calc_score(min_value)
            if facility[0][:2] == "In":
                min_key, min_value = min(facility[4].items(), key=lambda x: x[1])
                print(
                    f"   | The nearest Industrial Area is: {round(facility[2] * 10, 1)}m far, takes {round(min_value, 1)} minutes (by {min_key})")
                will_score -= calc_score(min_value)
        print((f"  * The score for Happniess facilities is {round(1.25* will_score, 2)}"))
        print("")
        print((f"# The overall score for this building is {round(will_score+hap_score+requisite_score+30, 2)} / 100"))
        print("")


def calc_score(min_value):
    if min_value < 3:
        return 10
    if min_value >= 20:
        return 0
    return 11.5 - 0.5*min_value