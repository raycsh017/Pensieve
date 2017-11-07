# System Design and Scalability

## Key Concepts

### Horizontal vs Vertical Scaling
**Horizontal scaling** means increasing the number of nodes. For example, you might add additional servers, thus decreasing the load on any server

**Vertical scaling** means increasing the resources of a specific node. For example, you might add additional memory to a server to improve its ability to handle load changes. 

### Load Balancing
**Load balancing** is a technique(?) that aims to increase reliability and availability through redundancy. The idea is to distribute workloads across multiple computing resources to optimize resource usage, maximize throughput, minimize response time, and avoid overload of any single resource. 

### Database Denormalization and NoSQL
**Denormalization** is the process of trying to improve the read performance of a database, at the expense of losing some write performance, by adding redundant copies of data or grouping data. This is useful for avoiding `join`s in a relational database such as SQL, as `join`s can get very slow as the system grows bigger.

**NoSQL** databases are non-relational databases that utilize a variety of data models, including document, graph, key-value, and columnar. They are widely recognized for their ease of development, scalable performance, high availability, and resilience

#### Relational Database vs NoSQL Database
**Relational Database**
- Data model: The relational model normalizes data into tabular structures known as tables, which consist of rows and columns. A schema strictly defines the tables, columns, indexes, relationships between tables, and other database elements.

- ACID Properties: Traditional relational database management systems (RDBMS) support a set of properties defined by the acronym ACID: Atomicity, Consistency, Isolation, and Durability. **Atomicity** means “all or nothing” – a transaction executes completely or not at all. **Consistency** means once a transaction has been committed, the data must conform to the database schema. **Isolation** requires that concurrent transactions execute separately from one another. **Durability** is the ability to recover from an unexpected system failure or power outage to the last known state.

- Performance: Performance is generally dependent on the disk subsystem. Optimization of queries, indexes, and table structure is required to achieve peak performance.

- Scale: Easiest to scale “up” with faster hardware.  Additional investments are required for relational tables to span a distributed system.

- APIs: Requests to store and retrieve data are communicated using queries which conform to a structured query language (SQL). These queries are parsed and executed by relational database management systems (RDBMS).

- Tools: SQL databases generally offer a rich set of tools for simplifying the development of database-driven applications.

**NoSQL Database**
- Data model: Non-relational (NoSQL) databases typically do not enforce a schema. A partition key is generally used to retrieve values, column sets, or semi-structured JSON, XML, or other documents containing related item attributes.

- ACID Properties: NoSQL databases often trade some ACID properties of traditional relational database management systems (RDBMS) for a more flexible data model that scales horizontally. These characteristics make NoSQL databases an excellent choice in situations where traditional RDBMS encounter architectural challenges to overcome some combination of performance bottlenecks, scalability, operational complexity, and increasing administration and support costs.

- Performance: Performance is generally a function of the underlying hardware cluster size, network latency, and the calling application.

- Scale: 	Designed to scale “out” using distributed clusters of low-cost hardware to increase throughput without increasing latency.

- APIs: Object-based APIs allow app developers to easily store and retrieve in-memory data structures. Partition keys let apps look up key-value pairs, column sets, or semi-structured documents containing serialized app objects and attributes.

- Tools: NoSQL databases generally offer tools to manage clusters and scaling. Applications are the primary interface to the underlying data.

### Database Partitioning (Sharding)
Sharding refers to splitting data across multiple machines while ensuring you have a way of figuring out which data is on which machine.

#### Vertical Partitioning
Partitioning by feature. For example, for a social network, you might have one partition for tables relating to profiles, another one for messages, and so on. One drawback is that if one of these tables gets very large, you might need to repartition that database

#### Key-Based Partitioning
Using some part of data to partition on it. A very simple way to do this is to allocate N servers and put the data on mod(key, n). One issue with this is that the number of servers you have is effectively fixed. Addition additional servers means reallocating all the data, which is a very expensive task.

#### Directory Based Partitioning
In this scheme, you maintain a lookup table for where the data can be found. This makes it relatively easy to add additional servers, but it comes with two major drawbacks. First, the lookup table can be a single point of failure. Second, constantly accessing this table impacts performance. 

### Caching
It is a simple key-value pairing and typically sits between your application layer and your data store. 

When an application requests a piece of information, it first tries the cache. If the cache does not contain the key, it will then look up the data in the data store. 

### Networking Metrics

#### Bandwidth
This is the maximum amount of data that can be transferred in a unit of time.

#### Throughput
This is the actual amount of data that is transferred.

#### Latency
This is how long it takes data to go from one end to the other (ie. the delay between the sender sending information and the receiver receiving it).

### MapReduce
MapReduce is a programming model and an associated implementation for processing and generating big data sets with a parallel, distributed algorithm on a cluster. 

It requires you to write a Map step and Reduce step. 
- **Map** takes in some data and emits a <key, value> pair.
- **Reduce** takes a key and a set of associated values and "reduce"s them in some way, emitting a new key and value. The results of this might be fed back into the Reduce program for more reducing.

## From:
- Cracking the Coding Interview
- [AWS: NoSQL](https://aws.amazon.com/nosql/)