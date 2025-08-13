# DevOps Milestone Exam Preparation – Wipro June 2025

This repository is your one-stop guide to prepare for the milestone exam covering DevOps fundamentals, CI/CD, Infrastructure as Code (IaC), Site Reliability Engineering (SRE), Linux basics, Shell commands, Python basics, YAML, project setup/management, and Jira tracking/reporting.

Repository: https://github.com/syaddays/wipro_june_2025

---

## Table of Contents
- Overview of DevOps Concepts
- Importance and Benefits of DevOps
- DevOps Culture and Collaboration
- Introduction to CI/CD, IaC, and SRE
- Principles of CI/CD
- Benefits and Implementation Strategies for CI/CD
- Introduction to IaC and Benefits in DevOps
- Tools for IaC (Terraform)
- Introduction to SRE
- Key Principles and Practices of SRE
- SRE in the DevOps Lifecycle
- Introduction to Linux Operating System
- Basic Shell Commands
- Basic Python Syntax and Constructs
- Writing and Running Python Scripts
- Syntax and Structure of YAML
- Using YAML for Configuration Files
- Setting Up and Managing Projects (Git, Branching, Structure)
- Tracking and Reporting with Jira
- Study Plan, Checklist, and Sample Questions

---

## Overview of DevOps Concepts
- DevOps is a set of practices that combines software development (Dev) and IT operations (Ops).
- Goal: shorten the system development life cycle and provide continuous delivery with high software quality.
- Emphasis on automation, collaboration, measurement, and sharing.

Core pillars (CAMS):
- Culture: collaboration, feedback, blameless postmortems
- Automation: CI/CD, testing, provisioning
- Measurement: metrics, SLIs/SLOs, DORA metrics
- Sharing: knowledge, tools, standards

---

## Importance and Benefits of DevOps
- Faster time-to-market via automation and iterative delivery
- Improved reliability and quality with automated testing and monitoring
- Better collaboration across teams and reduced silos
- Scalability and repeatability using code-driven processes
- Visibility via metrics dashboards and logs

Key outcome metrics (DORA): Deployment Frequency, Lead Time for Changes, Change Failure Rate, Mean Time to Restore (MTTR)

---

## DevOps Culture and Collaboration
- Shared responsibility: Developers own quality; Ops owns reliability with dev participation
- Blameless retrospectives; focus on learning and systems improvement
- Transparent work via boards (e.g., Jira), chatops, and documentation
- Trunk-based development or short-lived branches; frequent small releases

Practices:
- Pairing/mobbing, internal demos, documentation-first mindset
- "You build it, you run it" – dev teams participate in on-call

---

## Introduction to CI/CD, IaC, and SRE
- CI (Continuous Integration): Merge code frequently, run automated builds/tests
- CD (Continuous Delivery/Deployment): Automate release process; deploy to production safely
- IaC: Manage infrastructure with code (e.g., Terraform); idempotent, versioned, reviewable
- SRE: Engineering discipline focused on reliability using software engineering principles

---

## Principles of CI/CD
- Version control everything (code, config, infra)
- Automated builds and test suites on every commit
- Artifacts promotion through environments (dev → test → prod)
- Environment parity and reproducibility
- Feature flags for safe releases
- Observability baked into pipelines (logs, metrics)

Minimal CI pipeline stages:
1) Checkout → 2) Build → 3) Test → 4) Package → 5) Scan → 6) Deploy → 7) Verify

Example (GitHub Actions YAML – conceptual):
```yaml
name: ci
on: [push, pull_request]
jobs:
  build-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.11' }
      - run: pip install -r requirements.txt
      - run: pytest -q
```

---

## Benefits and Implementation Strategies for CI/CD
- Catch defects early; reduce integration risk
- Faster iterations and feedback
- Consistent, auditable releases

Implementation tips:
- Start with unit tests, then add integration and e2e tests
- Keep pipelines fast (<10 minutes where possible)
- Cache dependencies; run tests in parallel
- Use infrastructure as code to spin up ephemeral test environments
- Enforce policies (linting, code coverage thresholds)

---

## Introduction to IaC and Benefits in DevOps
- Treat infra like app code: versioned, code-reviewed, tested
- Idempotency and reproducibility reduce configuration drift
- Faster provisioning and teardown; supports ephemeral environments
- Improved compliance via declarative definitions and policy-as-code

---

## Tools for IaC (Terraform)
Terraform basics:
- HCL (HashiCorp Configuration Language)
- Providers (AWS, Azure, GCP, Kubernetes, etc.)
- Core workflow: `init` → `plan` → `apply` → `destroy`

