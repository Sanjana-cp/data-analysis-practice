import numpy as np
students=10
subjects=5

marks=np.random.randint(0,101,size=(students,subjects))

print(marks)

# student_avg=[]

# for i in marks:
#     avg=np.mean(i)
#     student_avg.append(avg)

student_avg=np.mean(marks,axis=1)
subject_avg=np.mean(marks,axis=0)
    
# print(student_avg)
# print(subject_avg)

grades=[]

for i in student_avg:
    if i>=80:
        grades.append("a")
    elif i<80 and i>=60:
        grades.append("b")
    else:
        grades.append("c") 
        
print(grades)

# np.argsort(x) returns the indices that would sort array x in ascending order (smallest → largest)
# Ranking needs highest score first, so we use -x to reverse the order (descending sort)
# Example:
#   total = [263, 217, 283, 188]
#   -total = [-263, -217, -283, -188]
#   argsort(-total) gives indices of students from highest to lowest score
# NumPy uses 0-based indexing, but ranks should start from 1
# So we add +1 to convert index positions into human-friendly ranks
# Final result: highest total → Rank 1, next → Rank 2, etc.

total=np.sum(marks,axis=1) 
avg=np.argsort(-total)+1
print(avg)


subj_top=np.sum(marks,axis=0)
avg2=np.argsort(-subj_top)+1
print(avg2)
# topper_index=np.argmax(student_avg)
# print(topper_index+1)
# print(student_avg[topper_index])

# weakest_student=np.argmin(student_avg)
# print(weakest_student+1)
# print(student_avg[weakest_student])