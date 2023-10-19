import time

from pytest_bdd import parsers
from selenium import webdriver
from behave import given, when, then
from pages.ProductPage import ProductPage
import tests.features.locators.ProductLocator as pl
from util.logger_util import get_logger
from util.CommonMethods import CommonMethods
logger = get_logger(__name__)

@given(u'Launch the browser')
def step_launch_browser(context):
    context.driver = webdriver.Chrome()
    cm = CommonMethods(context.driver)
    cm.open_url("https://react-shopping-cart-67954.firebaseapp.com/")
    # context.driver.get("https://react-shopping-cart-67954.firebaseapp.com/")

@then(u'get all products list')
def get_all_products_list(context):
    pp = ProductPage(context.driver)
    pp.get_product_list()

@then(u'the user apply/remove "{filter_type:S}" filter')
def step_apply_remove_filter(context, filter_type):
    pp = ProductPage(context.driver)
    pp.select_filter(filter_type)

@then(u'the user apply/remove at once "{mf_type1}" "{mf_type2}" filters')
def step_apply_remove_mutiple_filter(context, mf_type1, mf_type2):
    pp = ProductPage(context.driver)
    if mf_type1 != mf_type2:
        pp.select_filter(mf_type1)
        pp.select_filter(mf_type2)
    else:
        logger.error(f"Check the input pls, as '{mf_type1}' or '{mf_type2}' isn't present or are same!!")

@then(u'items with double "{filter_type1}" "{filter_type2}" sizes gets filtered')
def step_double_sizes_get_filtered(context, filter_type1, filter_type2):
    global product_found
    product_found = None
    logger.info(f"first filter = {filter_type1}, second filter = {filter_type2}")
    cm = CommonMethods(context.driver)
    if (
            (filter_type1 == "XS" or filter_type1 == "S" or filter_type1 == "M" or filter_type1 == "ML" or filter_type1 == "L" or filter_type1 == "XL" or filter_type1 == "XXL") and
            (filter_type2 == "XS" or filter_type2 == "S" or filter_type2 == "M" or filter_type2 == "ML" or filter_type2 == "L" or filter_type2 == "XL" or filter_type2 == "XXL") and
            filter_type1 != filter_type2
    ):
        if (filter_type1 == "XS" and filter_type2 == "S") or (filter_type2 == "XS" and filter_type1 == "S"):
            cm.wait_for_element_visible(pl.extraSmallSizeItem)
            cm.wait_for_element_visible(pl.smallSizeItem)
            product_found = (
                pl.productsFoundText[0],
                pl.productsFoundText[1].replace("count", "2"),
            )
        elif (filter_type1 == "S" and filter_type2 == "M") or (filter_type2 == "S" and filter_type1 == "M"):
            cm.wait_for_element_visible(pl.smallSizeItem)
            cm.wait_for_element_visible(pl.mediumSizedItem)
            product_found = (
                pl.productsFoundText[0],
                pl.productsFoundText[1].replace("count", "3"),
            )
        elif (filter_type1 == "M" and filter_type2 == "ML") or (filter_type2 == "M" and filter_type1 == "ML"):
            cm.wait_for_element_visible(pl.mediumSizedItem)
            cm.wait_for_element_visible(pl.mediumLargeSizedItem)
            product_found = (
                pl.productsFoundText[0],
                pl.productsFoundText[1].replace("count", "2"),
            )
        elif (filter_type1 == "ML" and filter_type2 == "L") or (filter_type2 == "ML" and filter_type1 == "L"):
            cm.wait_for_element_visible(pl.mediumSizedItem)
            cm.wait_for_element_visible(pl.mediumLargeSizedItem)
            product_found = (
                pl.productsFoundText[0],
                pl.productsFoundText[1].replace("count", "11"),
            )
        elif (filter_type1 == "L" and filter_type2 == "XL") or (filter_type2 == "L" and filter_type1 == "XL"):
            cm.wait_for_element_visible(pl.largeSizedItem)
            cm.wait_for_element_visible(pl.extraLargeSizedItem)
            product_found = (
                pl.productsFoundText[0],
                pl.productsFoundText[1].replace("count", "13"),
            )
        elif (filter_type1 == "XL" and filter_type2 == "XXL") or (filter_type2 == "XL" and filter_type1 == "XXL"):
            cm.wait_for_element_visible(pl.extraLargeSizedItem)
            cm.wait_for_element_visible(pl.doubleExtraLargedSizedItem)
            cm.wait_for_element_visible(pl.doubleExtraLargedSizedItem2)
            cm.wait_for_element_visible(pl.doubleExtraLargedSizedItem3)
            cm.wait_for_element_visible(pl.doubleExtraLargedSizedItem4)
            product_found = (
                pl.productsFoundText[0],
                pl.productsFoundText[1].replace("count", "10"),
            )
        elif (filter_type1 == "XXL" and filter_type2 == "XS") or (filter_type2 == "XXL" and filter_type1 == "XS"):
            cm.wait_for_element_visible(pl.doubleExtraLargedSizedItem)
            cm.wait_for_element_visible(pl.doubleExtraLargedSizedItem2)
            cm.wait_for_element_visible(pl.doubleExtraLargedSizedItem3)
            cm.wait_for_element_visible(pl.doubleExtraLargedSizedItem4)
            cm.wait_for_element_visible(pl.extraSmallSizeItem)
            product_found = (
                pl.productsFoundText[0],
                pl.productsFoundText[1].replace("count", "5"),
            )
        if product_found:
            cm.wait_for_element_visible(product_found)
    else:
        logger.error(f"Check the input pls, as '{filter_type1}' or '{filter_type2}' isn't present or are same!!")

