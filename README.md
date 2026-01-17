# AI-Driven Fraud Detection & AML Monitoring Platform (BFSI-Grade)

## 📌 Overview
This project is an **end-to-end AI-driven Fraud Detection & AML Monitoring Platform** designed to reflect how **banks, fintechs, and payment companies** build real-world fraud and compliance systems.

The focus is **not on black-box ML**, but on:
- Explainable fraud detection  
- Risk-based prioritization  
- Human-in-the-loop workflows  
- Compliance-aligned reporting  

The platform is **cloud-ready, regulator-aware, and interview-defensible**.

---

## 🎯 Key Objectives
- Ingest realistic transaction-like data
- Detect suspicious and anomalous behavior
- Assign transparent risk scores to transactions and accounts
- Use AI for **explainability**, not autonomous decisions
- Simulate fraud analyst workflows
- Generate technical, executive, and AML-aligned reports

---

## 🧱 High-Level Architecture

Transaction Ingestion
↓
Fraud & Anomaly Detection
↓
Risk Scoring Engine
↓
AI Explanation Engine
↓
Alert & Case Management
↓
Compliance & Reporting


---

## 🧩 Core Components

### 1️⃣ Transaction Ingestion
- Simulated transaction data (amount, velocity, geography, behavior)
- Account-level behavioral baselines
- Supports batch ingestion (CSV-based, cloud-ready)

---

### 2️⃣ Fraud & Anomaly Detection
Explainable, rule-based detection including:
- Unusual transaction amounts
- Rapid transaction bursts (velocity spikes)
- Geographic anomalies
- Behavioral drift
- AML structuring patterns  

Each detector produces **human-interpretable risk signals**.

---

### 3️⃣ Risk Scoring System
- Weighted risk scoring model
- Signal-strength multipliers (LOW / MEDIUM / HIGH)
- Account-level risk aggregation
- Priority classification: **LOW / MEDIUM / HIGH**
- Fully auditable calculations

---

### 4️⃣ AI Explanation Engine (Core Differentiator)
- Converts technical signals into plain-English explanations
- Groups related alerts into account-level narratives
- Produces:
  - Analyst-ready explanations
  - Executive-level summaries
- AI is used **only for reasoning and summarization**, not prediction

---

### 5️⃣ Alerting & Case Management
- High-risk cases generate alerts
- Alerts are grouped into investigation cases
- Case lifecycle simulation:
  - NEW
  - UNDER_REVIEW
  - ESCALATED / CLOSED
- Human-in-the-loop analyst decision modeling

---

### 6️⃣ Compliance & Reporting
- **Technical Investigation Reports** (audit & risk teams)
- **Executive Summaries** (management-friendly)
- **AML Principle Alignment** (conceptual mapping, no regulatory claims)

This mirrors how real institutions document and justify fraud decisions.

---

## ☁️ Cloud Readiness (AWS)
The platform is **cloud-ready by design** and maps cleanly to AWS services:

- **Amazon S3** – transaction ingestion & report storage  
- **AWS Lambda / ECS Fargate** – detection, scoring, and AI reasoning  
- **Amazon DynamoDB** – alerts and case state  
- **IAM & CloudWatch** – security, logging, and auditability  

Core logic is **stateless**, enabling scalable cloud deployment.

---

## 🛠️ Tech Stack
- Python
- Pandas / NumPy
- Rule-based detection & scoring
- Modular AI explainability layer
- Git & GitHub

---

## 🧠 Design Principles
- Explainability over opaque accuracy
- Risk-based decisioning
- Human-in-the-loop controls
- Compliance-first mindset
- Cloud-native architecture

---

## ▶️ How to Run (Local)

```bash
python3 -m detection.signal_engine
