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
* Generate Gherkin Acceptance Criteria
* Validate generated documents
* Store generated documents back to Google Drive

---

# Architecture

```
Customer Requirement
        │
        ▼
Google Drive Loader
        │
        ▼
Document Extraction Agent
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
        │
        ▼
Acceptance Criteria Generator
        │
        ▼
Review Agent
        │
        ▼
Google Drive Export
```

---

# AI Agents

| Agent                          | Responsibility                       |
| ------------------------------ | ------------------------------------ |
| Document Loader                | Read documents from Google Drive     |
| Extraction Agent               | Extract text from PDF, DOCX, TXT     |
| Summarizer Agent               | Generate business summary            |
| Requirement Classifier         | Categorize requirements              |
| Gap Analysis Agent             | Detect missing requirements          |
| BRD Generator                  | Create Business Requirement Document |
| Functional Specification Agent | Generate functional specifications   |
| User Story Agent               | Generate Agile User Stories          |
| Acceptance Criteria Agent      | Generate Gherkin scenarios           |
| Review Agent                   | Validate generated documents         |
| Drive Export Agent             | Upload artifacts to Google Drive     |

---

# Technology Stack

| Component        | Technology                         |
| ---------------- | ---------------------------------- |
| Framework        | LangChain                          |
| Orchestration    | LangGraph                          |
| LLM              | Ollama                             |
| Model            | Gemma 4                            |
| Embeddings       | Ollama Embeddings                  |
| Vector Database  | ChromaDB                           |
| Language         | Python                             |
| Document Parsing | Unstructured, PyMuPDF, python-docx |
| Storage          | PostgreSQL                         |
| Cloud Storage    | Google Drive API                   |

---

# Project Structure

```
ai-requirements-analyst-agent/

├── agents/
│   ├── loader.py
│   ├── extractor.py
│   ├── summarizer.py
│   ├── classifier.py
│   ├── gap_analysis.py
│   ├── brd_generator.py
│   ├── functional_spec.py
│   ├── user_story.py
│   ├── acceptance.py
│   ├── reviewer.py
│   └── drive_export.py
│
├── graph/
│   └── workflow.py
│
├── prompts/
│
├── schemas/
│
├── tools/
│
├── config/
│
├── sample_documents/
│
├── outputs/
│
├── main.py
│
└── requirements.txt
```

---

# Input

The system accepts customer requirement documents in formats such as:

* PDF
* DOCX
* TXT
* Markdown

Example input:

```
Hospital Management System Requirement.pdf
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

ReviewReport.md
```

---

# Workflow

```
Read Document
      ↓
Extract Content
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
      ↓
Generate Acceptance Criteria
      ↓
Review
      ↓
Export to Google Drive
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

# Roadmap

## Phase 1

* Google Drive Integration
* Requirement Summarization
* BRD Generation

## Phase 2

* Requirement Classification
* Functional Specification Generation
* User Story Generation
* Acceptance Criteria Generation

## Phase 3

* Requirement Gap Analysis
* Document Review Agent
* Human-in-the-Loop Approval

## Phase 4

* JIRA Integration
* Confluence Integration
* RAG with Historical Requirements
* Multi-document Analysis
* Requirement Traceability Matrix

---

# Future Enhancements

* Retrieval-Augmented Generation (RAG)
* Multi-Agent Collaboration
* Requirement Versioning
* Requirement Traceability Matrix
* Confidence Scoring
* Interactive Requirement Chat
* JIRA Ticket Creation
* Confluence Publishing

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

