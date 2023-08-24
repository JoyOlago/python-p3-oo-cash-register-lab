#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=20):
        self.total = 0
        self.item_count = 0
        self.discount = discount
        self.items = []

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        self.item_count += quantity
        self.items.extend([item] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            return f"After {self.discount}% discount: ${self.total:.2f}"
        else:
            return "No discount applied"

    def void_last_transaction(self):
        if self.item_count > 0:
            last_item = self.items[-1]
            last_item_price = self.total / self.item_count
            self.total -= last_item_price
            self.item_count -= 1
            self.items.remove(last_item)
        else:
            return "No items to void"
