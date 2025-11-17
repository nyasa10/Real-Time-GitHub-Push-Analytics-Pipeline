CREATE STREAM GITHUB_EVENTS_RAW (
    id STRING KEY,
    type STRING,
    actor STRUCT<name STRING, login STRING>,
    repo STRUCT<name STRING>,
    payload STRUCT<ref STRING>
) WITH (
    KAFKA_TOPIC = 'github-events-raw',
    VALUE_FORMAT = 'JSON',
    PARTITIONS = 3,
    KEY_FORMAT = 'KAFKA'
);



CREATE STREAM GITHUB_EVENTS_INTERMEDIATE WITH (
    KAFKA_TOPIC = 'github-events-intermediate',
    VALUE_FORMAT = 'JSON',
    PARTITIONS = 3,
    KEY_FORMAT = 'KAFKA'
) AS
SELECT 
    id AS ID,
    CAST(id AS STRING) AS ID_VALUE,
    type,
    actor,
    repo,
    payload
FROM GITHUB_EVENTS_RAW
PARTITION BY id
EMIT CHANGES;



CREATE STREAM GITHUB_PUSH_STREAM_NEW WITH (
    KAFKA_TOPIC = 'github-push-transformed-new',
    VALUE_FORMAT = 'JSON',
    PARTITIONS = 3,
    KEY_FORMAT = 'KAFKA'
) AS
SELECT
    ID AS id,           
    TYPE AS type,         
    ACTOR->NAME AS actor_name,   
    ACTOR->LOGIN AS actor_login, 
    REPO->NAME AS repo_name,   
    PAYLOAD->REF AS payload_ref  
FROM GITHUB_EVENTS_INTERMEDIATE
WHERE TYPE = 'PushEvent'
PARTITION BY ID
EMIT CHANGES;
