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
  memory/
  workers/
  db/
  schemas/
