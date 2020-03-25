
def age_categories(age_data):

    # Checked data
    # Index should start from 1 as first value is data name (e.g. Personality), string
    index = 1

    group1_indices = []
    group2_indices = []

    for age in age_data:
        age = float(age)
        if age == 18:  # Representing Age Range 18 - 30
            group1_indices.append(index)
        elif age == 31:  # Representing Age Range 31 - 40
            group2_indices.append(index)
        elif age == 40:  # Representing Age Range more than 40
            group2_indices.append(index)

        index += 1
    return "Age 18-30", "Age 31-40 and > 40", group1_indices, group2_indices


def vehicle_categorization(vehicle_data):

    # 3 N/A values are out of consideration for analysis
    # "N/A" values were represented by the value "9999999999999"

    # Index should start from 1 as first value is data name (e.g. Personality), string

    index = 1
    group1_indices = []
    group2_indices = []

    for vehicle in vehicle_data:
        vehicle = vehicle.strip().upper()

        if vehicle == "P":  # Private Car
            group1_indices.append(index)
        elif vehicle == "C":  # Commercial Car
            group2_indices.append(index)

        index += 1
    return "Private Car", "Commercial Car", group1_indices, group2_indices


def experience_categorization(experience_data):

    # 3 "N/A" values were represented by the value "9999999999999"
    # Index should start from 1 as first value is data name (e.g. Personality), string
    # Checked

    index = 1
    group_1 = []
    group_2 = []

    for experience in experience_data:
        experience = float(experience)
        if experience == 4:  # Experience is less than 5 years
            group_1.append(index)
        elif experience == 6:  # Experience is between 6 and 10 years
            group_1.append(index)
        elif experience == 11:  # Experience is more than 10 years
            group_2.append(index)
        index += 1

    return "Experience <= 10 years", "Experience > 10 years", group_1, group_2


def driving_hour_categorization(hours_data):

    # "N/A" values (for 4 samples) were represented by the value "9999999999999"

    # Index should start from 1 as first value is data name (e.g. Personality), string

    for driving_hour in hours_data:
        if driving_hour == 2:  # Drives less than or equal to 2 hours
            print("Do something")
        elif driving_hour == 3:  # Drives between 3 to 5 hours
            print("Do something")
        elif driving_hour == 6:  # Drives more than 6 hours
            print("Do something")


def rest_interval_categorization(interval_hours_data):  # Interval of rest

    # "N/A" values (for 4 samples) were represented by the value "9999999999999"

    # Index should start from 1 as first value is data name (e.g. Personality), string

    for interval in interval_hours_data:
        if interval == 1:  # Interval is between 1 and 2 hours
            print("Do something")
        elif interval == 3:  # Interval is between 3 and 4 hours
            print("Do something")
        elif interval == 6:  # Interval is more than 5 hours
            print("Do something")


def duty_hours_categorization(duty_hours):
    # Considered the average duty hours where range of value was reported, instead of a fixed value
    # For example: 15 to 17 hours was considered as 16 hours.
    # Several samples reported "No Limit" as their duty hours, they were coded as the value 24 hours
    # However, "No Limit" may not mean that they have worked extremely
    # Rather, it may mean there is no lower or upper bound.
    # "N/A" values (for 4 samples) were represented by the value "9999999999999"

    # Index should start from 1 as first value is data name (e.g. Personality), string

    for duty_hour in duty_hours:
        if duty_hour == 24:  # Samples, who reported "No Limit" as their duty hours
            print("Do Something")


def rest_hours_categorization(rest_hours):
    # Considered the average rest hours where range of value was reported, instead of a fixed value
    # For example: 15 to 17 hours was considered as 16 hours.
    # Several samples reported "No Limit" as their rest hours, they were coded as the value 24
    # However, "No Limit" may not mean that they took rest extremely
    # Rather, it may mean there is no lower or upper bound.
    # "N/A" values (for 4 samples) were represented by the value "9999999999999"

    # Index should start from 1 as first value is data name (e.g. Personality), string

    for rest_hour in rest_hours:
        if rest_hour == 24:  # Samples, who reported "No Limit" as their rest hours
            print("Do Something")


