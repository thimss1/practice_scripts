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
        # go th home page
        home_page = HomePage(self.driver)
        home_page.go_to_home_page()

        # add item to cart
        home_page.click_first_add_to_cart_button()

        # make sure the cart is updated before going to cart
        # because when we click on add to cart and we go to cart, it happens so fast that we
        # get to the cart page before the cart is updated. So we see that there is '1 item' in the cart on the
        # top nav bar but the middle of the page says that there is no item in cart
        header = Header(self.driver)
        header.wait_until_cart_item_count(1)

        # go to cart
        cart_page = CartPage(self.driver)
        cart_page.go_to_cart_page()

        # before applying the coupon get the total amount
        total_price_before_coupon = cart_page.get_cart_total()

        # apply a 50% off coupon
        # first get the coupon from config
        coupon_50_off = MainConfigs.get_coupon_code("50 OFF")
        cart_page.apply_coupon(coupon_50_off)

        # before getting the cart total, verify the page has updated
        cart_page.verify_displayed_success_messafe('Coupon code applied successfully.')
        time.sleep(1)

        # after applying the coupon get the total amount
        total_price_after_coupon = cart_page.get_cart_total()

        # the coupon is supposed to give 50% off. So calculate what should be 50% off the original price
        expected_new_total = .5 * total_price_before_coupon

        # if expected_new_total !=total_price_after_coupon:
        #   raise Exceptional(f"After applying 50% off coupon, the total cart price did not update by 50%. Coupon code = {coupon_50_off}")

        assert expected_new_total == total_price_after_coupon, f"After applying 50% off coupon, "\
                        "the total cart price did not update by 50%. Coupon code = '{coupon_50_off}' "\
                        f"Expected total: {expected_new_total}, Actual page total: {total_price_after_coupon}"




