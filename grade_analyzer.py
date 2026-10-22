# grade_analyzer.py - basic structure

scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]

for score in scores:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

print("===  Grade Analyzer ===")

print(f"Total scores: {len(scores)}")
print(f"Average: {sum(scores) / len(scores):.1f}")
print(f"Highest: {max(scores)}")
print(f"Lowest: {min(scores)}")
print(f"Passing: {len([score for score in scores if score >= 60])}")
print(f"Failing: {len([score for score in scores if score < 60])}")

# grade distribution
grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
for score in scores:
    if score >= 90:
        grade_counts["A"] += 1
    elif score >= 80:
        grade_counts["B"] += 1
    elif score >= 70:
        grade_counts["C"] += 1
    elif score >= 60:
        grade_counts["D"] += 1
    else:
        grade_counts["F"] += 1

print("\nGrade Distribution:")
for grade, count in grade_counts.items():
    print(f"{grade}: {count}")

# add more scores
print("\n--- Add More Scores ---")
print("Enter another score (or 'done' to finish): ")
while True:
    user_input = input()
    if user_input.lower() == 'done':
        break
    try:
        new_score = int(user_input)
        scores.append(new_score)
    except ValueError:
        print("Please enter a valid score or 'done'.")

# updated average
print(f"\nUpdated Average: {sum(scores) / len(scores):.1f}")

# final average
print("Final average: {:.1f}".format(sum(scores) / len(scores)))
