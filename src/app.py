def calculate_average(marks):
    return sum(marks) / len(marks)

def get_result(average):
    if average >= 50:
        return "Pass"
    return "Fail - Need Improvement"

if __name__ == "__main__":
    marks = [80, 75, 90, 65, 85]
    average = calculate_average(marks)

    print("Marks:", marks)
    print("Average:", average)
    print("Result:", get_result(average))

