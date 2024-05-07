## KBTools
import requests,configparser
from kubernetes import client, config as kube_config
import urllib3

__all__ = [
    "load_app_config"
    "get_token_from_defectdojo",
    "load_k8s_kb_cluster_info"
]
try:
  kube_config.load_kube_config()
except Exception as e:
  print("Not able to load kubernetes configuration.")
  print("------------")
  print(e)
  print("------------")
  
urllib3.disable_warnings()

def load_app_config():
    global config
    config = configparser.ConfigParser()
    config.read('config.ini');
    return config
    pass

config = load_app_config()

def get_token_from_defectdojo():
    # Receive token from defectdojo
    global config
    dojo_url=config['DefectDojo']['url']+"api/v2/api-token-auth/"
    dojo_user=config['DefectDojo']['username']
    dojo_pass=config['DefectDojo']['password']
    query={'username':dojo_user, 'password': dojo_pass}
    headers={'accept': 'application/json','Content-Type':'application/x-www-form-urlencoded'}
    response = requests.post(dojo_url,data=query,headers=headers).json()
    return response['token']
    pass

dojo_api_token = get_token_from_defectdojo()

def load_k8s_kb_cluster_info():
    # Load configmap k8s-kb-cluster-info
    from kubernetes import client
    resource = client.CoreV1Api()
    cm_name = config['Cluster']['cm_name'].replace('"','')
    cm_namespace = config['Cluster']['cm_namespace'].replace('"','')
    config_cm = resource.read_namespaced_config_map(cm_name,cm_namespace)
    
    return { 
             "cluster_name": config_cm.data['cluster_name'],
             "tenant_prefix": config_cm.data['tenant_prefix'],
             "env": config_cm.data["cluster_env"].lower()
            }
    pass

cluster_configmap = load_k8s_kb_cluster_info()

def init_check():
    passed = False
    if config and dojo_api_token and cluster_configmap :
      passed = True
    return passed
    pass