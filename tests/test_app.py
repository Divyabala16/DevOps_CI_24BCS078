import sys
sys.path.append("src")

from app import calculate_average, get_result

def test_calculate_average():
    assert calculate_average([80, 75, 90, 65, 85]) == 79.0

def test_pass_result():
    assert get_result(79.0) == "Pass"

def test_fail_result():
    assert get_result(40.0) == "Fail"

if __name__ == "__main__":
    test_calculate_average()
    test_pass_result()
    test_fail_result()
    print("All tests passed!")
