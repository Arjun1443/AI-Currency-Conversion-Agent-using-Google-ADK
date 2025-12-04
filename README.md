# AI Currency Conversion Agent using Google ADK

This repository contains an implementation of an **intelligent currency-conversion assistant** built using the **Google Agent Development Kit (ADK)**. The notebook demonstrates how to build a structured LLM agent capable of performing precise currency conversions, handling financial instructions, and executing requests with reasoning steps.

---

## ✔️ Key Features Implemented (Problems Solved)

### 1. Secure API Setup

* Loaded and configured **Google API Key** using **Kaggle Secrets**
* Added environment variable injection for ADK model authentication

### 2. Currency Conversion Agent

Created a specialized agent using the **Gemini model (`gemini-2.5-flash-lite`)** with:

* Step-by-step reasoning
* Exact arithmetic calculation
* Support for inputs containing commas (e.g., `1,250 USD`)
* Support for conversion methods (e.g., Cash, Bank Transfer, Online Payment)
* Response formatting logic

### 3. Enhanced Instruction Layer

The agent was upgraded with a clear instruction block:

* Understands multi-format numeric inputs
* Calculates conversion cleanly
* Provides final answer with exact math steps
* Behaves consistently and reliably

### 4. Error Handling & Retry Logic

Added robust retry configuration to handle:

* Temporary API unavailability
* Timeout scenarios
* Network variations in Kaggle environment

### 5. In-Memory Execution Runner

Used **InMemoryRunner** for debug-friendly execution:

```python
enhanced_runner = InMemoryRunner(agent=enhanced_currency_agent)
```

This allows:

* Full reasoning visibility
* Tracing each processing stage
* Reliable debugging and validation of agent behavior

### 6. Real Test Query

Executed a complete end-to-end test:

> Convert **1,250 USD to INR** using a **Bank Transfer** and show precise calculation.

The system calculates the amount using model-retrieved exchange rate + logic from instructions.

---

## 📂 Repository Contents

```
adk-2.ipynb   # Complete currency conversion agent implementation
```

---

## 🧠 Workflow Overview

1. Load API key from Kaggle Secrets
2. Initialize Gemini model with retry logic
3. Define `CurrencyConversionAgent` with improved instructions
4. Wrap agent in **InMemoryRunner**
5. Run conversion queries with detailed reasoning output

---

## 📝 How to Run

1. Open the notebook in **Kaggle** or **Jupyter Notebook**
2. Add your Google API key under:
   **Add-on → Secrets → GOOGLE_API_KEY**
3. Run all cells sequentially
4. Test the system with queries like:

```
"Convert 950 EUR to GBP using an Online Payment method."
```

5. View exact calculations and final converted result.

---

## 🔧 Possible Extensions

* Auto-fetching live forex rates
* Support for historical currency conversion
* Adding tax/fee simulation (bank fee, service fee, forex margin)
* Deployment as a microservice or FastAPI endpoint

---

## 📜 License

Open for educational, research, and personal use.
