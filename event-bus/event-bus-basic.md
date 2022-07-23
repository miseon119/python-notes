# Event Bus Basic

## Core Components

![core components](https://images.squarespace-cdn.com/content/v1/5c6981e251f4d413f6629afd/1613317033757-GYESUW4NAULS9ER0MUG2/Blank+diagram+%283%29.png?format=500w)

An event bus is an important piece of the event-based architecture puzzle. It is the middleman, with the responsibility of matching the correct event generator (emitter) to the correct event consumer (listener), through an event identifier or key (event_name). 

Event bus requires:
1. A way to add and remove **listeners**. 

2. A means to track what kind of events these listeners are interested in. These kinds of events are identified by a unique key, referred to above as the event_name. 

3. A way for event generators to fire events, and for these events to be matched directly to the listeners that are interested in them, through a unique key.

## EVENT BUS CLASS

UML Class Diagram:
![class diagram](https://images.squarespace-cdn.com/content/v1/5c6981e251f4d413f6629afd/1613316774251-KH0P32YSU6QZ6B2ZF4E1/Blank+diagram+%282%29.png?format=500w)


```python
class EventBus():
  def __init__(self):
    self.listeners = {}

  def add_listener(self, event_name, listener):
    # ...

  def remove_listener(self, event_name, listener):
    # ...

  def emit(self, event_name, event):
    # ...
```

PYTHON IMPLEMENTATION

```python
import asyncio

class EventBus():
  def __init__(self):
    self.listeners = {}

  def add_listener(self, event_name, listener):
    if not self.listeners.get(event_name, None):
      self.listeners[event_name] = {listener}
    else:
      self.listeners[event_name].add(listener)

  def remove_listener(self, event_name, listener):
    self.listeners[event_name].remove(listener)
    if len(self.listeners[event_name]) == 0:
      del self.listeners[event_name]

  def emit(self, event_name, event):
    listeners = self.listeners.get(event_name, [])
    for listener in listeners:
      asyncio.create_task(listener(event))
```

- LISTENER HAS TO BE AN ASYNC FUNCTION: note that listener is actually an async function, rather than an object instance. 
- EACH LISTENER IS ADDED TO A SET: we add each listener to a set, rather than a list. This allows for efficient lookup. This is possible because each function in Python has its own method address, which can act as a unique key. This naturally means that addition and removal are cheap, and has the added benefit of disallowing repeat listens by the same function. 
- EMIT IS NOT ASYNCHRONOUS: Notice that emit is not an async function. This is because we do not want to block the event bus’ loop while waiting for a fired event to return. Instead, we create a task, spinning off the subroutine returned when we call the listener. This way events can happen in parallel without blocking each other. 