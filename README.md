# AI Task Tagger (SE Toolkit Hackathon)

An intelligent task management system that automatically categorizes and tags your workflow using the high-efficiency **Liquid LFM-2.5 (1.2B)** model via OpenRouter API.

**Live Demo:** [http://10.93.26.56:8000/](http://10.93.26.56:8000/)  


---

## 💡 Project Context
AI Task Tagger was developed for the SE Toolkit Hackathon to demonstrate how lightweight "Small Language Models" (SLMs) can provide enterprise-grade utility with minimal latency. 



## Features
- **Smart Auto-Tagging:** Leverages Liquid LFM to assign descriptive tags instantly.
- **Persistent Storage:** Tasks and AI-generated metadata are stored in a SQLite database.
- **Modern UI:** Clean, responsive interface built with FastAPI, Jinja2, and TailwindCSS.
- **Dockerized Deployment:** Fully containerized and optimized for remote VM deployment.

## 🛠 Tech Stack

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
git clone [https://github.com/trinh000/se-toolkit-hackathon.git](https://github.com/trinh000/se-toolkit-hackathon.git)
cd se-toolkit-hackathon

# Setup environment variables
# Create a .env file and add your OpenRouter API key:
echo "OPENROUTER_API_KEY=your_sk_key_here" > .env
