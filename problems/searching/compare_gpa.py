import collections
import bisect

Student = collections.namedtuple('Student', ('name', 'gpa'))

def comp_gpa(student):
    # negate since bisect only works on ascending lists
    return (-student.gpa, student.name)

def search_student(students, target, comp_gpa):
    i = bisect.bisect_left([comp_gpa(s) for s in students], comp_gpa(target))
    print(i)
    return 0 <= i < len(students) and students[i] == target

def main():
    names = ['Joe', 'Wendy', 'Bob', 'Josh', 'John', 'Bill', 'Mary']
    gpas = [4.0 , 4.0, 3.7, 3.5, 3.4, 3.2, 3.0]
    students = [ Student(name,gpa) for name, gpa in zip(names,gpas)]
    
    target1 = Student('Wendy', 4.0)
    target2 = Student('Darian', 3.2)
    print('Found Wendy:')
    print(search_student(students, target1, comp_gpa))
    print('Found Darian:')
    print(search_student(students, target2, comp_gpa))
    
    
 
if __name__ == '__main__':
    main()
