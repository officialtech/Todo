import asana
from pprint import pprint as p
from django.shortcuts import resolve_url

from django.urls.base import reverse

ACCESS_TOKEN = "1/1200852251571420:5aa33400c5eb23f759052becfb896093"
CLIENT_ID = "1200852290101635"
WORKSPACE = "1200852178821700"
ASSIGNEE = "1200852251571420"
headers = {
    "Asana-Enable": "new_user_task_lists"
}

def call_this():
    client = asana.Client.access_token(ACCESS_TOKEN)
    # projects = client.get('/projects', {})
    # p(projects) # [{'gid': '1200852232528393', 'name': 'curd operation', 'resource_type': 'project'}, {'gid': '1200862466736262', 'name': 'test project', 'resource_type': 'project'}]
    
    # tasks = client.get('/tasks', {"assignee": ASSIGNEE, "workspace": WORKSPACE})
    # p(tasks)

    # post_task = client.post('/tasks', {'name': 'This is test from utils', "notes": "This is notes from utils", "workspace": WORKSPACE, "assignee": ASSIGNEE}, headers=headers)
    # p(post_task)

    # me = client.users.me()
    # print("...........", me)
    # print("Hello " + me['name'])

    # workspace_id = me['workspaces'][0]['gid']
    # project = client.projects.create_in_workspace(workspace_id, { 'name': 'please delete me', 'list': 'Destroy it' })
    # print("Created project with id: " + project['gid'])

    # result = client.tasks.get_tasks(gid="1200852232528393", opt_pretty=True)
    # workspaces = client.workspaces.find_all(item_limit=1)
    # w = [_ for _ in workspaces]
    # print("Workspaces.....", w)
    # r = [r for r in result]
    # print("All tasks...", r)

    # result = client.put("/tasks/1200868116974158", {"notes" : 'you are new so updating, UPDATE UPDATE UPDATE updaing this'}, opt_pretty=True, headers=headers)
    # print(result)

    # result = client.delete('/tasks/1200868111151665', {'gid': '1200868111151665'}, opt_pretty=True, headers=headers)
    # print(result)

# call_this()










def create_task(payload):
    client = asana.Client.access_token(ACCESS_TOKEN)
    post_task = client.post('/tasks', payload, headers=headers)
    return post_task

def get_all_tasks():
    client = asana.Client.access_token(ACCESS_TOKEN)
    gen_data = client.get("/tasks", {"opt_fields": ["name", "notes", "completed", "created_at", "assignee", "assignee_status"], "assignee": ASSIGNEE, "workspace": WORKSPACE, "limit": "50"}, headers=headers)
    return gen_data

def update_task(payload, gid):
    client = asana.Client.access_token(ACCESS_TOKEN)
    result = client.put(f"/tasks/{gid}", payload, opt_pretty=True, headers=headers)
    return result

def delete_task(gid):
    client = asana.Client.access_token(ACCESS_TOKEN)
    result = client.delete(f'/tasks/{gid}', {'gid': gid}, opt_pretty=True, headers=headers)
    return result
