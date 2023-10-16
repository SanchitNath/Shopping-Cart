import time
from util.CommonMethods import CommonMethods
import tests.features.locators.ProductLocator as pl
from util.logger_util import get_logger

logger = get_logger(__name__)

class ProductPage:
    product_added = None
    global product_count_dic
    product_count_dic = {}
    free_shipping_products_list = []
    all_products_list = []
    non_free_shipping_products_list = []
    price_of_item = 0.0
    def __init__(self, driver):
        self.driver = driver
        self.cm = CommonMethods(driver)

    def get_product_list(self):
        time.sleep(2)
        self.cm.wait_for_element_visible(pl.freeShippingProducts)
        all_free_shipping_elements = self.cm.get_elements(pl.freeShippingProducts)
        for afse in all_free_shipping_elements:
            free_shipping_products = afse.get_attribute('alt')
            self.free_shipping_products_list.append(free_shipping_products)
        logger.info(f"Free shipping products = {self.free_shipping_products_list}")
        assert self.free_shipping_products_list != [], f"Free shipping products aren't present"

        all_elements = self.cm.get_elements(pl.allProducts)
        for ae in all_elements:
            all_products = ae.text
            self.all_products_list.append(all_products)
        logger.info(f"All products = {self.all_products_list}")
        assert self.all_products_list != [], f"All products aren't present"

    def user_empties_cart(self):
        """
        User empties the cart, verify - price, count change to 0
        Make the dictionary of save data empty, check the price again and save it globally
        :return:
        """
        try:
            global product_count_dic
            product_count_dic = {}
            self.cm.wait_for_element_visible(pl.removeIconInCart, 10)
            close_icon_list = self.cm.get_elements(pl.removeIconInCart, 5)
            for close_icon in close_icon_list:
                self.cm.click_element(pl.removeIconInCart)
            self.verify_price_reduced()
            # Verify message shown
            self.cm.wait_for_element_visible(pl.emptyCartMessage)
            self.verify_count_reduced()
            # product_count_dic.clear()
            # Update the price shown
        except:
            logger.info("Cart is empty already")
        self.save_total_price()
        logger.info(
            f"User has emptied the cart as saved product is {product_count_dic} and total price is {sub_total_price}")
    def select_filter(self, filter_type):
        """
        Apply filter according to sizes
        :param filter_type:
        :return:
        """
        self.cm.wait_for_element_visible(pl.sizeText)
        filter = (
            pl.filterIcon[0],
            pl.filterIcon[1].replace("Icon", filter_type),
        )
        self.cm.wait_for_element_visible(filter)
        self.cm.click_element(filter)
        # Since adding filter shows a page loader icon, added sleep of 1 sec
        time.sleep(1)
        return self

    def update_count_in_dict(self, item):
        """
        Update count in dictionary to verify the products added in order, for future use
        :param item:
        :return:
        """
        if product_count_dic == {}:
            # For first item, the count will be 1
            product_count_dic[item] = 1
        else:
            if item not in product_count_dic.keys():
                # For any new entry of item in dict, the count will be 1
                product_count_dic[item] = 1
            else:
                # For rest all, the count will be increased by 1 everytime it gets added
                product_count_dic[item] += 1
        logger.info(f"Product selected added in dict = {product_count_dic}")

    def add_free_shipping_to_cart(self):
        """
        Randomly add a free shipping item to cart and save the item:count in order in a "dictionary"
        :return:
        """
        logger.info(f"Inside free_shipping() -> {self.free_shipping_products_list}")
        # Pick an item randomly from free_shipping products
        item = self.cm.random_picker(self.free_shipping_products_list)
        add_to_cart = (
            pl.freeShippingAddToCart[0],
            pl.freeShippingAddToCart[1].replace("product_name", item),
        )
        self.cm.click_element(add_to_cart)
        self.update_count_in_dict(item)
        item_added_in_cart = (
            pl.itemInCart[0],
            pl.itemInCart[1].replace("product_name", item),
        )
        self.cm.wait_for_element_visible(item_added_in_cart)

    def add_paid_shipping_to_cart(self):
        logger.info(f"Inside add_shipping() -> {self.non_free_shipping_products_list}")
        """
        Randomly add a paid shipping item to cart and save the item:count in order in a "dictionary"
        :return:
        """
        # Since there is no tag for "non_free_shipping_products", we remove the list of free_shipping_products from all_products
        self.non_free_shipping_products_list = list(
            set(self.all_products_list).difference(set(self.free_shipping_products_list)))
        logger.info(f"Paid products = {self.non_free_shipping_products_list}")
        assert self.non_free_shipping_products_list != [], f"Paid products aren't present"
        # Pick an item randomly from paid_shipping products
        item = self.cm.random_picker(self.non_free_shipping_products_list)
        add_to_cart = (
            pl.freeShippingAddToCart[0],
            pl.freeShippingAddToCart[1].replace("product_name", item),
        )
        self.cm.click_element(add_to_cart)
        self.update_count_in_dict(item)
        item_added_in_cart = (
            pl.itemInCart[0],
            pl.itemInCart[1].replace("product_name", item),
        )
        self.cm.wait_for_element_visible(item_added_in_cart)
        self.non_free_shipping_products_list = []

    def verify_button_text_in_cart(self):
        """
        Verify button and text message in the cart
        :return:
        """
        self.cm.wait_for_element_visible(pl.closeCartIcon)
        self.cm.wait_for_element_visible(pl.totalCountInCart)
        self.cm.wait_for_element_visible(pl.subTotalText)
        self.cm.wait_for_element_visible(pl.subTotalPrice)
        self.cm.wait_for_element_visible(pl.checkoutBtn)

    def save_total_price(self):
        """
        Save the total price shown
        :return:
        """
        global sub_total_price
        total_price_shown = self.cm.get_text(pl.subTotalPrice)[2:]
        sub_total_price = float(total_price_shown)
        logger.info(f"Total price saved = {sub_total_price}")

    def save_price(self, product):
        """
        Save the price of the product
        :return:
        """
        price_of_item_in_cart = (
            pl.priceOfItemInCart[0],
            pl.priceOfItemInCart[1].replace("product_name", product),
        )
        price_of_item = self.cm.get_text(price_of_item_in_cart)[2:]
        self.price_of_item = price_of_item
        logger.info(f"Price of {product} item in cart = {self.price_of_item}")

    def close_the_cart(self):
        """
        Close the cart after checking all the elements, items, count of items, subtotal price
        :return:
        """
        self.verify_button_text_in_cart()
        # Assert the total count of product is correct
        total_count_in_cart = self.cm.get_text(pl.totalCountInCart)
        total_count_in_cart = int(total_count_in_cart)
        if total_count_in_cart != 0:
            total_from_dic = 0
            values_from_dic = product_count_dic.values()
            for value in values_from_dic:
                total_from_dic += int(value)
            assert total_count_in_cart == total_from_dic, f"Total count is wrong as cart shows '{total_count_in_cart}' count"
            # Verify the last added item & it's quantity from dict, it's price (visible)
            last_added_distinct_product = list(product_count_dic.keys())[-1]
            quantity_of_last_added_product = list(product_count_dic.values())[-1]
            last_item_in_cart = (
                pl.itemInCart[0],
                pl.itemInCart[1].replace("product_name", last_added_distinct_product),
            )
            self.cm.wait_for_element_visible(last_item_in_cart)
            price_of_last_item_in_cart = (
                pl.priceOfItemInCart[0],
                pl.priceOfItemInCart[1].replace("product_name", last_added_distinct_product),
            )
            self.cm.wait_for_element_visible(price_of_last_item_in_cart)
            quantity_item_in_cart = (
                pl.quantityOfItemInCart[0],
                pl.quantityOfItemInCart[1].replace("product_name", last_added_distinct_product),
            )
            self.cm.wait_for_element_presence(quantity_item_in_cart)
            quantity_in_cart = self.cm.get_text(quantity_item_in_cart)
            assert str(quantity_of_last_added_product) in quantity_in_cart, f"Quantity of {last_added_distinct_product} product is stored as '{quantity_of_last_added_product}' in dict but is '{quantity_in_cart}'"
        self.cm.click_element(pl.closeCartIcon)
        self.cm.wait_until_element_not_visible(pl.checkoutBtn)

    def verify_products_added_in_order(self):
        """
        Verifies that the item added are in-order only
        :return:
        """
        print(f"Stored data = {product_count_dic}")
        # Get the products list and length of the unique products
        products_in_order = product_count_dic.keys()
        number_of_products = len(products_in_order)
        i = 1
        for product in products_in_order:
            inordered_product = (
                pl.inorderedProducts[0],
                pl.inorderedProducts[1]
                .replace("order", str(i))
                .replace("product_name", product),
            )
            self.cm.wait_for_element_visible(inordered_product)
            if i < number_of_products:
                i += 1

    def verify_total_price(self):
        """
        Verifies the total price calculated in the cart is proper or not
        :return:
        """
        self.verify_button_text_in_cart()
        products_in_order = product_count_dic.keys()
        total_price_calculated = 0
        for product in products_in_order:
            price_of_item = (
                pl.priceOfItemInCart[0],
                pl.priceOfItemInCart[1].replace("product_name", product),
            )
            price = self.cm.get_text(price_of_item)
            price = float(price[2:])
            quantity_of_item = product_count_dic[product]
            quantity_of_item = int(quantity_of_item)
            total_price_calculated += float(price * quantity_of_item)
            total_price_calculated = round(total_price_calculated, 2)
        total_price_shown = self.cm.get_text(pl.subTotalPrice)[2:]
        total_price_shown = float(total_price_shown)
        assert total_price_shown == total_price_calculated, f"Calculation is wrong as {total_price_calculated} != {total_price_shown} !!"

    def verify_price_reduced(self):
        """
        Verify price reduced to 0
        :return:
        """
        # Assert price shown
        total_price_shown = self.cm.get_text(pl.subTotalPrice)[2:]
        total_price_shown = float(total_price_shown)
        assert total_price_shown == 0.00, f"Price should be $0.00 and not ${total_price_shown}!"

    def verify_count_reduced(self):
        """
        Verify count reduced to 0
        :return:
        """
        # Assert count shown at cart
        total_count_in_cart = int(self.cm.get_text(pl.totalCountInCart))
        assert total_count_in_cart == 0, f"Count should be 0 but is {total_count_in_cart}!"

    def open_cart(self):
        time.sleep(1)
        self.cm.wait_for_element_visible(pl.cartIcon)
        self.cm.click_element(pl.cartIcon)

    def add_item_in_cart(self, product_name):
        """
        Add an item to cart and save the item:count in order in a "dictionary"
        :return:
        """
        add_to_cart = (
            pl.productAddToCart[0],
            pl.productAddToCart[1].replace("product_name", product_name),
        )
        self.cm.click_element(add_to_cart)
        self.update_count_in_dict(product_name)
        # Update the price shown
        self.save_price(product_name)

    def increase_quantity_in_cart(self, product_name):
        """
        Increase the quantity of product in cart
        :param product_name:
        :return:
        """
        increase_quantity = (
            pl.increaseDecreaseItemInCart[0],
            pl.increaseDecreaseItemInCart[1]
            .replace("product_name", product_name)
            .replace("plusminus", '+'),
        )
        self.cm.wait_for_element_visible(increase_quantity)
        self.cm.click_element(increase_quantity)
        self.update_count_in_dict(product_name)

    def verify_price_change_in_cart(self, product_name):
        """
        # find quantity, price of item
        # get total price
        # increase quantity by 1
        # Verify the price change, quantity change, subtotal price change
        # Update the total price as per shown in the cart
        :param product_name:
        :return:
        """
        # Get the products list and check if product_name is present in list
        products_in_order = product_count_dic.keys()
        quantity_item_in_cart = (
            pl.quantityOfItemInCart[0],
            pl.quantityOfItemInCart[1].replace("product_name", product_name),
        )
        quantity_in_cart = self.cm.get_text(quantity_item_in_cart)
        logger.info(f"Quantity in cart = {quantity_in_cart}")
        # This will get the text as "Quantity: " "1"
        if product_name in products_in_order:
            actual_quantity_product = product_count_dic[product_name]
            # Assert quantity shown of the item is correct or not
            assert str(actual_quantity_product) in quantity_in_cart, f"Quantity of {product_name} item saved is {actual_quantity_product} and not {quantity_in_cart}!"
            # Find price of product
            price_of_item = (
                pl.priceOfItemInCart[0],
                pl.priceOfItemInCart[1].replace("product_name", product_name),
            )
            price_text = self.cm.get_text(price_of_item)
            price = float(price_text[2:])
            # Get total price
            total_price_before = self.price_of_item
            logger.info(f"Total price before = {total_price_before}")
            # Calculate subtotal price change
            calculated_price = float(total_price_before + price)
            total_price_shown = self.cm.get_text(pl.subTotalPrice)[2:]
            total_price_shown = float(total_price_shown)
            assert calculated_price == total_price_shown, f"Price change should be from {sub_total_price} to {total_price_shown} as addition of {price}!!"
            # Update the price shown
            self.save_total_price()

    def place_order(self):
        """
        Place the order now
        :return:
        """
        self.verify_button_text_in_cart()
        total_price_shown = self.cm.get_text(pl.subTotalPrice)[2:]
        total_price_shown = float(total_price_shown)
        # Update the price shown
        self.save_total_price()
        if total_price_shown > 0.0:
            time.sleep(2)
            self.cm.click_element(pl.checkoutBtn)
            time.sleep(2)
            logger.info("Clicked on checkout button")
        else:
            logger.warn("Price shown is 0.0, order can be placed but please add items in cart!!")
        logger.info("Order placed")

    def verify_price_shown_in_alert(self):
        """
        Verify the price shown in alert
        :return:
        """
        total_price = 0.0
        logger.info("Verify price shown")
        time.sleep(5)
        alert_text = self.cm.get_alert_text()
        logger.info(f"Text shown in alert {alert_text}")
        price_shown_alert = alert_text[23:]
        logger.info(f"Price shown in alert {price_shown_alert}")
        logger.info(f"Total value saved = {sub_total_price}")
        if sub_total_price != 0.0:
            total_price = sub_total_price
            logger.info(f"total price = {total_price}")
        if total_price > 0.0:
            # Verify the price in cart
            assert str(total_price) in alert_text, f"alert text - {alert_text} isn't showing correct subtotal price"
            assert total_price == float(price_shown_alert), f"Price shown in alert should be {total_price} not {price_shown_alert}!"
        else:
            # Verify the alert message only
            assert alert_text == "Add some products in the cart!", "Change the RHS message to assert!"
