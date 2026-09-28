def calculate_average(marks):
    return sum(marks) / len(marks)

def get_result(average):
    if average >= 50:
        return "Pass"
    return "Fail - Need Improvement"

if __name__ == "__main__":
    marks = [70, 65, 80, 60, 75]
    average = calculate_average(marks)

    print("Marks:", marks)
    print("Average:", average)
    print("Result:", get_result(average))

