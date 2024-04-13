"""Operators: Used to simplify operations like arthimetic, logical, assignment etc.,"""

#Deterimine if the shipping list item is eligible for free shipping & discount

def main():
    """Assignment operator"""
    #Set item name, quantity, item price, discount rate and eligible items
    item_name="Banana"
    quantity= 5
    item_price= 2 #USD
    discount_rate= 0.1
    eligible_items= "Orange Banana Carrot"

    """Arthimetic Operators"""
    #Calculate Subtotal
    Subtotal=quantity*item_price
    #Print Item name and Subtotal
    print(f"Item name : {item_name}, Subtotal : {Subtotal}")
    
    #Check if item name is eligible for discount
    if item_name in eligible_items:
        discount=Subtotal*discount_rate
    print(f"discount: {discount}")

    #Comparision operators
    #Check if discount applied (discount>0)
    was_discount_applied= discount>0
    print(f"was discount applied : {was_discount_applied}")

    #logical operators
    #Check if free shipping is eligible or not
    Does_free_shipping_apply= quantity>=5 and item_name=="Banana"
    print(f"Is this item eligible for free shipping ? {Does_free_shipping_apply}")

if __name__ == '__main__':
    main()


