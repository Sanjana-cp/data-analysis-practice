import numpy as np
marks=np.array([[85,78,92,88],[72,80,75,70],[90,88,95,92],[60,65,70,68],[88,90,85,87]])


mean=np.mean(marks,axis=0)
stand=np.std(marks,axis=0)

z_score1=marks-mean

z_score2=z_score1/stand

total=np.sum(z_score2,axis=1)

tup=z_score2.shape

total=total/tup[1]
print("marks:")
print(marks,"\n")
print("Z-score matrix:")
print(z_score2, "\n")

print("Final student scores:")
print(total, "\n")

print("Student classification:")

for i in total:
    if i>= +1:
        print("the student is strong")
    elif i<= -1:
        print("the student is weak")
    else:
        print("student is average")
