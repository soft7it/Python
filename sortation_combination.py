from collections import defaultdict
from itertools import combinations

# List of lists
numbers = [
    # [4, 8, 10, 16, 34],
    [15, 22, 35, 44, 48],
    [2, 32, 35, 36, 39],
    [12, 18, 24, 25, 39],
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
