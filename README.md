# Maypo AI Consulting Platform

[![GitHub](https://img.shields.io/badge/GitHub-juicedUPDev%2Fmaypo-blue?logo=github)](https://github.com/juicedUPDev/maypo)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen)](https://github.com/juicedUPDev/maypo)
[![Version](https://img.shields.io/badge/Version-1.0.0-blue)](https://github.com/juicedUPDev/maypo/releases)

An enterprise-grade AI consulting platform powered by advanced prompt engineering with versioning, cost optimization, and real-time analytics.

---

## 📋 Table of Contents

- [Features](#features)
- [Quick Start](#quick-start)
- [Documentation](#documentation)
- [Project Structure](#project-structure)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

- 🤖 **AI-Powered Consulting**: Intelligent recommendations for various business needs
- 🔧 **Prompt Engineering Console**: Customize and version AI prompts for specific use cases
- 📊 **Real-Time Analytics**: Live data processing and performance monitoring
- 💰 **Cost Optimization**: Built-in strategies to minimize expenses while maximizing performance
- 🔐 **Enterprise Security**: Secure API endpoints with authentication
- 📈 **Scalable Architecture**: Handles high-volume concurrent requests
- 🔄 **Version Control**: Full prompt versioning and rollback capabilities
- 🎯 **Multi-Model Support**: Compatible with multiple AI models (GPT, Claude, etc.)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- PostgreSQL 12+ (or use Docker)
- Redis (optional, for caching)

### Installation

```bash
# 1. Clone repository
git clone https://github.com/juicedUPDev/maypo.git
cd maypo

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env
# Edit .env with your API keys and settings

# 5. Run application
python src/main.py
```

### Quick Start with Docker

```bash
docker-compose up -d
```

Access the application at `http://localhost:8000`

---

## 📚 Documentation

Complete documentation is available in the `/docs` directory:

| Document | Purpose |
|----------|---------|
| **[CONFIGURATION.md](docs/CONFIGURATION.md)** | Environment variables, settings, and configuration examples |
| **[API.md](docs/API.md)** | Complete API reference with examples |
| **[PROMPTS.md](docs/PROMPTS.md)** | Prompt engineering guide and best practices |
| **[DEPLOYMENT.md](docs/DEPLOYMENT.md)** | Deployment instructions for AWS, Azure, Heroku |
| **[ARCHITECTURE.md](docs/ARCHITECTURE.md)** | System architecture and design patterns |

### Quick Links
- 📖 [Full Documentation](docs/)
- 🔌 [API Reference](docs/API.md)
- ⚙️ [Configuration Guide](docs/CONFIGURATION.md)
- 🚀 [Deployment Guide](docs/DEPLOYMENT.md)
- 💡 [Prompt Engineering](docs/PROMPTS.md)

---

## 📁 Project Structure

```
maypo/
├── src/
│   ├── api/                    # API endpoints and routes
│   ├── prompts/                # Prompt templates and versions
│   ├── models/                 # AI model integrations
│   ├── utils/                  # Utility functions
│   ├── config/                 # Configuration files
│   └── main.py                 # Application entry point
├── docs/
│   ├── API.md                  # API documentation
│   ├── CONFIGURATION.md        # Configuration guide
│   ├── PROMPTS.md              # Prompt engineering guide
│   ├── ARCHITECTURE.md         # System architecture
│   └── DEPLOYMENT.md           # Deployment guide
├── tests/
│   ├── unit/                   # Unit tests
│   ├── integration/            # Integration tests
│   └── conftest.py             # Pytest configuration
├── .env.example                # Environment variables template
├── requirements.txt            # Python dependencies
├── docker-compose.yml          # Docker configuration
├── Dockerfile                  # Docker image
├── setup.py                    # Package setup
└── README.md                   # This file
```

---

## 🖥️ System Requirements

### Minimum
- **Python**: 3.8+
- **RAM**: 4GB
- **Storage**: 2GB
- **CPU**: 2 cores

### Recommended
- **Python**: 3.10+
- **RAM**: 16GB+
- **Storage**: 10GB+
- **CPU**: 8+ cores
- **Database**: PostgreSQL 12+
- **Cache**: Redis 6.0+

---

## 📦 Installation

### Step 1: Clone Repository
```bash
git clone https://github.com/juicedUPDev/maypo.git
cd maypo
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment
```bash
cp .env.example .env
nano .env  # Edit with your settings
```

### Step 5: Initialize Database
```bash
python src/main.py --init-db
```

### Step 6: Run Application
```bash
python src/main.py
```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file based on `.env.example`:

```env
# Server
HOST=0.0.0.0
PORT=8000
DEBUG=false
ENVIRONMENT=production

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/maypo

# API Keys
OPENAI_API_KEY=sk-your-key-here

# Authentication
JWT_SECRET=your-secret-key-here

# Cost Management
MONTHLY_BUDGET_LIMIT=5000
```

**For complete configuration options, see [CONFIGURATION.md](docs/CONFIGURATION.md)**

### Docker Configuration

```bash
# Build and start services
docker-compose up -d

# View logs
docker-compose logs -f app

# Stop services
docker-compose down
```

---

## 💻 Usage

### Running the Application

```bash
# Development mode
python src/main.py --reload

# Production mode
python src/main.py

# Specify port
python src/main.py --port 8080
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test
pytest tests/unit/test_api.py -v
```

### Accessing the API

```bash
# Health check
curl http://localhost:8000/health

# Get consultation
curl -H "Authorization: Bearer YOUR_TOKEN" \
  http://localhost:8000/api/v1/consult?query=your+query

# Submit data
curl -X POST http://localhost:8000/api/v1/submit \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"data": {...}}'
```

**For complete API documentation, see [API.md](docs/API.md)**

### Web Dashboard

Access the web interface at: `http://localhost:8000`

Features:
- Consultation history
- Prompt engineering console
- Cost analytics
- Usage statistics
- API key management

---

## 🔧 API Endpoints

### Consultation Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/consult` | Get consultation |
| POST | `/api/v1/submit` | Submit user data |
| GET | `/api/v1/history` | View history |
| GET | `/api/v1/consult/{id}` | Get details |
| DELETE | `/api/v1/consult/{id}` | Delete consultation |

### Prompt Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/prompts` | List prompts |
| POST | `/api/v1/prompts` | Create prompt |
| GET | `/api/v1/prompts/{id}` | Get prompt |
| PUT | `/api/v1/prompts/{id}` | Update prompt |

### Analytics Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/analytics/usage` | Usage stats |
| GET | `/api/v1/analytics/costs` | Cost report |

**For complete API reference, see [API.md](docs/API.md)**

---

## 📊 Features Deep Dive

### Prompt Engineering Console

Access at: `http://localhost:8000/console`

- **Prompt Builder**: Visual interface for creating prompts
- **Template Library**: Pre-built templates
- **Version Control**: Track and rollback changes
- **A/B Testing**: Compare prompt performance
- **Analytics**: Monitor effectiveness

See [PROMPTS.md](docs/PROMPTS.md) for detailed guide.

### Cost Optimization

Maypo includes built-in cost reduction strategies:
- Request caching (reduce duplicate calls by ~40%)
- Batch processing (reduces overhead)
- Smart model selection (balances cost vs quality)
- Token optimization (reduce usage by ~30%)
- Budget alerts (prevent overspending)

See [CONFIGURATION.md](docs/CONFIGURATION.md) for cost settings.

### Real-Time Analytics

Monitor key metrics:
- API usage and throughput
- Cost breakdown by model
- Response time statistics
- Error rates and alerts
- User activity logs

---

## 🚀 Deployment

### Quick Deployment Options

| Platform | Guide |
|----------|-------|
| **AWS** | [DEPLOYMENT.md](docs/DEPLOYMENT.md#aws) |
| **Azure** | [DEPLOYMENT.md](docs/DEPLOYMENT.md#azure) |
| **Heroku** | [DEPLOYMENT.md](docs/DEPLOYMENT.md#heroku) |
| **Docker** | [DEPLOYMENT.md](docs/DEPLOYMENT.md#docker) |

### Production Checklist

- [ ] Environment variables configured
- [ ] Database backups enabled
- [ ] SSL/TLS certificates installed
- [ ] Rate limiting enabled
- [ ] Monitoring configured
- [ ] Health checks enabled
- [ ] Auto-scaling policies set

See [DEPLOYMENT.md](docs/DEPLOYMENT.md) for complete instructions.

---

## 📈 Performance & Monitoring

### Health Check

```bash
curl http://localhost:8000/health
```

### Metrics

```bash
# Prometheus format
curl http://localhost:8000/metrics

# JSON format
curl http://localhost:8000/api/v1/metrics
```

### Common Metrics

- Response time: < 500ms
- API uptime: > 99.9%
- Cache hit rate: > 60%
- Error rate: < 0.1%

---

## 🐛 Troubleshooting

### Common Issues

**Issue: "API Key Invalid"**
```bash
# Verify key in .env
echo $OPENAI_API_KEY

# Test connection
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

**Issue: "Database Connection Failed"**
```bash
# Test connection
psql $DATABASE_URL -c "SELECT 1"

# Restart database
docker-compose restart db
```

**Issue: "Redis Timeout"**
```bash
# Test Redis
redis-cli ping

# Check status
docker-compose logs redis
```

For more troubleshooting, see [CONFIGURATION.md](docs/CONFIGURATION.md#troubleshooting)

---

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/maypo.git
   cd maypo
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature
   ```

3. **Make your changes**
   ```bash
   # Write code, add tests
   pytest --cov=src
   ```

4. **Commit and push**
   ```bash
   git commit -m "Add your feature"
   git push origin feature/your-feature
   ```

5. **Submit a Pull Request**
   - Provide clear description
   - Link related issues
   - Ensure tests pass

### Code Standards
- Follow PEP 8
- Add tests for new features
- Update documentation
- Run linting: `flake8 src/`

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### MIT License Summary
- ✅ Commercial use allowed
- ✅ Modification allowed
- ✅ Distribution allowed
- ✅ Private use allowed
- ⚠️ Requires license inclusion
- ❌ No warranty provided
- ❌ No liability

---

## 📞 Support & Contact

- **Issues**: [GitHub Issues](https://github.com/juicedUPDev/maypo/issues)
- **Discussions**: [GitHub Discussions](https://github.com/juicedUPDev/maypo/discussions)
- **Email**: support@maypo.ai
- **Website**: www.maypo.ai

---

## 🔗 Related Resources

- [Python Documentation](https://docs.python.org/3/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [OpenAI API Docs](https://platform.openai.com/docs/)
- [PostgreSQL Docs](https://www.postgresql.org/docs/)
- [Docker Docs](https://docs.docker.com/)

---

## 🙏 Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- AI models powered by [OpenAI](https://openai.com/)
- Database by [PostgreSQL](https://www.postgresql.org/)
- Caching with [Redis](https://redis.io/)
- Containerized with [Docker](https://www.docker.com/)

---

**Made with ❤️ by the juicedUp Team**

Last Updated: June 11, 2026 | Version: 1.0.0
