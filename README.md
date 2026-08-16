#  SenseLab

### Web Application Security Assessment & Penetration Testing Training Laboratory

> **Think like an attacker. Build like an engineer. Defend like a security professional.**

**SenseLab** is a controlled, scenario-driven cybersecurity laboratory built with Python and Streamlit to demonstrate practical security-assessment methodology across reconnaissance, attack-surface analysis, HTTP and API analysis, vulnerability identification, risk assessment, remediation and retesting.

The project was developed as an independent technical portfolio project to strengthen practical application-security and penetration-testing skills while combining an existing background in **software engineering, DevOps, IT operations and application development** with offensive-security learning.

---

##  Why SenseLab?

Learning cybersecurity concepts is different from learning how to apply them.

SenseLab turns security concepts into an interactive assessment workflow where the learner must:

**Investigate → Analyse → Identify → Assess → Remediate → Retest**

Instead of simply answering cybersecurity questions, users work through controlled security scenarios and make decisions based on simulated technical evidence.

---

##  Authorized-Lab Notice

SenseLab is designed exclusively for **authorized cybersecurity education and controlled security testing**.

All targets and environments used by the application are simulated, fictional or intentionally provided as laboratory scenarios.

SenseLab does **not** provide unrestricted functionality for scanning or attacking arbitrary external systems.

> Never use security-testing techniques against systems, networks, applications or accounts without explicit authorization.

---

#  Core Capabilities

###  Reconnaissance

Explore simulated target information and identify:

* IP addresses
* domains
* services
* technologies
* application components
* potential attack surfaces

### Network & DNS Analysis

Work with controlled examples involving:

* RFC1918 private IPv4 addressing
* A records
* CNAME records
* TXT records
* MX records
* NS records
* simulated infrastructure relationships

### HTTP Analysis

Analyse simulated HTTP requests and responses.

Investigate:

* HTTP methods
* status codes
* headers
* cookies
* parameters
* content types
* application behaviour
* information disclosure

###  API Security

Investigate simulated REST APIs and identify security issues involving:

* authorization
* object access
* resource ownership
* excessive data exposure
* input handling
* API configuration

###  Vulnerability Laboratory

Controlled scenarios cover concepts such as:

* Broken Access Control
* Authentication weaknesses
* Input-validation weaknesses
* Cross-site scripting concepts
* SQL-injection concepts
* Information disclosure
* Insecure configuration
* API security weaknesses

###  Risk Assessment

Evaluate findings using:

* likelihood
* impact
* exploitability

SenseLab calculates an educational **SenseLab Risk Score** and explains how the score was produced.

###  Remediation

For each finding, users determine an appropriate remediation strategy and understand why the selected control addresses the underlying security problem.

###  Retesting

Security findings do not end at discovery.

SenseLab simulates the complete cycle:

**Finding → Remediation → Retest → Resolution**

### 📄 Security Reporting

Generate a structured security-assessment report containing:

* Executive Summary
* Scope
* Methodology
* Attack Surface
* Findings
* Evidence
* Impact
* Severity
* Recommendations
* Retesting Results

---

#  Assessment Methodology

SenseLab follows a simplified security-assessment lifecycle:

```text
┌──────────────┐
│    Scope     │
└──────┬───────┘
       ↓
┌──────────────┐
│Reconnaissance│
└──────┬───────┘
       ↓
┌──────────────┐
│Attack Surface│
│   Mapping    │
└──────┬───────┘
       ↓
┌──────────────┐
│HTTP / API    │
│   Analysis   │
└──────┬───────┘
       ↓
┌──────────────┐
│ Vulnerability│
│ Identification│
└──────┬───────┘
       ↓
┌──────────────┐
│Risk Assessment│
└──────┬───────┘
       ↓
┌──────────────┐
│ Remediation  │
└──────┬───────┘
       ↓
┌──────────────┐
│    Retest    │
└──────┬───────┘
       ↓
┌──────────────┐
│Security Report│
└──────────────┘
```

---

# Example Security Scenario

A controlled API scenario may expose:

```http
GET /api/users/1002 HTTP/1.1
Host: research.lab
Cookie: session=LAB_SESSION
```

The simulated application returns information belonging to another user.

The learner must determine:

1. What happened?
2. What security property was violated?
3. What evidence supports the finding?
4. What is the potential impact?
5. How should the application be remediated?
6. How should the remediation be retested?

This encourages security reasoning rather than memorisation.

---

# Attack-Surface Model

SenseLab represents application components as interconnected attack surfaces:

```text
                 ┌─────────────────┐
                 │ Web Application │
                 └────────┬────────┘
                          │
          ┌───────────────┼────────────────┐
          ↓               ↓                ↓
   Authentication        API          Admin Interface
          │               │                │
          ↓               ↓                ↓
       Sessions       Database         User Data
```

Each component can be investigated within the controlled scenario.

---

#  Risk Assessment

SenseLab uses an educational risk model based on:

```text
Likelihood
Impact
Exploitability
```

Example:

```text
Likelihood       4 / 5
Impact           5 / 5
Exploitability   4 / 5

SenseLab Risk Score
80 / 100

Risk Level
CRITICAL
```

The score is a **project-specific educational model** and is not presented as an official industry-standard rating.

---

#  Training Mode

Training Mode provides progressive hints.

Example:

