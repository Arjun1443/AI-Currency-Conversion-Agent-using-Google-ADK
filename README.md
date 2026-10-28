# Currency Conversion Agent with Google ADK

[**Launch Currency Conversion Studio →**](https://ai-currency-conversion-agent-using-app-ad.streamlit.app/) · [Deployment guide](DEPLOYMENT.md)


## Interactive Streamlit app

A companion application is available in [streamlit_app/app.py](streamlit_app/app.py).

```bash
python -m pip install -r streamlit_app/requirements.txt
python -m streamlit run streamlit_app/app.py
```

This calculator uses Decimal arithmetic and a visitor-supplied rate. It does not run the ADK agent or fetch market rates.

See [DEPLOYMENT.md](DEPLOYMENT.md) for Community Cloud setup, validation coverage, and runtime requirements. Deployment URL supplied by the project owner: https://ai-currency-conversion-agent-using-app-ad.streamlit.app/


An educational notebook exploring a Gemini-powered agent for currency conversion prompts, input formatting, and retry configuration.

## Why this project matters

A focused task makes agent instructions, execution behavior, and failure cases easier to inspect.

## Technical focus

Python · Google ADK · Gemini · in-memory runner · retry configuration

## Explore the implementation

Open [the notebook](<AI Currency Conversion Agent using Google ADK.ipynb>) to inspect preprocessing, implementation, and saved outputs.

## Run locally

```bash
git clone https://github.com/Arjun1443/AI-Currency-Conversion-Agent-using-Google-ADK.git
cd AI-Currency-Conversion-Agent-using-Google-ADK
python -m venv .venv
# Activate .venv before continuing.
python -m pip install google-adk google-genai jupyter
python -m jupyter notebook
```

Select `AI Currency Conversion Agent using Google ADK.ipynb` in Jupyter and review its configuration before executing cells in order.

## Reproducibility notes

The notebook uses Kaggle Secrets for `GOOGLE_API_KEY`. In Kaggle, configure the secret before execution; outside Kaggle, adapt that cell to read an environment variable. A verified live exchange-rate feed is not integrated. Treat model-provided rates and arithmetic as demonstration output, not a financial quote. API access and model availability must be checked in your environment.

Saved notebook outputs describe a prior execution; they are not an independently reproduced benchmark. Dependency versions are not locked, so compatibility may require adjustment.


## Author

[Naga Anweesh Reddy](https://github.com/Arjun1443/Naga-Anweesh-Reddy) · AI development and technical training
