# Design Decisions

## Why FastAPI?

FastAPI provides high performance, automatic API documentation, and strong typing support, making it ideal for building scalable AI systems.

---

## Why PostgreSQL?

PostgreSQL is used for structured data storage including tasks, workflows, and audit logs. It ensures reliability and strong consistency.

---

## Why Redis?

Redis is used as:
- message broker for Celery
- caching layer
- transient memory store

---

## Why Celery?

Celery enables:
- asynchronous task execution
- retries and fault tolerance
- distributed worker architecture

---

## Why Multi-Agent Architecture?

Instead of a single LLM call, we use multiple agents:

- Router → understands intent
- Planner → decomposes tasks
- Executor → performs actions
- Reviewer → validates outputs

This improves reliability and modularity.

---

## Why Tool-Based Execution?

Tools allow the system to:
- interact with external systems
- perform structured actions
- extend capabilities without changing core logic

---

## Why Memory Layer?

Memory allows:
- contextual reasoning
- reuse of past results
- personalization of workflows

---

## Why Audit Logs?

Audit logs ensure:
- traceability
- debugging
- compliance (important for enterprise AI systems)

---

## Why Modular Folder Structure?

Each component is isolated to:
- improve maintainability
- enable independent scaling
- support team collaboration
