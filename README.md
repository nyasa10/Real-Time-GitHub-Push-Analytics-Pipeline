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
