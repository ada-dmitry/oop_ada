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
    def __init__(self, id, name, position, department):
        self.id = id
        self.name = name
        self.position = position
        self.department = department

    def hiring(self): # Добавление в базу данных
        conn = None
        cur = None
        try:
            conn = self.db.connect()
            cur = conn.cursor()
            cur.execute("INSERT INTO employees (id, name, position, department) VALUES (%s, %s, %s, %s)",\
                         (self.id, self.name, self.position, self.department))
            conn.commit()
        finally:
            self.db.close(conn, cur)

    def dismissal(self): # Удаление из базы данных
        conn = None
        cur = None
        try:
            conn = self.db.connect()
            cur = conn.cursor()
            cur.execute("DELETE FROM employees WHERE id = %s", self.id)
            conn.commit()
        finally:
            self.db.close(conn, cur)
        
    def get_details(self):
        return f"ID: {self.id}, Name: {self.name}, Position: {self.position}, Department: {self.department}"

    def assign_to_department(self, new_department):
        # self.department = new_department
        conn = None
        cur = None
        try:
            conn = self.db.connect()
            cur = conn.cursor()
            cur.execute("UPDATE employees SET department = %s WHERE id = %s", new_department, self.id)
            conn.commit()
        finally:
            self.db.close(conn, cur)
        


    def promote(self):
        # Логика для продвижения по службе
        pass

    def calculate_salary(self):
        # Логика для расчета зарплаты
        pass

class Developer(Employee):
    def __init__(self, id, name, position, department, languages, experience_level):
        super().__init__(id, name, position, department)
        self.languages = languages
        self.experience_level = experience_level
    
    def code(self):
        # Логика для написания кода
        pass

    def attend_tech_conferences(self):
        # Логика для посещения технических конференций
        pass

    def update_skills(self):
        # Логика для обновления навыков
        pass

    def collaborate(self):
        # Логика для совместной работы над проектами
        pass

class Tester(Employee):
    def __init__(self, id, name, position, department, testing_tools, automation_level):
        super().__init__(id, name, position, department)
        self.testing_tools = testing_tools
        self.automation_level = automation_level

    def run_tests(self):
        # Логика для запуска тестов
        pass

    def report_bugs(self):
        # Логика для создания отчетов о найденных ошибках
        pass

    def automate_tests(self):
        # Логика для автоматизации тестирования
        pass

    def collaborate(self):
        # Логика для совместной работы над проектами
        pass

class ProjectManager(Employee):
    def __init__(self, id, name, position, department, projects_managed, team_size):
        super().__init__(id, name, position, department)
        self.projects_managed = projects_managed
        self.team_size = team_size

    def plan_project(self):
        # Логика для планирования проекта
        pass

    def allocate_resources(self):
        # Логика для выделения ресурсов на проект
        pass

    def communicate(self):
        # Логика для коммуникации с командой и заинтересованными сторонами
        pass

    def track_progress(self):
        # Логика для отслеживания прогресса проекта
        pass

class SalesPerson(Employee):
    def __init__(self, id, name, position, department, sales_region, sales_targets):
        super().__init__(id, name, position, department)
        self.sales_region = sales_region
        self.sales_targets = sales_targets

    def meet_clients(self):
        # Логика для встречи с клиентами
        pass

    def negotiate_deals(self):
        # Логика для ведения переговоров
        pass

    def analyze_market(self):
        # Логика для анализа рынка
        pass

    def strategize(self):
        # Логика для разработки стратегий продаж
        pass

class Department:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def list_employees(self):
        # Логика для вывода списка сотрудников отдела
        pass

    def add_employee(self, employee):
        # Логика для добавления сотрудника в отдел
        pass

    def remove_employee(self, employee):
        # Логика для удаления сотрудника из отдела
        pass

    def update_department_head(self, new_head):
        # Логика для обновления начальника отдела
        pass
