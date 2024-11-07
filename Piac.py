class Product:
    def __init__(self, product_id, price, quantity):
        self.product_id = product_id
        self.price = price
        self.quantity = quantity

    def get_revenue(self):
        return self.price * self.quantity

class Trader:
    def __init__(self, trader_id):
        self.trader_id = trader_id
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_total_revenue(self):
        total = 0
        for product in self.products:
            total += product.get_revenue()
        return total

    def count_unique_high_priced_products(self, other_traders):
        unique_count = 0
        for product in self.products:
            is_unique = True
            for other_trader in other_traders:
                if other_trader.trader_id == self.trader_id:
                    continue
                for other_product in other_trader.products:
                    if other_product.product_id == product.product_id and other_product.price >= product.price:
                        is_unique = False
                        break
                if not is_unique:
                    break
            if is_unique:
                unique_count += 1
        return unique_count

class Market:
    def __init__(self, product_to_analyze):
        self.traders = []
        self.product_to_analyze = product_to_analyze

    def add_trader(self, trader):
        self.traders.append(trader)

    def get_above_average_revenue_traders(self):
        total_revenue = 0
        for trader in self.traders:
            total_revenue += trader.get_total_revenue()

        if len(self.traders) > 0:
            average_revenue = total_revenue / len(self.traders)
        else:
            average_revenue = 0

        above_average_traders = []
        for trader in self.traders:
            if trader.get_total_revenue() > average_revenue:
                above_average_traders.append(trader.trader_id)

        above_average_traders.sort()
        return above_average_traders

    def get_product_with_highest_quantity(self):
        max_quantity = -1
        trader_id_with_max_quantity = -1

        for trader in self.traders:
            for product in trader.products:
                if product.product_id == self.product_to_analyze:
                    if product.quantity > max_quantity:
                        max_quantity = product.quantity
                        trader_id_with_max_quantity = trader.trader_id
                    elif product.quantity == max_quantity and trader.trader_id < trader_id_with_max_quantity:
                        trader_id_with_max_quantity = trader.trader_id

        return trader_id_with_max_quantity

    def get_trader_with_most_unique_high_priced_products(self):
        max_unique_count = 0
        trader_id_with_most_unique = -1

        for trader in self.traders:
            unique_count = trader.count_unique_high_priced_products(self.traders)
            if unique_count > max_unique_count or (unique_count == max_unique_count and trader.trader_id < trader_id_with_most_unique):
                max_unique_count = unique_count
                trader_id_with_most_unique = trader.trader_id

        return trader_id_with_most_unique

# Főprogram a bemenet feldolgozásához és eredmények kiírásához
def main():
    # Első sor beolvasása
    first_line = input().strip().split()
    number_of_traders = int(first_line[0])
    number_of_products = int(first_line[1])
    product_to_analyze = int(first_line[2])

    market = Market(product_to_analyze)

    # Kereskedők és termékek beolvasása
    for i in range(number_of_traders):
        trader_info = list(map(int, input().strip().split()))
        product_count = trader_info[0]
        trader = Trader(i + 1)

        for j in range(product_count):
            product_id = trader_info[1 + j * 3]
            price = trader_info[2 + j * 3]
            quantity = trader_info[3 + j * 3]
            product = Product(product_id, price, quantity)
            trader.add_product(product)

        market.add_trader(trader)

    # Eredmények kiírása
    above_average_traders = market.get_above_average_revenue_traders()
    print(len(above_average_traders), end=' ')
    print(" ".join(map(str, above_average_traders)))

    product_with_highest_quantity = market.get_product_with_highest_quantity()
    print(product_with_highest_quantity)

    trader_with_most_unique_high_priced = market.get_trader_with_most_unique_high_priced_products()
    print(trader_with_most_unique_high_priced)


# Program indítása
if __name__ == "__main__":
    main()