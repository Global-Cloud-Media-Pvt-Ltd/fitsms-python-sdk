# FitSMS Python SDK (v4)

The official Python SDK for the [FitSMS.lk](https://fitsms.lk) gateway, maintained by **Global Cloud Media**. Seamlessly integrate SMS capabilities into your Python applications, automation scripts, and AI agents.

## Features
* **Sri Lankan Number Formatting**: Automatically handles `07...` and `7...` formats to the required `947...` standard.
* **v4 API Integration**: Fully compatible with the latest FitSMS REST API.
* **Lightweight**: Minimal dependencies (uses `requests`).
* **DevOps Ready**: Perfect for VPS monitoring and alert scripts.

---

## Installation

### From Source (Local Development)
```bash
git clone [https://github.com/Global-Cloud-Media-Pvt-Ltd/fitsms-python-sdk.git](https://github.com/Global-Cloud-Media-Pvt-Ltd/fitsms-python-sdk.git)
cd fitsms-python-sdk
pip install .