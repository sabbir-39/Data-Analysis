import os
import re
import numpy as np
import scipy.stats as stats

root_data_path = r'C:\Users\HP\Desktop\5th & 6th Semester\Bap Re Bap\CSV File\Pulse.csv'


# To detect outliers we are using IQR(Inter Quartile Range) method instead of using Z Score.
# The reason is, after data analysis, I have found IQR works better than Z score(for these app usage data).
# Parameter "sorted_data" must have to be sorted since IQR method needs to find median
def detect_outlier_z_score(data):
    outliers_indices = []
    threshold = 3
    mean = np.mean(data)
    std = np.std(data)

    index = 0
    for value in data:
        z_score = (value - mean) / std
        if np.abs(z_score) > threshold:
            outliers_indices.append(index)
        index += 1

    return outliers_indices


def detect_outlier_iqr(sorted_data):
    outliers_indices = []
    index = 0
    data = np.array(sorted_data)

    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)

    for duration in data:
        if duration < lower_bound or duration > upper_bound:
            outliers_indices.append(index)
        index += 1
    return outliers_indices


def get_2_decimal(value):
    return str(float("{0:.3f}".format(value)))


# To analyze the data
def analyze_data():

    group1 = []
    group2 = []

    y_crdnt = 0.88
    duration_list = []  # This will work as x value in data visualization or as a parameter to find PCC
    CGPA_list = []  # This will work as y value in data visualization or as parameter to find PCC
    students_ID = []

    with open(root_data_path, encoding="utf8") as opened_file:
        data = opened_file.readlines()

        if len(data) > 0:
            # Reading the data(line by line)
            for datum in data:
                datum = datum.split(',')

                if len(datum) > 1:

                    # Adding duration and CGPA in the respective lists
                    print(datum[0])
                    duration = float(datum[0].strip()) / 1
                    CGPA = float(datum[1].strip())

                    if duration > 0:
                        duration_list.append(duration)
                        CGPA_list.append(CGPA)
                        students_ID.append(datum[0].strip())

            # To plot data properly, we have sorted data based on duration.
            duration_list, CGPA_list, students_ID = zip(*sorted(zip(duration_list, CGPA_list, students_ID)))
            n_outlier = 0
            title = re.sub('[^A-Za-z0-9]+', '  ', str(os.path.basename(root_data_path)[0]))
            if len(duration_list) > 0:
                print("Prior to removing outliers, N = ", len(duration_list))

                #  Removing outliers of app usage data
                duration_list = list(duration_list)
                CGPA_list = list(CGPA_list)
                outliers_indices = detect_outlier_z_score(duration_list)
                for index in sorted(outliers_indices, reverse=True):
                    print("Outlier : ", duration_list[index])
                    # del duration_list[index]
                    # del CGPA_list[index]
                    n_outlier += 1

                # Removing outliers of CGPA
                duration_list = list(duration_list)
                CGPA_list = list(CGPA_list)
                outliers_indices = detect_outlier_z_score(CGPA_list)
                for index in sorted(outliers_indices, reverse=True):
                    print("Outlier CGPA: ", CGPA_list[index])
                    # del duration_list[index]
                    # del CGPA_list[index]
                    n_outlier += 1

                print("\n\n")

                print("N Outlier: ", n_outlier)
                print("After clearing outliers, Sample Size : ",len(duration_list))
                print("Min ", get_2_decimal(duration_list[0]))
                print("Max ", get_2_decimal(duration_list[len(duration_list) - 1]))
                print("Mean ", get_2_decimal(np.mean(duration_list)))
                print("SD ", get_2_decimal(np.std(duration_list)))
                print("Median ", get_2_decimal(np.median(duration_list)))
                print("\n\n")

