# School Exam Score Report

scores = [
    [85, 90, 78],
    [92, 88, 95],
    [70, 75, 80]
]

print(
    "Maths scores -> Student 1:", scores[0][0],
    "| Student 2:", scores[1][0],
    "| Student 3:", scores[2][0]
)

all_scores = []

all_scores.extend(scores[0])
all_scores.extend(scores[1])
all_scores.extend(scores[2])

print("Highest score in class:", max(all_scores))

print("Student 2's Science score:", scores[1][1])