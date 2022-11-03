melon_cost = 1.00

customer1_name = "Joe"
customer1_melons = 5
customer1_paid = 5.00

customer2_name = "Frank"
customer2_melons = 6
customer2_paid = 6.00

customer3_name = "Sally"
customer3_melons = 3
customer3_paid = 3.00

customer4_name = "Sean"
customer4_melons = 9
customer4_paid = 9.50

customer5_name = "David"
customer5_melons = 4
customer5_paid = 4.00

customer6_name = "Ashley"
customer6_melons = 3
customer6_paid = 2.00


def customer_payments(customers_orders_file):
    melon_cost = float(int(1.00))
    customers_orders = open(customers_orders_file)
    
    for line in customers_orders:
        line = line.rstrip()
        words = line.split('|')

        
        customer_name = words[1]
        count = int(words[2])
        customer_payment= float(words[3])
        customer_expected = melon_cost * count
        if customer_expected != customer_payment:
            print(f"{customer_name} paid ${customer_payment: .2f},",
                f"expected ${customer_expected: .2f}")
       
    customers_orders.close()   
customer_payments("customer-orders.txt")
