"""
A script that has a set of tests for testing applying coupons.
"""

import pytest
import time
from demostore_automation.src.pages.HomePage import HomePage
from demostore_automation.src.pages.CartPage import CartPage
from demostore_automation.src.pages.Header import Header
from demostore_automation.src.configs.MainConfigs import MainConfigs


@pytest.mark.usefixtures("init_driver")
class Test50OffCoupon:
    """
    Test class for applying discount with coupon.
    """

    @pytest.mark.esqf4
    def test_verify_50_off_coupon_works(self):
        """
        Test to verify that a 50% off coupon correctly updates the cart total in an e-commerce scenario.

        This automated test follows these steps:
        1. Navigate to the home page.
        2. Add the first item displayed on the home page to the shopping cart.
        3. Ensures that the cart is correctly updated by waiting until the cart item count reflects the addition.
        4. Navigate to the cart page.
        5. Capture and store the total price in the cart before applying the coupon.
        6. Apply a '50OFF' coupon code.
        7. Verify that a success message is displayed confirming the coupon application.
        8. Capture and store the total price in the cart after applying the coupon.
        9. Calculate the expected total price as 50% of the original total.
        10. Assert that the actual cart total after applying the coupon matches the expected total, raising an assertion error with a detailed message if they do not match.

        The test ensures that the e-commerce system correctly implements the discount logic associated with coupon codes, specifically testing the functionality of a 50% reduction.

        Attributes:
            self (unittest.TestCase): Instance of the test case.

        Raises:
            AssertionError: If the final cart total does not reflect a 50% reduction after the coupon is applied.
        """