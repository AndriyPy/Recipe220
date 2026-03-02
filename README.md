<p align="center">
  <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWh2Z29nbG5xZG4zd282ZXlmYW5kaTN3cXIwZ292cWdlNGV4eXh4OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/Pcvj0fxvnO4I0khDQX/giphy.gif" width="60" />
</p>

<h1 align="center">
  <span style="font-size: 4em; font-weight: 800; background: linear-gradient(135deg, #F58220 0%, #2D4635 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
    SMART RECIPE
  </span>
</h1>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Playfair+Display&weight=700&size=28&duration=3000&pause=1000&color=F58220&center=true&vCenter=true&random=false&width=600&lines=Your+AI-Powered+Kitchen+Assistant;4,300%2B+Recipes+at+Your+Fingertips;Cook+Smarter%2C+Not+Harder!" alt="Typing SVG" />
</p>


![Project: Recipe220](https://img.shields.io/badge/Project-Recipe220-blue?style=for-the-badge)
![Site: Smart Recipe](https://img.shields.io/badge/Site-Smart%20Recipe-orange?style=for-the-badge)
![Recipes: 5k+](https://img.shields.io/badge/Recipes-5k%2B-brightgreen?style=for-the-badge)
![Generator: AI + Heuristics](https://img.shields.io/badge/Generator-AI%20%2B%20Heuristics-yellow?style=for-the-badge)

Welcome to **Smart Recipe** — the delightful web experience powered by the Recipe220 project. Smart Recipe helps you discover, create, and cook amazing meals: browse our 5,000+ recipe database, or generate new recipes instantly from the ingredients you already have. Ready to turn leftovers into magic? Let's cook!

---

## Table of Contents
- [About](#about)
- [Functionality](#functionality)
- [Key Features](#key-features)
- [How It Works](#how-it-works)
- [Tech Stack](#tech-stack)
- [Quick Start](#quick-Start)
  - [Prerequisites](#prerequisites)
  - [Install & Run](#install--run)
- [Prerequisites](#prerequisites)
- [Developers](#developers)

---

## About
Smart Recipe is a modern, friendly site built from the Recipe220 project. Its core idea: combine a large curated recipe collection (5,000+ recipes) with an intelligent generator that crafts recipe suggestions based on the exact ingredients you have on hand. Whether you want a tried-and-true classic or a brand-new creation, Smart Recipe helps you move from pantry to plate.

Project repository: [Recipe220](https://github.com/AndriyPy/Recipe220)

---

### Functionality

### **User Management*
- Registration with email verification (6-digit code)
- Login with Cloudflare Turnstile (bot protection)
- Google SSO authentication
- Profile editing (gender, birth date, country)

### **Recipes*
- **Database**: 5,000+ recipes
- **Search**: 
  - Fuzzy search (typo-tolerant)
  - Search by name and ingredients
- **Sorting(SOON)**:  
  - By name (A-Z, Z-A)
  - By rating
  - By cooking time
  - By servings
- **Recipe details(soon)** page with:
  - Ingredients list
  - Step-by-step instructions
  - Preparation time
  - Rating

### **AI Assistant*
- Generate recipes based on available ingredients
- Personalized recommendations
- OpenRouter AI integration

### **Monitoring Stack*
- **Grafana** — metrics visualization
- **Prometheus** — metrics collection
- **Loki** — log aggregation
- **cAdvisor** — container monitoring
- **Promtail** — log collection agent
  
---


### Key Features

<div align="center">
  <table>
    <tr>
      <td align="center" width="200">
        <img src="https://img.icons8.com/color/96/000000/search--v1.png" width="60"/><br/>
        <b>Smart Search</b><br/>
        <sub>Fuzzy search finds recipes even with typos(?)</sub>
      </td>
      <td align="center" width="200">
        <img src="https://img.icons8.com/color/96/000000/artificial-intelligence.png" width="60"/><br/>
        <b>AI Generator</b><br/>
        <sub>Create recipes from your ingredients</sub>
      </td>
      <td align="center" width="200">
        <img src="https://img.icons8.com/color/96/000000/google-logo.png" width="60"/><br/>
        <b>Google SSO</b><br/>
        <sub>One-click login</sub>
      </td>
    </tr>
    <tr>
      <td align="center" width="200">
        <img src="https://img.icons8.com/color/96/000000/dashboard.png" width="60"/><br/>
        <b>Full Monitoring</b><br/>
        <sub>Grafana + Prometheus stack</sub>
      </td>
      <td align="center" width="200">
        <img src="https://img.icons8.com/color/96/000000/docker.png" width="60"/><br/>
        <b>Docker Ready</b><br/>
        <sub>Easy deployment with containers</sub>
      </td>
      <td align="center" width="200">
        <img src="https://img.icons8.com/color/96/000000/cloudflare.png" width="60"/><br/>
        <b>Bot Protection</b><br/>
        <sub>Cloudflare Turnstile</sub>
      </td>
    </tr>
  </table>
</div>

---

## 🚀 Getting Started

### Prerequisites

*   **Docker & Docker Compose** (recommended)
*   **Python 3.11+** (for local launch))
*   **PostgreSQL 15+**

### Install & Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com
    cd Recipe220
    ```

2.  **Настройте переменные окружения:**
    Create a `.env` file in the root folder and add the necessary keys (OpenRouter API, Google Credentials, DB settings):
    ```bash
    cp .env.example .env
    ```

3.  **Launch via Docker (the fastest way):**
    ```bash
    docker-compose up --build
    ```

4.  **Local launch (without Docker):**
    *   Create a virtual environment:
        ```bash
        python -m venv venv
        source venv/bin/activate  # Для Windows: venv\Scripts\activate
        ```
    *   Set dependencies:
        ```bash
        pip install -r requirements.txt
        ```
    *   Launch the application:
        ```bash
        python main.py
        ```
      
---

### Prerequisites

| Tool | Version | Badge |
|------|---------|-------|
| Docker | 24.0+ | ![Docker](https://img.shields.io/badge/Docker-24.0+-2496ED?logo=docker) |
| Python | 3.11+ | ![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python) |
| PostgreSQL | 15+ | ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-4169E1?logo=postgresql) |
---

## Tech Stack

<details>
<summary><b>Click to expand full tech stack</b></summary>

### **Backend**
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-15-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Gunicorn-20.1-499848?style=for-the-badge&logo=gunicorn&logoColor=white" />
</p>

### **Frontend**
<p align="center">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/Font_Awesome-528DD7?style=for-the-badge&logo=font-awesome&logoColor=white" />
</p>

### **DevOps**
<p align="center">
  <img src="https://img.shields.io/badge/Docker-24.0-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker_Compose-✓-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
</p>

### **Monitoring**
<p align="center">
  <img src="https://img.shields.io/badge/Grafana-10.2-F46800?style=for-the-badge&logo=grafana&logoColor=white" />
  <img src="https://img.shields.io/badge/Prometheus-2.48-E6522C?style=for-the-badge&logo=prometheus&logoColor=white" />
  <img src="https://img.shields.io/badge/Loki-2.9-FFA500?style=for-the-badge&logo=grafana&logoColor=white" />
  <img src="https://img.shields.io/badge/cAdvisor-✓-00ADD8?style=for-the-badge&logo=google&logoColor=white" />
</p>

### **Integrations**
<p align="center">
  <img src="https://img.shields.io/badge/Cloudflare_Turnstile-F38020?style=for-the-badge&logo=cloudflare&logoColor=white" />
  <img src="https://img.shields.io/badge/Google_SSO-4285F4?style=for-the-badge&logo=google&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenRouter_AI-412991?style=for-the-badge&logo=openai&logoColor=white" />
  <img src="https://img.shields.io/badge/SMTP-✓-EA4335?style=for-the-badge&logo=gmail&logoColor=white" />
</p>
</details>

---

### Developers

<div align="center">
  <br />
  <img src="https://img.shields.io/badge/%20TEAM-F58220?style=for-the-badge" />
  <br /><br />


<div>
  <a href="https://github.com/AndriyPy">
    <img src="https://avatars.githubusercontent.com/u/187444054?v=4" width="100">
  </a>

  <a href="https://github.com/pypok-1">
    <img src="https://avatars.githubusercontent.com/u/187442340?v=4" width="100">
  </a>
</div>>
