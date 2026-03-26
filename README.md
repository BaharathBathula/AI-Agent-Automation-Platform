# AI Agent & Automation Platform

Production-grade AI agent and automation system with workflow orchestration, tool calling, memory, scheduling, and observability.

## Overview

This project is a modular backend platform for building AI agents that can:

- accept tasks
- plan multi-step actions
- call tools
- store memory
- run scheduled workflows
- log execution history

## Tech Stack

- FastAPI
- PostgreSQL
- Redis
- Celery
- SQLAlchemy
- Docker

## Project Structure

```bash
app/
  api/
  agents/
  orchestration/
  tools/

## Example Workflow

### Input Task
"Summarize customer support tickets and generate a report."

### System Execution

1. Planner Agent creates execution steps
2. Executor Agent runs tools
3. Results are aggregated
4. Output is returned

### Output

- Key issues identified
- Priority classification
- Suggested actions
  memory/
  workers/
  db/
  schemas/

## Execution Flow

1. Task is submitted via API
2. Task is stored in PostgreSQL
3. AgentRunner orchestrates execution
4. Planner generates steps
5. Executor executes each step
6. Results returned and logged

## Current Capabilities

- Task persistence
- Multi-agent orchestration
- Planner + Executor pipeline
- Tool registry system
- Audit-ready architecture
