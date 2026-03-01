### <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWh2Z29nbG5xZG4zd282ZXlmYW5kaTN3cXIwZ292cWdlNGV4eXh4OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/Pcvj0fxvnO4I0khDQX/giphy.gif" width="35"> Smart Recipe 

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
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Install & Run](#install--run)
- [Usage Examples](#usage-examples)
- [Database & Content](#database--content)
- [Contributing](#contributing)
- [License](#license)
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
### Developers

<div>
  <a href="https://github.com/AndriyPy">
    <img src="https://avatars.githubusercontent.com/u/187444054?v=4" width="100">
  </a>

  <a href="https://github.com/pypok-1">
    <img src="https://avatars.githubusercontent.com/u/187442340?v=4" width="100">
  </a>
</div>
