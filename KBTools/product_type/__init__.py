# product_type
import requests
import KBTools

class ProductType:
    """This class describes a product_type -> tribe_id+squad_name (tenant prefix) e.g. iao_sq013"""
    
    def __init__(self) -> None:
        self.name = KBTools.cluster_configmap["tenant_prefix"]
        self.description = KBTools.cluster_configmap["tenant_prefix"] + " cluster"
        self.__api_token = KBTools.dojo_api_token
        self.__config = KBTools.config
        pass

    def check_endpoint_existence(self) -> bool:

        dojo_url=self.__config['DefectDojo']['url'] + "api/v2/endpoints/"
        headers={'accept': 'application/json', 'Authorization':'Token ' + self.__api_token}
        params = {'host': 'api.'+ KBTools.cluster_configmap["cluster_name"] +'.service.ist.consul-'+KBTools.cluster_configmap["env"]+'.kb.cz','port': '6443', 'protocol': 'https'}
        response = requests.get(dojo_url,headers=headers, params=params, verify=False).json()
        if response["count"] > 0 :
          return True
        else:
          return False
        pass