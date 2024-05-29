## Central Hash

<div align="center">
  <a href="https://pypi.org/project/fastapi/" target="_blank"><img src="https://img.shields.io/pypi/v/fastapi?style=flat-square" alt="PyPI Version"/></a>
  <a href="https://pypi.org/project/fastapi/" target="_blank"><img src="https://img.shields.io/pypi/l/fastapi?style=flat-square" alt="Package License"/></a>
  <a href="https://discord.gg/pdHUXqNY" target="_blank"><img src="https://img.shields.io/badge/discord-online-brightgreen.svg?style=flat-square" alt="Discord"/></a>
</div>

**Project Description:**

Central Hash is an innovative open-source software project that aims to revolutionize hash management by centralizing it. With a focus on security, efficiency, and scalability, Central Hash empowers organizations to streamline and optimize their hash management processes, making it an indispensable tool for cybersecurity.

**Key Features:**

- **Centralized Hash Management:** CentralHash provides a secure and centralized backend for hash management.

- **Scalability:** Built to handle large datasets, CentralHash can scale to accommodate the growing needs of your organization.

- **Security:** Security is our top priority. CentralHash employs robust encryption and access control measures to protect the keys.

- **Open Source:** Central Hash is open-source, providing transparency and the flexibility to customize the software to your organization's unique requirements.

**Getting Started:**

To get started with Central Hash, follow the installation guide and documentation below.

## Installation

```bash
$ docker-compose up
```

## Development

Activate the virtual environment:

```bash
centralhash\Scripts\activate
```

## Folder Structure

```
central_hash_api/
├── app/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── database.py
│   ├── errors/
│   │   ├── __init__.py
│   │   ├── handlers.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── post.py
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── post.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │       ├── __init__.py
│   │       ├── models/
│   │           ├── __init__.py
│   │           ├── user.py
│   │       ├── endpoints/
│   │           ├── __init__.py
│   │           ├── access.py
│   │           ├── agents.py
│   │           ├── router.py
│   │           ├── auth.py
│   │           ├── configuration.py
│   │           ├── endpoints.py
│   │           ├── files.py
│   │           ├── hashlists.py
│   │           ├── tasks.py
│   │           ├── users.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── calculations.py
│   │   ├── cache.py
│   ├── main.py
│   └── logging.conf
├── database/
│   ├── initialize_db.py
│   ├── docker-compose.mssql.yml
│   ├── docker-compose.mysql.yml
│   ├── docker-compose.postgres.yml
│   ├── schema.sql
├── tests/
│   ├── __init__.py
│   ├── test_user.py
│   ├── test_post.py
├── alembic/
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
├── alembic.ini
├── docker-compose.yml
├── docker-entrypoint.sh
├── Dockerfile
├── prometheus.yml
├── requirements.txt
└── README.md
```

## Basic Running Commands

### Access Documentation

- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Access Monitoring

Prometheus: [http://127.0.0.1:9090](http://127.0.0.1:9090)

Grafana: [http://127.0.0.1:3000](http://127.0.0.1:3000)

### Development

```bash
uvicorn app.main:app --reload
```

**Contributions:**

We welcome contributions from the open-source community. If you have ideas, bug fixes, or feature requests, please submit a pull request or open an issue on our GitHub repository.

**License:**

CentralHash is distributed under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute it as needed.
