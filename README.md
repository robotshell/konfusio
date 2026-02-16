# Konfusio

**Konfusio** is a multi-ecosystem Dependency Confusion detection tool designed for serious Bug Bounty hunters and security researchers.

It crawls targets, discovers dependency manifests automatically, extracts real package names, checks the correct public registry for each ecosystem, and highlights **realistic Dependency Confusion risks**.

Konfusio focuses on **exploitable** scenarios, not noisy multi-registry guessing

---

## 🚀 Features

- Multi-registry support:
  - **npm** → JavaScript (.js, package.json, package-lock.json)
  - **PyPI** → Python (requirements.txt)
  - **Maven Central** → Java (pom.xml)
  - **RubyGems** → Ruby (Gemfile)
  - **Packagist** → PHP (composer.json)
  - **Go Modules** → Go (go.mod)
  - **NuGet** → .NET
- Single target or multiple targets from file
- Automatic crawling and manifest discovery
- Intelligent corporate-name heuristics
- Real Dependency Confusion detection (not artificial scoring)
- Shows exact vulnerable file
- JSON export support
- Registry caching to reduce duplicate queries
- Modular registry architecture

---

## 🧠 What is Dependency Confusion?

Dependency Confusion occurs when a private or internal package name is unintentionally exposed and does not exist in the corresponding public registry.

If an attacker registers that package name publicly, build systems may download the malicious version instead of the internal one.

Konfusio detects:

- Internal-looking package names

- Missing packages in public registries

- Exact source file where the dependency was found

- Ecosystem-specific exposure
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

JSON output
```bash
python main.py -u https://target.com --json report.json
```

## 🔍 Example Output
```bash
Scanning targets: 100%|████████████████|
Analyzing files (corp.com): 100%|████████████|

🔥 Potential Dependency Confusion Findings:

--------------------------------
Target     : https://corp.com
Package    : @corp/internal-auth
Ecosystem  : npm
Source file: https://corp.com/static/app.js
```

If no risks are found:

```
No Dependency Confusion risks detected.

```

## 📐 Risk Logic
A package is flagged when:

- It looks internal or corporate (e.g. scoped packages, internal keywords)

- It does NOT exist in its corresponding public registry

- It was found in a real dependency context (manifest or JS import)

Konfusio does NOT:

- Inflate scores artificially

- Flag public packages like jquery

- Check unrelated registries

- Generate noisy false positives

## 📜 License
MIT License

## 🛡️ Responsible Usage

This tool is intended for:
- Authorized security testing.
- Bug bounty programs within scope.
- Research environments.

Important: Do not publish or register potentially private packages without authorization. Always follow responsible disclosure policies.
