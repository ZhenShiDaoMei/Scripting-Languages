"""Calculate student grades by combining data from many sources.

Using Pandas, this script combines data from the:

* Roster
* Homework & Exam grades
* Quiz grades

to calculate final grades for a class.
"""

#part 1
#Importing Libraries and Setting Paths
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

HERE = Path(__file__).parent
DATA_FOLDER = HERE / "data"

#part 2
#Data Importation and Cleaning
roster = pd.read_csv(DATA_FOLDER / "roster.csv", usecols=['NetID', 'Email Address', 'Section'])
roster['NetID'] = roster['NetID'].str.lower()
roster['Email Address'] = roster['Email Address'].str.lower()
roster.set_index('NetID', inplace=True)

hw_exam_grades = pd.read_csv(DATA_FOLDER / "hw_exam_grades.csv")
hw_exam_grades['SID'] = hw_exam_grades['SID'].str.lower()
hw_exam_grades.set_index('SID', inplace=True)

quiz_grades = pd.DataFrame()
for quiz_file in DATA_FOLDER.glob('quiz_*_grades.csv'):
    quiz_df = pd.read_csv(quiz_file)
    quiz_df.set_index("Email", inplace=True)
    quiz_df.sort_values(by="Email", inplace=True)
    quiz_name = quiz_file.stem 
    quiz_df.rename(columns={'Grade': quiz_name}, inplace=True)
    quiz_df.drop(columns=['Last Name', 'First Name'], inplace=True)
    if quiz_grades.empty:
        quiz_grades = quiz_df
    else:
        quiz_grades = pd.merge(quiz_grades, quiz_df, left_index=True, right_index=True, how='outer')

#part 3
#Data Merging: roaster and homework
final_data = pd.merge(roster, hw_exam_grades, left_index=True, right_index=True)

#Data Merging: Final data and quiz grades
final_data = pd.merge(final_data, quiz_grades, left_on='Email Address', right_index=True)
final_data = final_data.fillna(0)

#part 4
#Data Processing and Score Calculation
n_exams = 3
for n in range(1, n_exams + 1):
    exam_col = f'Exam {n}'
    max_points_col = f'Exam {n} - Max Points'
    final_data[exam_col] = final_data[exam_col] / final_data[max_points_col]

#Calculating Exam Scores:
#Filter homework and Homework - for max points
homework_scores = final_data.filter(regex='^Homework \d+$')
homework_max_points = final_data.filter(regex='^Homework \d+ - Max Points$')

#Calculating Total Homework score
sum_of_hw_scores = homework_scores.sum(axis=1)
sum_of_hw_max = homework_max_points.sum(axis=1)
final_data["Total Homework"] = sum_of_hw_scores / sum_of_hw_max

#Calculating Average Homework Scores
hw_max_renamed = homework_max_points.rename(columns=lambda x: x.split(' - ')[0])
average_hw_scores = homework_scores.div(hw_max_renamed)
average_hw_scores = average_hw_scores.mean(axis=1)


final_data["Average Homework"] = average_hw_scores

#Final Homework Score Calculation
final_data["Homework Score"] = final_data[["Total Homework", "Average Homework"]].max(axis=1)

#Calculating Total and Average Quiz Scores:
quiz_scores = final_data.filter(regex='^quiz_.*_grades$')
quiz_max_points = pd.Series(
    {"Quiz 1": 11, "Quiz 2": 15, "Quiz 3": 17, "Quiz 4": 14, "Quiz 5": 12}
)

#Final Quiz Score Calculation:
sum_of_quiz_scores = quiz_scores.sum(axis=1)
sum_of_quiz_max = quiz_max_points.sum()
final_data["Total Quizzes"] = sum_of_quiz_scores / sum_of_quiz_max

quiz_max_points.index = quiz_scores.columns
average_quiz_scores = quiz_scores.div(quiz_max_points, axis='columns')
average_quiz_scores = average_quiz_scores.mean(axis=1)
final_data["Average Quizzes"] = average_quiz_scores
final_data["Quiz Score"] = final_data[["Total Quizzes", "Average Quizzes"]].max(axis=1)

#Calculating the Final Score:
weightings = pd.Series({
    "Exam 1": 0.05,
    "Exam 2": 0.10,
    "Exam 3": 0.15,
    "Quiz Score": 0.30,
    "Homework Score": 0.40,
})

final_data["Final Score"] = final_data[list(weightings.index)].mul(weightings).sum(axis=1)

#Rounding Up the Final Score:
final_data["Ceiling Score"] = np.ceil(final_data["Final Score"] * 100)

#part 5
#Defining Grade Mapping:
grades = {
    90: "A",
    80: "B", 
    70: "C", 
    60: "D", 
    0: "F"}

#Applying Grade Mapping to Data:
def grade_mapping(value):
    for threshold, letter_grade in grades.items():
        if value >= threshold:
            return letter_grade
    return 'F'
letter_grades = final_data["Ceiling Score"].apply(grade_mapping)
final_data["Final Grade"] = letter_grades

#Processing Data by Sections:
for section, table in final_data.groupby("Section"):
    filename = DATA_FOLDER / f'Section {section} Grades.csv'
    table.sort_values(by=['Last Name', 'First Name']).to_csv(filename)
    print(f"Section {section}: {len(table)} students, file saved as {filename}")

#Visualizing Grade Distribution: Get Grade Counts and use plot to plot the grades
grade_counts = final_data["Final Grade"].value_counts().sort_index()
print(grade_counts)
grade_counts.plot(kind='bar')
plt.xlabel('Grade')
plt.ylabel('Number of Students')
plt.title('Grade Distribution')
plt.show()

#Visualize the data on with Histogram and use Matplotlib density function to print Kernel Density Estimate
final_data["Final Score"].plot.hist(bins=20, density=True, alpha=0.5, label="Histogram")
final_data["Final Score"].plot.density(linewidth=4, label="Kernel Density Estimate")
final_mean = final_data["Final Score"].mean()
final_std = final_data["Final Score"].std()
x = np.linspace(final_mean - 5*final_std, final_mean + 5*final_std, 100)

#Plotting Normal Distribution:
plt.plot(x, scipy.stats.norm.pdf(x, final_mean, final_std), label='Normal Distribution')
plt.xlabel('Final Score')
plt.ylabel('Density')
plt.title('Distribution of Final Scores')
plt.legend()
plt.show()