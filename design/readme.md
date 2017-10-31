# Metric Collection & Query System
The system contains two components:

1.	Collection Service

2.	Query Service

### Collection Service

The Collection service transports response times from Client Apps to our system through web service using GET requests.

While we are looking for response times – Throughput, Latency, Success %, Error %, Network Bandwidth, Disk IO, CPU and Resource Utilization, we collect as many metrics possible and especially those providing granular data to identify patterns through visualizing spikes as part of the record.

The data is in the form of JSON to accept key value inputs. And this data is stored for back up in a Database for backup. We write a service over the database and the Query Service provides aggregated values (average, min, max and median) for the metrics that are collected through a web service with a JSON endpoint for every hour in the day of the format ```http://hostname/<key>/<stat_type>/<date>/<hour>```

### Query Service

The data needs to be dumped somewhere. A database seems to be a good choice. Provides a Straightforward way to provide clients access to querying, Becomes handy to back up data & database is secure and Access to certain views can be given without giving the table access for querying.

Security levels are high and can be manipulated according to the needs but need to keep in mind when using such a service. Inefficient queries adds cost on the server. A database record is not easily readable like xml or json. So, additional implementation on the DB is an overhead

## Design
![Alt text](initialsystemdesign.png?raw=true "Optional Title")


### Failures May Happen Here
Due to the following reasons:

1. Not resilient. When the system is overlaoded with 10x, 100x, 1000x, the collection service gets overloaded and the consumer faces a problem and pings the producer and the system collapses.
2. Not Scalabile. During increased loads, the server cannot withstand the high requests
3. Availability. When the clients access data on the query service the data is not available


## Final Design

Addresses the above failures

Implementing a message bus between the collection service and the query service that can buffer the messages for scalable, higher volume capacity. With the loosely coupled architecture it scales better and resolves the availability of data even when the producer or consumer is not available.

On higher volumes, with some providers, we can horizontally or vertically scale the clusters when using cloud services and not manipulate the servers that support this architecture.

![Alt text](systemdesign.png?raw=true "Optional Title")

