from docx import Document

# Create a new Document
doc = Document()

# Title
doc.add_heading('Parallel Distributed System', level=1)

# Description
doc.add_paragraph(
    "This project implements a fully parallel distributed system using RabbitMQ, FastAPI, Uvicorn, and Celery. "
    "The core functionality is demonstrated by sending 1,000 messages, where multiple processes dequeue and process each message."
)

# Prerequisites
doc.add_heading('Prerequisites', level=2)
doc.add_paragraph(
    "- Docker Desktop installed on your machine. "
    "[Download Docker Desktop](https://www.docker.com/products/docker-desktop/)\n"
    "- Git installed on your machine.\n"
    "- Terminal or command prompt access."
)

# Getting Started
doc.add_heading('Getting Started', level=2)
doc.add_paragraph("There are two methods to get started with this project:")

# Method 1: Cloning the GitHub Repository and Running It on Terminal
doc.add_heading('Method 1: Cloning the GitHub Repository and Running It on Terminal', level=3)

doc.add_paragraph("1. **Clone the repository:**")
doc.add_paragraph("```bash\ngit clone https://github.com/eshwarsaistudent/eshwarsaistudent.git\n```", style='Normal')

doc.add_paragraph("2. **Navigate to the project directory:**")
doc.add_paragraph("```bash\ncd eshwarsaistudent\n```", style='Normal')

doc.add_paragraph("3. **Build and start the containers:**")
doc.add_paragraph("```bash\ndocker-compose up --build\n```", style='Normal')

doc.add_paragraph("4. **Send 1,000 messages:**")
doc.add_paragraph("Open your terminal and run:\n```bash\nInvoke-RestMethod -Method Post -Uri \"http://localhost:8000/send-messages/?count=1000\"\n```", style='Normal')

doc.add_paragraph("5. **Access RabbitMQ Management:**")
doc.add_paragraph("Open your web browser and go to:\n```bash\nhttp://localhost:15672\n```\nLog in using the credentials specified in your `.env` file.", style='Normal')

# Method 2: Downloading the Repository and Running It Locally
doc.add_heading('Method 2: Downloading the Repository and Running It Locally', level=3)

doc.add_paragraph("1. **Download the repository:**")
doc.add_paragraph("[Download ZIP](https://github.com/eshwarsaistudent/eshwarsaistudent/archive/refs/heads/main.zip) and extract it.", style='Normal')

doc.add_paragraph("2. **Navigate to the project directory:**")
doc.add_paragraph("```bash\ncd eshwarsaistudent\n```", style='Normal')

doc.add_paragraph("3. **Build and start the containers:**")
doc.add_paragraph("```bash\ndocker-compose up --build\n```", style='Normal')

doc.add_paragraph("4. **Send 1,000 messages:**")
doc.add_paragraph("Open your terminal and run:\n```bash\nInvoke-RestMethod -Method Post -Uri \"http://localhost:8000/send-messages/?count=1000\"\n```", style='Normal')

doc.add_paragraph("5. **Access RabbitMQ Management:**")
doc.add_paragraph("Open your web browser and go to:\n```bash\nhttp://localhost:15672\n```\nLog in using the credentials specified in your `.env` file.", style='Normal')

# Docker Hub Section
doc.add_heading('Docker Hub', level=2)

doc.add_paragraph(
    "If you plan to push the Docker image to Docker Hub, ensure you have a Docker Hub account and are logged in via the terminal."
)
doc.add_paragraph("```bash\ndocker login\ndocker tag eshwarsaistudent/distributed-system:latest <your-dockerhub-username>/distributed-system:latest\ndocker push <your-dockerhub-username>/distributed-system:latest\n```", style='Normal')

# License
doc.add_heading('License', level=2)
doc.add_paragraph("This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.")

# Save the document
file_path = "/mnt/data/Parallel_Distributed_System_README.docx"
doc.save(file_path)

file_path
