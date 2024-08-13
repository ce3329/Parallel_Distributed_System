# Parallel Distributed System

## Prerequisites

- Docker Desktop installed on your machine.
- Git installed on your machine.
- Terminal (Command Prompt, PowerShell, etc.).

### Method 1: Cloning the Git Repository and Running It on Terminal

1. **Clone the repository:**

    ```bash
    git clone https://github.com/eshwarsaistudent/eshwarsaistudent.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd eshwarsaistudent
    ```

3. **Build and start the containers:**

    ```bash
    docker-compose up --build
    ```

4. **Send 1,000 messages:**

    Open your terminal and run:

    ```bash
    Invoke-RestMethod -Method Post -Uri "http://localhost:8000/send-messages/?count=1001"
    ```

5. **Access RabbitMQ Management:**

    Open your web browser and go to:

    ```bash
    http://localhost:15672
    ```

    Log in using the credentials specified in your `.env` file.

### Method 2: Downloading the Repository and Running It Locally

1. **Download the repository:**

    - [Download ZIP](https://github.com/eshwarsaistudent/eshwarsaistudent/archive/refs/heads/main.zip) and extract it.

2. **Navigate to the project directory:**

    ```bash
    cd eshwarsaistudent
    ```

3. **Build and start the containers:**

    ```bash
    docker-compose up --build
    ```

4. **Send 1,000 messages:**

    Open your terminal and run:

    ```bash
    Invoke-RestMethod -Method Post -Uri "http://localhost:8000/send-messages/?count=1001"
    ```

5. **Access RabbitMQ Management:**

    Open your web browser and go to:

    ```bash
    http://localhost:15672
    ```

    Log in using the credentials

       RABBITMQ_USER=guest
       RABBITMQ_PASSWORD=guest

