# Design Patterns

## Strategy
You take a class that performs a specific task in different ways and extract those functions into separate classes called Strategies.
The original class (context) must have a reference to one of these strategies.
The context delegates the work to a strategy object instead of executing it itself.
The client passes the desired strategy to the context; the context doesn't know much about the strategies, it works with them through a generic interface.
The context is independent of the strategies, so it can add new algorithms or modify existing ones without modifying the context class.

## Decorator
O Decorator é uma padrão estrutural que permite que você acople novos comporatmentos para objetos ao colocá-los dentro de invólucros de objetos que contêm esses comportamentos.
Usar quando precisa ser capaz de projectar comportamentos adicionais para objetos em tempo de execução sem quebrar o código que usa esses objetos.
Utilize o padrão Decorator quando é complicado ou impossível estender o comportamento de um objeto usando herança.
Conhecido como **Wrapper**:
- anexe novas responsabilidades a um objeto dinamicamente.
- altere o comportamento de um objeto sem criar uma nova subclasse
- combine vários comportamentos embrulhando um objeto em vários decoradores.

## Abstract Factory
O padrão Abstract Factory é um padrão criacional que resolve o problema de criar familias inteiras de produtos sem especificar suas classes concretas.
Define uma interface para criar todos os produtos distintos, mas deixa a criação real do produto para classes fábricas concretas.
O código cliente chama os métodos de criação de um objeto fábrica em vez de criar produtos diretamente com uma chamada de construtor.
O código cliente permite que o mesmo código cliente funcione com produtos diferentes. Você apenas cria uma nova classe fábrica concreta e passa para o código cliente.

No caso do Python não é recomendado o uso desse padrão, pois a linguagem já possui mecanismos nativos que facilitam a criação de objetos sem a necessidade de uma fábrica abstrata, inclusive existe métodos pythonicos para isso como o uso de funções.