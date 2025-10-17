from SqlTabel import  SqlTable

db = SqlTable("postgresql://postgres:ghjikjtytdthyenm@localhost:5432/qa")

def test_new_teacher():

    teacher_id = 66666
    email = 'Kolobok@gmail.com'
    groop_id = 57

    db.create(teacher_id,email,groop_id)
    teacher = db.get_teacher_by_id(teacher_id)
    db.delete(teacher_id)
    assert teacher[0]['email'] == email

def test_delete_teacher():
    teacher_id = 66666
    email = 'Kolobok@gmail.com'
    groop_id = 57

    db.create(teacher_id,email,groop_id)
    db.delete(teacher_id)
    teacher = db.get_teacher_by_id(teacher_id)
    assert len(teacher) == 0

def test_edit_teacher():
    teacher_id = 66666
    email = 'Kolobok@gmail.com'
    groop_id = 57

    db.create(teacher_id,email,groop_id)
    new_email = 'Ubazaal@gmail.com'
    db.update_email_teacher(teacher_id, new_email)
    teacher = db.get_teacher_by_id(teacher_id)
    db.delete(teacher_id)
    assert teacher[0]['email'] == new_email
    assert teacher[0]['email'] != email


