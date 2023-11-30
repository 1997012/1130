class Student:
    def __init__(self, school_name, department_name, dean_name, student_name, student_id, address, earned_credits, gpa):
        # 初始化函式，設定學生的初始屬性
        self.school_name = school_name  # 學校名稱
        self.department_name = department_name  # 科系名稱
        self.dean_name = dean_name  # 系主任姓名
        self.student_name = student_name  # 學生姓名
        self.student_id = student_id  # 學生學號(ID)
        self.address = address  # 個人通訊地址
        self.earned_credits = earned_credits  # 已取得學分數
        self.gpa = gpa  # 成績GPA

    # 取得和設定學校名稱的方法
    def getSchoolName(self):
        return self.school_name

    def setSchoolName(self, school_name):
        self.school_name = school_name

    # 取得和設定科系名稱的方法
    def getDepartmentName(self):
        return self.department_name

    def setDepartmentName(self, department_name):
        self.department_name = department_name

    # 取得和設定系主任姓名的方法
    def getDeanName(self):
        return self.dean_name

    def setDeanName(self, dean_name):
        self.dean_name = dean_name

    # 取得和設定學生姓名的方法
    def getStudentName(self):
        return self.student_name

    def setStudentName(self, student_name):
        self.student_name = student_name

    # 取得和設定學生學號的方法
    def getStudentID(self):
        return self.student_id

    def setStudentID(self, student_id):
        self.student_id = student_id

    # 取得和設定個人通訊地址的方法
    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    # 取得和設定已取得學分數的方法
    def getEarnedCredits(self):
        return self.earned_credits

    def setEarnedCredits(self, earned_credits):
        self.earned_credits = earned_credits

    # 取得和設定GPA的方法
    def getGPA(self):
        return self.gpa

    def setGPA(self, gpa):
        self.gpa = gpa
