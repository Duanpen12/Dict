lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]

for student_get in students:
    print(student_get.get('name'))
    print(student_get.get('homework'))
    print(student_get.get('quizzes'))
    print(student_get.get('tests'))

def average(numbers):
    total_sum = float(sum(numbers))
    return total_sum / len(numbers)

def get_average(student):
    return average(student['homework']) * 0.1 + average(student['quizzes']) * 0.3 + average(student['tests']) * 0.6

score_num = \
    {
        90: "A",
        80: "B",
        70: "C",
        60: "E"
    }

def get_letter_grade(score):
    for score_name in score_num.keys():
        if score >= score_name:
            return score_num.get(score_name)
    return "F"

print(get_letter_grade(get_average(lloyd)))

def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
        return average(results)

print(get_class_average(students))
print(get_letter_grade(get_class_average(students)))


