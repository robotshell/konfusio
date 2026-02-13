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

Multi-registry scanning
```bash
python main.py -u https://target.com --multi
```

Aggressive mode
```bash
python main.py -u https://target.com --multi --aggressive
```

JSON output
```bash
python main.py -u https://target.com --json output.json
```

## 🔍 Example Output
```bash
Target: https://example.com
JS files: 42
Dependencies found: 87
Potential risks: 5

[HIGH]   @acme/internal-auth (npm=False, PyPI=True, Maven=False) Score: 10
[MEDIUM] acme-logger (npm=False, PyPI=False) Score: 6
[LOW]    lodash (npm=True) Score: 1
```

## 📐 Scoring Logic
- Registry not found → +5 per registry
- Private registry detected → +5
- Name contains company hint → +3

Severity:
- 8+ → HIGH
- 4–7 → MEDIUM
- 0–3 → LOW

## 📜 License
MIT License

## 🛡️ Responsible Usage

This tool is intended for:
- Authorized security testing.
- Bug bounty programs within scope.
- Research environments.

Important: Do not publish or register potentially private packages without authorization. Always follow responsible disclosure policies.
