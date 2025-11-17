# Real-Time-GitHub-Push-Analytics-Pipeline

### Tech Stack & Tools

**Core Streaming Platform**

• Apache Kafka (3-broker cluster with replication & fault tolerance)  
• Confluent Schema Registry + Avro serialization  
• ksqlDB (real-time stream processing & transformations)  
• Kafka Connect + JDBC Sink Connector  

**Data Warehouse & Analytics**

• Amazon Redshift Serverless  

**Programming & Automation**

• Python 3 (producer, consumer, email alerting)  
• REST API integration (GitHub Events API)  

**Infrastructure & Ops** 

• Ubuntu / WSL2 (local development environment)  

**Features Implemented**

• Fault-tolerant 3-node Kafka cluster 
• Exactly-once semantics (idempotent producer)  
• Event-time processing with timestamps from GitHub
• Schema evolution support via Avro + Schema Registry  
• Real-time email alerting on high-activity repositories  
• 1M+ events/day scalable pipeline
