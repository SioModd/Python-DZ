from YougileProgect import YougileProgect
from config import token, user_info
api =YougileProgect('https://ru.yougile.com')
    
def test_new_project():
    titel = 'Булочная Колобок'
    resp = api.new_project(token,user_info,titel)
    list_progect = api.get_project_list(token)
    assert resp['id'] == list_progect['content'][-1]['id']

def test_new_project_emty_titel():
    titel = ''
    resp = api.new_project(token,user_info,titel)
    assert resp['message'] == ['title should not be empty']

def test_get_project_bu_id():
    titel = 'Булочная Колобок'
    resp = api.new_project(token,user_info,titel)
    id = resp['id']
    resp_info = api.get_progect_info(token,id)
    assert resp_info['id'] == id

def test_get_project_bu_wrong_id():
    id = '7fgvgbg456jkh67'
    resp = api.get_progect_info(token,id)
    assert resp['message'] == 'Проект не найден'

def test_project_rename():
    titel = 'Булочная Колобок'
    resp = api.new_project(token,user_info,titel)
    id = resp['id']
    new_titel = 'Булочная Пышка'
    resp_rename = api.rename_project(token,user_info,id,new_titel)
    resp_info_rename = api.get_progect_info(token,id)
    assert resp_rename['id'] == id
    assert resp_info_rename['title'] == new_titel
    assert resp_info_rename['title'] != titel
    
def test_project_rename_emty_titel():
    titel = 'Булочная Колобок'
    resp = api.new_project(token,user_info,titel)
    id = resp['id']
    new_titel = ''
    resp_rename = api.rename_project(token,user_info,id,new_titel)
    assert resp_rename['message'] == ['title should not be empty']
    