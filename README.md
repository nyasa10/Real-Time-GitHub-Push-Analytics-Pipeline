# Real-Time-GitHub-Push-Analytics-Pipeline

### Tech Stack & Tools

| Category | Technologies |
|----------|--------------|
| **Core Streaming Platform** | **Apache Kafka** (3-broker cluster with replication & fault tolerance) <br> **Confluent Schema Registry** + **Avro** serialization <br> **ksqlDB** (real-time stream processing & transformations) <br> **Kafka Connect** + **JDBC Sink Connector** |
| **Data Warehouse & Analytics** | **Amazon Redshift Serverless** |
| **Programming & Automation** | **Python 3** (producer, consumer, email alerting) <br> **GitHub Events REST API** |
| **Infrastructure & Ops** | **Ubuntu / WSL2** (local dev) |


## Features Implemented

- **Fault-tolerant 3-node Kafka cluster** 
- **Exactly-once semantics** via idempotent producer (`enable.idempotence=true`)  
- **Event-time processing** using `created_at` timestamps from GitHub  
- **Schema evolution** with Avro + Schema Registry
- **Real-time email alerting** on repositories exceeding 10 pushes / 5-min window  
- **Scalable to 1 M+ events/day**

```mermaid
flowchart TD
    A[GitHub API Events] -->|REST| B[Python Producer]
    
    B --> C[Kafka Cluster 3 Brokers]
    C --> D[github-events-raw JSON]
    
    D --> E[ksqlDB]
    E --> F[github-push-transformed-new AVRO]
    
    G[Schema Registry] <--> F
    
    F --> H[Kafka Connect]
    H --> I[Redshift Table]
    
    F --> J[Email Alert Consumer]
    J --> K[Email Alerts]
    
    classDef src fill:#4CAF50
    classDef kafka fill:#FF9800
    classDef proc fill:#2196F3
    classDef sink fill:#9C27B0
    classDef alert fill:#F44336
    
    class A src
    class C kafka
    class E,F,G proc
    class H,I sink
    class J,K alert
