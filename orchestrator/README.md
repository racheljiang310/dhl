# Orchestrator Service

## Architecture

```
[Host Server] → HTTP GET request → [API Server (Orchestrator)]
                                |
                                ├─ Looks up data location
                                ├─ Notifies correct cart(s)
                                └─ Awaits "delivery" (real or simulated)

```

## Tech Stack Recommendation
API Server: Python (with Flask) or Node.js
Cart Simulation: Local scripts that act as networked clients (These can be our clients)
Data Map: JSON files in local fs or something like that
Communication: REST (for MVP), upgrade to MQTT or WebSockets later


## Tree Diagram

```
/orchestrator/
├── README.md
├── cache.json
├── client.py
├── config
├── datasets/
│   ├── fake_real_tweets
│   └── gpt2_corpus
├── logs/
│   └── orchestrator.log
├── metadata.json
├── orchestrator.py
├── requirements.txt
├── scripts/
└── utils/
```
