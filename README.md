# 🚀 MISRA AI Agent

### AI-Powered MISRA-C Compliance & Automated Code Remediation Platform

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-green)
![MISRA-C](https://img.shields.io/badge/Compliance-MISRA--C-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 📌 Overview

MISRA AI Agent is an intelligent static-analysis and remediation platform designed to automatically detect, analyze, validate, and fix MISRA-C rule violations in C programs.

The system combines:

* ⚡ Static Analysis
* 🤖 AI-based Code Remediation
* ✅ MISRA-C Compliance Validation
* 🎨 Interactive Professional UI
* 🔍 Automated Violation Reporting

to provide a complete end-to-end MISRA compliance workflow for embedded and safety-critical software development.

---

# 🎥 Demo Video

> 📹 **Live Project Demonstration:**
> https://github.com/user-attachments/assets/495579cc-5fae-4b74-b2d5-e908d8c3799e

---

# ✨ Key Features

## 🔍 Static Code Analysis

* Detects MISRA-C violations automatically
* Identifies:

  * Array bounds violations
  * Dangerous functions (`gets`)
  * Assignment inside conditions
  * Unused variables
  * Missing static linkage
  * Unsafe memory handling
  * Format string vulnerabilities

---

## 🤖 AI-Powered Code Fixing

* Automatically converts unsafe C code into MISRA-compliant code
* Applies:

  * Safe input handling
  * Proper declarations
  * Explicit return handling
  * Safer formatting
  * MISRA-oriented coding style

---

## ✅ Compliance Validation

* Re-validates generated code after remediation
* Ensures cleaner MISRA-oriented output
* Displays compliance status dynamically

---

## 🎨 Professional Interactive UI

* Dark futuristic UI
* Scrollable code panels
* Violation cards with categorized issues
* Compliance score visualization
* Copy-to-clipboard functionality
* Colored dynamic scrollbars
* Real-time validation status

---

## 🧩 Modular Backend Architecture

* Analyzer Engine
* Fixer Engine
* Validation Engine
* Reporting Engine
* API Layer
* Frontend Visualization Layer

---

# 🏗️ Project Architecture

```text
MISRA-AI-AGENT/
│
├── backend/
│   ├── tools/
│   │   ├── analyzer_tool.py
│   │   ├── fixer_tool.py
│   │   ├── report_tool.py
│   │   └── validator_tool.py
│   │
│   ├── analyzer.py
│   ├── api.py
│   ├── fixer.py
│   ├── main.py
│   ├── mcp_server.py
│   ├── prompts.py
│   ├── tinyllama_client.py
│   └── validator.py
│
├── frontend/
│   └── app.py
│
├── input/
│   └── sample.c
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Technologies Used

## Programming Language

* Python

## Frontend

* Streamlit
* HTML/CSS
* JavaScript

## Backend

* FastAPI
* Uvicorn

## Static Analysis

* Cppcheck

## AI/LLM Integration

* TinyLlama
* Prompt Engineering

## Version Control

* Git
* GitHub

---

# 🧠 MISRA Fixes Applied

The platform automatically performs fixes such as:

* Replacing unsafe functions
* Preventing buffer overflows
* Removing dangerous memory handling
* Correcting loop boundaries
* Enforcing proper return types
* Applying explicit type-safe formatting
* Ensuring internal linkage using `static`
* Improving overall MISRA-style formatting

---

# 🚀 How to Run

## 1️⃣ Clone Repository

```bash
git clone https://github.com/M-Veda/misra-ai-agent.git
cd misra-ai-agent
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Backend

```bash
cd backend
uvicorn api:app --reload
```

---

# ▶️ Run Frontend

Open a new terminal:

```bash
streamlit run frontend/app.py
```

---

# 🌐 Open Application

```text
http://localhost:8501
```

---

# 📊 Workflow

```text
C Code Input
      ↓
Static Analysis
      ↓
Violation Detection
      ↓
AI-Based Remediation
      ↓
Validation
      ↓
MISRA-Compliant Output
```

---

# 🎯 Use Cases

* Embedded Systems Development
* Automotive Software
* Safety-Critical Applications
* Academic Research
* Secure C Programming
* Static Analysis Demonstrations
* MISRA Compliance Training

---

# 📌 Future Improvements

* Multi-file project analysis
* Full MISRA rule mapping
* PDF compliance report export
* Docker deployment
* Cloud-hosted API
* CI/CD integration
* Support for additional analyzers

---

# 👨‍💻 Author

**Veda**
B.Tech AI & ML Student
Passionate about AI systems, software quality, and intelligent automation.

---

# ⭐ Support

If you found this project useful:

* ⭐ Star the repository
* 🍴 Fork the project
* 📢 Share it with others

---

> Developed as an AI-driven software quality and MISRA compliance automation system for intelligent static-analysis remediation workflows.
