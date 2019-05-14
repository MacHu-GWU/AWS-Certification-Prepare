Securing an EMR Cluster
=======================

Accessing a Cluster

1. IAM
2. Kerberos: Kerberos is a computer network authentication protocol that works on the basis of tickets to allow nodes communicating over a non-secure network to prove their identity to one another in a secure manner.
3. SSH

EMR IAM roles

- You can customize and restrict the permissions on an EMR cluster in order secure your data
- Be default, EMRFS uses the IAM role attached to the cluster to access to S3
- EMR can be configured with a role that allows it to automatically scale to meet demand
