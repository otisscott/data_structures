num_students = int(input("How many students are in your class? "))
while num_students < 1:
    print("Invalid # of students, try again.\n")
    num_students = int(input("How many students are in your class? "))

num_tests = int(input("How many tests are in your class? "))
while num_tests < 1:
    print("Invalid # of tests, try again.\n")
    num_tests = int(input("How many tests are in this class? "))

print("\nHere we go!")
class_score_total = 0
for i in range(1, num_students+1):
    print("\n**** Student #" + str(i) + "****")
    student_score_total = 0
    for j in range(1, num_tests+1):
        score = int(input("Enter score for test #" + str(j) + ": "))
        while score < 0:
            print("Invalid score, try again")
            score = int(input("Enter score for test #" + str(j) + ": "))
        student_score_total += score
    class_score_total += student_score_total
    print("Average score for student #" + str(i) + " is " + str(round(student_score_total/num_tests, 2)))

print("\nAverage score for all students is: " + str(round(class_score_total/(num_students*num_tests), 2)))
