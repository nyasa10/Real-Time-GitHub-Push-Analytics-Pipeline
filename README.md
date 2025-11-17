# Real-Time-GitHub-Push-Analytics-Pipeline

### Tech Stack & Tools

**Features Implemented**

• Fault-tolerant 3-node Kafka cluster 
• Exactly-once semantics (idempotent producer)  
• Event-time processing with timestamps from GitHub
• Schema evolution support via Avro + Schema Registry  
• Real-time email alerting on high-activity repositories  
• 1M+ events/day scalable pipeline


| Category | Technologies |
|----------|--------------|
| **Core Streaming Platform** | **Apache Kafka** (3-broker cluster with replication & fault tolerance) <br> **Confluent Schema Registry** + **Avro** serialization <br> **ksqlDB** (real-time stream processing & transformations) <br> **Kafka Connect** + **JDBC Sink Connector** |
| **Data Warehouse & Analytics** | **Amazon Redshift Serverless** |
| **Programming & Automation** | **Python 3** (producer, consumer, email alerting) <br> **GitHub Events REST API** |
| **Infrastructure & Ops** | **Ubuntu / WSL2** (local dev) |
