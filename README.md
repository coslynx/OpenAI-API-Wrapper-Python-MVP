<div class="hero-icon" align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
</div>

<h1 align="center">
OpenAI-API-Wrapper-Python-MVP
</h1>
<h4 align="center">Streamlined Python Backend for Effortless OpenAI API Interactions</h4>
<h4 align="center">Developed with the software and tools below.</h4>
<div class="badges" align="center">
  <img src="https://img.shields.io/badge/Framework-FastAPI-blue" alt="FastAPI Framework" />
  <img src="https://img.shields.io/badge/Language-Python-red" alt="Python Language" />
  <img src="https://img.shields.io/badge/API-OpenAI-blue" alt="OpenAI API" />
  <img src="https://img.shields.io/badge/LLMs-GPT-3,_GPT-4-black" alt="Large Language Models" />
</div>
<div class="badges" align="center">
  <img src="https://img.shields.io/github/last-commit/coslynx/OpenAI-API-Wrapper-Python-MVP?style=flat-square&color=5D6D7E" alt="git-last-commit" />
  <img src="https://img.shields.io/github/commit-activity/m/coslynx/OpenAI-API-Wrapper-Python-MVP?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
  <img src="https://img.shields.io/github/languages/top/coslynx/OpenAI-API-Wrapper-Python-MVP?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</div>

## 📑 Table of Contents
- 📍 Overview
- 📦 Features
- 📂 Structure
- 💻 Installation
- 🏗️ Usage
- 🌐 Hosting
- 📄 License
- 👏 Authors

## 📍 Overview

This repository contains a Minimum Viable Product (MVP) called "OpenAI-API-Wrapper-Python-MVP" that simplifies interacting with OpenAI's powerful language models through a Python backend service. This MVP empowers developers to leverage AI capabilities without the complexity of directly working with the OpenAI API.

## 📦 Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The codebase follows a modular structure, separating functionalities into distinct modules for easier maintenance and scalability. |
| 📄 | **Documentation**  | This README.md file provides a detailed overview of the MVP, its dependencies, and usage instructions. |
| 🔗 | **Dependencies**   | The codebase relies on several external libraries and packages, including `fastapi`, `uvicorn`, `pydantic`, `openai`, and `requests`. |
| 🧩 | **Modularity**     | The modular structure allows for easier maintenance and reusability of the code, with separate directories and files for different functionalities. |
| 🧪 | **Testing**        | Includes unit tests to ensure the codebase is reliable and robust. |
| ⚡️  | **Performance**    | The MVP is optimized for performance and efficiency, using asynchronous processing and other techniques. |
| 🔐 | **Security**       | The code implements basic security measures such as API key management and input validation. |
| 🔀 | **Version Control**| Uses Git for version control and GitHub Actions for automated builds and releases. |
| 🔌 | **Integrations**   | Integrates seamlessly with the OpenAI API, enabling various AI tasks like text generation, translation, question answering, and code completion. |

## 📂 Structure

```text
├── main.py
├── routers
│   ├── models.py
│   ├── generate.py
│   ├── translate.py
│   ├── question.py
│   └── code.py
├── services
│   ├── openai_service.py
│   └── auth_service.py
├── models
│   ├── request.py
│   └── response.py
├── utils
│   ├── logger.py
│   ├── exceptions.py
│   ├── config.py
│   └── auth.py
└── tests
    └── test_main.py

```

## 💻 Installation

### 🔧 Prerequisites

- Python 3.9+
- A virtual environment (recommended)
- An OpenAI API key (obtain one from [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys))

### 🚀 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/coslynx/OpenAI-API-Wrapper-Python-MVP.git
   cd OpenAI-API-Wrapper-Python-MVP
   ```

2. **Create a virtual environment (optional):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   ```bash
   cp .env.example .env
   # Fill in your OpenAI API key:
   OPENAI_API_KEY=<your_openai_api_key>
   ```

## 🏗️ Usage

### 🏃‍♂️ Running the MVP

1. **Start the FastAPI server:**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

## 🌐 Hosting

### 🚀 Deployment Instructions

1. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   ```bash
   cp .env.example .env
   # Fill in your OpenAI API key and other necessary variables:
   OPENAI_API_KEY=<your_openai_api_key>
   ```

4. **Run the application:**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

## 📜 API Documentation

### 🔍 Endpoints

- **`/models`:** (GET) Returns a list of available OpenAI models.
- **`/generate`:** (POST) Generates text using a chosen OpenAI model.
- **`/translate`:** (POST) Translates text between languages.
- **`/question`:** (POST) Answers a question using an OpenAI model.
- **`/code`:** (POST) Generates code in a specified programming language.

### 🔒 Authentication

The API uses basic authentication. You need to provide your OpenAI API key in the request header:

```bash
Authorization: Bearer <your_openai_api_key>
```

### 📝 Examples

**Text Generation:**

```bash
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your_openai_api_key>" \
  -d '{"model": "text-davinci-003", "prompt": "Write a short story about a cat who goes on an adventure.", "temperature": 0.7}'
```

**Translation:**

```bash
curl -X POST http://localhost:8000/translate \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your_openai_api_key>" \
  -d '{"source_language": "en", "target_language": "fr", "text": "Hello, world!"}' 
```

**Question Answering:**

```bash
curl -X POST http://localhost:8000/question \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your_openai_api_key>" \
  -d '{"question": "What is the capital of France?"}'
```

**Code Generation:**

```bash
curl -X POST http://localhost:8000/code \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your_openai_api_key>" \
  -d '{"language": "python", "prompt": "Write a function that prints Hello World."}'
```

## 📜 License & Attribution

### 📄 License

This Minimum Viable Product (MVP) is licensed under the [GNU AGPLv3](https://choosealicense.com/licenses/agpl-3.0/) license.

### 🤖 AI-Generated MVP

This MVP was entirely generated using artificial intelligence through [CosLynx.com](https://coslynx.com).

No human was directly involved in the coding process of the repository: OpenAI-API-Wrapper-Python-MVP

### 📞 Contact

For any questions or concerns regarding this AI-generated MVP, please contact CosLynx at:
- Website: [CosLynx.com](https://coslynx.com)
- Twitter: [@CosLynxAI](https://x.com/CosLynxAI)

<p align="center">
  <h1 align="center">🌐 CosLynx.com</h1>
</p>
<p align="center">
  <em>Create Your Custom MVP in Minutes With CosLynxAI!</em>
</p>
<div class="badges" align="center">
  <img src="https://img.shields.io/badge/Developers-Drix10,_Kais_Radwan-red" alt="" />
  <img src="https://img.shields.io/badge/Website-CosLynx.com-blue" alt="" />
  <img src="https://img.shields.io/badge/Backed_by-Google,_Microsoft_&_Amazon_for_Startups-red" alt="" />
  <img src="https://img.shields.io/badge/Finalist-Backdrop_Build_v4,_v6-black" alt="" />
</div>