# ----------------->>> Start - Lab - Careful <<<-----------------------------
                duration_list_out = duration_list
                CGPA_list_out = CGPA_list
                duration_list = []
                CGPA_list = []
                index = 0
                high_users_usage_data = []
                low_users_usage_data = []

                for duration in duration_list_out:
                    CGPA = CGPA_list_out[index]
                    if duration > np.median(duration_list_out):
                        duration_list.append(duration)
                        CGPA_list.append(CGPA)

                    # if duration > np.percentile(duration_list_out, 67):
                    #     group1.append(CGPA)
                    #     group1_ID.append(students_ID[index])
                    #     high_users_usage_data.append(duration)
                    # elif duration < np.percentile(duration_list_out, 33):
                    #     group2.append(CGPA)
                    #     group2_ID.append(students_ID[index])
                    #     low_users_usage_data.append(duration)

                    if 80 < CGPA <= 100:
                        group1.append(duration)
                        high_users_usage_data.append(CGPA)
                    elif 60 <= CGPA <= 80:
                        group2.append(duration)
                        low_users_usage_data.append(CGPA)

                    index += 1

                print("Before equalizing the groups : ", "High N : ", len(group1), " Low : ", len(group2))
                # if len(group1) > len(group2):
                #     group1 = group1[:len(group2)]
                # else:
                #     group2 = group2[:len(group1)]

                print(len(duration_list_out)*0.33)
                print("Length : ", len(group1))
                print("Length : ", len(group2))

                print("CGPA High  m,sd   ", get_2_decimal(np.mean(group1)),
                      "("+get_2_decimal(np.std(group1))+")",
                      "Mdn: ", get_2_decimal(np.median(group1)))
                print("CGPA Low  m,sd   ", get_2_decimal(np.mean(group2)),
                      "("+get_2_decimal(np.std(group2))+")",
                      "Mdn: ", get_2_decimal(np.median(group2)))

                print("Usage data - High  m,sd   ", get_2_decimal(np.mean(high_users_usage_data)),
                      "(" + get_2_decimal(np.std(high_users_usage_data)) + ")", " Median: ",
                      get_2_decimal(np.median(high_users_usage_data)))
                print("Usage data - Low  m,sd   ", get_2_decimal(np.mean(low_users_usage_data)),
                      "(" + get_2_decimal(np.std(low_users_usage_data)) + ")", " Median: ",
                      get_2_decimal(np.median(low_users_usage_data)))

                print("\n\n")
                print("High : ", np.percentile(duration_list_out, 67))
                print("Low : ", np.percentile(duration_list_out, 33))
                print(duration_list_out)
                print(CGPA_list_out)
                print(group1)
                print(group2)

                if len(group1) >= 8:
                    normality, p_value_norm_g1 = stats.normaltest(group1)
                    normality, p_value_norm_g2 = stats.normaltest(group2)

                    print("Normality Test\n")
                    print(p_value_norm_g1)
                    print(p_value_norm_g2)

## <<<<>>@@@@Check >>>>>>>>>>>>>> Start of difference lab >>>>>>>>>>>>>>>>>>>>>>
                    value, p_vlaue_eq_variance = stats.bartlett(group1, group2)

                    if len(group1) >= 20 and len(group2) >= 20:

                        if p_vlaue_eq_variance > 0.05 and len(group1) == len(group2):
                            print(stats.ttest_ind(group1, group2, equal_var=True))
                            t_stats, t_test_p_value = stats.ttest_ind(group1, group2, equal_var=True)
                            test_name = "Standard T test"
                        else:
                            print(stats.ttest_ind(group1, group2, equal_var=False))
                            t_stats, t_test_p_value = stats.ttest_ind(group1, group2, equal_var=False)
                            test_name = "Welch's T Test"
                    else:
                        print(stats.mannwhitneyu(group1, group2, use_continuity=False, alternative='two-sided'))
                        t_stats, t_test_p_value = stats.mannwhitneyu(group1, group2, use_continuity=False, alternative='two-sided')
                        test_name = "Mann Whitney U Test"

                    p_values.append(get_2_decimal___TO_FLOAT(t_test_p_value))
                    # if np.mean(group1) > np.mean(group2):
                    #     print("TS: ", stats.t.sf(t_stats, len(group1) + len(group2) - 2))
                    # else:
                    #     print("TS: ", stats.t.cdf(t_stats, len(group1) + len(group2) - 2))


## >>>>>>>@@@@@Check >>>>>> End of difference lab >>>>>>>>>>>>>>>>>>>>>>>>>>>>

                    t_stats = float("{0:.2f}".format(t_stats))
                    t_test_p_value = float("{0:.6f}".format(t_test_p_value))
                    str_T_Test = test_name + " : " + get_2_decimal(t_stats) + ", p= " + get_2_decimal(t_test_p_value)
                    n_student_T_Test = "Samples for " + test_name + " : " + str(len(group1))
                    print(n_student_T_Test)
                    print(str_T_Test)
                else:
                    print("\nSorry\n")
# -------------------->>> End - Lab -  Careful <<<-----------------


analyze_data(root_data_path)