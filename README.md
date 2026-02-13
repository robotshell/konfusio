# konfusio
# Konfusio

Konfusio is a minimalistic yet solid Dependency Confusion hunting tool designed for Bug Bounty hunters and offensive security researchers.

It automatically crawls a target, extracts JavaScript dependencies, checks them against the public npm registry, and highlights potential Dependency Confusion risks.

---

## 🚀 Features

- Single URL scanning
- Bulk target scanning
- Direct JavaScript file analysis
- Automatic JS discovery via crawling
- Dependency extraction (ES6, CommonJS, dynamic imports)
- Public npm registry verification
- Intelligent scoring system
- JSON output support
- Clean modular architecture

---

## 🧠 What is Dependency Confusion?

Dependency Confusion is a supply-chain attack technique where internal/private package names are accidentally exposed and can be claimed in public registries.

This technique was popularized by security researcher Alex Birsan.

Konfusio helps identify potentially exposed internal package names from frontend JavaScript assets.

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/konfusio.git
cd konfusio
pip install -r requirements.txt
