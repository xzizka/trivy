## test
import KBTools, requests 
from kubernetes import client

class Test:
    def __init__(test_crd, test_namespace, test_name) -> None:
        self.test_crd = test_crd
        self.test_namespace = test_namespace
        self.test_name = test_name
        load_test()
        pass
    
    def load_data_from_cluster(self):
        resource = client.CoreV1Api()
        apirres = resource.ApiextensionsV1Api()
        print(apirres)
        pass
    
    def load_test():
        pass
