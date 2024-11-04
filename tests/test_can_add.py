from shopping_cart import ShoppingCart

def test_can_add_to_cart():
    cart=ShoppingCart()
    cart.add("Apple")
    # cart.add("Banana")

    assert cart.size()==1