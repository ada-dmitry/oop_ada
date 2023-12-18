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


class patient:
    def __init__(self, pat_id, pat_fio, pat_born, medcard_id, db):
        self.pat_id = pat_id
        self.pat_fio = pat_fio
        self.pat_born = pat_born
        self.medcardc_id = medcard_id
        self.db = db
    
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
    
    def note_check(self):
        conn = None
        cur = None
        try:
            conn = self.db.connect()
            cur = conn.cursor()
            cur.execute("SELECT * FROM appointment WHERE pat_id = %s", (self.pat_id))
            conn.commit()
        finally:
            self.db.close(conn, cur)

class doctor:
    def __init__(self, doc_id, doc_fio, doc_specialization, doc_room, db): 
        self.doc_id = doc_id
        self.doc_fio = doc_fio
        self.doc_specialization = doc_specialization
        self.doc_room = doc_room
        self.db = db

    def add2db(self):
        conn = None
        cur = None
        try:
            conn = self.db.connect()
            cur = conn.cursor()
            cur.execute("INSERT INTO doctors_db (doc_id, doc_fio, doc_specialization, doc_room) VALUES (%s, %s, %s, %s)", \
                        (self.doc_id, self.doc_fio, self.doc_specialization, self.doc_room))
            conn.commit()
        finally:
            self.db.close(conn, cur)
    
    def workload_check(self, time_of_appoint): 
        conn = None
        cur = None
        try:
            conn = self.db.connect()
            cur = conn.cursor()
            if (self.time_of_appoint == time_of_appoint):
                cur.execute("UPDATE  SET status = %s WHERE application_id = %s", ('approved', time_of_appoint.applicationID))
            else:
                cur.execute("UPDATE SET status = %s WHERE application_id = %s", ('rejected', time_of_appoint.applicationID))  
            conn.commit()
        finally:
            self.db.close(conn, cur)

class MedWorker:
    def __init__(self, mw_id, mw_fio, mw_born, mw_education, db):
        self.mw_id = mw_id
        self.mw_fio = mw_fio
        self.mw_born = mw_born
        self.db = db

class DocAppointment:
    def __init__(self, appointment_id, patient, status, db):
        self.appointment_id = appointment_id
        self.patient = patient
        self.status = status
        self.time_of_appoint
        self.db = db
        
    def del_appoint(self):
        conn = None
        cur = None
        try:
            conn = self.database.connect()
            cur = conn.cursor()
            cur.execute("DELETE FROM appointment WHERE appointment_id = %s", self.appointment_id)
            conn.commit()
        finally:
            self.database.close(conn, cur)        

    def add_appoint(self):
        conn = None
        cur = None
        try:
            conn = self.database.connect()
            cur = conn.cursor()
            cur.execute("INSERT INTO appointment (appointment_id, patient, status, time_of_appoint) VALUES (%s, %s, %s, %s)",\
                         self.appointment_id, self.patient, self.status, self.time_of_appoint)
            conn.commit()
        finally:
            self.database.close(conn, cur) 


database = data_base()

my_patient = patient(pat_id=11, name='Володимир Володимирович Володимир', email='volodimir@example.com', database=database)
my_patient.note_check()

application = DocAppointment(application_id=1, patient=my_patient, status='waiting', database=database)
application.add2bd()

doc = doctor(doc_id=11, doc_fio='Доктор Врачов Докторович', doc_specialization='Врач', doc_room=228, database=database)
doc.add2db()
 
