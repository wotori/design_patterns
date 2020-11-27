from python_model.adapter.adapter import Adaptee, Adapter
from python_model.adapter.client import client_code
from python_model.adapter.target import Target

if __name__ == "__main__":
    print("Клиень может работать с целевыми объектами:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Клиент не понимает интерфейс класса Adaptee.")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Клиент может работать с Adaptee через адаптер")
    adapter = Adapter()
    client_code(adapter)
