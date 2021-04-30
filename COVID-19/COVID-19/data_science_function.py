# author : Heginio Jr Taeza
# GitHub @ juniortaeza

import pandas as pd
import numpy as np


def summary_statistics(data_set: pd.DataFrame) -> pd.DataFrame:
    summary_data = dict()

    summary_data['mean'] = data_set.mean(numeric_only=True)
    summary_data['std'] = data_set.std(ddof=1, numeric_only=True)
    summary_data['min'] = data_set.min(numeric_only=True)
    summary_data['max'] = data_set.max(numeric_only=True)

    return pd.DataFrame(summary_data).T


if __name__ == '__main__':
    # test function
    low_score = 0
    high_score = 100
    size = (5, 5)
    headers = ("Assignment 01", "Assignment 02", "Assignment 03", "Assignment 04", "Assignment 05")
    students = ("Junior", "Kyle", "Bridget", "Jason", "Michael")

    # seed random number generator
    np.random.seed(33)
    student_scores = np.random.randint(low_score, high_score, size)
    student_scores = pd.DataFrame(student_scores, columns=headers)

    print(student_scores)
    print()

    print(summary_statistics(student_scores))