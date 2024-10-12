--TODO: Add image and sold boolean to property
-- Use the RealEstateDB database
USE RealEstateDB;

-- Create the Agents table
CREATE TABLE IF NOT EXISTS Agents (
    agent_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE
);

-- Create the Clients table
CREATE TABLE IF NOT EXISTS Clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE
);

-- Create the Properties table
CREATE TABLE IF NOT EXISTS Properties (
    property_id INT AUTO_INCREMENT PRIMARY KEY,
    agent_id INT,
    address VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
	area DECIMAL(10,2) NOT NULL,
    description TEXT,
    listing_date DATE,
	sold boolean,
    FOREIGN KEY (agent_id) REFERENCES Agents(agent_id) ON DELETE CASCADE
);

-- Create the Transactions table
CREATE TABLE IF NOT EXISTS Transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT,
    transaction_date DATE,
    buyer_id INT
);
