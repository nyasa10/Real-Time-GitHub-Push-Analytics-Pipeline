DROP TABLE IF EXISTS public.github_pushes;

CREATE TABLE github_pushes (
    id VARCHAR(255) DISTKEY NOT NULL,
    type VARCHAR(50),
    actor_name VARCHAR(100),
    actor_login VARCHAR(100),
    repo_name VARCHAR(100),
    payload_ref VARCHAR(255)
);

SELECT * FROM github_pushes ORDER BY id DESC LIMIT 5;
