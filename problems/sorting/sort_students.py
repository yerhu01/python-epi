class Student(object):
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    # Behavior of less than operator
    def __lt__(self, other):
        return self.name < other.name

    def __repr__(self):
        return "Student(name='%s', gpa=%.1f)" % (self.name, self.gpa)

def main():
    students = [
        Student('A', 4.0),
        Student('C', 3.0),
        Student('B', 2.0),
        Student('D', 3.2),
        ]
    
    print('Original:')
    print(students)

    # Sort accorting to __lt__. students remained unchanged
    print('Sorted by name:')
    students_sort_by_name = sorted(students)    
    print(students_sort_by_name)
    print('Original:')
    print(students)

    # Sort in-place by gpa (lowest to highest)
    print('Sorted by GPA:')
    students.sort(key=lambda student: student.gpa)
    print(students)
    print('Original:')
    print(students)

if __name__ == '__main__':
    main()
