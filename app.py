from version import __version__
import time
import os
import yaml
import json
import config as env
from kubernetes import client, config
from kubernetes.client.rest import ApiException
from pprint import pprint

path = env.AP_POLICY_PATH
namespace = env.AP_NAMESPACE
name = env.AP_CONFIGMAP_NAME

def main():
    config.load_incluster_config()
    v1 = client.CoreV1Api()
    try: 
        api_response = v1.read_namespaced_config_map(name, namespace, pretty=False)
        policy_obj = (api_response.data['policy.yaml'])
        f = open('{}'.format(path), 'w')
        print(yaml.safe_dump(yaml.safe_load(policy_obj), f))
        f.close()
    except ApiException as e:
        print("Exception when calling CoreV1Api->read_namespaced_config_map: %s\n" % e)

if __name__ == '__main__':
    while True:
        time.sleep(5)
        main()
