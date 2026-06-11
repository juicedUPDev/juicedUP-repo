# Maypo Configuration Guide

This file documents all configuration options for the Maypo AI Consulting Platform.

---

## Environment Variables (.env)

### Server Configuration
```env
# Host and port settings
HOST=0.0.0.0                    # Server bind address
PORT=8000                        # Server port
DEBUG=false                      # Enable debug mode (dev only)
ENVIRONMENT=production           # Environment: development, staging, production
LOG_LEVEL=INFO                   # Logging level: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FORMAT=json                  # Log format: json or text
```

### API Keys & Credentials
```env
# OpenAI Configuration
OPENAI_API_KEY=sk-your-key-here
OPENAI_MODEL=gpt-4              # Default model: gpt-4, gpt-3.5-turbo
OPENAI_ORG_ID=                  # Optional: Organization ID

# Alternative LLM (Claude, etc.)
ALTERNATIVE_LLM_API_KEY=
ALTERNATIVE_LLM_PROVIDER=       # Provider: anthropic, cohere, huggingface

# API Rate Limiting
API_RATE_LIMIT=1000             # Requests per hour
API_RATE_LIMIT_BURST=100        # Burst allowance
```

### Database Configuration
```env
# PostgreSQL
DATABASE_URL=postgresql://user:password@localhost:5432/maypo
DB_POOL_SIZE=10                 # Connection pool size
DB_POOL_TIMEOUT=30              # Connection timeout (seconds)
DB_ECHO=false                   # Log all SQL statements (dev only)
DB_MIGRATION_AUTO=true          # Auto-run migrations on startup

# Redis (optional, for caching)
REDIS_URL=redis://localhost:6379/0
REDIS_PASSWORD=                 # Redis password (if required)
REDIS_DB=0                      # Redis database number
```

### Authentication
```env
# JWT Configuration
JWT_SECRET=your-super-secret-key-change-in-production
JWT_ALGORITHM=HS256             # Algorithm: HS256, HS512, RS256
JWT_EXPIRATION_HOURS=24         # Token expiration time
JWT_REFRESH_EXPIRATION_DAYS=30  # Refresh token expiration

# OAuth (optional)
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
GITHUB_CLIENT_ID=
GITHUB_CLIENT_SECRET=
```

### Cost Management
```env
# Budget & Alerts
MONTHLY_BUDGET_LIMIT=5000       # Monthly spending limit ($)
COST_ALERT_THRESHOLD=0.80       # Alert at 80% of budget
COST_ALERT_EMAIL=admin@maypo.ai # Alert recipient

# Token Optimization
ENABLE_TOKEN_OPTIMIZATION=true
TOKEN_COMPRESSION_LEVEL=high    # low, medium, high
```

### Feature Flags
```env
# Feature Toggle
ENABLE_ANALYTICS=true           # Enable analytics collection
ENABLE_VERSIONING=true          # Enable prompt versioning
ENABLE_COST_OPTIMIZATION=true   # Enable cost optimization
ENABLE_CACHE=true               # Enable caching
ENABLE_BATCH_PROCESSING=true    # Enable batch processing
ENABLE_A_B_TESTING=true         # Enable A/B testing
ENABLE_WEBHOOKS=true            # Enable webhook support
```

### Email Configuration
```env
# SMTP Settings
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password
SMTP_FROM_EMAIL=noreply@maypo.ai
SMTP_FROM_NAME=Maypo
```

### Monitoring & Logging
```env
# Sentry (Error Tracking)
SENTRY_DSN=https://your-sentry-dsn

# DataDog (Monitoring)
DATADOG_API_KEY=
DATADOG_APP_KEY=

# Prometheus
PROMETHEUS_ENABLED=true
PROMETHEUS_PORT=9090
```

---

## Configuration Files

### 1. `src/config/settings.py`

Main application settings configuration:

```python
from pydantic import BaseSettings

class Settings(BaseSettings):
    # Application
    app_name: str = "Maypo AI Consulting"
    app_version: str = "1.0.0"
    debug: bool = False
    
    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    workers: int = 4
    reload: bool = False
    
    # Database
    database_url: str
    db_pool_size: int = 10
    db_pool_timeout: int = 30
    
    # Cache
    redis_url: str = "redis://localhost:6379/0"
    cache_ttl: int = 3600
    
    # API Keys
    openai_api_key: str
    openai_model: str = "gpt-4"
    
    # JWT
    jwt_secret: str
    jwt_algorithm: str = "HS256"
    jwt_expiration_hours: int = 24
    
    # Cost Management
    monthly_budget: float = 5000
    alert_threshold: float = 0.80
    
    class Config:
        env_file = ".env"
        case_sensitive = False
```

### 2. `src/config/models.py`

AI model configurations:

```python
MODELS = {
    "gpt-4": {
        "provider": "openai",
        "context_window": 8192,
        "cost_per_1k_input": 0.03,
        "cost_per_1k_output": 0.06,
        "enabled": True,
    },
    "gpt-3.5-turbo": {
        "provider": "openai",
        "context_window": 4096,
        "cost_per_1k_input": 0.0015,
        "cost_per_1k_output": 0.002,
        "enabled": True,
    },
    "claude-2": {
        "provider": "anthropic",
        "context_window": 100000,
        "cost_per_1k_input": 0.008,
        "cost_per_1k_output": 0.024,
        "enabled": False,
    },
}

DEFAULT_MODEL = "gpt-4"
FALLBACK_MODEL = "gpt-3.5-turbo"
```

### 3. `src/config/prompts.py`

Default prompt templates:

