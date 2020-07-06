names = ('Fazul', 'Aidan', 'Mushin', 'Armin', 'Hanh', 'Alek', 'Ahmed', 'Mustafa', 'Akeno', 'Oskar')
ages = [19, 38, 25, 17, 34, 29, 67, 53, 20, 27]
continentOfBirth = ['Asia', 'Europe', 'Asia', 'Europe', 'Asia', 'Europe', 'Asia', 'Asia', 'Asia', 'Europe']
gender = ['Male', 'Male', 'Male', 'Male', 'Female', 'Male', 'Male', 'Male', 'Male', 'Male']
maritalStatus = ['M', 'S', 'S', 'S', 'M', 'S', 'M', 'M', 'S', 'M']
postSecondaryEducation = [True, False, False, False, False, True, False, False, True, True]


def list_set_up():
    suspects_dictionary = []
    for name in names:
        index = names.index(name)
        suspect = {
            "name": name,
            "age": int(ages[index]),
            "continentOfBirth": continentOfBirth[index],
            "gender": gender[index],
            "maritalStatus": maritalStatus[index],
            "postSecondaryEducation": postSecondaryEducation[index]
        }
        suspects_dictionary.append(suspect)
    return suspects_dictionary


def suspects_gender(suspects_gender_list):
    for suspect in list(suspects_gender_list):
        if suspect['gender'] == "Female":
            suspects_gender_list.remove(suspect)
    return suspects_gender_list


def suspects_age(suspects_age_list):
    for suspect in list(suspects_age_list):
        if suspect["age"] > 30:
            suspects_age_list.remove(suspect)
    return suspects_age_list


def suspects_marital_status(suspects_marital_status_list):
    for suspect in list(suspects_marital_status_list):
        if suspect["maritalStatus"] == "M":
            suspects_marital_status_list.remove(suspect)
    return suspects_marital_status_list


def suspects_education(suspects_education_list):
    for suspect in list(suspects_education_list):
        if not suspect['postSecondaryEducation']:
            suspects_education_list.remove(suspect)
    return suspects_education_list


def suspects_continent(suspects_continent_list):
    for suspect in list(suspects_continent_list):
        if suspect['continentOfBirth'] != "Europe":
            suspects_continent_list.remove(suspect)
    return suspects_continent_list


suspects = list_set_up()
suspects = suspects_gender(suspects)
print(suspects_gender(suspects))
suspects = suspects_age(suspects)
print(suspects_age(suspects))
suspects = suspects_marital_status(suspects)
print(suspects_marital_status(suspects))
suspects = suspects_education(suspects)
print(suspects_education(suspects))
suspects = suspects_continent(suspects)
print(suspects_continent(suspects))
print(suspects)
print(f"The terrorist is {suspects}. The software detected that this person matches all of the attributes stated.")
