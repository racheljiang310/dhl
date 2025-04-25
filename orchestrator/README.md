# Orchestrator Service

## Architecture
[Host Server] → HTTP GET request → [API Server (Orchestrator)]
                                |
                                ├─ Looks up data location
                                ├─ Notifies correct cart(s)
                                └─ Awaits "delivery" (real or simulated)


## Tech Stack Recommendation
API Server: Python (with Flask) or Node.js
Cart Simulation: Local scripts that act as networked clients (These can be our clients)
Data Map: JSON files in local fs or something like that
Communication: REST (for MVP), upgrade to MQTT or WebSockets later


## Tree Diagram
/orchestrator/
├── orchestrator.py              # Main API server
├── requirements.txt             # Python dependencies
├── config/
│   └── sys_config.json          # Static config (zone, server names...)
├── datasets/
│   ├── name/...                 # Maps datasets to carts/SSDs
├── metadata/
│   └── metadata.json            # Cart metadata (status, SSDs, zones)
├── logs/
│   └── orchestrator.log         # Runtime logs from the API
├── scripts/
│   ├── simulate_cart.py         # Fake cart client for testing
│   └── ingest_dataset.py        # Register or update datasets
├── utils/
│   ├── file_ops.py              # File I/O and JSON helpers
│   └── routing_logic.py         # Smart cart selection (distance, load)
└── README.md                    # Project overview
