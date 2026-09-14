from tools.common_information_tool import common_information


def test_common_information():
    print("\n=== TEST COMMON INFORMATION ===")

    # Test 1: Tracking pesanan
    result_tracking = common_information(
        "Bagaimana cara melacak pesanan saya?"
    )

    print("\n[TEST 1 - Tracking]")
    print(result_tracking)

    assert "nomor resi" in result_tracking.lower()
    print("Tracking test: PASSED ✅")

    # Test 2: Pengiriman
    result_shipping = common_information(
        "Berapa lama proses pengiriman?"
    )

    print("\n[TEST 2 - Shipping]")
    print(result_shipping)

    assert "1-3 hari kerja" in result_shipping.lower()
    print("Shipping test: PASSED ✅")

    # Test 3: Refund
    result_refund = common_information(
        "Bagaimana cara mengajukan refund?"
    )

    print("\n[TEST 3 - Refund]")
    print(result_refund)

    assert "refund" in result_refund.lower()
    print("Refund test: PASSED ✅")

    print("\nCommon Information test: PASSED ✅")


if __name__ == "__main__":
    test_common_information()