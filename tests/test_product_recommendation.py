from tools.product_recommendation_tool import product_recommendation


def test_product_recommendation():
    query = "smartphone gaming budget 5 juta"

    result = product_recommendation(query)

    print("\n=== TEST PRODUCT RECOMMENDATION ===")
    print(result)

    assert "Smartphone A" in result
    assert "Smartphone B" in result
    assert "Smartphone D" in result

    # Smartphone C harganya Rp5.499.000,
    # sehingga tidak boleh muncul untuk budget Rp5 juta
    assert "Smartphone C" not in result

    print("Product recommendation test: PASSED ✅")


if __name__ == "__main__":
    test_product_recommendation()