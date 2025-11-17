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
    %% ==== Sources ====
    A[GitHub API<br/>Public Events] -->|REST Polling| B[Python Producer<br/>github_producer.py]

    %% ==== Kafka Cluster ====
    B --> C[Kafka Cluster<br/>3 Brokers<br/>(9092, 9094, 9095)]
    C -->|Topic| D[github-events-raw<br/>JSON]

    %% ==== ksqlDB ====
    D --> E[ksqlDB<br/>~/KafkaProject/ksqldb-0.29.0]
    E -->|Filter & Transform| F[github-events-intermediate]
    F -->|PushEvent Only| G[github-push-transformed-new<br/>AVRO + Schema Registry]

    %% ==== Schema Registry ====
    H[Schema Registry<br/>port 8081] <--> G

    %% ==== Sink ====
    G --> I[Kafka Connect<br/>JDBC Sink]
    I --> J[Amazon Redshift Serverless<br/>Table: github_pushes]

    %% ==== Alerting ====
    G --> K[Python Consumer<br/>email_alert_consumer.py]
    K --> L[SMTP Email Alerts<br/>High Push Activity]

    %% ==== Styling ====
    classDef src   fill:#4CAF50,color:#fff
    classDef kafka fill:#FF9800,color:#fff
    classDef proc  fill:#2196F3,color:#fff
    classDef sink  fill:#9C27B0,color:#fff
    classDef alert fill:#F44336,color:#fff

    class A src
    class C kafka
    class E,F,G,H proc
    class I,J sink
    class K,L alert
