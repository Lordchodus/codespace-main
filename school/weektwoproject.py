# Write a program called Score Tracker.
# It should:
# Repeatedly ask the user to enter a score until they type done.
# Validate each score:
# Must be a number.
# Must be from 0 to 100 (inclusive).
# If not valid, keep asking until a valid score or done.
# Store every valid score in a list.
# When the user types done, print:
# The minimum score.
# The maximum score.
# The average score (to two decimals).
# The sorted list of scores.
# Must use:
# A loop for input.
# List methods like append and sort.
# An f-string for the formatted average.

# --------Score Tracker------- #
scores = []
while True:
    score_entered = input("Enter a score (0-100) (or type 'done'): ")
    if score_entered == 'done':
        break
    try:
        score = int(score_entered)
    except ValueError:
        print("Invalid input. Please enter a score between 0 and 100.")
        continue
    if score < 0 or score > 100:
        print("Score must be between 0 and 100")
        continue
    scores.append(score)
sorted = scores.sort()
if scores:
    scores.sort()
    minimum = min(scores)
    maximum = max(scores)
    average = sum(scores) / len(scores)
    print(f"\nMinimum score: {minimum}")
    print(f"Maximum score: {maximum}")
    print(f"Average score: {average:.2f}")
    print(f"Sorted scores: {scores}")
else:
    print("No scores were entered.")
    

