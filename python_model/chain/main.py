from __future__ import annotations

from python_model.chain.client import client_code
from python_model.chain.handlers import MoneySpliter

if __name__ == "__main__":
    money_spliter = MoneySpliter()

    client_code(money_spliter, currency="RUB", money_amount=2050)
    print("\n")

    client_code(money_spliter, currency="USD", money_amount=2003)
