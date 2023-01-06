class Course:
    teachers = []

    def __init__(self, course_name, teacher, program):
        self.course_name = course_name
        self.teachers.append(teacher)
        self.program = program

    @property
    def course_name(self):
        return self.__course_name

    @course_name.setter
    def course_name(self, value):
        self.__course_name = str(value)

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, value):
        self.__teacher = str(value)

    @property
    def program(self):
        return self.__program

    @program.setter
    def program(self, value):
        self.__program = str(value)

    def add_teachers(self, name):
        self.teachers.append(name)


class LocalCourse(Course):
    def __init__(self, course_name, teacher, program, lab):
        super().__init__(course_name, teacher, program)
        self.lab = lab

    @property
    def lab(self):
        return self.__lab

    @lab.setter
    def lab(self, value):
        self.__lab = value


class OffsiteCourse(Course):
    def __init__(self, course_name, teacher, program, adress):
        super().__init__(course_name, teacher, program)
        self.adress = adress

    @property
    def adress(self):
        return self.__adress

    @adress.setter
    def adress(self, value):
        self.__adress = value


class Teacher:
    courses = []

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def add_course(self, course_name):
        self.courses.append(course_name)
