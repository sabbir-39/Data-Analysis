# This can be used to correlate two variables
# Data should be ordinal type
# As our data is likert scale (ordinal), we are using non-parametric test: Spearman Rank Correlation

import os
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

root_data_path = r'C:\Users\HP\Desktop\5th & 6th Semester\Bap Re Bap\HCI Lab Data Sets\dataset_web\participant_6.csv'
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

    file_name = os.path.basename(root_data_path).replace(".csv","")
    corr_coef_writer = open("C:\\Users\\HP\\Desktop\\5th & 6th Semester\\Bap Re Bap\\Results\\Results - txt Files\\HCI Lab - Germany\\Seconds\\HCI_Lab_Vector_"+file_name+"__Vector.txt", "a")

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
                    # print("Outlier variable_1_data: ", variable_1_data[index])
                    # del variable_1_data[index]
                    # del variable_2_data[index]
                    n_outlier += 1

                # Outlier Detection for variable_2_data
                print("Prior to removing outliers, var 2 :N = ", len(variable_2_data))
                outliers_indices = detect_outlier_z_score(variable_2_data)

                for index in sorted(outliers_indices, reverse=True):
                    # print("Outlier variable_2_data: ", variable_2_data[index])
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
                    # print(variable_1_data)
                    # print(variable_2_data)
                    print(n_student_PCC)
                    print(str_PCC)
                    print("\n\n")

                    plt.show()


def time_upto_sec(time):
    time = time.strip()
    str_data = ''.join(char for char in time[:8] if char.isnumeric())
    return str_data


def get_data(dataset_60_130):

    time_id_list = []
    columns_name = dataset_60_130[0]

    acc_magnitude_list = []
    heart_rate = []

    time_id_list.append(columns_name[0])
    acc_magnitude_list.append("Acceleration")
    heart_rate.append(columns_name[4])

    first_row_of_data = dataset_60_130[1]
    prev_time_accel = time_upto_sec(first_row_of_data[0])
    time_id_list.append(prev_time_accel)

    sum_accel_x = float(first_row_of_data[1])
    sum_accel_y = float(first_row_of_data[2])
    sum_accel_z = float(first_row_of_data[3])
    sum_heart_rate = float(first_row_of_data[4])

    n_value = 1

    for line in dataset_60_130[2:]:

        current_time_accel = time_upto_sec(line[0])
        if current_time_accel == prev_time_accel:
            sum_accel_x += float(line[1])
            sum_accel_y += float(line[2])
            sum_accel_z += float(line[3])
            sum_heart_rate += float(line[4])
            n_value += 1
        else:

            x_acc_avg = sum_accel_x / n_value
            y_acc_avg = sum_accel_y / n_value
            z_acc_avg = sum_accel_z / n_value

            sqrd_value = x_acc_avg*x_acc_avg + y_acc_avg*y_acc_avg + z_acc_avg*z_acc_avg
            root_value = sqrd_value ** 0.5

            acc_magnitude_list.append(root_value)
            heart_rate.append(sum_heart_rate / n_value)

            sum_accel_x = float(line[1])
            sum_accel_y = float(line[2])
            sum_accel_z = float(line[3])
            sum_heart_rate = float(line[4])
            n_value = 1
            prev_time_accel = current_time_accel
            time_id_list.append(prev_time_accel)

    x_acc_avg = sum_accel_x / n_value
    y_acc_avg = sum_accel_y / n_value
    z_acc_avg = sum_accel_z / n_value

    sqrd_value = x_acc_avg*x_acc_avg + y_acc_avg*y_acc_avg + z_acc_avg*z_acc_avg
    root_value = sqrd_value ** 0.5

    acc_magnitude_list.append(root_value)
    heart_rate.append(sum_heart_rate / n_value)

    return time_id_list, acc_magnitude_list, heart_rate


# To analyze the data
# We have to send the data path where the files will contain data
def analyze_data():
    with open(root_data_path, encoding="utf-8") as opened_file:
        print(os.path.basename(root_data_path))
        data = opened_file.readlines()

        columns_name = data[0]
        check_by_seconds = True

# By seconds..............................Start..............................Seconds................................
        if check_by_seconds:
            single_line_data = []

            single_line_data.append(columns_name.split(';')[3])
            single_line_data.append(columns_name.split(';')[5])
            single_line_data.append(columns_name.split(';')[6])
            single_line_data.append(columns_name.split(';')[7])
            single_line_data.append(columns_name.split(';')[20])

            dataset_60_to_130 = []
            dataset_60_to_130.append(single_line_data)
            single_line_data = []

            for line in data[1:]:
                line = line.split(';')
                HR = float(line[20])

                if 60 <= HR <= 130:
                    single_line_data.append(line[3])
                    single_line_data.append(float(line[5]))
                    single_line_data.append(float(line[6]))
                    single_line_data.append(float(line[7]))
                    single_line_data.append(HR)
                    dataset_60_to_130.append(single_line_data)
                    single_line_data = []
            time_id_list, acc_magnitude_list, heart_rate = get_data(dataset_60_to_130)

# By seconds...............................End.............................Seconds.....................................

        else:
            acceleration_x = []
            acceleration_x.append(columns_name.split(';')[5])
            acceleration_y = []
            acceleration_y.append(columns_name.split(';')[6])
            acceleration_z = []
            acceleration_z.append(columns_name.split(';')[7])
            heart_rate = []
            heart_rate.append(columns_name.split(';')[20])

            excluded_values = []
            index = 2

            for line in data[1:]:
                line = line.split(';')

                if 60 <= float(line[20]) <= 130:
                    acceleration_x.append(float(line[5]))
                    acceleration_y.append(float(line[6]))
                    acceleration_z.append(float(line[7]))
                    heart_rate.append(float(line[20]))
                else:
                    excluded_values.append(float(line[20]))
                    # print(index, line)
                # print(index, line)
                index += 1
            print("Excluded Data Length: ", len(excluded_values))

        data_set.append(acc_magnitude_list)
        data_set.append(heart_rate)

        # print(excluded_values)
        print("Total Data Length", len(data))
        print(len(acc_magnitude_list))

# Testing.............................Checking.............................................
        # print(acceleration_x)
        # print(acceleration_y)
        # print(acceleration_z)
        # print(heart_rate)

        data_writer = open("C:\\Users\\HP\\Desktop\\5th & 6th Semester\\Bap Re Bap\\Results\\Data_HCI_Lab\\Vector\\HCI_Vector_"+os.path.basename(root_data_path)+"_Vector_HCI.txt",
                                "w")
        for (time_id, magnitude, pulse) in zip(time_id_list, acc_magnitude_list, heart_rate):
            str_data_write = str(time_id)+","+str(magnitude)+ "," + str(pulse)
            data_writer.write(str_data_write+"\n")
# Testing...............................Checking...............................................

        # Find the correlation one by one
        # for per_data_in_dataset in data_set:
        #     find_the_correlation(per_data_in_dataset)


analyze_data()
