Configuring and Launching an EMR Cluster
========================================

Transient vs Long-running cluster

Launch Node:

- Cluster = Long-running cluster
- Step execution = Transient, scheduled work, cron job


EMR Cluster Lifecycle

- Starting
- Bootstraping
    - run any boostrapping actions
    - install custom applications
    - perform customizations
- EMR installing the native applications:
    - Hive, Spark, Hadoop ...
- Running
- Waiting
- Shutting Down
- Completed