def marital_status_categorization(marital_data):

    # 4 samples data are un-available (Mentioned as N/A)
    # "N/A" values (for 4 samples) were represented by the value "9999999999999"

    # Index should start from 1 as first value is data name (e.g. Personality), string

    for marital in marital_data:
        marital = marital.strip().upper()

        if marital == "M":  # Married
            print("Married")
        elif marital == "U":  # Unmarried
            print("Unmarried")


def lives_with_family_categorization(live_with_family_data):

    # 4 samples data are un-available (Mentioned as N/A)
    # "N/A" values (for 4 samples) were represented by the value "9999999999999"
    # Index should start from 1 as first value is data name (e.g. Personality), string
    # Checked data

    index = 1
    group1_indices = []
    group2_indices = []

    for data in live_with_family_data:
        data = data.strip().upper()

        if data == "Y":  # Lives with family
            group1_indices.append(index)
        elif data == "N":  # Does not live with family
            group2_indices.append(index)
        index += 1
    return "Lives With Family", "Does Not Live with Family", group1_indices, group2_indices


def no_of_housemates_categorization(housemates_data):

    # One data was 10+ which was encoded as 11 another one was 2-3 which was encoded as 2
    # 4 samples data are un-available (Mentioned as N/A)
    # "N/A" values (for 4 samples) were represented by the value "9999999999999"

    # Index should start from 1 as first value is data name (e.g. Personality), string

    print("Do something")


def education_level_categorization(education_data):
    # Checked data
    # Index should start from 1 as first value (Index 0) is data name (e.g. Personality), string

    index = 1
    group1_indices = []
    group2_indices = []

    for data in education_data:
        data = float(data.strip())

        if data == 8:  # Below SSC
            group1_indices.append(index)
        elif data == 10:  # SSC
            group2_indices.append(index)
        elif data == 16:  # Bachelor
            group2_indices.append(index)
        elif data == 18:  # Masters
            group2_indices.append(index)
        index += 1
    return "Below SSC", "At Least SSC", group1_indices, group2_indices


# The following method will be used to find out education level of a specific number of people
# e.g. You may use this method to find out the people whose age is 18 to 30 years (have to pass indices
# through "indices" argument) and education level is at least SSC.
def compound_education_categorize_atlesat_ssc(indices, education_data):
    # Index should start from 1 as first value (Index 0) is data name (e.g. Personality), string
    # Indices mean the indices of the samples data for which we need to check education level

    group_1_indices = []
    group_2_indices = []

    for index in indices:
        education = int(education_data[index])
        if education == 10:  # SSC
            group_1_indices.append(index)
        elif education == 16:  # Bachelor
            group_1_indices.append(index)
        elif education == 18:  # Masters
            group_1_indices.append(index)
        elif education == 8:  # Below SSC
            group_2_indices.append(index)

    return "Education >= SSC", group_1_indices


def compound_education_categorize_below_ssc(indices, education_data):
    # Index should start from 1 as first value (Index 0) is data name (e.g. Personality), string
    # Indices mean the indices of the samples data for which we need to check education level

    group_1_indices = []
    group_2_indices = []

    for index in indices:
        education = int(education_data[index])
        if education == 10:  # SSC
            group_1_indices.append(index)
        elif education == 16:  # Bachelor
            group_1_indices.append(index)
        elif education == 18:  # Masters
            group_1_indices.append(index)
        elif education == 8:  # Below SSC
            group_2_indices.append(index)

    return "Education < SSC", group_2_indices



# This method will be used to find
def compound_family_categorization(indices, family_data):
    # Index should start from 1 as first value (Index 0) is data name (e.g. Personality), string
    # Indices mean the indices of the samples data for which we need to check whether a person
    # stays at family or not

    group_1_indices = []
    group_2_indices = []

    for index in indices:
        stays_with_f = family_data[index].strip().upper()
        if stays_with_f == "Y":
            group_1_indices.append(index)
        elif stays_with_f == "N":
            group_2_indices.append(index)

    return "Stays With Family", "Does Not Stay With Family", group_1_indices, group_2_indices
