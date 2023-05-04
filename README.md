# Ask Question to a Novel

A (more substantial) [Langchain](https://python.langchain.com/en/latest/getting_started/getting_started.html) experiment.

Create a vectorstore embedding of a document, then query the document.

The current prompt is a question on one of the main characters of [In Another World With My Smartphone](https://en.wikipedia.org/wiki/In_Another_World_with_My_Smartphone).

## Installation

1. On a Python virtual environment, run

```bash
pip install -r requirements.txt
```

2. Copy `example.env` to `.env` and add your OpenAPI API key.

## Setting up the vector store

After setting up the document you want to load, run the following command on a Python virtual environment.

```bash
python3 create_embedding.py
```

It defaults to looking for an epub file named `vol01.epub`.

## Running it

```bash
python3 main.py
```

## Tracing

If you need tracing for some reason:

1. Run the following command

```bash
docker-compose up
```

2. Change the `LANGCHAIN_TRACING` key on `.env` to `true`
