from python_model.chain.handlers import Handler


def client_code(handler: Handler, currency, money_amount) -> None:
    print(f"\nКилент запросил {currency} в размере: {money_amount}")
    result = handler.handle(money_amount)
    if result:
        print(f"Запрошенная сумма выдана. Операция завершена", end="")
    else:
        print(f"Банкомат не может выдать введённую сумму: {money_amount}. Операция отменена.", end="")
