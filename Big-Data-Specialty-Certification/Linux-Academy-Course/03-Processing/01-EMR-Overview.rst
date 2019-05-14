EMR Overview
============

1. Leader Node (Master Node)
    - Manages the Cluster by coodinating the distribution of data and task
    - Track status of tasks
    - Every cluster has leader node
2. Work Node (Slave Node)
    - Core Node
        - store data in the HDFS of the cluster
        - multi-node clusters have at least one work node
    - Task Node
        - does not store data
