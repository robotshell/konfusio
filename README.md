# Konfusio

**Konfusio** is a multi-ecosystem Dependency Confusion hunting tool for Bug Bounty hunters and security researchers.

It crawls targets, extracts dependencies, checks multiple public registries, and highlights potential supply-chain risks.

---

## 🚀 Features

- Multi-registry support:
  - **npm** → JavaScript
  - **PyPI** → Python
  - **Maven Central** → Java
  - **RubyGems** → Ruby
  - **Packagist** → PHP
  - **Go Modules** → Go
  - **NuGet** → .NET
- Single URL or multiple targets
- Direct JS or source file analysis
- Sourcemap support for real dependency detection
- Detection of private/internal registries
- Multi-threaded HTTP requests
- Intelligent scoring system
- JSON and CLI output
- Extensible modular registry architecture

---

## 🧠 What is Dependency Confusion?

Dependency Confusion occurs when private/internal package names are accidentally exposed and claimed in public registries. Konfusio helps identify these risks across multiple languages and ecosystems.

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/konfusio.git
cd konfusio
pip install -r requirements.txt
```

## ⚙️ Usage
Scan a single target
```bash
python main.py -u https://target.com
```

Scan multiple targets
```bash
python main.py -l targets.txt
```

Analyze direct JS file list
```bash
python main.py --js-list js.txt
```

## 🔍 Example Output
```bash
[HIGH]   @company/internal-auth   | Exists: False | Score: 10
[MEDIUM] company-logger           | Exists: False | Score: 6
[LOW]    lodash                   | Exists: True  | Score: 1
```

## JSON Output
Generate structured output:
```bash
python main.py -u [https://target.com](https://target.com) --json output.json
```

## 📜 License
MIT License

## 🛡️ Responsible Usage

This tool is intended for:
- Authorized security testing.
- Bug bounty programs within scope.
- Research environments.

Important: Do not publish or register potentially private packages without authorization. Always follow responsible disclosure policies.
