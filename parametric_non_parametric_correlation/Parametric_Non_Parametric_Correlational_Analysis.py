# This can be used to correlate two variables
# Data should be ordinal type
# As our data is likert scale (ordinal), we are using non-parametric test; Spearman Rank Correlation

import os
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

root_data_path = r'C:\Users\HP\Desktop\5th & 6th Semester\Bap Re Bap\Heart Rate Data\participant_5.csv'
DEGREE = 1  # Fit a polynomial

x_axis_label = "X Axis"
y_axis_label = "Y Axis"
data_set = []
already_calculated = []


# To detect outliers we are using IQR(Inter Quartile Range) method instead of using Z Score.
# The reason is, after data analysis, I have found IQR works better than Z score
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

    for value in data:
        if value < lower_bound or value > upper_bound:
            outliers_indices.append(index)
        index += 1
    return outliers_indices


def get_2_decimal(value):
    return str(float("{0:.4f}".format(value)))


def not_calculated_correlation(var1_name, var2_name):
    for name in already_calculated:
        if var1_name in name and var2_name in name:
            return False

    already_calculated.append(var1_name+"_"+var2_name)
    return True


def find_the_correlation(variable_1_data):
    corr_coef_writer = open("C:\\Users\\HP\\Desktop\\5th & 6th Semester\\Bap Re Bap\\Results\\cc_TESSTTTTTT.txt", "a")

    variable_1_name = variable_1_data[0].replace("\n","")
    variable_1_data = variable_1_data[1:]
    variable_1_data = np.array(variable_1_data, dtype=np.float32)
    variable_1_data_not_sorted = variable_1_data

    for variable_2_data in data_set:

        variable_1_data = variable_1_data_not_sorted

        variable_2_name = variable_2_data[0].replace("\n","")
        variable_2_data = variable_2_data[1:]
        variable_2_data = np.array(variable_2_data, dtype=np.float32)

        x_axis_label = variable_1_name
        y_axis_label = variable_2_name

        if not_calculated_correlation(variable_1_name, variable_2_name):
            variable_1_data, variable_2_data = zip(*sorted(zip(variable_1_data, variable_2_data)))
            n_outlier = 0
            title = "Correlation between " + variable_1_name + " and " + variable_2_name

            if len(variable_1_data) > 0 and len(variable_2_data) > 0:

                #  Outlier detection for variable_1_data
                print("Prior to removing outliers, var 1 :N = ", len(variable_1_data))
                outliers_indices = detect_outlier_z_score(variable_1_data)

                for index in sorted(outliers_indices, reverse=True):
                    print("Outlier variable_1_data: ", variable_1_data[index])
                    # del variable_1_data[index]
                    # del variable_2_data[index]
                    n_outlier += 1

                # Outlier Detection for variable_2_data
                print("Prior to removing outliers, var 2 :N = ", len(variable_2_data))
                outliers_indices = detect_outlier_z_score(variable_2_data)

                for index in sorted(outliers_indices, reverse=True):
                    print("Outlier variable_2_data: ", variable_2_data[index])
                    # del variable_1_data[index]
                    # del variable_2_data[index]
                    n_outlier += 1

                if (len(variable_1_data) >= 8 and len(variable_2_data) >= 8) and (len(variable_2_data) == len(variable_1_data)):

                    # Doing Normality Test
                    normality_stats_var1, p_value_norm_var1 = stats.normaltest(variable_1_data)
                    normality_stats_var2, p_value_norm_var2 = stats.normaltest(variable_2_data)

                    # Printing the findings of normality test
                    print(normality_stats_var1, p_value_norm_var1)
                    print(normality_stats_var2, p_value_norm_var2)

                    if p_value_norm_var1 > 0.05 and p_value_norm_var2 > 0.05 and n_outlier == 0:

                        # Pearson Correlation coefficient(PCC) and P Value
                        # We are calculating PCC as data is normally distributed and outlier free
                        print(stats.pearsonr(variable_1_data, variable_2_data))
                        pcc, pcc_p_value = stats.pearsonr(variable_1_data, variable_2_data)
                        print("Pearson")
                        r_text = "r = "
                    else:
                        # Spearman Correlation Coefficient and P value
                        print(stats.spearmanr(variable_1_data, variable_2_data))
                        pcc, pcc_p_value = stats.spearmanr(variable_1_data, variable_2_data)
                        print("Spearman")
                        r_text = "rs = "

                    # Data visualization
                    plt.xlabel(x_axis_label, fontweight='bold')
                    plt.ylabel(y_axis_label, fontweight='bold')
                    plt.title(title)

                    # Drawing the trending line
                    z = np.polyfit(variable_1_data, variable_2_data, DEGREE)
                    p = np.poly1d(z)
                    plt.plot(variable_1_data, variable_2_data, linestyle='-.', marker='o', color='b')
                    # plt.plot(duration_list, p(duration_list), "k", label='Trending line')
                    plt.plot(variable_1_data, p(variable_1_data), "k")
                    # plt.legend(loc='best')

                    # Printing the findings
                    n_student_PCC = "N=" + str(len(variable_2_data))
                    str_PCC = r_text + get_2_decimal(pcc) + ", p=" + get_2_decimal(pcc_p_value)

                    if pcc_p_value > 0.0001:
                        cc_data = variable_1_name + " , " + variable_2_name + " ," + str(len(variable_1_data)) + " , " + r_text\
                                  + get_2_decimal(pcc) + " , " + get_2_decimal(pcc_p_value) + "\n"
                    else:
                        cc_data = variable_1_name + " , " + variable_2_name + " ," + str(len(variable_1_data)) + " , " + r_text\
                                  + get_2_decimal(pcc) + " , " + str(pcc_p_value) + "\n"

                    # corr_coef_writer.write(cc_data)

                    print(title)
                    print(variable_1_data)
                    print(variable_2_data)
                    print(n_student_PCC)
                    print(str_PCC)
                    print("\n\n")

                    plt.show()


# To analyze the data
# We have to send the data path where the files will contain data
def analyze_data():

    with open(root_data_path, encoding="utf-8") as opened_file:
        print(os.path.basename(root_data_path))
        data = opened_file.readlines()

        x_y_z_pulse = data[0]

        acceleration_x = []
        acceleration_x.append(x_y_z_pulse.split(',')[0])
        acceleration_y = []
        acceleration_y.append(x_y_z_pulse.split(',')[1])
        acceleration_z = []
        acceleration_z.append(x_y_z_pulse.split(',')[2])
        heart_rate = []
        heart_rate.append(x_y_z_pulse.split(',')[3])

        excluded_values = []
        index = 2

        # Reading the data(line by line)
        # Each row should contain data of one type. e.g. All participants data of personality
        for line in data[1:]:
            line = line.split(',')

            if 60 <= float(line[3]) <= 130:
                acceleration_x.append(float(line[0]))
                acceleration_y.append(float(line[1]))
                acceleration_z.append(float(line[2]))
                heart_rate.append(float(line[3]))
            else:
                excluded_values.append(float(line[3]))
                print(index, line)
            # print(index, line)
            index += 1

        data_set.append(acceleration_x)
        data_set.append(acceleration_y)
        data_set.append(acceleration_z)
        data_set.append(heart_rate)

        print(excluded_values)
        print(len(data))
        print(len(excluded_values))
        print(acceleration_x)
        print(acceleration_y)
        print(acceleration_z)
        print(heart_rate)

        # Find the correlation one by one
        for per_data_in_dataset in data_set:
            find_the_correlation(per_data_in_dataset)


analyze_data()