Example (Terraform – AWS EC2, conceptual):
```hcl
terraform {
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 5.0" }
  }
}

provider "aws" {
  region = var.region
}

variable "region" { default = "us-east-1" }

resource "aws_instance" "web" {
  ami           = "ami-xxxxxxxx"
  instance_type = "t3.micro"
  tags = { Name = "dev-web" }
}
```

Commands:
```bash
terraform init
terraform fmt
terraform validate
terraform plan -out=tfplan
terraform apply tfplan
terraform destroy -auto-approve
```

Best practices:
- Use modules and remote state (e.g., S3 + DynamoDB lock)
- Separate workspaces/environments; least-privilege IAM
- Review plans; tag resources; manage secrets securely

---

## Introduction to SRE
- SRE blends ops with software engineering to achieve reliable, scalable services
- Key constructs: SLIs, SLOs, error budgets; incident response; toil reduction

---

## Key Principles and Practices of SRE
- SLIs (Service Level Indicators): measurements (latency, availability, error rate)
- SLOs (Service Level Objectives): targets for SLIs (e.g., 99.9% availability)
- Error Budgets: allowed unreliability over period; governs release velocity
- Toil Reduction: automate manual, repetitive tasks
- Incident Management: detection, mitigation, postmortems
- Capacity Planning and Load Management
- Reliability-oriented design: graceful degradation, circuit breakers, retries with backoff

Example SLI/SLO definitions:
- Availability SLI: successful requests / total requests
- SLO: 99.9% over 30 days; alert at 2% budget burn per hour

---

## SRE in the DevOps Lifecycle
- Plan: reliability requirements via SLOs
- Build: resilience patterns, fault injection tests
- Ship: progressive delivery (canary, blue/green), automated rollbacks
- Run: monitoring (metrics/logs/traces), alerting on symptoms, not causes
- Learn: blameless postmortems, action items tracked in backlog

Tooling examples:
- Monitoring: Prometheus, Grafana
- Tracing: OpenTelemetry, Jaeger
- Incident Mgmt: PagerDuty, Opsgenie

---

## Introduction to Linux Operating System
- Everything is a file; hierarchical filesystem
- Common directories: `/etc` configs, `/var/log` logs, `/home` users, `/usr/bin` binaries
- Permissions: user/group/other; rwx bits; `chmod`, `chown`
- Package managers: `apt`, `yum/dnf`, `zypper`
- Services: `systemd` with `systemctl`

---

## Basic Shell Commands
Navigation and files:
```bash
pwd
ls -al
cd /path/to/dir
cat file.txt
less file.txt
head -n 20 file.txt
tail -f /var/log/syslog
cp src dst
mv old new
rm -rf dir
mkdir -p /tmp/demo
```

Search and filters:
```bash
grep -R "pattern" ./
find . -type f -name "*.py"
awk '{ print $1 }' file.txt
sed -n '1,10p' file.txt
sort file.txt | uniq -c | sort -nr
```

Networking and downloads:
```bash
curl -I https://example.com
wget https://example.com/file.tar.gz
ss -tulpn
ping -c 4 8.8.8.8
```

Processes and services:
```bash
top
ps aux | grep python
systemctl status nginx
journalctl -u nginx --since "2 hours ago"
```

Permissions and users:
```bash
chmod 640 file
chown user:group file
useradd -m devuser && passwd devuser
```

Compression and archives:
```bash
tar -czf archive.tgz dir/
tar -xzf archive.tgz
zip -r archive.zip dir/
unzip archive.zip
```

SSH and file transfer:
```bash
ssh user@host
scp file user@host:/path/
```

---

## Basic Python Syntax and Constructs
Data types: `int`, `float`, `str`, `bool`, `list`, `tuple`, `dict`, `set`

Control flow:
```python
x = 10
if x > 5:
    print("big")
elif x == 5:
    print("equal")
else:
    print("small")

for i in range(3):
    print(i)

while x > 0:
    x -= 1
```

Functions and modules:
```python
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(2, 3))
```

Virtual environments and dependencies:
```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell
. .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip freeze > requirements.txt
```

---

## Writing and Running Python Scripts
- Place scripts under `src/` or a clear directory
- Use `if __name__ == "__main__":` guard for entry points
- Add `argparse` for CLI parameters
- Testing with `pytest`

Run:
```bash
python script.py
python -m package.module
pytest -q
```

---

