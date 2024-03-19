import sqlite3

CONN = sqlite3.connect('data/Office.db')
CURSOR = CONN.cursor()

class Employee:
    all = {}

    def __init__(self,name,email,manager_id):
        self.id = None
        self.name = name
        self.email = email
        self.username = 'user'
        self.manager_id = manager_id
        pass

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        if isinstance(value,str) and len(value):
            self._name = value
        else:
            raise ValueError('Invalid name input')

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self,value):
        if isinstance(value,str) and len(value):
            self._email = value
        else:
            raise ValueError('Invalid email input')

    @property
    def manager_id(self):
        return self._manager_id
    @manager_id.setter
    def manager_id(self,value):
        from classes.managers import Manager
        if isinstance(value,int) and Manager.find_by_id(value):
            self._manager_id = value 

    def save(self):
        sql="""
            INSERT INTO employees (name,email,username,manager_id)
                        VALUES (?,?,?,?);
        """
        CURSOR.execute(sql,(self.name,self.email,self.username,self.manager_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def delete(self):
        sql="""
            DELETE FROM employees WHERE id = ?;
        """
        CURSOR.execute(sql,(self.id, ))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls,row):
        employee = cls.all.get(row[0])
        if employee:
            employee.name = row[1]
            employee.email = row[2]
            employee.username = row[3]
            employee.manager_id = row[4]
        else:
            employee = cls(row[1],row[2],row[4])
            employee.id = row[0]
            cls.all[employee.id] = employee
        return employee
    
    @classmethod
    def find_by_id(cls,id):
        sql="""
            SELECT * FROM employees WHERE id=?;
        """
        row = CURSOR.execute(sql,(id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_email(cls,email):
        sql="""
            SELECT * FROM employees WHERE email=?;
        """
        row = CURSOR.execute(sql,(email,)).fetchone()
        return cls.instance_from_db(row) if row else None