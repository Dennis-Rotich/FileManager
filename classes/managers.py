import sqlite3

CONN = sqlite3.connect('data/Office.db')
CURSOR = CONN.cursor()

class Manager:
    all = {}

    def __init__(self,name,email):
        self.id = None
        self.name = name
        self.email = email
        self.username = 'admin'
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

    def save(self):
        sql = """
            INSERT INTO  managers (name,email,username)
                        VALUES (?,?,?); 
        """
        CURSOR.execute(sql,(self.name,self.email,self.username))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def delete(self):
        sql = """
            DELETE FROM managers WHERE id = ?
        """
        CURSOR.execute(sql,(self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls,row):
        manager = cls.all.get(row[0])
        if manager:
            manager.name = row[1]
            manager.email = row[2]
            manager.username = row[3]
        else:
            manager = cls(row[1],row[2])
            manager.id = row[0]
            cls.all[manager.id] = manager
        return manager    

    @classmethod
    def find_by_id(cls,id):
        sql = """
            SELECT * FROM managers WHERE id = ?
        """
        row = CURSOR.execute(sql,(id, )).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_email(cls,email):
        sql = """
            SELECT * FROM managers WHERE email = ?
        """
        row = CURSOR.execute(sql,(email, )).fetchone()
        return cls.instance_from_db(row) if row else None            