## Syntax and Structure of YAML
- YAML is indentation-sensitive, uses key-value pairs, lists, and scalars
- Indentation with spaces only; consistent levels
- Use `---` to separate documents; `#` for comments

Examples:
```yaml
# Scalars and mappings
app: demo
replicas: 3
enabled: true

# Lists
regions:
  - us-east-1
  - eu-west-1
```

Common pitfalls:
- Tabs are not allowed; only spaces
- Be consistent with indentation
- Quote strings that contain special characters (`:`, `-`, `#`)

---

## Using YAML for Configuration Files
Kubernetes Deployment (minimal):
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 2
  selector:
    matchLabels: { app: web }
  template:
    metadata:
      labels: { app: web }
    spec:
      containers:
        - name: web
          image: nginx:1.25
          ports:
            - containerPort: 80
```

GitHub Actions (CI workflow):
```yaml
name: ci
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo "Hello CI"
```

Ansible Playbook (simple):
```yaml
- hosts: all
  become: true
  tasks:
    - name: Ensure Nginx
      apt:
        name: nginx
        state: present
        update_cache: true
```

---

## Setting Up and Managing Projects (Git, Branching, Structure)
Repository hygiene:
- Use `README.md`, `LICENSE`, `.gitignore`, `CONTRIBUTING.md`
- Keep a clear directory structure (e.g., `src/`, `infra/`, `docs/`, `tests/`)
- Use semantic versioning where applicable

Git quickstart:
```bash
git init
git remote add origin <repo-url>
git checkout -b main

git add .
git commit -m "Initial commit"

git push -u origin main
```

Branching and PRs:
- Keep branches small and focused; name by purpose (e.g., `feat/`, `fix/`, `docs/`)
- Protect `main` with required reviews and status checks
- Use conventional commits for clarity

Commit messages:
- Format: `<type>(scope): <short summary>`
- Types: feat, fix, docs, style, refactor, perf, test, chore

Code reviews:
- Be kind, specific, and actionable; review for correctness, readability, and tests

---

## Tracking and Reporting with Jira
Key elements:
- Issue types: Epic, Story, Task, Bug, Sub-task
- Workflow states: To Do → In Progress → In Review → Done
- Boards: Scrum (sprints) or Kanban (continuous)
- Estimation: Story points or time-based; Definition of Done

JQL basics:
```text
project = DEV AND status != Done ORDER BY priority DESC
assignee = currentUser() AND sprint in openSprints()
```

Reporting and visibility:
- Burndown and velocity (Scrum)
- Cumulative flow diagram (Kanban)
- Release and epic reports

Best practices:
- Keep issues small and INVEST (Independent, Negotiable, Valuable, Estimable, Small, Testable)
- Link commits/PRs to issues; update status promptly
- Capture acceptance criteria and Definition of Done

---

## Study Plan, Checklist, and Sample Questions
7-day quick plan (adjust as needed):
- Day 1: DevOps overview, culture; DORA metrics
- Day 2: CI/CD principles; hands-on with a simple pipeline
- Day 3: IaC with Terraform basics; `init/plan/apply/destroy`
- Day 4: SRE fundamentals; define SLIs/SLOs and error budgets
- Day 5: Linux + Shell commands; practice file, process, and service management
- Day 6: Python + YAML exercises; write a small script and a CI YAML
- Day 7: Review + mock questions; summarize notes

Checklist:
- Understand CI vs CD; pipeline stages
- Be able to explain IaC benefits and Terraform workflow
- Define SLIs/SLOs; explain error budgets and incident process
- Comfortable with Linux navigation, permissions, networking basics
- Write simple Python scripts and read/write YAML
- Know Git basics: clone, branch, commit, PR, merge
- Use Jira boards, write good tickets, basic JQL

Sample questions:
1) Define DevOps and explain the CAMS model.
2) Differentiate Continuous Delivery vs Continuous Deployment.
3) What are SLIs, SLOs, and error budgets? Provide an example.
4) Explain how Terraform ensures idempotency and state management.
5) Show commands to find all `.py` files modified in the last day.
6) Write a small Python function and explain how to run it in a virtualenv.
7) Given a YAML snippet, identify indentation errors and fix them.
8) Describe a branching strategy for a small team and PR best practices.
9) How do you handle incidents and postmortems in SRE?
10) Write a basic JQL to list your open high-priority issues.

---

Good luck on your milestone exam! Strengthen your understanding by building a tiny project that uses a CI pipeline, provisions a small resource with Terraform, defines SLOs, and documents everything in this repository. 