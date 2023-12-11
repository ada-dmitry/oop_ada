import psycopg2

class Database:
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

class ServiceDepartment:
    def __init__(self, departmentID, departmentName, database):
        self.departmentID = departmentID
        self.departmentName = departmentName
        self.database = database
        
    def addToDatabase(self):
        conn = None
        cur = None
        try:
            conn = self.database.connect()
            cur = conn.cursor()
            cur.execute("INSERT INTO service_department (department_id, name) VALUES (%s, %s)", (self.departmentID, self.departmentName))
            conn.commit()
        finally:
            self.database.close(conn, cur)

    def handleInquires(self, application):
        conn = None
        cur = None
        try:
            conn = self.database.connect()
            cur = conn.cursor()
            cur.execute("UPDATE loan_applications SET status = %s WHERE application_id = %s", ('processed', application.applicationID))
            conn.commit()
        finally:
            self.database.close(conn, cur)

class LoanOfficer:
    def __init__(self, officerID, name, database):
        self.officerID = officerID
        self.name = name
        self.database = database

    def addToDatabase(self):
        conn = None
        cur = None
        try:
            conn = self.database.connect()
            cur = conn.cursor()
            cur.execute("INSERT INTO loan_officer (officer_id, name) VALUES (%s, %s)", (self.officerID, self.name))
            conn.commit()
        finally:
            self.database.close(conn, cur)
    
    def processLoanApplication(self, application):
        conn = None
        cur = None
        try:
            conn = self.database.connect()
            cur = conn.cursor()
            if (application.loanAmount <= 50000):
                cur.execute("UPDATE loan_applications SET status = %s WHERE application_id = %s", ('approved', application.applicationID))
            else:
                cur.execute("UPDATE loan_applications SET status = %s WHERE application_id = %s", ('rejected', application.applicationID))  
            conn.commit()
        finally:
            self.database.close(conn, cur)

class Client:
    def __init__(self, clientID, name, email, database):
        self.clientID = clientID
        self.name = name
        self.email = email
        self.database = database

    def submitApplication(self):
        conn = None
        cur = None
        try:
            conn = self.database.connect()
            cur = conn.cursor()
            cur.execute("INSERT INTO client (client_id, name, email) VALUES (%s, %s, %s)", (self.clientID, self.name, self.email))
            conn.commit()
        finally:
            self.database.close(conn, cur)

class LoanApplication:
    def __init__(self, applicationID, client, loanAmount, status, database):
        self.applicationID = applicationID
        self.client = client
        self.loanAmount = loanAmount
        self.status = status
        self.database = database
        
    def addToDatabase(self):
        conn = None
        cur = None
        try:
            conn = self.database.connect()
            cur = conn.cursor()
            cur.execute("INSERT INTO loan_applications (client_id, loan_amount, status) VALUES (%s, %s, %s)", (self.client.clientID, self.loanAmount, self.status))
            conn.commit()
        finally:
            self.database.close(conn, cur)
            
 
# Создание объектов
database = Database()

my_client = Client(clientID=1, name='Alice Smith', email='alice@example.com', database=database)
my_client.submitApplication()

# Подача заявки на кредит
application = LoanApplication(applicationID=1, client=my_client, loanAmount=20000.00, status='waiting', database=database)
application.addToDatabase()
 
# Создание объектов
service_dept = ServiceDepartment(departmentID=1, departmentName='Customer Service', database=database)
service_dept.addToDatabase()

# Обработка заявки на кредит
service_dept.handleInquires(application)

# Создание объектов
loan_officer = LoanOfficer(officerID=1, name='John Doe', database=database)
loan_officer.addToDatabase()

# Вынесение решения по заявке на кредит
loan_officer.processLoanApplication(application)