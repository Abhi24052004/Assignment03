# QualityMS — SDLC Quality Management System

A full-stack web application for managing software development lifecycle quality. Track audits, non-conformances, corrective actions, documents, and quality gates across every SDLC phase — ensuring projects meet quality standards before advancing.

---

## Table of Contents

1. [System Overview](#system-overview)
2. [User Roles & Responsibilities](#user-roles--responsibilities)
3. [Core Workflows](#core-workflows)
4. [Entity Lifecycle Diagrams](#entity-lifecycle-diagrams)
5. [SDLC Phases & Quality Gates](#sdlc-phases--quality-gates)
6. [Notifications & Audit Trail](#notifications--audit-trail)
7. [Dashboard & Reports](#dashboard--reports)
8. [Quick Reference — Who Can Do What](#quick-reference--who-can-do-what)
9. [Getting Started](#getting-started)
10. [Sample Users](#sample-users)

---

## System Overview

QualityMS manages the **quality assurance lifecycle** across 6 SDLC phases:

```
Requirement → Design → Development → Testing → Deployment → Maintenance
```

At each phase, the system tracks:

| Entity | Purpose |
|---|---|
| **Audits** | Formal reviews of phase deliverables (pass/fail with score) |
| **Non-Conformances (NCs)** | Issues found during audits or testing (Minor/Major/Critical) |
| **CAPAs** | Corrective & Preventive Actions to fix the root cause of NCs |
| **Documents** | Phase deliverables (requirements, designs, test cases, manuals) |
| **Quality Gates** | Mandatory checkpoints before advancing to the next phase |

Everything is **project-scoped** — users first select a project, then manage its quality data.

---

## User Roles & Responsibilities

### 1. Admin
**Purpose:** System administrator — manages users and has full access.

| Duty | Details |
|---|---|
| User Management | Create, edit, activate, suspend, and assign roles to all users |
| System Oversight | View all projects, audits, NCs, CAPAs, documents |
| Audit Logs | Review the complete system audit trail (who did what, when) |
| Initial Setup | Seed projects, configure quality gates, manage SDLC phases |

> The Admin does not typically create audits or NCs — they ensure the right people are in place.

---

### 2. Project Manager
**Purpose:** Owns one or more projects — responsible for delivery, team, and phase progression.

| Duty | Details |
|---|---|
| Create Projects | Define project code, name, description, dates, and assign themselves or others as manager |
| Manage Team | Add/remove team members and assign project roles (Lead Dev, QA Lead, etc.) |
| Track Progress | Monitor dashboard — audit pass rates, open NCs, CAPA status per project |
| Advance Phases | Request phase advancement after quality gates are met (no open Critical/Major NCs) |
| Update Phase Gates | Mark phase gates as passed/pending/blocked/in-progress |
| Assign Work | Assign NCs to developers, request CAPAs, schedule audit dates |
| Review Reports | Analyze NC trends, audit compliance rates, CAPA effectiveness across their projects |

**Key Metric Watched:** Quality Rating (0-5 scale, auto-calculated from audit scores, NC penalties, CAPA effectiveness)

---

### 3. Auditor
**Purpose:** Conducts formal audits of SDLC phase deliverables.

| Duty | Details |
|---|---|
| Conduct Audits | Execute audits assigned to them — review deliverables against the checklist |
| Build Checklists | Create checklist items for each audit (e.g., "Code review completed", "Unit tests pass") |
| Score Audits | Mark each checklist item as Pass/Fail/Partial/Not Applicable |
| Record Findings | Document findings with type (Conformance, Non-Conformance, Observation, Improvement) and severity |
| Complete Audits | Set final result (Pass/Fail/Partial), overall score (0-100), and findings summary |
| Raise NCs | When findings reveal non-conformances, create NC records linked to the audit |

**Audit Workflow:**
1. Receive notification of assigned audit
2. Review phase deliverables against checklist
3. Score each checklist item
4. Record findings
5. Set overall result and score
6. Complete the audit → triggers quality gate evaluation

---

### 4. Quality Manager
**Purpose:** Oversees the entire quality program — monitors trends, verifies CAPAs, approves phase gates.

| Duty | Details |
|---|---|
| Monitor All Projects | Global dashboard — active projects, open NCs, CAPA progress, overdue items |
| Critical NC Alerts | Automatically notified when any Critical NC is created across any project |
| Verify CAPAs | Review corrective/preventive actions, rate effectiveness (1-5), approve or return to In Progress |
| Approve Quality Gates | Authorize phase advancement by confirming gate criteria are met |
| NC Trend Analysis | Track NC creation rate by severity and month — identify systemic issues |
| CAPA Effectiveness Review | Monitor whether closed CAPAs actually prevented recurrence |
| Audit Compliance | Review audit pass rates per project and per phase — flag low-compliance areas |
| Generate Reports | Export audit, NC, CAPA, and document analytics as CSV |

**Key Decision:** Whether a CAPA is truly "Effective" — this directly impacts whether linked NCs can be closed and phases can advance.

---

### 5. QA (Quality Assurance)
**Purpose:** Tests deliverables, reports issues, and validates that fixes are correct.

| Duty | Details |
|---|---|
| Report NCs | Create non-conformance records when defects or deviations are found |
| Investigate NCs | Document root cause analysis and impact assessment for opened NCs |
| Validate Fixes | After corrective actions are implemented, verify the fix resolves the issue |
| Execute Checklists | Support audits by providing testing evidence and test results |
| Track NC Status | Monitor their assigned NCs through the full lifecycle (Open → Investigation → Closed) |
| Document Test Cases | Upload and manage test case documents per SDLC phase |

**NC Reporting Workflow:**
1. Find a defect during testing or review
2. Create NC with: title, description, severity, SDLC phase, optional audit link
3. Assign to the responsible Developer
4. Track progress until resolution
5. Validate fix and confirm closure

---

### 6. Developer
**Purpose:** Builds deliverables and resolves non-conformances.

| Duty | Details |
|---|---|
| Resolve Assigned NCs | Receive NC assignments, investigate root cause, implement fixes |
| Update NC Status | Move NCs through workflow: Open → Under Investigation → In Progress |
| Implement CAPAs | Execute corrective and preventive action tasks assigned to them |
| Complete CAPA Tasks | Update task status (Pending → In Progress → Completed) with completion notes |
| Create Documents | Upload design docs, API docs, and other deliverables |
| Respond to Audit Findings | Provide evidence or remediation for findings raised during audits |

**Developer's NC Resolution Process:**
1. Receive notification: "NC-007: Critical — SQL injection in login API"
2. Investigate root cause → update NC with root cause analysis
3. Implement fix
4. Update NC status to "In Progress"
5. QA/Auditor validates and closes

---

### 7. Management
**Purpose:** Executive oversight — views dashboards and reports without day-to-day operations.

| Duty | Details |
|---|---|
| Executive Dashboard | View high-level metrics across all projects |
| Quality Ratings | Monitor project quality ratings (0-5 scale) |
| Compliance Overview | Review audit compliance rates and NC trends |
| Resource Utilization | See which team members are assigned to which projects |
| Risk Assessment | Identify projects with high critical NC counts or overdue CAPAs |
| Report Export | Export dashboards and reports for management reviews |

> Management has read-only operational access — they can view everything but typically don't create or modify records.

---

## Core Workflows

### Workflow 1: Audit Lifecycle

```
                    +-----------+
                    | Scheduled |
                    +-----+-----+
                          |
                  Auditor starts
                          |
                  +-------v-------+
                  |  In Progress  |
                  +-------+-------+
                          |
              Checklist items scored
              Findings recorded
                          |
                  +-------v-------+         +----------+
                  |   Completed   |  or     | Cancelled|
                  +-------+-------+         +----------+
                          |
              Result: Pass / Fail / Partial
              Score: 0-100
                          |
              If Fail → Create NCs from findings
```

**Who does what:**
- **Project Manager** schedules the audit (creates record, assigns auditor, sets date)
- **Auditor** receives notification → conducts audit → scores checklist → records findings → completes
- **Quality Manager** reviews results → validates findings → confirms quality impact
- **System** auto-generates audit number (AUD-001, AUD-002, ...)

---

### Workflow 2: Non-Conformance (NC) Lifecycle

```
     +------+
     | Open |  ← QA/Auditor reports issue
     +--+---+
        |
        v
+-------+----------+
| Under Investigation| ← Developer/QA investigates root cause
+-------+----------+
        |
        v
  +-----+------+
  | In Progress | ← Fix being implemented
  +-----+------+
        |
        v
  +-----+------+     +----------+
  |  Verified  | --> |  Closed  |  ← All linked CAPAs must be Closed/Verified first
  +-----+------+     +----------+
        |
        v (if needed)
  +-----+------+
  |  Reopened  |  ← Fix was inadequate
  +------------+
```

**Severity levels and their impact:**
| Severity | Impact on Quality Gate | Example |
|---|---|---|
| **Critical** | BLOCKS phase advancement until closed | Security vulnerability, data loss |
| **Major** | BLOCKS phase advancement until closed | Functional defect, performance failure |
| **Minor** | Does NOT block phase advancement | UI issues, documentation gaps |

**Auto-numbering:** NC-001, NC-002, NC-003, ...

**Closure rule:** An NC can only be closed when ALL linked CAPAs are in Closed or Verified status. The system enforces this automatically.

---

### Workflow 3: CAPA (Corrective/Preventive Action) Lifecycle

```
     +------+
     | Open |  ← Created, linked to an NC (optional)
     +--+---+
        |
   Owner assigned and notified
        |
        v
  +-----+------+
  | In Progress | ← Corrective/Preventive actions being executed
  +-----+------+
        |
   Tasks completed
        |
        v
  +-----+--------+
  | Under Review  | ← Awaiting Quality Manager verification
  +-----+--------+
        |
   Quality Manager verifies
   Rates effectiveness (1-5)
        |
   +----+----+----+
   |         |    |
   v         v    v
+------+ +--------+ +-------------+
|Closed| |Verified| |Back to       |
|      | |(follow | | In Progress  |
|      | | up req)| |(Ineffective) |
+------+ +--------+ +-------------+
```

**Two types of CAPA:**
| Type | Purpose | Example |
|---|---|---|
| **Corrective** | Fix the immediate problem | "Patch SQL injection vulnerability" |
| **Preventive** | Prevent recurrence | "Add parameterized query linting rule to CI pipeline" |

**CAPA Tasks:** Each CAPA can have multiple sub-tasks assigned to different team members:
- Task: "Update ORM queries" → assigned to Dev1 → due March 15
- Task: "Add SQL injection tests" → assigned to QA1 → due March 18
- Task: "Update coding standards doc" → assigned to Dev2 → due March 20

**Effectiveness scoring (by Quality Manager):**
| Score | Meaning |
|---|---|
| 5 | Highly effective — issue fully resolved, no recurrence |
| 4 | Effective — issue resolved with minor follow-up |
| 3 | Partially effective — some improvement, needs more work |
| 2 | Minimally effective — problem persists |
| 1 | Ineffective — no improvement, CAPA returned |

**Auto-numbering:** CAPA-001, CAPA-002, CAPA-003, ...

---

### Workflow 4: Document Approval Lifecycle

```
     +-------+
     | Draft |  ← Author creates and uploads
     +---+---+
         |
    Submit for review
         |
         v
  +------+-------+
  | Under Review  |  ← Approvers review in sequence
  +------+-------+
         |
    +----+----+
    |         |
    v         v
+--------+  +------+
|Approved|  |Reject| → Returns to Draft
+--------+  +------+
    |
  (Later)
    v
+--------+
|Obsolete|  ← Superseded by newer version
+--------+
```

**Document types:**
- Requirement (SRS, BRS)
- Design (HLD, LLD, architecture diagrams)
- Test Case (test plans, test scripts)
- User Manual (end-user documentation)
- API Doc (API specifications)
- Other

**Version management:** Each document tracks version history with change descriptions. New versions can be uploaded while preserving the complete history.

**Approval chain:** When submitted for review, one or more approvers are assigned. ALL must approve for the document to be approved. If ANY rejects, the document returns to Draft.

**Auto-numbering:** DOC-001, DOC-002, DOC-003, ...

---

### Workflow 5: Phase Advancement (Quality Gate)

```
Project: Patient Portal
Current Phase: Development

Quality Gate Check:
  ✅ Phase status = "In Progress" or "Completed"
  ✅ No open Critical NCs in Development phase
  ✅ No open Major NCs in Development phase
  ❌ Open Minor NC-005 exists (does NOT block)
  ✅ At least 1 completed audit exists for this phase

Result: GATE PASSED → Advance to Testing
  - Development phase → Completed (100%)
  - Testing phase → In Progress (start_date = today)
  - project.current_phase updated

If last phase (Maintenance) completed:
  → Project status = "Completed"
  → actual_end_date = today
```

**Who approves phase advancement:**
1. **Project Manager** requests advancement
2. **System** automatically checks: open Critical/Major NCs
3. If no blockers → auto-passes the gate
4. If blockers exist → returns error message listing blocking NCs
5. **Quality Manager** can manually approve/override gate status

---

## Entity Lifecycle Diagrams

### The Audit → NC → CAPA Chain

This is the core quality workflow — how a defect is found, tracked, and resolved:

```
STEP 1: AUDIT
  Auditor reviews Development phase deliverables
  Finds: "No input validation on user registration API"
  Creates: AUD-005 (result: Fail, score: 45)
       |
       v
STEP 2: NON-CONFORMANCE
  Auditor creates NC from finding:
  NC-012: "Missing input validation — SQL injection risk"
  Severity: Critical    Phase: Development
  Assigned to: Dev Kumar (Developer)
       |
       v
STEP 3: INVESTIGATION
  Dev Kumar investigates:
  Root cause: "ORM bypass — raw SQL used for custom queries"
  Impact: "All 14 custom query endpoints affected"
       |
       v
STEP 4: CAPA CREATION
  CAPA-008: "Remediate SQL injection and prevent recurrence"
  Type: Corrective + Preventive
  Corrective: "Replace all raw SQL with parameterized queries"
  Preventive: "Add SQLi detection to CI pipeline"
  Owner: Dev Kumar    Due: March 15
       |
       v
STEP 5: CAPA TASKS
  Task 1: "Refactor all 14 endpoints" → Dev Kumar → Mar 12
  Task 2: "Add SQLi unit tests" → QA Qazi → Mar 13
  Task 3: "Configure CI rule" → Dev Anita → Mar 14
       |
       v
STEP 6: VERIFICATION
  Quality Manager Nina reviews:
  - All 14 endpoints refactored ✅
  - 28 new test cases pass ✅
  - CI blocks raw SQL ✅
  Effectiveness: 5/5
  → CAPA-008 Closed
       |
       v
STEP 7: NC CLOSURE
  System check: All CAPAs for NC-012 are Closed ✅
  → NC-012 Closed
       |
       v
STEP 8: PHASE CAN ADVANCE
  No more open Critical/Major NCs in Development
  → Quality gate passes → Project advances to Testing
```

---

## SDLC Phases & Quality Gates

### The 6 Phases

| # | Phase | Requires Audit | Quality Gate | Typical Deliverables |
|---|---|---|---|---|
| 1 | **Requirement** | Yes | Yes | SRS, BRS, requirement traceability matrix |
| 2 | **Design** | Yes | Yes | HLD, LLD, architecture diagrams, DB schema |
| 3 | **Development** | No* | Yes | Source code, code review reports, unit tests |
| 4 | **Testing** | Yes | Yes | Test plans, test cases, test results, defect reports |
| 5 | **Deployment** | Yes | Yes | Release notes, deployment guide, UAT sign-off |
| 6 | **Maintenance** | No* | No | Change requests, maintenance logs |

*Audits can still be scheduled for any phase — "No" means not mandatory.

### Quality Gate Criteria Per Phase

Each phase has configurable gate criteria. Example for **Development** phase:

| Criterion | Type | Required Value |
|---|---|---|
| Code review completed | Review | All critical modules reviewed |
| Unit test coverage | Test | ≥ 80% |
| No Critical NCs open | Audit | 0 Critical NCs |
| Security scan passed | Test | No high/critical vulnerabilities |
| Design documents approved | Document | All Approved status |

### Phase Status Values

| Status | Meaning |
|---|---|
| **Not Started** | Phase hasn't begun |
| **In Progress** | Active work happening |
| **Completed** | All deliverables done, gate passed |
| **Blocked** | Cannot proceed (e.g., dependency, resource issue) |

---

## Notifications & Audit Trail

### Automatic Notifications

The system creates notifications automatically:

| Trigger | Who Receives | Message |
|---|---|---|
| Audit created | Assigned Auditor | "You have been assigned audit AUD-005" |
| NC created | Assigned Developer/QA | "You have been assigned NC-012: Missing input validation" |
| Critical NC created | ALL Quality Managers | "Critical NC Alert: NC-012 — Missing input validation" |
| CAPA created | Assigned Owner | "CAPA Assigned: CAPA-008 — Remediate SQL injection" |
| Team member added | New member | "You have been added to project Patient Portal" |

### Audit Log (System-wide)

Every action is logged in the `audit_logs` table:

| Field | Example |
|---|---|
| User | Dev Kumar |
| Action | CREATE, UPDATE, CLOSE, VERIFY, PHASE_ADVANCE, APPROVE |
| Entity Type | project, audit, non_conformance, capa, document |
| Entity ID | UUID of the record |
| Old/New Values | JSON showing what changed |
| Timestamp | 2026-03-07 10:15:32 |

This is a permanent, tamper-evident record of all changes — critical for compliance and regulatory audits.

---

## Dashboard & Reports

### Project Dashboard (per-project view)

| Metric | Description |
|---|---|
| Total Documents | Count of all documents in the project |
| Completed Audits | Audits with result recorded |
| Pending Audits | Scheduled or in-progress audits |
| Open NCs | NCs not yet Closed/Verified |
| Critical NCs | Open NCs with Critical severity |
| Open CAPAs | CAPAs not yet Closed/Verified |
| Phase Progress | Pipeline showing status + completion % of each phase |

### Global Dashboard (all projects)

| Metric | Description |
|---|---|
| Active Projects | Projects with status = Active |
| Active Audits | Audits currently In Progress |
| Open NCs | Total across all projects |
| CAPAs In Progress | Total across all projects |
| NCs Closed (30 days) | Recently resolved issues |
| Overdue Items | NCs and CAPAs past their due date |

### Charts

1. **NC Trend** — Line chart showing NCs created per month by severity (last 12 months)
2. **Audit Compliance** — Bar chart showing pass rate per project
3. **CAPA Effectiveness** — Trend of effective vs total CAPAs per month
4. **NC Severity Distribution** — Pie/bar chart of Critical/Major/Minor breakdown
5. **CAPA Status Distribution** — Pie chart of Open/In Progress/Closed

### Reports & Export

Filter by project, phase, date range, severity, or status. Export as CSV for:
- Audit reports
- NC reports
- CAPA reports
- Document reports

---

## Quick Reference — Who Can Do What

| Action | Admin | PM | Auditor | QM | QA | Dev | Mgmt |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Projects** |||||||
| View all projects | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Create project | ✅ | ✅ | | | | | |
| Edit project | ✅ | ✅ | | | | | |
| Manage team | ✅ | ✅ | | | | | |
| Advance phase | ✅ | ✅ | | ✅ | | | |
| Update phase gates | ✅ | ✅ | | ✅ | | | |
| **Audits** |||||||
| View audits | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Schedule audit | ✅ | ✅ | ✅ | ✅ | | | |
| Conduct audit | | | ✅ | ✅ | | | |
| Complete audit | | | ✅ | ✅ | | | |
| Add findings | | | ✅ | ✅ | | | |
| **Non-Conformances** |||||||
| View NCs | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Create NC | ✅ | ✅ | ✅ | ✅ | ✅ | | |
| Update NC | ✅ | ✅ | ✅ | ✅ | ✅ | ✅* | |
| Close NC | ✅ | ✅ | | ✅ | | | |
| Add investigation | ✅ | | ✅ | ✅ | ✅ | ✅ | |
| **CAPAs** |||||||
| View CAPAs | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Create CAPA | ✅ | ✅ | ✅ | ✅ | ✅ | | |
| Update CAPA | ✅ | ✅ | | ✅ | | ✅* | |
| Verify CAPA | ✅ | | | ✅ | | | |
| Manage CAPA tasks | ✅ | ✅ | | ✅ | ✅ | ✅* | |
| **Documents** |||||||
| View documents | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Upload document | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | |
| Approve document | ✅ | ✅ | | ✅ | | | |
| **Users** |||||||
| Manage users | ✅ | | | | | | |
| View user list | ✅ | ✅ | | ✅ | | | |
| Invite users | ✅ | | | | | | |
| **System** |||||||
| View audit logs | ✅ | | | ✅ | | | |
| View notifications | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| View dashboard | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Export reports | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

*\*Dev can only update NCs/CAPAs/tasks assigned to them.*

---

## Quality Rating Formula

Each project has an auto-calculated quality rating (0.00 - 5.00):

```
Rating = (Average Audit Score / 20) - NC Penalty + CAPA Bonus

NC Penalty:
  - Each open Critical NC:  −0.50
  - Each open Major NC:     −0.20
  - Each open Minor NC:     −0.05

CAPA Bonus:
  - Average effectiveness score × 0.10

Example:
  Avg audit score = 82 → 82/20 = 4.10
  2 open Major NCs → -0.40
  CAPA avg effectiveness = 4.2 → +0.42
  Rating = 4.10 - 0.40 + 0.42 = 4.12
```

---

## Getting Started

### Prerequisites
- Node.js 18+
- MySQL 8.x (running on port 3307)
- npm

### Backend Setup
```bash
cd Backend
npm install               # express, cors, mysql2, bcrypt, jsonwebtoken, uuid, dotenv

# Initialize database
mysql -u root -P 3307 -p < db/schema.sql
mysql -u root -P 3307 -p < db/procedures.sql
mysql -u root -P 3307 -p < db/seed.sql

# Start server
node server.js            # Runs on http://localhost:5000
```

### Frontend Setup
```bash
cd ..                     # Back to QualityMS root
npm install               # react, vite, tailwindcss, shadcn/ui, recharts, etc.
npm run dev               # Runs on http://localhost:5173
```

### Verify
```bash
curl http://localhost:5000/api/health   # → { "status": "ok" }
```

---

## Sample Users

All users share the password: **`Password@123`**

| Email | Name | Role |
|---|---|---|
| admin@qualityms.com | System Admin | Admin |
| priya@qualityms.com | Priya Mehra | Project Manager |
| rahul@qualityms.com | Rahul Sharma | Project Manager |
| dev.kumar@qualityms.com | Dev Kumar | Developer |
| anita@qualityms.com | Anita Rajan | Developer |
| vijay@qualityms.com | Vijay Pillai | Developer |
| qazi@qualityms.com | Qazi Tester | QA |
| meena@qualityms.com | Meena Krishnan | QA |
| aditi@qualityms.com | Aditi Auditor | Auditor |
| suresh@qualityms.com | Suresh Nair | Auditor |
| nina@qualityms.com | Nina Quality | Quality Manager |
| mohan@qualityms.com | Mohan Director | Management |

### Sample Projects

| Code | Name | Manager | Phase | Status |
|---|---|---|---|---|
| PRJ-001 | Patient Portal | Priya Mehra | Development | Active |
| PRJ-002 | ERP Migration | Rahul Sharma | Design | Active |
| PRJ-003 | Mobile Banking App | Priya Mehra | Testing | Active |
| PRJ-004 | Inventory System | Rahul Sharma | Maintenance | Completed |

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React 18, Vite, Tailwind CSS, shadcn/ui, Recharts, React Router v6, TanStack React Query |
| Backend | Node.js, Express.js, JWT, bcrypt |
| Database | MySQL 8.x (30+ tables, 15 stored procedures, 4 views) |
| Icons | Lucide React |
| Theme | Dark/Light mode (next-themes) |

---

## Backend Architecture

### Overview

```
Backend/
├── server.js                  # Express app entry point (port 5000)
├── db/
│   ├── connection.js          # MySQL2 connection pool (max 20 connections)
│   ├── schema.sql             # 25 tables, 4 views, indexes
│   ├── procedures.sql         # 14 stored procedures
│   └── seed.sql               # Sample data (12 users, 4 projects)
├── middleware/
│   └── auth.js                # JWT authentication + RBAC authorization
├── rbac/
│   └── permissions.js         # 57 permissions, 7 roles, permission matrix
├── route/
│   ├── authRoutes.js          # /api/auth/*
│   ├── projectRoutes.js       # /api/projects/*
│   ├── auditRoutes.js         # /api/audits/*
│   ├── ncRoutes.js            # /api/ncs/*
│   ├── capaRoutes.js          # /api/capas/*
│   ├── documentRoutes.js      # /api/documents/*
│   ├── rbacRoutes.js          # /api/rbac/*
│   └── miscRoutes.js          # /api/* (dashboard, notifications, etc.)
├── controller/                # Request handling (7 controllers)
└── service/                   # Business logic + DB queries (8 services)
```

**Pattern:** Route → Middleware → Controller → Service → Database (MySQL pool)

### Database Connection

- **Driver:** `mysql2/promise` (async/await)
- **Host:** `localhost:3307` (configurable via `.env`)
- **Database:** `qms`
- **Pool:** max 20 connections, keep-alive enabled, multi-statement support

```
DB_HOST=localhost
DB_PORT=3307
DB_USER=root
DB_PASSWORD=
DB_NAME=qms
JWT_SECRET=qms_jwt_secret_change_in_production_2026
PORT=5000
```

---

## Authentication & Authorization

### JWT Authentication

- Token generated on login with 24h expiry
- Payload: `{ id, email, role, username }`
- Passed as `Authorization: Bearer <token>` header
- `authenticateToken` middleware validates and attaches `req.user` + `req.user.permissions[]`

### RBAC Middleware

| Middleware | Logic | Usage |
|---|---|---|
| `authenticateToken` | Validates JWT, attaches user + permission array | Every protected route |
| `requirePermission(...perms)` | **OR logic** — user needs ANY of the listed permissions | Route-level guards |
| `requireAllPermissions(...perms)` | **AND logic** — user needs ALL listed permissions | Strict combined checks |
| `authorizeRoles(...roles)` | Legacy role check — user must have one of the listed roles | Backwards compatibility |
| `hasPermission(role, perm)` | Non-middleware boolean check for controller-level logic | Conditional branching |

### Permission System

**57 granular permissions** organized into 12 groups:

| Group | Permissions | Examples |
|---|---|---|
| Project Management | 9 | `project.view_all`, `project.create`, `project.manage_team` |
| Milestones | 4 | `milestone.create`, `milestone.approve` |
| SDLC Phases | 5 | `phase.advance`, `phase.override_gate` |
| Quality Gates | 5 | `quality_gate.define`, `quality_gate.verify` |
| Document Management | 8 | `document.upload`, `document.approve`, `document.delete` |
| Audit Management | 6 | `audit.create`, `audit.complete`, `audit.add_finding` |
| NC Management | 6 | `nc.create`, `nc.close`, `nc.assign` |
| CAPA Management | 6 | `capa.create`, `capa.verify`, `capa.add_task` |
| User Management | 4 | `user.view`, `user.create`, `user.delete` |
| Reports & Dashboard | 3 | `report.view_dashboard`, `report.export` |
| Notifications | 2 | `notification.view`, `notification.manage` |
| System | 1 | `system.manage` |

### Role → Permission Summary

| Role | Total Permissions | Key Capabilities |
|---|---|---|
| **Admin** | 57 (all) | Full system access |
| **Project Manager** | 33 | Project CRUD, team, milestones, phase advance, document approve, NC create/assign |
| **Developer** | 14 | View projects, upload docs, view audits/NCs, update CAPA tasks |
| **QA** | 22 | NC create/edit/investigate, CAPA create/edit/tasks, quality gate verify |
| **Auditor** | 22 | Audit CRUD/complete, checklist/findings, NC create, report export |
| **Quality Manager** | 45 | Phase override, quality gate define/override, NC close, CAPA verify, system manage |
| **Management** | 16 | Read-only across all entities, CAPA verify, report export |

### Document Type Permissions

| Document Type | Who Can Upload | Who Can Approve |
|---|---|---|
| Requirement | PM, QM, Admin | QM, PM, Admin |
| Design | Dev, PM, Admin | QM, PM, Admin |
| Test Case | QA, Admin | QA, QM, Admin |
| API Doc | Dev, Admin | PM, QM, Admin |
| User Manual | Dev, PM, Admin | PM, QM, Admin |
| Other | PM, Dev, QA, Auditor, QM, Admin | QM, PM, Mgmt, Admin |

---

## API Routes Reference

### Authentication — `/api/auth`

| Method | Endpoint | Auth | Permission | Description |
|---|---|---|---|---|
| POST | `/login` | No | — | Authenticate with email/password. Returns JWT token + user object with permissions array |
| GET | `/login-users` | No | — | List all users (email, name, role) for login dropdown |
| GET | `/me` | Yes | — | Get current user profile with permissions |
| PUT | `/me` | Yes | — | Update own profile (first_name, last_name, department, phone) |
| GET | `/me/permissions` | Yes | — | Get current user's role, permissions list, and grouped permissions |
| GET | `/users` | Yes | `user.view` | List all users |
| GET | `/users/:id` | Yes | `user.view` | Get user by ID |
| POST | `/users` | Yes | `user.create` | Create new user (requires username, email, password, role) |
| PUT | `/users/:id` | Yes | `user.edit` | Update user (role, status, password, etc.) |
| DELETE | `/users/:id` | Yes | `user.delete` | Deactivate user (sets status to Inactive) |

**Login Response:**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIs...",
  "user": {
    "id": "uuid",
    "username": "admin",
    "email": "admin@qualityms.com",
    "first_name": "System",
    "last_name": "Admin",
    "role": "Admin",
    "status": "Active",
    "permissions": ["project.view_all", "project.create", "..."]
  }
}
```

---

### Projects — `/api/projects`

All routes require authentication.

| Method | Endpoint | Permission | Description |
|---|---|---|---|
| GET | `/` | — | List projects. Users with `project.view_all` see all projects; others see only assigned projects |
| GET | `/:id` | — | Get project details by ID |
| POST | `/` | `project.create` | Create new project. Calls `sp_create_project` which auto-creates phase tracking records and adds PM to team |
| PUT | `/:id` | `project.edit` | Update project details (name, description, dates, status) |
| DELETE | `/:id` | `project.delete` | Archive project (sets status to Archived) |
| PATCH | `/:id/status` | `project.change_status` | Change project status (Active, On Hold, Completed, Archived) |
| PATCH | `/:id/assign-manager` | `project.assign_manager` | Assign a different Project Manager |

**Team Management:**

| Method | Endpoint | Permission | Description |
|---|---|---|---|
| GET | `/:id/team` | `project.view_team` | Get all team members for a project |
| POST | `/:id/team` | `project.manage_team` | Add team member. Calls `sp_add_team_member` which sends notification to the added user |
| DELETE | `/:id/team/:userId` | `project.manage_team` | Remove team member from project |

**Milestones:**

| Method | Endpoint | Permission | Description |
|---|---|---|---|
| GET | `/:id/milestones` | `milestone.view` | List project milestones |
| POST | `/:id/milestones` | `milestone.create` | Create new milestone (name, description, target_date) |
| PUT | `/:id/milestones/:milestoneId` | `milestone.edit` | Update milestone details |
| POST | `/:id/milestones/:milestoneId/approve` | `milestone.approve` | Approve milestone completion |

**SDLC Phases:**

| Method | Endpoint | Permission | Description |
|---|---|---|---|
| GET | `/:id/phases` | — | Get all SDLC phase statuses for a project (ordered by phase_order) |
| PUT | `/:id/phase-gates` | `quality_gate.verify` OR `quality_gate.override` | Update phase gate status |
| POST | `/:id/advance-phase` | `phase.advance` | Advance to next SDLC phase. Calls `sp_advance_project_phase` which checks quality gates and open NCs |
| POST | `/:id/override-gate` | `phase.override_gate` | Override a failed quality gate (records override note) |

---

### Audits — `/api/audits`

All routes require authentication.

| Method | Endpoint | Permission | Description |
|---|---|---|---|
| GET | `/` | `audit.view` | List audits. Supports query filters: `project_id`, `status`, `auditor_id` |
| GET | `/:id` | `audit.view` | Get full audit details with project, phase, and auditor info |
| POST | `/` | `audit.create` | Create audit. Calls `sp_create_audit` which auto-generates audit number (AUD-001, AUD-002...) and notifies the assigned auditor |
| PUT | `/:id` | `audit.edit` | Update audit (status, date, auditor assignment) |
| POST | `/:id/complete` | `audit.complete` | Complete audit. Calls `sp_complete_audit` with result (Pass/Fail/Partial), score (0-100), and findings summary |

**Checklist:**

| Method | Endpoint | Permission | Description |
|---|---|---|---|
| GET | `/:id/checklist` | `audit.view` | Get checklist items for an audit |
| POST | `/:id/checklist` | `audit.add_checklist` | Add checklist item (checklist_item, expected_evidence, result, comments) |

**Findings:**

| Method | Endpoint | Permission | Description |
|---|---|---|---|
| GET | `/:id/findings` | `audit.view` | Get all findings for an audit |
| POST | `/:id/findings` | `audit.add_finding` | Add finding (type: Conformance/Non-Conformance/Observation/Improvement, severity, description) |

---

### Non-Conformances — `/api/ncs`

All routes require authentication.

| Method | Endpoint | Permission | Description |
|---|---|---|---|
| GET | `/` | `nc.view` | List NCs. Supports filters: `project_id`, `status`, `severity`, `assigned_to` |
| GET | `/:id` | `nc.view` | Get NC details with project, phase, reporter, and assignee info |
| POST | `/` | `nc.create` | Create NC. Calls `sp_create_nc` which auto-generates NC number (NC-001, NC-002...), notifies assignee, and alerts all Quality Managers if severity is Critical |
| PUT | `/:id` | `nc.edit` | Update NC (status, root_cause, impact_analysis, assigned_to) |
| POST | `/:id/close` | `nc.close` | Close NC. Calls `sp_close_nc` which **blocks closure if any linked CAPAs are still open** |
| PATCH | `/:id/assign` | `nc.assign` | Reassign NC to a different user |

**Investigations:**

| Method | Endpoint | Permission | Description |
|---|---|---|---|
| GET | `/:id/investigations` | `nc.view` | List all investigations for an NC |
| POST | `/:id/investigations` | `nc.investigate` | Add investigation (findings, recommended_actions) |

---

### CAPAs — `/api/capas`

All routes require authentication.

| Method | Endpoint | Permission | Description |
|---|---|---|---|
| GET | `/` | `capa.view` | List CAPAs. Supports filters: `nc_id`, `status`, `owner_id`, `type` |
| GET | `/:id` | `capa.view` | Get CAPA details with linked NC, owner, and verification info |
| POST | `/` | `capa.create` | Create CAPA. Calls `sp_create_capa` which auto-generates CAPA number (CAPA-001...), links to NC, and notifies assigned owner |
| PUT | `/:id` | `capa.edit` | Update CAPA (description, root_cause, corrective/preventive actions, status) |
| POST | `/:id/verify` | `capa.verify` | Verify CAPA. Calls `sp_verify_capa` which records verification, rates effectiveness (1-5), and sets status to Closed/Verified/In Progress based on result |

**Tasks:**

| Method | Endpoint | Permission | Description |
|---|---|---|---|
| GET | `/:id/tasks` | `capa.view` | List all tasks for a CAPA |
| POST | `/:id/tasks` | `capa.add_task` | Add task (task_description, assigned_to, due_date) |
| PUT | `/:id/tasks/:taskId` | `capa.update_task` | Update task (status: Pending→In Progress→Completed, completion_notes) |

**Verifications:**

| Method | Endpoint | Permission | Description |
|---|---|---|---|
| GET | `/:id/verifications` | `capa.view` | List all verification records for a CAPA |

---

### Documents — `/api/documents`

All routes require authentication.

| Method | Endpoint | Permission | Description |
|---|---|---|---|
| GET | `/` | — | List documents. Users with `document.view_all` see all; others see only own documents |
| GET | `/:id` | — | Get document details with project, phase, creator info |
| POST | `/` | `document.upload` | Create document. **Enforces document type upload permissions** — only allowed roles can upload specific document types |
| PUT | `/:id` | `document.edit_metadata` OR `document.upload` | Update document metadata |
| DELETE | `/:id` | `document.delete` | Soft-delete document (sets status to Obsolete) |

**Approval Workflow:**

| Method | Endpoint | Permission | Description |
|---|---|---|---|
| POST | `/:id/submit-review` | `document.submit_review` | Submit document for review (Draft → Under Review) |
| POST | `/:id/approve` | `document.approve` | Approve/reject document. Calls `sp_approve_document`. **Enforces document type approval permissions.** If rejected → returns to Draft. If all approvers approve → status becomes Approved |

**Versions & Downloads:**

| Method | Endpoint | Permission | Description |
|---|---|---|---|
| GET | `/:id/versions` | — | Get version history for a document |
| GET | `/:id/approvals` | — | Get approval chain status for a document |
| GET | `/:id/download` | `document.download` | Download document (returns metadata/file path) |

---

### RBAC — `/api/rbac`

All routes require authentication. These are read-only informational endpoints.

| Method | Endpoint | Permission | Description |
|---|---|---|---|
| GET | `/matrix` | — | Get complete role × permission matrix for all 7 roles |
| GET | `/roles` | — | Get all roles with permission count summary |
| GET | `/roles/:role/permissions` | — | Get all permissions for a specific role |
| GET | `/permissions` | — | List all 57 permission keys with descriptions |
| GET | `/permissions/grouped` | — | Get permissions organized by category (12 groups) |
| GET | `/check?role=X&permission=Y` | — | Check if a role has a specific permission. Returns `{ granted: true/false }` |
| GET | `/me/effective` | — | Get current user's effective permissions (includes DB-level overrides) |
| GET | `/document-types` | — | Get document type permission matrix (who can upload/approve each type) |
| GET | `/document-workflow` | — | Get 6-step document approval workflow definition |

---

### Miscellaneous — `/api`

All routes require authentication.

**SDLC Phases:**

| Method | Endpoint | Permission | Description |
|---|---|---|---|
| GET | `/sdlc-phases` | — | Get all 6 SDLC phases (Requirement → Maintenance) with order and metadata |

**Dashboard:**

| Method | Endpoint | Permission | Description |
|---|---|---|---|
| GET | `/dashboard` | `report.view_dashboard` | Global dashboard. Calls `sp_global_dashboard` returning: summary cards, NC trend (12 months), audit compliance per project, CAPA effectiveness trend, overdue items |
| GET | `/dashboard/:projectId` | `report.view_dashboard` | Project-specific dashboard. Calls `sp_project_dashboard` returning: counts (docs, audits, NCs, CAPAs), phase progress, recent audit results |

**Notifications:**

| Method | Endpoint | Permission | Description |
|---|---|---|---|
| GET | `/notifications` | `notification.view` | Get user's notifications. Pass `?unread=true` for unread only |
| PUT | `/notifications/:id/read` | `notification.view` | Mark a single notification as read |
| PUT | `/notifications/read-all` | `notification.view` | Mark all notifications as read |

**Audit Logs:**

| Method | Endpoint | Permission | Description |
|---|---|---|---|
| GET | `/audit-logs` | `report.view_audit_logs` | Get system audit trail. Every CREATE, UPDATE, DELETE, CLOSE, VERIFY, PHASE_ADVANCE action is logged with old/new values as JSON |

**Quality Gates:**

| Method | Endpoint | Permission | Description |
|---|---|---|---|
| GET | `/quality-gates` | `quality_gate.view` | List quality gates. Optional filter: `?phase_id=` |
| GET | `/quality-gates/:id/criteria` | `quality_gate.view` | Get criteria for a specific quality gate |
| POST | `/quality-gates` | `quality_gate.define` | Create a new quality gate (gate_name, phase_id, description, is_mandatory) |
| PUT | `/quality-gates/:id` | `quality_gate.modify_criteria` | Update quality gate details |
| POST | `/quality-gates/:id/criteria` | `quality_gate.modify_criteria` | Add criteria to a quality gate (criteria_name, criteria_type, required_value) |

**Export:**

| Method | Endpoint | Permission | Description |
|---|---|---|---|
| GET | `/export/:entity` | `report.export` | Export data as JSON. Supported entities: `projects`, `audits`, `ncs`, `capas`, `documents`. Supports query filters |

**Health Check:**

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET | `/api/health` | No | Returns `{ status: "ok", timestamp: "..." }` |

---

## Database Schema

### Tables (25 total)

#### Core Tables

| Table | Description | Key Fields |
|---|---|---|
| `sdlc_phases` | 6 SDLC phases reference table | phase_name, phase_order, requires_audit, quality_gate_required |
| `users` | System users with role-based access | username, email, password_hash, role (7 roles), status (Active/Inactive/Suspended) |
| `projects` | SDLC projects | project_code (unique), project_name, project_manager_id, status, current_phase, quality_rating |
| `project_team` | Project membership (many-to-many) | project_id, user_id, role_in_project. Unique constraint on (project_id, user_id) |
| `project_phases` | Phase tracking per project (1 row per project per phase) | status, completion_percentage, quality_gate_passed, quality_gate_approved_by |
| `project_milestones` | Project milestones with approval | milestone_name, target_date, status (Not Started/In Progress/Completed/Overdue), approved_by |

#### Document Management

| Table | Description | Key Fields |
|---|---|---|
| `documents` | Project documents | document_number (DOC-###), document_type (6 types), version, status (Draft/Under Review/Approved/Obsolete) |
| `document_versions` | Version history per document | version, file_path, change_description |
| `document_approvals` | Approval chain per document | approver_id, approval_order, status (Pending/Approved/Rejected) |

#### Audit Management

| Table | Description | Key Fields |
|---|---|---|
| `audits` | Formal phase audits | audit_number (AUD-###), auditor_id, status, result (Pass/Fail/Partial), score (0-100) |
| `audit_checklist` | Checklist items per audit | checklist_item, expected_evidence, result (Pass/Fail/Partial/N/A) |
| `audit_findings` | Findings per audit | finding_type (Conformance/Non-Conformance/Observation/Improvement), severity, nc_id |

#### Non-Conformance Management

| Table | Description | Key Fields |
|---|---|---|
| `non_conformances` | Quality issues/defects | nc_number (NC-###), severity (Critical/Major/Minor), status (5 states), assigned_to, audit_id |
| `nc_investigation` | Root cause investigations | investigator_id, findings, recommended_actions |

#### CAPA Management

| Table | Description | Key Fields |
|---|---|---|
| `capa` | Corrective/Preventive Actions | capa_number (CAPA-###), type (Corrective/Preventive), nc_id, effectiveness_score (1-5), status (5 states) |
| `capa_tasks` | Sub-tasks per CAPA | task_description, assigned_to, status (Pending/In Progress/Completed) |
| `capa_verification` | Verification records | verifier_id, result (Effective/Partially Effective/Ineffective), follow_up_required |

#### Quality Gates

| Table | Description | Key Fields |
|---|---|---|
| `quality_gates` | Gate definitions per phase | gate_name, phase_id, is_mandatory |
| `quality_gate_criteria` | Criteria per gate | criteria_name, criteria_type (Document/Audit/Test/Review/Approval), required_value |
| `project_quality_gate_results` | Gate results per project | project_id, quality_gate_id, status (Pass/Fail/N/A), evidence, verified_by |

#### System Tables

| Table | Description | Key Fields |
|---|---|---|
| `notifications` | User notifications | user_id, title, message, type (Audit/NC/CAPA/Document/System/Approval), is_read |
| `audit_logs` | Complete system audit trail | user_id, action, entity_type, entity_id, old_values (JSON), new_values (JSON) |

#### RBAC Tables

| Table | Description | Key Fields |
|---|---|---|
| `user_permission_overrides` | Per-user permission grants/revocations beyond role defaults | user_id, permission_key, granted, reason, expires_at. Unique on (user_id, permission_key) |
| `permission_audit_log` | Trail of permission changes | user_id, permission_key, action (GRANT/REVOKE/CHECK_DENIED), performed_by |

### Views (4)

| View | Description |
|---|---|
| `dashboard_metrics` | Counts: active projects, active audits, open NCs, in-progress CAPAs, NCs closed in last 30 days |
| `nc_trend` | NC count by severity grouped by month (last 12 months) |
| `audit_compliance` | Per-project: total audits, passed audits, compliance rate (%) |
| `capa_effectiveness` | Per-month: total CAPAs closed, effective CAPAs (score ≥ 4), effectiveness rate (%) |

### Indexes

Performance indexes on: `users.email`, `users.role`, `projects.status`, `projects.project_manager_id`, `project_phases.project_id`, `documents.project_id`, `documents.status`, `audits.project_id`, `audits.auditor_id`, `audits.status`, `non_conformances.project_id`, `non_conformances.status`, `capa.nc_id`, `capa.owner_id`, `capa.status`, `notifications(user_id, is_read)`, `audit_logs.created_at`, `project_milestones.project_id`, `user_permission_overrides(user_id, active)`, `permission_audit_log(user_id, created_at)`.

---

## Stored Procedures

### `sp_create_project`

**Purpose:** Create a new project with all SDLC phase tracking records.

**Parameters:**
| Name | Direction | Type | Description |
|---|---|---|---|
| p_project_code | IN | VARCHAR(20) | Unique project code (e.g., PRJ-005) |
| p_project_name | IN | VARCHAR(200) | Project name |
| p_description | IN | TEXT | Project description |
| p_manager_id | IN | CHAR(36) | UUID of the project manager |
| p_start_date | IN | DATE | Project start date |
| p_target_end_date | IN | DATE | Target end date |
| p_created_by | IN | CHAR(36) | Creator's user UUID |
| p_project_id | OUT | CHAR(36) | Generated project UUID |

**What it does:**
1. Generates a UUID for the project
2. Inserts the project record with status `Active` and `current_phase` set to the first SDLC phase
3. Adds the project manager to `project_team` with role "Project Manager"
4. Creates a `project_phases` row for each of the 6 SDLC phases (all start as "Not Started", 0%)
5. Logs the action to `audit_logs`

---

### `sp_advance_project_phase`

**Purpose:** Advance a project to the next SDLC phase after quality gate verification.

**Parameters:**
| Name | Direction | Type | Description |
|---|---|---|---|
| p_project_id | IN | CHAR(36) | Project UUID |
| p_approved_by | IN | CHAR(36) | User approving the advancement |
| p_new_phase | OUT | VARCHAR(50) | The new phase name (or current if blocked) |
| p_result_msg | OUT | VARCHAR(255) | Result message |

**What it does:**
1. Gets the current phase and its order
2. Checks if the quality gate is already passed
3. If not passed, checks for open Critical/Major NCs in the current phase
4. If blocking NCs exist → returns error message listing them
5. If no blockers → auto-passes the gate
6. If gate is passed:
   - Marks current phase as Completed (100%)
   - If next phase exists → starts it (In Progress), updates `projects.current_phase`
   - If last phase → marks project as Completed with `actual_end_date`
7. Logs the `PHASE_ADVANCE` action

---

### `sp_create_audit`

**Purpose:** Create a new audit with auto-generated audit number.

**Parameters:**
| Name | Direction | Type | Description |
|---|---|---|---|
| p_project_id | IN | CHAR(36) | Project UUID |
| p_phase_id | IN | CHAR(36) | SDLC phase UUID |
| p_auditor_id | IN | CHAR(36) | Assigned auditor UUID |
| p_audit_date | IN | DATE | Scheduled audit date |
| p_created_by | IN | CHAR(36) | Creator UUID |
| p_audit_id | OUT | CHAR(36) | Generated audit UUID |
| p_audit_number | OUT | VARCHAR(50) | Generated number (AUD-001, AUD-002...) |

**What it does:**
1. Auto-generates the next audit number (AUD-XXX)
2. Inserts audit with status `Scheduled`
3. Creates a notification for the assigned auditor
4. Logs the action

---

### `sp_complete_audit`

**Purpose:** Complete an audit with result and score.

**Parameters:**
| Name | Direction | Type | Description |
|---|---|---|---|
| p_audit_id | IN | CHAR(36) | Audit UUID |
| p_result | IN | VARCHAR(20) | Pass, Fail, or Partial |
| p_score | IN | DECIMAL(5,2) | Score 0-100 |
| p_findings_summary | IN | TEXT | Summary text |
| p_updated_by | IN | CHAR(36) | User completing the audit |

**What it does:**
1. Updates audit status to `Completed` with result, score, and findings summary
2. Logs the action

---

### `sp_create_nc`

**Purpose:** Create a non-conformance with auto-number and Critical NC alerts.

**Parameters:**
| Name | Direction | Type | Description |
|---|---|---|---|
| p_project_id | IN | CHAR(36) | Project UUID |
| p_phase_id | IN | CHAR(36) | SDLC phase UUID |
| p_title | IN | VARCHAR(255) | NC title |
| p_description | IN | TEXT | NC description |
| p_severity | IN | VARCHAR(20) | Critical, Major, or Minor |
| p_reported_by | IN | CHAR(36) | Reporter UUID |
| p_assigned_to | IN | CHAR(36) | Assignee UUID |
| p_due_date | IN | DATE | Resolution due date |
| p_audit_id | IN | CHAR(36) | Linked audit UUID (optional) |
| p_nc_id | OUT | CHAR(36) | Generated NC UUID |
| p_nc_number | OUT | VARCHAR(50) | Generated number (NC-001, NC-002...) |

**What it does:**
1. Auto-generates the next NC number (NC-XXX)
2. Inserts NC with status `Open`
3. Sends notification to the assigned user
4. **If severity is Critical:** sends alert notifications to ALL active Quality Managers
5. Logs the action

---

### `sp_close_nc`

**Purpose:** Close a non-conformance after verifying all linked CAPAs are resolved.

**Parameters:**
| Name | Direction | Type | Description |
|---|---|---|---|
| p_nc_id | IN | CHAR(36) | NC UUID |
| p_closed_by | IN | CHAR(36) | User closing the NC |
| p_result_msg | OUT | VARCHAR(255) | Result message |

**What it does:**
1. Counts linked CAPAs that are NOT in Closed/Verified status
2. If open CAPAs exist → returns "Cannot close NC: X linked CAPA(s) still open"
3. If all CAPAs resolved → updates NC status to `Closed` and logs

---

### `sp_create_capa`

**Purpose:** Create a CAPA with auto-number, linked to an NC.

**Parameters:**
| Name | Direction | Type | Description |
|---|---|---|---|
| p_nc_id | IN | CHAR(36) | Linked NC UUID (optional) |
| p_title | IN | VARCHAR(255) | CAPA title |
| p_type | IN | VARCHAR(20) | Corrective or Preventive |
| p_description | IN | TEXT | Description |
| p_root_cause | IN | TEXT | Root cause analysis |
| p_corrective_action | IN | TEXT | Corrective action plan |
| p_preventive_action | IN | TEXT | Preventive action plan |
| p_owner_id | IN | CHAR(36) | Assigned owner UUID |
| p_due_date | IN | DATE | Due date |
| p_created_by | IN | CHAR(36) | Creator UUID |
| p_capa_id | OUT | CHAR(36) | Generated CAPA UUID |
| p_capa_number | OUT | VARCHAR(50) | Generated number (CAPA-001...) |

**What it does:**
1. Auto-generates the next CAPA number (CAPA-XXX)
2. Inserts CAPA with status `Open`
3. Sends notification to the assigned owner
4. Logs the action

---

### `sp_verify_capa`

**Purpose:** Verify a CAPA and rate its effectiveness.

**Parameters:**
| Name | Direction | Type | Description |
|---|---|---|---|
| p_capa_id | IN | CHAR(36) | CAPA UUID |
| p_verifier_id | IN | CHAR(36) | Quality Manager UUID |
| p_verification_notes | IN | TEXT | Verification notes |
| p_result | IN | VARCHAR(20) | Effective, Partially Effective, or Ineffective |
| p_effectiveness_score | IN | INT | 1-5 rating |
| p_follow_up | IN | TINYINT(1) | Whether follow-up is required |
| p_result_msg | OUT | VARCHAR(255) | Result message |

**What it does:**
1. Records verification in `capa_verification`
2. If Effective + no follow-up → status `Closed`, sets closed_date
3. If Effective + follow-up → status `Verified`
4. If not Effective → returns to `In Progress`
5. Logs the action

---

### `sp_project_dashboard`

**Purpose:** Get comprehensive project dashboard metrics.

**Parameters:**
| Name | Direction | Type | Description |
|---|---|---|---|
| p_project_id | IN | CHAR(36) | Project UUID |

**Returns 3 result sets:**
1. **Summary counts:** total documents, completed/pending audits, open NCs, critical NCs, open CAPAs
2. **Phase progress:** all 6 phases with status, completion %, gate passed, dates
3. **Recent audits:** last 10 audits with number, phase, result, score, auditor name

---

### `sp_nc_summary`

**Purpose:** Get NC breakdown for a project.

**Parameters:**
| Name | Direction | Type | Description |
|---|---|---|---|
| p_project_id | IN | CHAR(36) | Project UUID |

**Returns 2 result sets:**
1. **By severity/status:** count of NCs grouped by severity and status
2. **Overdue NCs:** list of overdue NCs with days overdue and assigned person

---

### `sp_calculate_quality_rating`

**Purpose:** Calculate and store a project's quality rating (0.00–5.00).

**Parameters:**
| Name | Direction | Type | Description |
|---|---|---|---|
| p_project_id | IN | CHAR(36) | Project UUID |
| p_rating | OUT | DECIMAL(3,2) | Calculated rating |

**Formula:**
```
Rating = (Avg Audit Score / 20) - NC Penalty + CAPA Bonus

NC Penalty: -0.50 per open Critical, -0.20 per Major, -0.05 per Minor
CAPA Bonus: Avg effectiveness_score × 0.10

Clamped to range [0.00, 5.00]
Returns 0.00 if no completed audits exist.
```

Updates `projects.quality_rating` in-place.

---

### `sp_approve_document`

**Purpose:** Process a document approval decision.

**Parameters:**
| Name | Direction | Type | Description |
|---|---|---|---|
| p_document_id | IN | CHAR(36) | Document UUID |
| p_approver_id | IN | CHAR(36) | Approver UUID |
| p_decision | IN | VARCHAR(20) | Approved or Rejected |
| p_comments | IN | TEXT | Approval comments |
| p_result_msg | OUT | VARCHAR(255) | Result message |

**What it does:**
1. Updates the pending approval record for this approver
2. If decision is `Rejected` → document returns to `Draft`
3. If decision is `Approved`:
   - Checks if ANY other approvals are still `Pending`
   - If none pending → document becomes `Approved`
   - If others pending → returns "awaiting other approvers"
4. Logs the action

---

### `sp_global_dashboard`

**Purpose:** Get system-wide dashboard data.

**Returns 5 result sets:**
1. **Summary cards:** from `dashboard_metrics` view
2. **NC trend:** from `nc_trend` view (last 6 months)
3. **Audit compliance:** per-project pass rates
4. **CAPA effectiveness:** from `capa_effectiveness` view
5. **Overdue items:** all overdue NCs and CAPAs combined

---

### `sp_add_team_member`

**Purpose:** Add a user to a project team with duplicate detection.

**Parameters:**
| Name | Direction | Type | Description |
|---|---|---|---|
| p_project_id | IN | CHAR(36) | Project UUID |
| p_user_id | IN | CHAR(36) | User UUID |
| p_role_in_project | IN | VARCHAR(100) | Role (e.g., "Lead Developer", "QA Lead") |
| p_added_by | IN | CHAR(36) | User performing the action |
| p_result_msg | OUT | VARCHAR(255) | Result message |

**What it does:**
1. Inserts into `project_team` (duplicate handler catches unique constraint violation)
2. Sends notification to the added user ("You have been added to project: X")
3. Logs the action

---

## Business Rules Enforced in Backend

### NC Closure Rule
An NC can only be closed when ALL linked CAPAs are in `Closed` or `Verified` status. Enforced at the database level in `sp_close_nc`.

### Phase Advancement Blocking
- **Open Critical/Major NCs** in the current phase block phase advancement
- **Open Minor NCs** do NOT block advancement
- Quality Manager or Admin can override gates via `phase.override_gate` permission

### Document Approval Chain
- When submitted for review, all assigned approvers must approve
- If ANY approver rejects → document returns to Draft
- Document type upload/approval restrictions are enforced at controller level

### Auto-Numbering
All entity numbers are auto-generated sequentially:
- Projects: `PRJ-001`, `PRJ-002`...
- Audits: `AUD-001`, `AUD-002`...
- NCs: `NC-001`, `NC-002`...
- CAPAs: `CAPA-001`, `CAPA-002`...
- Documents: `DOC-001`, `DOC-002`...

### Critical NC Alerts
When a Critical severity NC is created, ALL active Quality Managers receive an automatic notification.

### Self-Prevention Rules
- Users cannot verify their own CAPAs (enforced at service level)
- Users cannot approve their own documents
- Users cannot close NCs they reported

### Quality Rating
Automatically calculated via `sp_calculate_quality_rating`:
- Based on audit scores, NC penalties, and CAPA effectiveness
- Scale: 0.00 to 5.00
- Stored on the `projects` table

### Soft Deletes
- Deleting a project → status becomes `Archived`
- Deleting a document → status becomes `Obsolete`
- Deleting a user → status becomes `Inactive`
- No hard deletes on business entities
