
import e_commerse_utils as ecu

# Shopping cart (dictionary)
cart = {
    "Laptop": 55000,
    "Phone": 30000,
    "Headphones": 2000
}

ecu.generate_invoice(cart, discount_percent=10, gst_percent=18)
