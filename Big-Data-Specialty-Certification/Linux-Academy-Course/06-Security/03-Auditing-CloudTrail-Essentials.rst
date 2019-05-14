CloudTrail Essentials
==============================================================================

Reference: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html

- Cloudtrail is an API logging service that logs API calls made by AWS
- It does not matter if API calls from the CMD, SDK or Console
- All created logs are placed in to a designated S3 bucket, with these features:
    - Cross Account bucket for multiple accounts
    - Limit access to logs
    - Encrypted