import random
import string
import time
from dataclasses import dataclass

# Patient data class
@dataclass
class Patient:
    patient_id: str
    name: str
    age: int
    diagnosis: str

# Sorting Algorithms

# Bubble Sort
def bubble_sort(patients, key):
    n = len(patients)
    for i in range(n):
        for j in range(0, n-i-1):
            if getattr(patients[j], key) > getattr(patients[j+1], key):
                patients[j], patients[j+1] = patients[j+1], patients[j]
    return patients

# Merge Sort
def merge_sort(patients, key):
    if len(patients) <= 1:
        return patients
    mid = len(patients) // 2
    left = merge_sort(patients[:mid], key)
    right = merge_sort(patients[mid:], key)
    return merge(left, right, key)

def merge(left, right, key):
    sorted_list = []
    while left and right:
        if getattr(left[0], key) <= getattr(right[0], key):
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))
    sorted_list.extend(left or right)
    return sorted_list

# Quick Sort
def quick_sort(patients, key):
    if len(patients) <= 1:
        return patients
    pivot = patients[0]
    less = [x for x in patients[1:] if getattr(x, key) <= getattr(pivot, key)]
    greater = [x for x in patients[1:] if getattr(x, key) > getattr(pivot, key)]
    return quick_sort(less, key) + [pivot] + quick_sort(greater, key)

# Searching Algorithms

# Linear Search
def linear_search(patients, key, value):
    return [p for p in patients if str(getattr(p, key)).lower() == str(value).lower()]

# Binary Search (List must be sorted by key)
def binary_search(patients, key, value):
    low, high = 0, len(patients) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_value = getattr(patients[mid], key)
        if str(mid_value).lower() == str(value).lower():
            return patients[mid]
        elif str(mid_value).lower() < str(value).lower():
            low = mid + 1
        else:
            high = mid - 1
    return None

# Function to measure time
def measure_time(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, end - start

# Generate random patient data
def generate_patients(n):
    patients = []
    for _ in range(n):
        patient_id = ''.join(random.choices(string.digits, k=6))
        name = ''.join(random.choices(string.ascii_uppercase, k=5))
        age = random.randint(1, 100)
        diagnosis = random.choice(["Flu", "Cold", "Covid", "Allergy"])
        patients.append(Patient(patient_id, name, age, diagnosis))
    return patients

# Main performance test function
def performance_tests():
    sizes = [100, 500, 1000]
    for size in sizes:
        data = generate_patients(size)
        
        # Sorting by name
        _, t_bubble = measure_time(bubble_sort, data.copy(), "name")
        _, t_merge = measure_time(merge_sort, data.copy(), "name")
        _, t_quick = measure_time(quick_sort, data.copy(), "name")

        print(f"\nSize: {size}")
        print(f"Bubble Sort: {t_bubble:.6f}s")
        print(f"Merge Sort: {t_merge:.6f}s")
        print(f"Quick Sort: {t_quick:.6f}s")
        
        # Searching
        target_name = data[size // 2].name
        _, t_linear = measure_time(linear_search, data, "name", target_name)
        
        sorted_data = quick_sort(data, "name")
        _, t_binary = measure_time(binary_search, sorted_data, "name", target_name)
        
        print(f"Linear Search: {t_linear:.6f}s")
        print(f"Binary Search: {t_binary:.6f}s")

# Run the performance tests
performance_tests()