```python
PROMPT_TEMPLATES = {
    "business_analysis": """
        You are an expert business consultant.
        
        User Query: {query}
        Industry: {industry}
        
        Provide detailed analysis including:
        1. Key insights
        2. Actionable recommendations
        3. Risk assessment
        4. Expected outcomes
    """,
    
    "technical_support": """
        You are a technical support specialist.
        
        Issue: {issue}
        Context: {context}
        
        Provide step-by-step troubleshooting guide.
    """,
}

PROMPT_VERSIONS = {
    "business_analysis": {
        "v1": {...},
        "v2": {...},
        "current": "v2",
    }
}
```

### 4. `src/config/logging.py`

Logging configuration:

```python
import logging.config

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        },
        "json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(asctime)s %(name)s %(levelname)s %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "json",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "logs/app.log",
            "maxBytes": 10485760,  # 10MB
            "backupCount": 5,
            "formatter": "json",
        },
    },
    "loggers": {
        "": {
            "handlers": ["console", "file"],
            "level": "INFO",
        },
    },
}

logging.config.dictConfig(LOGGING_CONFIG)
```

### 5. `docker-compose.yml`

Docker container orchestration:

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://maypo:password@db:5432/maypo
      - REDIS_URL=redis://redis:6379/0
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    depends_on:
      - db
      - redis
    volumes:
      - ./logs:/app/logs
    restart: unless-stopped

  db:
    image: postgres:14-alpine
    environment:
      - POSTGRES_USER=maypo
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=maypo
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    restart: unless-stopped

volumes:
  postgres_data:
  redis_data:
```

---

## Performance Configuration

### Caching Strategy

```python
CACHE_CONFIG = {
    "backend": "redis",  # redis, memory, memcached
    "ttl": {
        "consultation": 3600,  # 1 hour
        "prompts": 86400,      # 24 hours
        "analytics": 300,      # 5 minutes
    },
    "key_prefix": "maypo:",
    "compression": True,
}
```

### Connection Pooling

```python
DATABASE_CONFIG = {
    "pool_size": 10,
    "max_overflow": 20,
    "pool_timeout": 30,
    "pool_recycle": 3600,
    "echo": False,
}
```

### API Rate Limiting

```python
RATE_LIMIT_CONFIG = {
    "enabled": True,
    "default": "1000/hour",
    "tiers": {
        "free": "100/hour",
        "pro": "10000/hour",
        "enterprise": "unlimited",
    },
    "burst_size": 100,
}
```

---

## Security Configuration

### CORS Settings

```python
CORS_CONFIG = {
    "allow_origins": ["https://maypo.ai", "https://console.maypo.ai"],
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"],
}
```

### HTTPS/TLS

```python
SSL_CONFIG = {
    "enabled": True,
    "certfile": "/etc/ssl/certs/server.crt",
    "keyfile": "/etc/ssl/private/server.key",
    "ssl_version": "TLSv1.3",
}
```

### API Security

```python
SECURITY_CONFIG = {
    "require_api_key": True,
    "api_key_header": "X-API-Key",
    "rate_limit_enabled": True,
    "require_https": True,
    "cors_enabled": True,
    "csrf_protection": True,
}
```

---

## Database Schema Configuration

### PostgreSQL Schema

```sql
-- Enable extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";  -- For full-text search

-- Configure WAL
ALTER SYSTEM SET wal_level = replica;
ALTER SYSTEM SET max_wal_senders = 3;

-- Configure shared_buffers (25% of system RAM)
ALTER SYSTEM SET shared_buffers = '2GB';

-- Configure effective_cache_size (50-75% of system RAM)
ALTER SYSTEM SET effective_cache_size = '8GB';
```

---

## Development vs Production

### Development Environment (.env.development)

```env
DEBUG=true
ENVIRONMENT=development
LOG_LEVEL=DEBUG
DATABASE_URL=postgresql://dev:dev@localhost:5432/maypo_dev
REDIS_URL=redis://localhost:6379/1
OPENAI_API_KEY=sk-test-key
```

### Production Environment (.env.production)

```env
DEBUG=false
ENVIRONMENT=production
LOG_LEVEL=WARNING
DATABASE_URL=postgresql://prod_user:secure_password@db.internal:5432/maypo
REDIS_URL=redis://redis.internal:6379/0
OPENAI_API_KEY=sk-real-key
JWT_SECRET=your-production-secret-key
```

---

## Configuration Validation

### Startup Configuration Check

```python
from pydantic import ValidationError

def validate_config():
    try:
        settings = Settings()
        print("✓ Configuration valid")
        return settings
    except ValidationError as e:
        print(f"✗ Configuration error: {e}")
        raise
```

### Health Check Endpoint

```python
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "version": settings.app_version,
        "environment": settings.environment,
        "database": check_database(),
        "redis": check_redis(),
    }
```

---

## Configuration Best Practices

1. **Use environment variables** for sensitive data
2. **Never commit .env files** - use .env.example
3. **Validate configuration on startup**
4. **Use different configs** for dev/prod
5. **Document all settings** in README
6. **Rotate secrets regularly** (JWT keys, API keys)
7. **Monitor configuration changes** in production
8. **Test configuration migrations** before deploying

---

## Common Configuration Issues

### Issue: "Invalid API Key"
```bash
# Verify key is set
echo $OPENAI_API_KEY

# Test API connection
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

### Issue: "Database Connection Failed"
```bash
# Test connection string
psql $DATABASE_URL -c "SELECT 1"

# Check credentials
# Check firewall rules
# Check network connectivity
```

### Issue: "Redis Connection Timeout"
```bash
# Test Redis connection
redis-cli -u $REDIS_URL ping

# Check Redis service
docker-compose ps redis
```

---

For more information, see [docs/DEPLOYMENT.md](../docs/DEPLOYMENT.md)