@then(u'items with "{filter_type}" size gets filtered')
def step_single_size_get_filtered(context, filter_type):
    global product_found
    product_found = None
    cm = CommonMethods(context.driver)
    if filter_type == "XS" or filter_type == "S" or filter_type == "M" or filter_type == "ML" or filter_type == "L" or filter_type == "XL" or filter_type == "XXL":
        if filter_type == "XS":
            cm.wait_for_element_visible(pl.extraSmallSizeItem)
            product_found = (
                pl.productsFoundText[0],
                pl.productsFoundText[1].replace("count", "1"),
            )
        elif filter_type == "S":
            cm.wait_for_element_visible(pl.extraSmallSizeItem)
            cm.wait_for_element_visible(pl.smallSizeItem)
            product_found = (
                pl.productsFoundText[0],
                pl.productsFoundText[1].replace("count", "2"),
            )
        elif filter_type == "M":
            cm.wait_for_element_visible(pl.mediumSizedItem)
            product_found = (
                pl.productsFoundText[0],
                pl.productsFoundText[1].replace("count", "1"),
            )
        elif filter_type == "ML":
            cm.wait_for_element_visible(pl.mediumSizedItem)
            cm.wait_for_element_visible(pl.mediumLargeSizedItem)
            product_found = (
                pl.productsFoundText[0],
                pl.productsFoundText[1].replace("count", "2"),
            )
        elif filter_type == "L":
            cm.wait_for_element_visible(pl.largeSizedItem)
            product_found = (
                pl.productsFoundText[0],
                pl.productsFoundText[1].replace("count", "10"),
            )
        elif filter_type == "XL":
            cm.wait_for_element_visible(pl.extraLargeSizedItem)
            product_found = (
                pl.productsFoundText[0],
                pl.productsFoundText[1].replace("count", "10"),
            )
        elif filter_type == "XXL":
            cm.wait_for_element_visible(pl.doubleExtraLargedSizedItem)
            cm.wait_for_element_visible(pl.doubleExtraLargedSizedItem2)
            cm.wait_for_element_visible(pl.doubleExtraLargedSizedItem3)
            cm.wait_for_element_visible(pl.doubleExtraLargedSizedItem4)
            product_found = (
                pl.productsFoundText[0],
                pl.productsFoundText[1].replace("count", "4"),
            )
        if product_found:
            cm.wait_for_element_visible(product_found)
    else:
        logger.error(f"Check the input pls, as '{filter_type}' isn't present!!")

@then(u'the user add free-shipping item in cart')
def step_add_free_shipping_item(context):
    pp = ProductPage(context.driver)
    pp.add_free_shipping_to_cart()

@then(u'close the cart')
def step_close_the_cart(context):
    pp = ProductPage(context.driver)
    pp.close_the_cart()

@then(u'the user add non-free-shipping item in cart')
def step_add_non_free_shipping_item(context):
    pp = ProductPage(context.driver)
    pp.add_paid_shipping_to_cart()

@then(u'verify the items added in cart are in order')
def step_verify_items_added_in_order(context):
    pp = ProductPage(context.driver)
    pp.verify_products_added_in_order()

@then(u'verify total price')
def step_verify_total_price(context):
    pp = ProductPage(context.driver)
    pp.verify_total_price()

@then(u'the user opens the cart')
def step_open_cart(context):
    pp = ProductPage(context.driver)
    pp.open_cart()

@then(u'the user empties the cart')
def step_user_empties_cart(context):
    pp = ProductPage(context.driver)
    pp.user_empties_cart()

@then(u'the user add "{product_name}" item in cart')
def step_user_add_item_in_cart(context, product_name):
    pp = ProductPage(context.driver)
    pp.add_item_in_cart(product_name)
    time.sleep(1)

@then(u'verify price change as per "{product_name}"')
def step_verify_price_change(context, product_name):
    pp = ProductPage(context.driver)
    pp.verify_price_change_in_cart(product_name)

@then(u'increase the quantity of "{product_name}" item in cart')
def step_increase_quantity_in_cart(context, product_name):
    pp = ProductPage(context.driver)
    pp.increase_quantity_in_cart(product_name)

@then(u'the user verifies price reduced to zero')
def step_user_verified_price_reduced_to_zero(context):
    pp = ProductPage(context.driver)
    pp.verify_price_reduced()

@then(u'the user verifies count reduced to zero')
def step_user_verified_count_reduced_to_zero(context):
    pp = ProductPage(context.driver)
    pp.verify_count_reduced()

@then(u'the user places the order')
def step_user_place_order(context):
    pp = ProductPage(context.driver)
    pp.place_order()

@then(u'verify the price shown in alert')
def step_verify_price_shown_in_alert(context):
    pp = ProductPage(context.driver)
    pp.verify_price_shown_in_alert()

@then(u'refresh the page')
def refresh_page(context):
    cm = CommonMethods(context.driver)
    cm.refresh_page()
    time.sleep(2)

@then(u'the user verifies the total count shown')
def verify_count_shown(context):
    pp = ProductPage(context.driver)
    pp.verify_count_shown()

@then(u'user remove the highest priced item from cart')
def step_remove_highest_quantity_item(context):
    pp = ProductPage(context.driver)
    pp.remove_highest_priced_item()