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
    %% Sources
    A[GitHub API\n(Public Events)] -->|REST Polling| B[Python Producer\ngithub_producer.py]

    %% Kafka Cluster (3 Brokers)
    B --> C[Kafka Cluster\n3 Brokers\n(9092, 9094, 9095)]
    C -->|Topic| D[github-events-raw\n(JSON)]

    %% ksqlDB Processing
    D --> E[ksqlDB\n(~/KafkaProject/ksqldb-0.29.0)]
    E -->|Filter & Transform| F[github-events-intermediate]
    F -->|PushEvent Only| G[github-push-transformed-new\n(AVRO + Schema Registry)]

    %% Schema Registry
    H[Schema Registry\n(port: 8081)] <--> G

    %% Sink to Redshift
    G --> I[Kafka Connect\n(JDBC Sink)]
    I --> J[Amazon Redshift Serverless\nTable: github_pushes]

    %% Alerting
    G --> K[Python Consumer\nemail_alert_consumer.py]
    K --> L[SMTP Email Alerts\n(High Push Activity)]

    %% Styling
    classDef source fill:#4CAF50,color:white
    classDef kafka fill:#FF9800,color:white
    classDef processing fill:#2196F3,color:white
    classDef sink fill:#9C27B0,color:white
    classDef alert fill:#F44336,color:white

    class A source
    class C kafka
    class E processing
    class I,J sink
    class K,L alert
