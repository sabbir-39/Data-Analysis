already_calculated = ["ABC", "DEF", "GHI", "JKL"]

print(already_calculated[len(already_calculated)-1])
print(already_calculated[:len(already_calculated)-1])


def not_calculated_correlation(var1_name, var2_name):
    for name in already_calculated:
        if var1_name in name and var2_name in name:
            return False
    return True


if not_calculated_correlation("I", "K"):
    print("Not Calculated")
else:
    print("Calculated")