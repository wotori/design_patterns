from __future__ import annotations

from python_model.state.context_and_state import Context, StatePrintFromUSB

if __name__ == "__main__":
    # Клиентский код.
    context = Context(StatePrintFromUSB())
    context.request1()
    context.request2()
