# Design Patterns

## Strategy
You take a class that performs a specific task in different ways and extract those functions into separate classes called Strategies.
The original class (context) must have a reference to one of these strategies.
The context delegates the work to a strategy object instead of executing it itself.
The client passes the desired strategy to the context; the context doesn't know much about the strategies, it works with them through a generic interface.
The context is independent of the strategies, so it can add new algorithms or modify existing ones without modifying the context class.

