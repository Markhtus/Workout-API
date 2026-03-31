# 🏋️‍♂️ Workout API

[![Status](https://img.shields.io/badge/status-active-green)](https://github.com/)
[![Python](https://img.shields.io/badge/Python-3.12%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.135%2B-brightgreen)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.48%20Async-orange)](https://www.sqlalchemy.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-v2.12%2B-yellow)](https://docs.pydantic.dev/)
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue)](https://docs.docker.com/compose/)

API REST moderna desenvolvida com **FastAPI**, **SQLAlchemy Async**, **PostgreSQL** e **Docker Compose**.  
Gerencia **atletas**, **categorias** e **centros de treinamento** de forma assíncrona, segura e escalável.

## 🚀 Quickstart

```bash
git clone <repo>
cd Workout_API
docker compose up -d
```

Acesse:  
➡ **API**: http://localhost:8000  
➡ **Swagger Docs**: http://localhost:8000/docs  
➡ **ReDoc**: http://localhost:8000/redoc  

**DB**: localhost:5432 (user: `workout`, pass: `workout`, db: `workout`)

---

## 📚 Conteúdo

- [⚙ Tecnologias](#-tecnologias)
- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
- [🧠 Arquitetura](#-arquitetura)
- [📌 Endpoints](#-endpoints)
- [🗃 Modelos e Relacionamentos](#-modelos-e-relacionamentos)
- [🐳 Docker](#-docker)
- [🔐 Variáveis de Ambiente](#-variáveis-de-ambiente)
- [🗄 Banco PostgreSQL](#-banco-postgresql)
- [🚀 Desenvolvimento Local](#-desenvolvimento-local)
- [🧪 Testes](#-testes)
- [📈 Migrations](#-migrations)
- [🧹 Gerenciar Containers](#-gerenciar-containers)
- [🤝 Contribuição](#-contribuição)
- [✨ Autor](#-autor)

## ⚙ Tecnologias

| Categoria | Tecnologias |
|-----------|-------------|
| **Backend** | Python 3.12+, FastAPI 0.135+, Uvicorn 0.42+ |
| **Banco** | PostgreSQL 11-alpine, SQLAlchemy 2.0.48 (Async), asyncpg 0.31+ |
| **Validação** | Pydantic v2.12+ |
| **Migrations** | Alembic 1.18+ |
| **DevOps** | Docker, Docker Compose |
| **Outros** | python-dotenv, greenlet, h11, starlette 0.52+ |

## 📁 Estrutura do Projeto

```
Workout_API/
├── README.md
├── docker-compose.yml
├── requirements.txt
├── alembic.ini
├── alembic/
│   ├── env.py
│   ├── versions/
│   │   └── 8e5a88f8a980_init_db.py
├── workout_api/
│   ├── __init__.py
│   ├── main.py                 # FastAPI app
│   ├── routers.py              # API Router principal
│   ├── configs/
│   │   ├── __init__.py
│   │   ├── settings.py         # Configs/Pydantic Settings
│   │   └── database.py         # DB engine/session
│   ├── contrib/
│   │   ├── __init__.py
│   │   ├── dependencies.py     # Deps FastAPI
│   │   ├── models.py           # Base models
│   │   └── repositorie/        # Repositórios
│   │       ├── __init__.py
│   │       └── models.py
│   ├── atleta/                 # Atletas CRUD
│   │   ├── __init__.py
│   │   ├── controller.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── categorias/             # Categorias
│   │   ├── __init__.py
│   │   ├── controller.py
│   │   ├── models.py
│   │   └── schemas.py
│   └── centro_treinamento/     # Centros
│       ├── __init__.py
│       ├── controller.py
│       ├── models.py
│       └── schemas.py
└── make.bat
```

## 🧠 Arquitetura

Arquitetura limpa e desacoplada (Controller → Repository → Model → DB):

```
[Client] → FastAPI (Routers) → Controllers → Dependencies → Repos → SQLAlchemy Models → PostgreSQL (asyncpg)
                    ↓
               Pydantic Schemas (In/Out)
```

- **Controllers**: Lógica de negócio, endpoints.
- **Schemas**: Validação/serialização.
- **Models**: ORM com relacionamentos.
- **Configs**: Settings via .env.
- **Async**: Full async stack.

## 📌 Endpoints

| Recurso | Método | Caminho | Descrição | Exemplo cURL |
|---------|--------|---------|-----------|--------------|
| **Atletas** | POST | `/atletas/` | Criar atleta | `curl -X POST http://localhost:8000/atletas/ -H "Content-Type: application/json" -d '{"nome": "João", "categoria_id": 1}'` |
| | GET | `/atletas/` | Listar todos | `curl http://localhost:8000/atletas/` |
| | GET | `/atletas/{id}` | Buscar por ID | `curl http://localhost:8000/atletas/1` |
| | PATCH | `/atletas/{id}` | Atualizar | `curl -X PATCH http://localhost:8000/atletas/1 -d '{"nome": "João Silva"}'` |
| | DELETE | `/atletas/{id}` | Deletar | `curl -X DELETE http://localhost:8000/atletas/1` |
| **Categorias** | POST | `/categorias/` | Criar categoria | Similar acima |
| | GET | `/categorias/` | Listar | - |
| | GET | `/categorias/{id}` | Por ID | - |
| **Centros** | POST | `/centros_treinamento/` | Criar centro | - |
| | GET | `/centros_treinamento/` | Listar | - |
| | GET | `/centros_treinamento/{id}` | Por ID | - |

**Tags**: `/atletas`, `/categorias`, `/centros_treinamento`. Veja Swagger para schemas completos.

## 🗃 Modelos e Relacionamentos

- **Atleta**: id, nome, email?, categoria_id (FK), centro_treinamento_id (FK)
- **Categoria**: id, nome
- **CentroTreinamento**: id, nome, endereco?

Relacionamentos:  
`Atleta.belongs_to Categoria` | `Atleta.belongs_to CentroTreinamento`

## 🐳 Docker

```bash
docker compose up -d  # Build & start
docker compose logs api  # Logs
```

Serviços: `api` (FastAPI), `db` (PostgreSQL).

## 🔐 Variáveis de Ambiente

Crie `.env`:

```
DB_URL=postgresql+asyncpg://workout:workout@localhost/workout
# Ou via Docker: postgresql+asyncpg://workout:workout@db:5432/workout
```

## 🗄 Banco PostgreSQL

- **Host**: localhost (5432)
- **DB**: workout
- **User/Pass**: workout/workout
- **Image**: postgres:11-alpine
- Ferramentas: DBeaver, pgAdmin.

## 🚀 Desenvolvimento Local (sem Docker)

```bash
python -m venv venv
venv\\Scripts\\activate  # Windows
pip install -r requirements.txt
alembic upgrade head
uvicorn workout_api.main:app --reload --port 8000
```

Atualize `configs/settings.py` DB_URL para local.

## 🧪 Testes

```bash
docker compose exec api pytest -v
# Ou local: pytest
```

## 📈 Migrations

```bash
docker compose exec api alembic revision --autogenerate -m "msg"
docker compose exec api alembic upgrade head
```

## 🧹 Gerenciar Containers

```bash
docker compose down
docker compose down -v  # Remove volumes/DB
docker compose restart
```

## 🤝 Contribuição

1. Fork → Clone → Branch
2. `docker compose up`
3. Code → Test → Commit → PR
4. Siga [PEP8](https://peps.python.org/pep-0008/), adicione testes.

Issues/PRs bem-vindos!

## ✨ Autor

**Marcus**  
Desenvolvido para estudos em FastAPI Async + Docker.   


