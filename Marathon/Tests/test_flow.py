def test_flow_add_to_cart(py, marathon):
    marathon.goto()
    marathon.home.add_to_cart()
    marathon.home.open_cart()

    assert py.contains('Ваш вибір:')


def test_flow_checkout(py, marathon):
    test_flow_add_to_cart(py, marathon)
    marathon.cart.open_checkout()
    marathon.cart.checkout_authorization('abramenko.mariia@gmail.com', '123456')
    marathon.cart.checkout_flow('mariia', 'ilchenko')
    marathon.cart.checkout_delivery()
    assert py.contains('Мне можно не перезванивать, информировать через SMS')

    # .shipping_method_box:nth-of-type(5)
