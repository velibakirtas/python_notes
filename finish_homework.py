import sys
student = 'Veli Bakirtas'
# check name
def check_name():
    counter = 1
    while counter < 4:
        name = input('Name and surname?: ')
        if name == student:
            print('Welcome')
            break        
        elif counter == 3:
            print('Please tyr again later')
            sys.exit()
        else:
            counter += 1
            print('incorrect entry')
            
check_name()            


                        
'''
lineer algebra
introduction to python
statistics
probability
algorithm
'''


import random as rn
lessons = []
counter = 1
print('You must choose at least 3 courses for grade assessment')
while counter < 6:
    lesson1 = input('Choose course: ')
    lessons.append(lesson1)
    if counter == 5:
        break
    check_continue = input("Press any key other than 'n' to continue selecting a lesson. \nPress n to finish the course selection: ")
    if check_continue == 'n':
        break
    else:
        counter += 1

if len(lessons) < 3:
    print('You failed in class')
    sys.exit()
else:
    if len(lessons) >= 3:
        print('course selection is succesful')      

# select a course for the exam      
choose_course = input('Select a course for the exam: ')
if choose_course in lessons:
    print(f"You can take the exam of the '{choose_course}' lesson")
    points = {choose_course: 
        {'midtern exam': rn.randint(1,100),
         'second midtern exam': rn.randint(1,100),
         'final': rn.randint(1,100)
             }
         }
    # notları kendim belirlemek yerine rastgele berlirlenmesini istedim
    show = input("you can use the 'show' command to see the results: ")
    if show == 'show':
        print(points)
   
def calculate_average():
    # midtern exam: %30
    # second midtern exam: %20
    # final :%50
    return (points[choose_course]['midtern exam'] * 0.3) + (points[choose_course]['second midtern exam'] * 0.2) + (points[choose_course]['final'] * 0.5)

   
# your GPA in math class is ...
print(f"Your GPA in {choose_course} class is '{calculate_average()}'. Your success will be determined after the evaluations.")

def letter_grade():
    if calculate_average() >= 90:
        AA ='AA'
        return AA
    elif calculate_average() < 90 and calculate_average() >= 70:
        BB = 'BB'
        return BB    
    elif calculate_average() < 70 and calculate_average() >= 50:  
        CC ='CC'  
        return CC
    elif calculate_average() < 50 and calculate_average() >=30:
        DD = 'DD' 
        return DD 
    elif calculate_average() < 30:
        FF = 'FF'
        return FF
# press a key to see the letter grade    
if letter_grade() == 'FF':
    print(f"Your GPA in {choose_course} class is {calculate_average()}. Your letter grade is {letter_grade()}")
    sys.exit()
check_gradeShow = input("Press 'l'  key to see the letter grade: ")
if check_gradeShow == 'l':
    print(letter_grade())    