import numpy as np
import pandas as pd
import random


def student_analysis():

    np.random.seed(42)

    number = 500
    subject = 3

    st_id = np.arange(1, number + 1)

    math = np.random.randint(40, 100, size=(number))
    science = np.random.randint(40, 100, size=(number))
    english = np.random.randint(40, 100, size=(number))

    attendance = np.random.randint(60, 100, size=(number))

    dept = np.array(["CS", "ISE", "ECE", "ME"])
    some_dpt = np.random.choice(dept, size=(number))

    data = {
        "student id": st_id,
        "math": math,
        "science": science,
        "english": english,
        "attendance": attendance,
        "department": some_dpt
    }

    df = pd.DataFrame(data)

    # average marks
    df["average"] = df[["math", "science", "english"]].mean(axis=1)

    # grade assignment
    df["grade"] = np.where(df["average"] >= 85, "A",
                   np.where(df["average"] >= 70, "B",
                   np.where(df["average"] >= 55, "C", "D")))

    # top students
    top_students = df.sort_values(by="average", ascending=False).head()

    # pass rate
    some = (df["average"] >= 50).mean()
    pass_rate = some * 100

    # department analysis
    group = df.groupby("department")
    dept_average = group["average"].mean()

    # numpy zscore for math
    array = np.array(df["math"])

    math_mean = np.mean(array)
    math_std = np.std(array)

    math_zscore = (array - math_mean) / math_std

    df["math_zscore"] = math_zscore

    # save csv
    df.to_csv("student_analysis.csv", index=False)

    results = {
        "shape": df.shape,
        "pass_rate": pass_rate,
        "department_average": dept_average,
        "top_students": top_students,
        "math_mean": math_mean,
        "math_std": math_std
    }

    return results


result = student_analysis()
print(result)
print("Student Analysis Done")