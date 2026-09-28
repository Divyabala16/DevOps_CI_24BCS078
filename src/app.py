def calculate_average(marks):
    return sum(marks) / len(marks)

def get_result(average):
    if average >= 50:
        return "Pass"
    return "Fail"

marks = [90, 80, 95, 75, 90]

average = calculate_average(marks)

print("Marks:", marks)
print("Average:", average)
print("Result:", get_result(average))
