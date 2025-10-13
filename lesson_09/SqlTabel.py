from sqlalchemy import create_engine, text

class SqlTable:
    __scripts = {
		"delete_by_id": text("DELETE FROM teacher WHERE teacher_id = :id_to_delete"),
		"insert_new_teacher": text("INSERT INTO teacher(\"teacher_id\", \"email\", \"group_id\") values (:new_teacher_id, :new_email,:new_group_id)"),
        "select_by_id": text("SELECT * FROM teacher WHERE teacher_id =:new_teacher_id"),
        "update_by_id": text("update teacher set email =:new_email WHERE teacher_id =:new_teacher_id ")
      }
    

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    
    def delete(self, teacher_id):
        conn = self.__db.connect()
        conn.execute(self.__scripts["delete_by_id"], {"id_to_delete": teacher_id})
        conn.commit()
        conn.close()

    def create(self, teacher_id, email, group_id ):
        conn = self.__db.connect()
        conn.execute(self.__scripts["insert_new_teacher"], {"new_teacher_id": teacher_id, "new_email": email, "new_group_id": group_id })
        conn.commit()
        conn.close()

    def get_teacher_by_id(self, teacher_id):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select_by_id"], {"new_teacher_id": teacher_id})
        teacher = result.mappings().all() 
        conn.close()
        return teacher
    
    def update_email_teacher(self, teacher_id, email):
         conn = self.__db.connect()
         conn.execute(self.__scripts["update_by_id"], { "new_email": email, "new_teacher_id": teacher_id })
         conn.commit()
         conn.close()
         