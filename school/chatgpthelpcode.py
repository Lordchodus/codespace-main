def score_tracker():
    scores = []

    while True:
        user_input = input("Enter a score (0-100) or type 'done': ")

        if user_input == 'done':
            break

        try:
            score = int(user_input)  # attempt conversion
        except ValueError:
            print("Invalid input. Please enter an integer between 0 and 100.")
            continue

        if 0 <= score <= 100:
            scores.append(score)
        else:
            print("Score must be between 0 and 100.")

    if scores:
        scores.sort()
        avg = sum(scores) / len(scores)
        print(f"\nMinimum score: {min(scores)}")
        print(f"Maximum score: {max(scores)}")
        print(f"Average score: {avg:.2f}")
        print(f"Sorted scores: {scores}")
    else:
        print("No scores were entered.")


# Run the program
score_tracker()
