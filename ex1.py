import numpy as np

student_scores = np.array([
    [80, 70, 75, 90],
    [60, 85, 78, 65],
    [95, 88, 82, 70],
    [70, 75, 80, 85]
])

subjects = ["Math", "Science", "English", "History"]

avg_scores = np.mean(student_scores, axis=0)
top_subject = subjects[np.argmax(avg_scores)]

print("Average scores:", avg_scores)
print("Highest average subject:", top_subject)