```text
Hint 1:
Look closely at the resource identifier.

Hint 2:
Ask whether the server verifies ownership.

Hint 3:
Consider authorization rather than authentication.
```

The objective is to develop the reasoning process required to investigate security weaknesses.

---

#  Assessment Mode

Assessment Mode removes progressive hints and evaluates the user's ability to independently:

* investigate evidence
* identify vulnerabilities
* classify findings
* assess risk
* recommend remediation
* complete retesting

The assessment produces a score out of 100.

---

#  Architecture

```text
                    Streamlit UI
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
      Scenarios       Assessment      Reporting
          │              │              │
          ↓              ↓              ↓
     Scenario Engine  Scoring Engine  Report Engine
          │              │              │
          └──────────────┼──────────────┘
                         ↓
                 Security Findings
                         │
                         ↓
                 Remediation Engine
                         │
                         ↓
                    Retesting
```

---

#  Repository Structure

```text
senselab/
│
├── app.py
│
├── pages/
│   ├── 01_Dashboard.py
│   ├── 02_Scenario.py
│   ├── 03_Reconnaissance.py
│   ├── 04_Network_DNS.py
│   ├── 05_HTTP_Analysis.py
│   ├── 06_API_Security.py
│   ├── 07_Vulnerability_Lab.py
│   ├── 08_Risk_Assessment.py
│   ├── 09_Remediation.py
│   ├── 10_Retesting.py
│   └── 11_Security_Report.py
│
├── engine/
│   ├── scenarios.py
│   ├── scoring.py
│   ├── risk.py
│   └── reporting.py
│
├── scenarios/
│   ├── access_control.json
│   ├── api_security.json
│   ├── information_disclosure.json
│   ├── authentication.json
│   └── configuration.json
│
├── tests/
│   ├── test_network.py
│   ├── test_risk.py
│   ├── test_scoring.py
│   ├── test_scenarios.py
│   └── test_reporting.py
│
├── docs/
│   ├── methodology.md
│   ├── security-model.md
│   └── scenarios.md
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── .devcontainer/
│   └── devcontainer.json
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .gitignore
├── .env.example
├── SECURITY.md
├── LICENSE
└── README.md
```

---

# 🛠️ Technology Stack

| Technology     | Purpose                        |
| -------------- | ------------------------------ |
| Python         | Application and security logic |
| Streamlit      | Interactive web interface      |
| Pandas         | Structured data handling       |
| NumPy          | Numerical calculations         |
| Plotly         | Interactive visualisations     |
| Pytest         | Automated testing              |
| Docker         | Reproducible deployment        |
| Git/GitHub     | Version control                |
| GitHub Actions | CI/testing                     |

---

# Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/senselab.git
cd senselab
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

#  Docker

Build:

```bash
docker build -t senselab .
```

Run:

```bash
docker run -p 8501:8501 senselab
```

Then open:

```text
http://localhost:8501
```

---

# 🧪 Testing

Run the automated test suite:

```bash
pytest
```

The tests cover core application functionality including:

* network classification
* risk calculations
* scoring
* scenario loading
* reporting
* remediation states

---

# 🔐 Security Engineering Principles

SenseLab itself is developed with security-aware engineering principles.

The project aims to demonstrate:

* input validation
* safe configuration
* dependency management
* secrets management
* error handling
* testing
* security-focused documentation
* controlled security scenarios

No credentials or API keys should be committed to the repository.

---

# Repository Security

For the public GitHub repository, enable GitHub security controls including:

* Dependabot alerts
* Secret scanning
* Push protection
* Code scanning

GitHub specifically recommends these controls for public repositories.

A `SECURITY.md` file is also included to document responsible vulnerability reporting.

---

#  Project Objectives

SenseLab was built to develop practical understanding of:

### Application Security

Understanding how application architecture, input handling, authentication, authorization and APIs contribute to security.

### Offensive-Security Thinking

Learning to investigate systems from an attacker's perspective within controlled and authorized environments.

### Defensive Engineering

Understanding how vulnerabilities can be remediated and validated through retesting.

### DevSecOps

Integrating security thinking into the software-development and deployment lifecycle.

### Technical Reporting

Translating technical observations into structured security findings and remediation recommendations.

---

# 👨‍💻 Author

**Gift Makoloi**

**Software Engineer | DevOps Engineer | AI Product Manager**

South Africa

Email: `giftmakoloi@gmail.com`

---

# 📌 Portfolio Context

SenseLab forms part of a broader technical portfolio spanning:

* Software Engineering
* DevOps
* IT Operations
* Data Engineering
* Quantitative Modelling
* Artificial Intelligence
* Application Development
* Cybersecurity

The project represents a deliberate transition from **building and operating software systems toward understanding how those systems can be assessed and secured from an offensive-security perspective.**

---

# 🚀 Future Development

Planned improvements include:

* additional controlled web-security scenarios
* expanded API-security scenarios
* authentication and session-management laboratories
* improved threat modelling
* security-header analysis
* dependency-security demonstrations
* expanded automated testing
* richer assessment reporting
* additional DevSecOps workflows
* expanded scenario scoring

---

# ⚖️ Responsible Use

SenseLab is intended for education, research and authorized security testing.

The author does not encourage unauthorized access, scanning, exploitation or disruption of systems.

Only use security techniques against systems for which you have explicit permission to test.

---

## Project Status

**Active Development**

SenseLab is an independent technical portfolio project and educational security laboratory.
