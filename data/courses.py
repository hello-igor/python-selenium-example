class Course:

    def __init__(self):
        self.full_name = None
        self.short_name = None

    def set_full_name(self, full_name):
        self.full_name = full_name

    def set_short_name(self, short_name):
        self.short_name = short_name


class ProgrammingCourseBuilder:

    def __init__(self):
        self.Course = Course()

    def build(self):
        self.Course.set_full_name('Python and Selenium basic programming course')
        self.Course.set_short_name('Python course')
        return self.Course