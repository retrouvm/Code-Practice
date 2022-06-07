def get_choice() :
    menu ='''
    0. Exit
    1. Enter student info
    2. Print grades for a student
    3. Print class max, min, and average grades'''
   
    
   
    ans = -1
    while ans < 0 or ans > 3:
        print(menu)
        ans = int(input("Enter your choice: "))
    return ans
   
def get_a_class() :
    a_class = []
    while True :
        ans = input('Do you want to enter student info (y/n): ')
        if ans[0].lower() == 'n' :
            break
        elif ans[0].lower() == 'y' :
            d = get_student_grades()
            a_class.append(d)
        else :
            continue
    return a_class

def get_student_grades() :
    student = {}
    student['name'] = input('Enter the student name: ')
    student['midterm_1'] = int(input('Enter midterm 1 grade: '))
    student['midterm_2'] = int(input('Enter midterm 2 grade: '))
    student['final'] = int(input('Enter final exam grade: '))
    return student
   
def print_student_grades(alist):
    print('print_student_grades(): ')
    stu_name=input('Enter student name:')
    if stu_name not in alist:
        print('No info for', stu_name)
    elif stu_name in alist:
        return alist.index(stu_name)
    print('print_student_grades(): ')
   
def print_stats(alist) :
    n = len(alist)
    for key in ['midterm_1', 'midterm_2', 'final'] :
        max_ = 0
        min_ = 100
        sum_ = 0
        for i in range(n) :
            sum_ += alist[i][key]
            if min_ > alist[i][key] :
                min_ = alist[i][key]
            if max_ < alist[i][key] :
                max_ = alist[i][key]
        print('%9s: max = %d, min = %d, avg = %.2f.' % (key, max_, min_, sum_/n))
       
def main() :
    my_class = []
    while True :
        user_choice = get_choice()
        if user_choice == 0:
            break
        elif user_choice == 1:
            my_class = get_a_class()
        elif user_choice == 2:
            print_student_grades(my_class)
        elif user_choice == 3:
            print_stats(my_class)
        else:
            print('Invalid user choice %d' % user_choice)
           
if __name__=='__main__' :
    main()