# Lab7-Proof API Backend

This is the FastAPI backend for the Lab7 Open Attestation Authority (OAA) service.

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the development server:
```bash
python app/main.py
```

Or using uvicorn directly:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## API Endpoints

### Health Checks
- `GET /health` - Simple health check
- `GET /healthz` - Alternative health check (Kubernetes style)
- `GET /oaa/health/redis` - Redis-specific health check

### Echo Ingest
- `POST /oaa/echo/ingest` - Ingest echo pulses

## Example Usage

### Health Check
```bash
curl http://localhost:8000/health
```

### Echo Ingest
```bash
curl -X POST http://localhost:8000/oaa/echo/ingest \
  -H "Content-Type: application/json" \
  -d '{
    "source": "test",
    "fingerprint": "abc123",
    "payload": {"message": "hello"}
  }'
```

## Development

The API will be available at `http://localhost:8000` with automatic API documentation at `http://localhost:8000/docs`.