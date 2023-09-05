class RegisterUser:
    def __init__(self, college_id, name, age, semester, stream, plan, username, password):
        self.college_id = college_id
        self.name = name
        self.age = age
        self.semester = semester
        self.stream = stream
        self.plan = plan
        self.username = username
        self.password = password

    def register(self):
        if all([self, self.college_id, self.name, self.age, self.semester, self.stream, self.plan, self.username, self.password]):
            # save all fields in database
            return 'Successfully Registered'
        else:
            return 'Write all Required Fields'
