from kubernetes import client, config

# --------------------
# 6. Kubernetes Dağıtımı
# --------------------
def deploy_kubernetes():
    """Kubernetes üzerinde dağıtım yapar."""
    config.load_kube_config()
    v1 = client.CoreV1Api()
    print("Kubernetes Namespace'leri:")
    for ns in v1.list_namespace().items:
        print(ns.metadata.name)
