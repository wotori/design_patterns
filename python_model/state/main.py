from __future__ import annotations
from python_model.state.machine import Machine

if __name__ == "__main__":
    # Клиентский код.
    # context = Context(StatePrintFromUSB())
    # context.request1()
    # context.request2()

    machine = Machine()
    machine.start(machine)
    print(machine.context)
