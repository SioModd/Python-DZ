import requests
class YougileProgect:

    def __init__(self, url):
        self.url = url
    
    def get_project_list(self,token):
          my_headers = {'Authorization': f'Bearer {token}'}
          resp = requests.get(self.url +'/api-v2/projects', headers= my_headers)
          return resp.json()
    
    def new_project(self,token,user_info,titel):
          my_headers = { "Content-Type": "application/json",'Authorization': f'Bearer {token}'}
          data = {"title": titel,"users": user_info}
          response = requests.post(self.url+'/api-v2/projects', json=data, headers=my_headers)
          return response.json()
    
    def get_progect_info(self, token, id):
          my_headers = { "Content-Type": "application/json",'Authorization': f'Bearer {token}'}
          resp = requests.get(self.url+'/api-v2/projects/'+id, headers=my_headers)
          return resp.json()
    
    def rename_project(self, token, user_info, id, new_titel):
          my_headers = { "Content-Type": "application/json",'Authorization': f'Bearer {token}'}
          data = { "deleted": False , "title": new_titel,"users": user_info}
          resp = requests.put(self.url+'/api-v2/projects/'+id, json=data,headers=my_headers)
          return resp.json()