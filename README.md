```markdown
# AI Task Tagger

An intelligent task management system that automatically categorizes and tags your workflow using the high-efficiency **Liquid LFM-2.5 (1.2B)** model via OpenRouter API.

**Live Demo:** [http://10.93.26.56:8000/](http://10.93.26.56:8000/)

**Screenshots:**
* [Screenshot 1](https://ibb.co/8gZvMf9N)
* [Screenshot 2](https://ibb.co/JW2X6ms0)

---

## Project Context
The main goal of **AI Task Tagger** is to eliminate the manual overhead of organizing to-do lists. Traditionally, users have to manually select priorities and categories for every task they create.

## Features
* **Smart Auto-Tagging:** Leverages Liquid LFM to assign descriptive tags instantly.
* **Persistent Storage:** Tasks and AI-generated metadata are stored in a SQLite database.
* **Modern UI:** Clean, responsive interface built with FastAPI, Jinja2, and TailwindCSS.
* **Dockerized Deployment:** Fully containerized and optimized for remote VM deployment.

## Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | FastAPI (Python 3.11) |
| **AI Agent** | **Liquid LFM-2.5-1.2B-Instruct** (via OpenRouter) |
| **Database** | SQLite + SQLAlchemy |
| **Frontend** | Jinja2 + TailwindCSS |
| **Deployment** | Docker & Docker Compose |

---

## Installation & Usage

### 1. Local Development
To run this project locally, ensure you have Docker installed.

```bash
# Clone the repository
git clone https://github.com/trinh000/se-toolkit-hackathon.git
cd se-toolkit-hackathon

# Setup environment variables
echo "OPENROUTER_API_KEY=your_sk_key_here" > .env

# Launch
sudo docker compose up -d --build
```

---

## Deployment 

This project is optimized for deployment on a **Virtual Machine (VM)**.

### 1. System Requirements
- **Operating System:** Ubuntu 24.04 LTS (Recommended)
- **Network:** Port `8000` must be open in your firewall/security groups.

### 2. Prerequisites
The following tools must be installed on the VM:
- **Git**
- **Docker** (Engine version 24.0+)
- **Docker Compose** (V2 plugin)

### 3. Step-by-Step Deployment

Follow these commands to deploy the project from scratch on your Ubuntu VM:

**Step 1: Update the system and install Docker**
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y docker.io docker-compose-v2 git
```

**Step 2: Clone the repository**
```bash
git clone https://github.com/trinh000/se-toolkit-hackathon.git
cd se-toolkit-hackathon
```

**Step 3: Configure Environment Variables**
```bash
echo "OPENROUTER_API_KEY=your_actual_api_key_here" > .env
```

**Step 4: Launch the Application**
```bash
sudo docker compose up -d --build
```

**Step 5: Verify Deployment**
```bash
sudo docker ps
```
```

