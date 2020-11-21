from python_model.state.context_and_state import Context, StatePrintFromUSB, StatePrintFromWiFi


class Machine():
    context = None
    payment_amount = 0
    doc_name = None

    def request_payment(self):
        while True:
            self.payment_amount = int(input("Введите средства для оплаты услуг печати:"))
            if self.payment_amount >= 10:
                print(f"Вы внесли {self.payment_amount} рублей")
                break
            else:
                print("Минимальная сумма для ввода - 10 рублей. Введите средства заново.")

    def select_mode(self):
        print("Выберете носитель:")
        selected_mode = int(input("1 - USB, 2 - WiFi:"))

        if selected_mode == 1:
            print("Вставлен USB носитель")
            self.context = Context(StatePrintFromUSB())

        if selected_mode == 2:
            print("Подключение к WiFi сети")
            self.context = Context(StatePrintFromWiFi())

    def pick_document(self):
        self.dock_name = str(input("Введите название документа"))
        print(f"Выбранный документ для печати: {self.dock_name}")

    def print_document(self):
        print(f"Процесс печати документа \"{self.dock_name}\" запущен")

    def return_cashe(self):
        print("Сдача: ", self.payment_amount - 10)

    def start(self, machine):
        machine.request_payment()
        machine.select_mode()
        machine.pick_document()
        machine.print_document()
        machine.return_cashe()
