-- sample_data.sql

-- Create a table for users
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    created_at TIMESTAMP
);

-- Generate 100 sample users
INSERT INTO users (username, email, created_at)
SELECT pgfaker.username(), pgfaker.email(), pgfaker.timestamp() FROM generate_series(1, 100);

