# STUDENTS GRADE ANALYSER
import numpy as np
import time

np.random.seed(69)
scores = np.random.randint(0, 101, size=50)
names = [
    'Aiden', 'Bella', 'Caleb', 'Diana', 'Ethan', 'Fiona', 'Gabriel', 'Hannah', 'Ian', 'Jasmine',
    'Kyle', 'Lily', 'Mason', 'Nora', 'Owen', 'Paisley', 'Quentin', 'Riley', 'Samuel', 'Tessa',
    'Umar', 'Violet', 'Wyatt', 'Xena', 'Yusuf', 'Zara', 'Ariana', 'Brandon', 'Carly', 'Derek',
    'Elena', 'Felix', 'Greta', 'Harvey', 'Ivy', 'Julian', 'Kendra', 'Luca', 'Maya', 'Noah',
    'Olivia', 'Parker', 'Quinn', 'Ruby', 'Spencer', 'Thisbe', 'Ulric', 'Vera', 'Wesley', 'Zoe'
]
# print(scores)

def statistic(data_array):
    print("-"*50,"CLASS SCORE STATISTIC","-"*50)
    print(f'Mean score: {np.mean(data_array)}')
    print(f'Median score: {np.median(data_array)}')
    print(f'Standard Deviation: {np.std(data_array)}')

def analysis(data_array):
    print("-"*50,"CLASS SCORE ANALYSIS","-"*50)
    time.sleep(1)

    # 1. Students who passed (score >= 50)
    print("THESE ARE THE STUDENTS WHO HAVE PASSED: ")
    time.sleep(1)
    passed_indices = np.where(data_array >= 50)[0]
    for idx in passed_indices:
        print(f"{names[idx]}: {data_array[idx]}")
        time.sleep(0.5)
    print(f"Students who passed: {passed_indices.size}")
    print()
    time.sleep(10)

    # 2. Students who scored above 90.
    print("THESE ARE THE STUDENTS WHO HAVE SCORE EQUAL TO 90 AND ABOVE: ")
    time.sleep(1)
    topper_indices = np.where(data_array >= 90)[0]
    for idx in topper_indices:
        print(f"{names[idx]}: {data_array[idx]}")
        time.sleep(0.5)
    print(f"The Toppers: {topper_indices.size}")
    print()
    time.sleep(10)

    # 3. Students who scored below 50.
    print("THESE ARE THE STUDENTS WHO HAVE FAILED: ")
    time.sleep(1)
    failed_indices = np.where(data_array < 50)[0]
    for idx in failed_indices:
        print(f"{names[idx]}: {data_array[idx]}")
        time.sleep(0.5)
    print(f"The Failures: {failed_indices.size}")
    print()
    time.sleep(10)

statistic(scores)
time.sleep(3)
print()
analysis(scores)