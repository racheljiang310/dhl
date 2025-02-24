# Integration / Schemas
---
## Server Request / Response

1. Request Metadata for location of data

```
Headers: {
  "dataset_id": "meta_spy_db",
  "file_path": "/training/batch_01",
  "requested_blocks": [0, 1, 2, 3], 
  "requesting_server_id": "ai-gpu-node-01"
}

```

2. Response metadata for location of data

```
   {
  "status": "success",
  "file_path": "/training/batch_01",
  "cart_locations": [
    {
      "cart_id": "cart-07",
      "ssds": [
          {
            "ssd-id": 2
            "offset": 4096,
            "block_size": 8192,
          },
          {
            "ssd-id": 3
            "offset": 2048,
            "block_size": 1024,
          },
      ],
    },
    { ... }
  ],
  "replica_count": 2,       // this could be optional
  "best_cart": "cart-07"    // this could be optional
}
```

3. Request data dispatch to cart controller server
```
{
  "cart_id": "cart-07"
  "requesting_server_id": "ai-gpu-node-01"
}
```
4. Cart controller server
   - checks if cart is stationed
   - checks if data in cart is "valid"
   - route cart path, configure route
   - dispatch cart onto rails on rails track
   - "ACK" the request and send dispatch start time, marks cart id busy

5. Cart arrives at dockings station @ rack R, server S
   - Server broadcasts for ssd_ids => wait for correct SSD to ACK
```
{
  "from": "ai-gpu-node-01"
  "ssd-id": "ssd-01"
},
{
  "from": "ai-gpu-node-01"
  "ssd-id": "ssd-05"
},
{
  "from": "ai-gpu-node-01"
  "ssd-id": "ssd-07"
}
```
   - Connections made => correct SSDs communicate with the server
```
{
  "from": "ssd-01"
  "to": "ai-gpu-node-01"
  "response": "ACK"
}
```

Network Switching - Multistops fit into this model? Maybe reroute on demand
  
7. Cart undocks from the station/zone
8. Server acknowledges to cart server of completion
9. Cart controller server routes cart / configures path
10. Cart controller maglev swooshes back to cart home => cart server marks cart id not busy
