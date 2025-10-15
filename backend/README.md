# Lab7 - Open Attestation Authority (OAA) Backend

FastAPI backend for the Lab7-Proof Open Attestation Authority system.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## API Endpoints

### Health Checks
- `GET /health` - Simple health check (returns status ok)
- `GET /healthz` - Alternative health check endpoint
- `GET /oaa/health/redis` - Redis-specific health check

### Echo Ingest
- `POST /oaa/echo/ingest` - Ingest echo pulse data
  
  Request body:
  ```json
  {
    "source": "string",
    "fingerprint": "string",
    "payload": {}
  }
  ```

### Information
- `GET /` - API information and available endpoints
- `GET /oaa/status` - OAA service status

## Development

The API is built with FastAPI and includes:
- CORS middleware configured for development
- Pydantic models for request validation
- Health check endpoints for monitoring
- Echo ingest functionality for data processing

## Version

Current version: 1.0.1