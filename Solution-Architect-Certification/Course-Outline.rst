Course Outline
==============================================================================

.. contents::
    :depth: 1
    :local:


INTRODUCTION
------------------------------------------------------------------------------

.. contents::
    :depth: 1
    :local:



1. Welcome To The Course Free (Time: 00 Hour 03 Mins 39 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



2. About The Instructor (Time: 00 Hour 03 Mins 34 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



3. Why Cloud Computing? (Time: 00 Hour 06 Mins 44 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



4. Why AWS? (Time: 00 Hour 03 Mins 55 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



5. Overview Of AWS Services (Time: 00 Hour 05 Mins 13 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


GETTING STARTED WITH AWS
------------------------------------------------------------------------------

.. contents::
    :depth: 1
    :local:



1. Overview Of The Exam (Time: 00 Hour 05 Mins 52 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



2. Overview Of This Course (Time: 00 Hour 03 Mins 12 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



3. Setting Up Free-Tier AWS Account (Time: 00 Hour 04 Mins 01 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



4. Getting Familiar With AWS Console (Time: 00 Hour 09 Mins 31 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


IDENTITY AND ACCESS MANAGEMENT
------------------------------------------------------------------------------

.. contents::
    :depth: 1
    :local:



1. Introduction To IAM Free (Time: 00 Hour 07 Mins 18 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



2. Getting Started With IAM (Time: 00 Hour 10 Mins 46 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



3. IAM Users And IAM Groups (Time: 00 Hour 20 Mins 18 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



4. IAM Policies (Time: 00 Hour 14 Mins 07 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Explicit Deny > Explicit Allow > Default Deny



5. IAM Roles (Time: 00 Hour 17 Mins 08 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



6. IAM Best Practices (Time: 00 Hour 06 Mins 22 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



7. IAM Summary (Time: 00 Hour 02 Mins 30 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


SIMPLE STORAGE SERVICE (S3)
------------------------------------------------------------------------------

.. contents::
    :depth: 1
    :local:



1. Introduction To S3 Free (Time: 00 Hour 05 Mins 58 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



2. Fundamentals (Time: 00 Hour 12 Mins 32 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



3. Object Storage Vs Block Storage (Time: 00 Hour 04 Mins 24 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



4. Getting Started With S3 (Time: 00 Hour 07 Mins 36 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



5. Versioning (Time: 00 Hour 15 Mins 48 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



6. Server Access Logging And Object Level Logging (Time: 00 Hour 11 Mins 57 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



7. Static Website Hosting Free (Time: 00 Hour 04 Mins 19 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



8. Encryption (Time: 00 Hour 11 Mins 39 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



9. Tags Transfer Acceleration And Multipart Upload (Time: 00 Hour 11 Mins 17 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



10. Events (Time: 00 Hour 07 Mins 34 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



11. Requester Pays (Time: 00 Hour 02 Mins 56 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



12. Permissions Access Control List And Bucket Policy (Time: 00 Hour 07 Mins 52 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



13. Object Lifecycle Management (Time: 00 Hour 09 Mins 37 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



14. Cross Region Replication (Time: 00 Hour 11 Mins 34 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



15. Analytics Metrics And Inventory (Time: 00 Hour 12 Mins 17 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

以下三个分析的选项都可以在 Bucket 界面看到.

S3 Analytics

S3 Metrics, CloudWatch metrics

S3 Inventory


16. Storage Classes (Time: 00 Hour 10 Mins 00 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

What are storage classes:

- S3 Stardard
- S3 Standard - Infrequent Access (S3 Standard-IA) and S3 One Zone-Infrequent Access (S3 One Zone-IA): Long-lived, but less frequently accessed data
- Glacier: Long-term archive

S3 Standard:

- Data is replicated across at least 3 different availability zones.
- Low latency and high throughput

S3 Standard IA:

- For data that is accessed less frequently, but requires rapid access when needed.
- Data is replicated across 3 different AZs for high durability and availability.
- Cost less than S3-Standard; charges you for retrieving the data per GB (Not based on request)

S3 One Zone IA:

- Same as Standard IA
- Stored in only a single availability zone (AZ)
- 20% less than S3 Standard-IA

Glacier:

Three options for retrieving the archives:

1. Standard
2. Expedited
3. Bulk


17. Select From (Time: 00 Hour 03 Mins 21 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



18. S3 Summary (Time: 00 Hour 07 Mins 55 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


EC2 AND EBS
------------------------------------------------------------------------------

.. contents::
    :depth: 1
    :local:



1. Introduction (Time: 00 Hour 00 Mins 59 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



2. Creating An EC2 Part I (Time: 00 Hour 08 Mins 12 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Amazone Machine Image: Customizable VM Image

Virtualization Type:

- HVM: Hardware assisted Virtual Machine
- Paravirtualization

Root Device Type:

- EBS
- Instance store

Instance Type:

- T: general purpose
- C: compute optimized
- X: memory optimized
- P: accelerated computing
- H: storage optimized


3. Creating An EC2 Part II (Time: 00 Hour 11 Mins 35 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Purchase Option:

On-Demand:

- pay as you go
- costliest option
- suitable when you are not sure about the capacity need beforehand. E.g. your application has sudden spike of traffic, short projects, R&D etc.

Reserved:

- Proactive type (有前瞻性的)
- You purchase the VMs beforehand.
- Earlier and longer the period for you reserve them, more is saves you the money
- Suitable for situations where you aware about the capacity needed. E.g. Minimum number of VMs needed to run your application smoothly

Scheduled:

Spot:

- Give me if available for this price type
- saves costs significantly
- in this option, you bid for the unused EC2 instance capacity of AWS
- if the actual price of that EC2 instance class becomes equal or less than the bid price, the instances get assigned to you at your bid price.
- However, if the actual price increases than your bid price, your instances may get terminated with a half an hour's notice. So, this options is little risky, since you might lose the instance in a short notice.
- Not that you will not be charged for that partial hour in which the instance was terminated.

spot terms:

- spot instance pool: which is a set of unused EC2 instance with same instance type, OS, AZ
- spot price
- spot instance request
- spot fleet: 用来 assign / launch EC2 的, 如果你的 bid 被接受的话
- spot instance interruption


Dedicated Instance / Dedicated Host:

- Hypervisor 是用来 run VM 的超级计算机
- Shared Instance: 每次你的 VM 可能会在不同的 Hypervisor 上跑
- Dedicated Instance: 每次你的 VM 在固定的几台 Hypervisor 上跑
- Dedicated Host: 每次你的 VM 在指定的一台 Hypervisor 上跑


4. Creating An EC2 Part III (Time: 00 Hour 15 Mins 32 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Volumn Type:

1. General Purpose SSD
2. Provisioned IOPS SSD (Database Instance)
3. Magnetic HDD

还有:

4. Throughput Optimized HDD

- SSD-backed volumes are optimized and more suited for applications that require frequent read/write operation with small I/O size.
- HDD-backed volumes are more useful when the throughput (MiB/s) is more critical than IOPS


You can't attach one volume to multiple instance

EC2 Security Group:

- protects the instance by applying a security wall of rules (like a firewall)


5. Managing The EC2 Instance (Time: 00 Hour 09 Mins 54 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Network Interface:

- A network interface is a component or a virtual network card that you can attach to an instance and detach from it so that it can be reattached to another instance
- A network interface has following properties or attributes:
    - a primary IPv4 address
    - one or more secondary private IPv4 addresses
    - One elastic IP address (IPv4)
    - One public IPv4 address
    - One or more IPv6 addresses
    - One or more security groups
    - A MAC address
    - A source/destination check flag
    - A description
- Every instance in a VPC has a default network interface, called the primary network interface (eth0).
- You cannot detach a primary network interface from an instance; but, you can create and attach additional network interfaces



6. AMI Image And Bundle Task (Time: 00 Hour 07 Mins 00 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



7. EBS Volume Snapshots Free (Time: 00 Hour 13 Mins 27 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



8. Instance Store And Placement Groups (Time: 00 Hour 06 Mins 54 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Instance Store:

1. **temporary** block-level storage located on disks that are physically attached to the host computer


Placement Group:

1. arrangements of instances on the underlying hardware/hypervisor.
2. two types:
    - cluster: instances on a single hypervisor in single AZs
    - spread: each instance on a separate hypervisor in separate AZs



9. Summary (Time: 00 Hour 02 Mins 52 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


ELB & AUTOSCALING
------------------------------------------------------------------------------

.. contents::
    :depth: 1
    :local:



1. ELB Introduction (Time: 00 Hour 11 Mins 15 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Application Load Balancer: Http, Https
- Network Load Balancer: TPC/IP
- Classic Balancer


2. Application Load Balancing - Demo (Time: 00 Hour 32 Mins 47 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Listener
- rules: 比如 /picture 则送到 图像服务器, /request 则送到 App 服务器
- Health check
- Target and Target Group



3. Network Load Balancing - Demo (Time: 00 Hour 21 Mins 22 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Listener
- rules: 比如 :80 则送到 图像服务器, :8080 则送到 视频服务器
- Health check
- Target and Target Group


4. Autoscaling - Launch Configuration And Autoscaling Group (Time: 00 Hour 11 Mins 59 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Autoscale 的机制:

设置3个重要参数 min / desired / max capacity 的 Copy


5. Autoscaling - Demo (Time: 00 Hour 08 Mins 51 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



6. Scheduled Scaling Demo (Time: 00 Hour 02 Mins 41 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



7. Lifecycle Of EC2 Instance And Lifecycle Hooks (Time: 00 Hour 03 Mins 12 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



8. EC2 Instance Termination Logic (Time: 00 Hour 02 Mins 26 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


CLOUDWATCH
------------------------------------------------------------------------------

.. contents::
    :depth: 1
    :local:



1. Overview (Time: 00 Hour 10 Mins 59 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



2. Dashboards And Alarms (Time: 00 Hour 10 Mins 29 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



3. ELB Monitoring (Time: 00 Hour 21 Mins 34 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



4. EBS Monitoring (Time: 00 Hour 13 Mins 36 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



5. EC2 Custom Metrics Monitoring (Time: 00 Hour 15 Mins 44 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


VPC
------------------------------------------------------------------------------

.. contents::
    :depth: 1
    :local:



1. VPC Basics (Time: 00 Hour 12 Mins 31 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



2. Setting Up VPC (Time: 00 Hour 17 Mins 16 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



3. Create VPCFrom Wizard (Time: 00 Hour 10 Mins 36 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



4. NAT Instance Vs NAT Gateway (Time: 00 Hour 02 Mins 49 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



5. VPC Peering And VPC Endpoints (Time: 00 Hour 07 Mins 57 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



6. VPC Flow Logs (Time: 00 Hour 15 Mins 14 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


DATABASES
------------------------------------------------------------------------------

.. contents::
    :depth: 1
    :local:



1. Creating An RDS Instance (Time: 00 Hour 20 Mins 07 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



2. RDS - Multi-AZ Deployment (Time: 00 Hour 02 Mins 32 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



3. RDS - Read Replicas (Time: 00 Hour 07 Mins 02 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



4. RDS - Multi-AZ Vs Read Replicas (Time: 00 Hour 01 Mins 33 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



5. RTO And RPO (Time: 00 Hour 01 Mins 00 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



6. Connecting To RDS Instance Via Workbench (Time: 00 Hour 07 Mins 41 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



7. Redshift (Time: 00 Hour 04 Mins 41 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



8. SQL Vs NoSQL (Time: 00 Hour 03 Mins 21 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



9. DynamoDB - Tables, Item, Attributes, And Indexes (Time: 00 Hour 09 Mins 30 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



10. Global Secondary Index Vs Local Secondary Index (Time: 00 Hour 01 Mins 13 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



11. Read Consistency And Throughput Capacity (Time: 00 Hour 07 Mins 40 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



12. Autoscaling (Time: 00 Hour 01 Mins 51 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



13. Encryption (Time: 00 Hour 01 Mins 27 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



14. Query Vs Scan (Time: 00 Hour 02 Mins 24 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



15. DynamoDB Streams (Time: 00 Hour 03 Mins 20 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



16. DynamoDB Accelerator (Time: 00 Hour 01 Mins 22 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


ROUTE53
------------------------------------------------------------------------------

.. contents::
    :depth: 1
    :local:



1. Basics (Time: 00 Hour 11 Mins 58 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



2. Registering A Domain (Time: 00 Hour 02 Mins 06 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



3. Simple Routing Policy - Demo (Time: 00 Hour 10 Mins 57 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



4. Weighted Routing Policy - Demo (Time: 00 Hour 08 Mins 39 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



5. Latency Routing Policy - Demo (Time: 00 Hour 08 Mins 17 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



6. Geographical Routing Policy - Demo (Time: 00 Hour 08 Mins 32 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



7. Failover Routing Policy - Demo (Time: 00 Hour 09 Mins 07 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



8. Multivalue Answer Routing Policy - Demo (Time: 00 Hour 07 Mins 16 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


ADDITIONAL KEY SERVICES
------------------------------------------------------------------------------

.. contents::
    :depth: 1
    :local:



1. Snowball (Time: 00 Hour 04 Mins 40 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



2. AWS Kinesis (Time: 00 Hour 12 Mins 39 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



3. CloudFront Overview (Time: 00 Hour 05 Mins 18 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



4. CloudFront Lab (Time: 00 Hour 19 Mins 37 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



5. KMS & CloudHSM (Time: 00 Hour 13 Mins 39 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



6. Elastic MapReduce(EMR) (Time: 00 Hour 18 Mins 11 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



7. AWS Athena (Time: 00 Hour 09 Mins 53 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



8. EFS (Time: 00 Hour 09 Mins 21 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



9. Elasticache (Time: 00 Hour 04 Mins 34 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



10. CloudFormation (Time: 00 Hour 18 Mins 47 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



11. OpsWork (Time: 00 Hour 04 Mins 30 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



12. AWS Direct Connect (Time: 00 Hour 04 Mins 43 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



13. AWS Lambda (Time: 00 Hour 18 Mins 48 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



14. ElasticBeanstalk (Time: 00 Hour 17 Mins 06 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



15. TrustedAdvisor (Time: 00 Hour 03 Mins 41 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



16. CloudTrail (Time: 00 Hour 11 Mins 31 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



17. WAF And Shield (Time: 00 Hour 07 Mins 38 Sec)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

18. SQS, SNS And SWF
Time: 00 Hour 12 Mins 48 Sec