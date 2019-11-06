# audit-policy-kubernetes-daemonset
Kubernetes Daemonset to write an audit policy to a HostPath

`audit-policy-kubernetes-daemonset` was created to solve a singular problem--to write an audit policy file to the Kubernetes controller node(s) disk to enable audit logging irrespective of the underlying distribution.[[1]](https://github.com/kubernetes/kops/blob/master/docs/cluster_spec.md#audit-logging) [[2]](https://github.com/kubernetes/kops/blob/master/docs/cluster_spec.md#fileassets)

--

### Disclaimer ###

This is pre-release software and is very limited. It will have bugs and lacks many features planned for later releases. The configuration may also change in ways which are not backwards compatible.

### Configuration ###

* `AP_POLICY_PATH`: Full path of file to be written within the container.
* `AP_NAMESPACE`: Name of the deployment
* `AP_CONFIGMAP_NAME`: Name of the configMap

### Usage ###

1. Create a configMap with a matching name to `AP_CONFIGMAP_NAME` in the same namespace as the audit-policy daemonset.
2. Deploy the audit-policy daemonset with RBAC policies, example can be found in /kubernetes.
3. Update cluster.yaml for kops to consume the file at `AP_POLICY_PATH`.

**Note**: For now, the policy file within the configMap **must** be named "policy.yaml."

```yaml
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: audit-policy
data:
  policy.yaml: |
    apiVersion: audit.k8s.io/v1
    kind: Policy
    omitStages:
      - "RequestReceived"
~~~
```