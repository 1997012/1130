class Student:

    schoolName = "南台科大"
    schoolAddress ="南台街1號"

    
    def __init__(self)-> None:
        pass
    def __init__(self,id,major,credits,gpa,address):
        self._id =id
        self._major=major
        self._credits =credits
        self._gpa =gpa
        self._address=address

    def get_ID(self):
        return self._id

    def set_ID(self, Value):
        self._id=Value