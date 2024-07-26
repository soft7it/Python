from collections import defaultdict
from itertools import combinations

# List of lists
numbers = [
    # [4, 8, 10, 16, 34],
    [15, 22, 35, 44, 48],
    [2, 32, 35, 36, 39],
    [12, 18, 24, 25, 39],
    [6, 15, 19, 28, 39],
    [11, 13, 29, 31, 47],
    [2, 7, 34, 35, 46],
    [10, 16, 18, 22, 35],
    [14, 16, 37, 45, 49],
    [3, 4, 7, 11, 17],
    [3, 11, 33, 34, 36],
    [2, 13, 16, 24, 32],
    [7, 15, 34, 45, 48],
    [15, 16, 26, 30, 37],
    [6, 7, 9, 14, 43],
    [4, 7, 16, 33, 34],
    [16, 18, 35, 36, 41],
    [9, 12, 18, 22, 50],
    [11, 13, 14, 34, 48],
    [18, 31, 32, 41, 46],
    [2, 8, 17, 28, 35],
    [13, 28, 29, 44, 48],
    [35, 36, 41, 42, 45],
    [6, 9, 10, 30, 49],
    [13, 22, 24, 33, 47],
    [2, 20, 39, 40, 47],
    [6, 9, 11, 32, 49],
    [10, 20, 40, 44, 46],
    [22, 29, 31, 39, 46],
    [2, 3, 12, 16, 45],
    [19, 23, 26, 27, 46],
    [13, 18, 26, 35, 37],
    [1, 23, 31, 36, 48],
    [16, 17, 35, 36, 49],
    [2, 13, 14, 26, 29],
    [8, 11, 23, 32, 44],
    [7, 16, 18, 20, 32],
    [1, 4, 31, 34, 40],
    [13, 19, 30, 38, 46],
    [8, 11, 12, 16, 44],
    [2, 15, 17, 23, 36],
    [4, 7, 19, 20, 34],
    [3, 4, 9, 12, 20],
    [24, 27, 28, 30, 49],
    [23, 31, 37, 42, 48],
    [8, 13, 14, 24, 26],
    [13, 17, 18, 20, 46],
    [23, 24, 35, 37, 45],
    [2, 7, 21, 28, 45],
    [13, 20, 23, 27, 42],
    [5, 10, 19, 27, 30],
    [8, 19, 32, 41, 42],
    [14, 23, 39, 48, 50],
    [27, 28, 44, 48, 50],
    [10, 18, 21, 33, 45],
    [16, 17, 18, 45, 49],
    [2, 9, 12, 39, 40],
    [4, 7, 18, 39, 50],
    [7, 15, 18, 46, 49],
    [2, 3, 19, 36, 37],
    [8, 27, 30, 35, 47],
]

### How many week past from to
from datetime import datetime

def weeks_passed_since(date):
    today = datetime.today()
    delta = today - date
    return delta.days // 7

# Date from which to start counting (January 1, 224)
start_date = datetime(2024, 1, 1)

# Calculate the number of weeks passed since the start date
weeks_passed = weeks_passed_since(start_date)

# Print the number of weeks passed
print(f"Weeks passed since January 1, 2024: {weeks_passed}")

# Function to count combinations
def count_combinations(numbers, r):
    combination_counts = defaultdict(int)
    for sublist in numbers:
        for combo in combinations(sorted(sublist), r):
            combination_counts[combo] += 1
    return combination_counts

# Count pairs, triplets, and quadruplets
pair_counts = count_combinations(numbers, 2)
triplet_counts = count_combinations(numbers, 3)
quadruplet_counts = count_combinations(numbers, 4)

# Function to filter frequent combinations
def filter_frequent_combinations(counts, min_occurrences):
    return {combo: count for combo, count in counts.items() if count >= min_occurrences}

# Filter combinations that appear frequently
min_occurrences = 2
frequent_pairs = filter_frequent_combinations(pair_counts, min_occurrences)
frequent_triplets = filter_frequent_combinations(triplet_counts, min_occurrences)
frequent_quadruplets = filter_frequent_combinations(quadruplet_counts, min_occurrences)

# Function to sort and print combinations
def sort_and_print_combinations(combos, title):
    sorted_combos = sorted(combos.items(), key=lambda item: item[1], reverse=True)
    print(title)
    for combo, count in sorted_combos:
        print(f"{combo}: {count} times")
    print()

# Print the sorted results
sort_and_print_combinations(frequent_pairs, "Frequent Pairs:")
sort_and_print_combinations(frequent_triplets, "Frequent Triplets:")
sort_and_print_combinations(frequent_quadruplets, "Frequent Quadruplets:")

#######################################################################

# Create a dictionary to count occurrences
# Count occurrences of each number
count_dict = defaultdict(int)
for pair in numbers:
    for number in pair:
        count_dict[number] += 1

# Sort the numbers by their count in descending order
sorted_count = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)

# Print the sorted result
print("Number frequencies sorted by occurrence:")
for number, count in sorted_count:
    print(f"Number: {number}, Count: {count}")

##########################################################################################
