# Software API Ideas: Cart/DHL_Home Server
---
## Architecture of Cart/SSD Server

### Inventory (Storage/DB):
* Knows existence of SSD Controller:
  * SSD (self) knows: id, state (free/in use), data storage, health, etc...
* Lookup Table: SSD containing data → Cart (know which to dispatch)

### Everything Else:
* REST or gRPC API?
* Mapping Table: potential lookup table in case the data request doesn't name the SSD-id, but, say, a directory or sth...
* Request Queue: buffer storing all the incoming server requests for cart data
* Dispatch Queue: buffer storing all the carts that will be dispatched to servers
* Routing Engine: formualate optimal routes for the cart to travel (this doesn't need to be super complex)
* Location Tracking: (could be a bonus) tracks where in-use ssd carts are currently located
---
## Flow

1. Server requests dataset X (via API)
2. API → Request Queue
3. Background worker:
   a. Look up SSDs that contain X
   b. Route carts from location source → destination
   c. Reserve SSD cart
   d. Add task to Dispatch Queue
4. Dispatch Queue entry → now a cart job
5. Cart with SSD → updates status via API
6. Cart moves
7. Cart docks → data transfer
8. Cart undocks → data transfer complete
9. Cart returns → updates status

```
POST /request-datasets
{
  "server_id": "ml-node-12", # source
  "directory": ["imagenet_train"]
}
```
```
→ Response:
{
  "status": 3,
  "cart_id": "cart-23",
  "server-id": "ml-node-12",
}
```
---
## Models
```
ENUM{ FREE, QUEUE, FLIGHT, DOCKED, TRANSFER } # cart status

# Lookup table between dataset name and cart location
ssd_datasets = Table(
    "cart_datasets", Base.metadata,
    Column("cart_id", FK("cart.id"), pk=True),
    Column("db_name", string?, pk=True)
)

class Cart(Base):
    __tablename__ = "carts"
    id = Column(int, pk=True)
    status = Column(String, default=FREE)
    ssds = relationship("SSD", bp="cart")

class SSD(Base):
    __tablename__ = "ssds"
    id = Column(int, pk=True)
    health = Column(String)
    storage_used = Column(int)
    cart_id = Column(int, FK("v.id"))

    cart = relationship("Cart", bp="ssds")
    # dataset_tags = ? Needed?
```
---
## Requests/Responses Formatting
```
class CartRequest(BaseModel):
    server_id: str
    datasets: List[str]

class CartResponse(BaseModel):
    assigned_cart_id: Optional[int]
    server-id: Optional[str]
    status: int

class Dispatch(BaseModel):
    cart_id: Optional[int]
    server-id: Optional[str]

class PingCart(BaseModel):
    cart_id: Optional[int]
    server-id: Optional[str]
    start-time: int
```
