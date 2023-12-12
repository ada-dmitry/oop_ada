import psycopg2

class data_base:
    def __init__(self):
        self.db_params = {
            "dbname": "postgres",
            "user": "myuser",
            "password": "qwerty",
            "host": "localhost"
        }

    def connect(self):
        return psycopg2.connect(**self.db_params)

    def close(self, conn, cur):
        if cur:
            cur.close()
        if conn:
            conn.close()

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

    def add2db(self):
        conn = None
        cur = None
        try:
            conn = self.db.connect()
            cur = conn.cursor()
            cur.execute("INSERT INTO patient_db (pat_id, pat_fio, pat_born, medcard_id) VALUES (%s, %s, %s, %s)",\
                         (self.pat_id, self.pat_fio, self.pat_born, self.medcardc_id))
            conn.commit()
        finally:
            self.db.close(conn, cur)

class Developer(Employee):
    def __init__(self, name, age, salary, programming_languages):
        super().__init__(name, age, salary)
        self.programming_languages = programming_languages

    def display_tech_stack(self):
        print(f"{self.name}'s tech stack: {', '.join(self.programming_languages)}")

class Department:
    def __init__(self, name, code, manager):
        self.name = name
        self.code = code
        self.manager = manager

    def get_manager_info(self):
        return f"The manager of the department {self.name} is {self.manager}"

class Project:
    def __init__(self, name):
        self.name = name

    def assign_team(self, team):
        print(f"The team for project {self.name} has been assigned: {', '.join(team)}")

class ProgrammingLanguage:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def display_info(self):
        print(f"Programming language: {self.name}, Type: {self.type}")

class Technology:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def display_tech_info(self):
        print(f"Technology: {self.name}, Description: {self.description}")

