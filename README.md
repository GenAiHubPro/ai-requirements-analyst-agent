# ai-requirements-analyst-agent
An AI-powered multi-agent Requirements Analyst built with LangChain, LangGraph, Ollama (Gemma 4), and Google Drive to automatically convert customer requirements into BRDs, User Stories, Functional Specifications, and Acceptance Criteria.

# AI Requirements Analyst Agent

An enterprise-grade **AI Requirements Analyst** built using **LangChain**, **LangGraph**, **Ollama (Gemma 4)**, and **Google Drive** that automatically transforms unstructured customer requirement documents into professional software requirement artifacts.

Instead of spending hours manually analyzing customer documents, this multi-agent system extracts business knowledge, identifies missing requirements, generates structured documentation, and prepares development-ready deliverables.

---

# Features

* Read requirement documents directly from Google Drive
* Summarize business requirements
* Classify requirements into categories
* Perform requirement gap analysis
* Generate Business Requirement Document (BRD)
* Generate Functional Specification Document
* Generate User Stories

---

# Architecture

```
Customer Requirement
        │
        ▼
Google Drive Loader
        │
        ▼
Requirement Summarizer
        │
        ▼
Requirement Classification
        │
        ▼
Gap Analysis
        │
        ▼
BRD Generator
        │
        ▼
Functional Specification Generator
        │
        ▼
User Story Generator
```

---

# AI Agents

| Agent                          | Responsibility                       |
| ------------------------------ | ------------------------------------ |
| Document Loader                | Read documents from Google Drive     |
| Summarizer Agent               | Generate business summary            |
| Requirement Classifier         | Categorize requirements              |
| Gap Analysis Agent             | Detect missing requirements          |
| BRD Generator                  | Create Business Requirement Document |
| Functional Specification Agent | Generate functional specifications   |
| User Story Agent               | Generate Agile User Stories          |

---

# Technology Stack

| Component        | Technology  |
| ---------------- | ----------- |
| Framework        | LangChain   |
| Orchestration    | LangGraph   |
| LLM              | Ollama      |
| Model            | Gemma 4     |
| Vector Database  | ChromaDB    |
| Language         | Python      |
| Document Parsing | python-docx |
| Storage          | PostgreSQL  |

---

# Input

The system accepts customer requirement documents in formats such as:

* DOCX

Example input:

```
Hospital Management System Requirement.docx
```

---

# Output

The AI generates:

```
BRD.docx

FunctionalSpecification.docx

UserStories.docx

AcceptanceCriteria.docx

RequirementSummary.md

GapAnalysis.md
```

---

# Workflow

```
Read Document
      ↓
Summarize Requirements
      ↓
Classify Requirements
      ↓
Gap Analysis
      ↓
Generate BRD
      ↓
Generate Functional Specification
      ↓
Generate User Stories
```

---

# Example Use Cases

* Healthcare Management Systems
* Banking Applications
* Insurance Platforms
* Retail Management Systems
* ERP Solutions
* CRM Applications
* HR Management Systems
* Government Portals

---

# Skills Demonstrated

* Agentic AI
* Multi-Agent Systems
* LangGraph Orchestration
* LangChain
* Ollama
* Local LLM Deployment
* Prompt Engineering
* Document Intelligence
* Business Analysis Automation
* Workflow Automation
* Google Drive Integration
* Python

---

# License

This project is licensed under the MIT License.

---

# Author

Jagadeeswara Rao Patta

Technical Manager | Full Stack Developer | AI Agent Engineer

I'm a software professional with 14+ years of experience in designing and developing enterprise applications using Python, React, FastAPI, Node.js, PostgreSQL, and MongoDB. My current focus is on Agentic AI, Large Language Models (LLMs), and building enterprise-grade AI agents using LangChain, LangGraph, Ollama, and open-source AI technologies.

This repository is part of my AI engineering portfolio, where I build practical, production-oriented AI solutions that solve real-world business problems through intelligent automation.

**Connect with Me**
- LinkedIn: https://www.linkedin.com/in/jagadeeswara-rao-patta-a6526a30/
- GitHub: [https://github.com/<your-github-username>](https://github.com/GenAiHubPro)
  
**Areas of Expertise**
- Agentic AI
- Large Language Models (LLMs)
- LangChain & LangGraph
- Ollama & Local AI Models
- Python & FastAPI
- React & Full Stack Development
- Cloud-Native Application Development
- Enterprise Software Architecture
- Intelligent Document Processing
- Workflow Automation

If you found this project useful, consider giving it a star and connecting with me on LinkedIn. I regularly build and share enterprise AI projects, open-source tools, and learning resources focused on Agentic AI and Generative AI.

