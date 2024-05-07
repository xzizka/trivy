#!/usr/bin/python3

from os import path
from pprint import pprint
# pip3 install kubernetes
import yaml,json
from kubernetes import client, config as kube_config, dynamic
import KBTools
import KBTools.product_type, KBTools.test

def main():
    # Load configuration from config file
    # KBTools.config = load_app_config()
    
    # DefectDojo API token
    # KBTools.dojo_api_token = get_token_from_defectdojo()
    
    # Load configuration for communication with cluster
    # kube_config.load_kube_config() is part of the KBTools module
    
    # Get info about the cluster
    # KBTools.cluster_configmap = load_k8s_kb_cluster_info()
       
    # KBTools.cluster_configmap["cluster_name"] = load_k8s_kb_cluster_info()["cluster_name"]
    # KBTools.cluster_configmap["tenant_prefix"] = load_k8s_kb_cluster_info()["tenant_prefix"]
    # KBTools.cluster_configmap["env"] = load_k8s_kb_cluster_info()["env"].lower()
    
    # Create instance of product_type
    #product_type = KBTools.product_type.ProductType(tenant_prefix, tenant_prefix + " cluster", dojo_api_token, config)
    try:
      KBTools.init_check() 
    except Exception as e:
      print("Inicialization failed")
      print("------------")
      print(e)
      print("------------")
    
    product_type = KBTools.product_type.ProductType()
    if product_type.check_endpoint_existence():
      client_res = dynamic.DynamicClient(client.ApiClient(configuration=kube_config.load_kube_config()))
      apirres = client_res.resources.get(api_version="aquasecurity.github.io/v1alpha1",kind="ConfigAuditReport")
      pprint(apirres.get(namespace="trivy-system",name=replicase))
      ##for crd in json.loads(KBTools.config["CRDs"]["crds_to_use"]):
        
if __name__ == '__main__':
    main()