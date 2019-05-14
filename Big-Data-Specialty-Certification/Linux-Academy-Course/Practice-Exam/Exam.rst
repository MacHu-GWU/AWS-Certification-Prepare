Question I got Wrong
====================

Kinesis PutRecords API vs Kinesis Producer Library
------------------------------------------------------------------------------

- Kinesis PutRecords API: synchronous, will wait for the API request to complete before the application to continue. Use it for Critical Event.
- Kinesis Producer Library: asynchronous, can send many messages withing needing to slow down your application.
