def clean_string(s):
    # Remove specified characters: "/", " ", and "."
    return s.replace("/", "").replace(" ", "").replace(".", "")

def compare_answers(user_answers, correct_answers):
    user_answers = clean_string(user_answers.lower())
    correct_answers = clean_string(correct_answers.lower())

    incorrect_indices = [i + 1 for i in range(len(user_answers)) if user_answers[i] != correct_answers[i]]
    accuracy = (len(user_answers) - len(incorrect_indices)) / len(user_answers) * 100

    if not incorrect_indices:
        print("All answers are correct! Accuracy: {:.2f}%".format(accuracy))
    else:
        print("Incorrect answers at positions:", ', '.join(map(str, incorrect_indices)))
        print("Accuracy: {:.2f}%".format(accuracy))

# Example usage with predefined correct answers
correct_answers = "ddddd"
user_input = input("Enter your answers: ")

# Ensure user input has the same length as the correct answers
if len(user_input) != len(correct_answers):
    print("Error: The length of your answers must be the same as the correct answers.")
else:
    compare_answers(user_input, correct_answers)
