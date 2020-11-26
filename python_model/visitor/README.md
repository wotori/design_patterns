```if __name__ == "__main__":
    components = [Circle(), Rectangle(), Triangle()]

    print("The client code works with all visitors via the base Visitor interface:")
    visitor1 = ConcreteVisitor1()
    client_code(components, visitor1)
    print(visitor1.circle, visitor1.rectangle, visitor1.triangle)
```

```
The client code works with all visitors via the base Visitor interface:
Circle rectangle triangle
```