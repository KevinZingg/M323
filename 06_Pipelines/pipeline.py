class Course:
    def __init__(self, title, students):
        self.title = title
        self.students = students

class CourseSubscriptions:
    def __init__(self, title, totalStudents):
        self.title = title
        self.totalStudents = totalStudents

# Initial courses data
courses = [
    Course("M323", ["Peter", "Petra", "Paul", "Paula"]),
    Course("M183", ["Paula", "Franz", "Franziska"]),
    Course("M117", ["Paul", "Paula"]),
    Course("M114", ["Petra", "Paul", "Paula"]),
]

def find_modules(student_name):
    modules = [course.title for course in courses if student_name in course.students]
    return f"{student_name} besucht folgende Module: {', '.join(modules)}"

def generate_course_subscriptions():
    return [CourseSubscriptions(course.title, len(course.students)) for course in courses]

# Find modules for specific students
print(find_modules("Peter"))
print(find_modules("Petra"))

# Generate course subscriptions
course_subscriptions = generate_course_subscriptions()

# Debugging print statements
for subscription in course_subscriptions:
    print(f"Debug: {subscription.title} has {subscription.totalStudents} students enrolled.")
