```if __name__ == "__main__":
    components = [Circle(), Rectangle(), Triangle()]

    print("Клиентский код работает со всеми посетителями через базовый интерфейс посетителей::")
    visitor1 = ConcreteVisitor1()
    client_code(components, visitor1)
    print(visitor1.circle, visitor1.rectangle, visitor1.triangle)
```

```
Клиентский код работает со всеми посетителями через базовый интерфейс посетителей::
Circle rectangle triangle
```