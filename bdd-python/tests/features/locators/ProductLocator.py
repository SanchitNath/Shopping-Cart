from selenium.webdriver.common.by import By

# Filter elements
sizeText = (By.XPATH, "//h4[text()='Sizes:']")
filterIcon = (By.XPATH, "//h4[text()='Sizes:']/following::*//span[text()='Icon']")
productsFoundText = (By.XPATH, "//p[text()='count' and text()=' Product(s) found']")
extraSmallSizeItem = (By.XPATH, "//p[text()='Black Batman T-shirt']")
smallSizeItem = (By.XPATH, "//p[text()='Blue Sweatshirt']")
mediumSizedItem = (By.XPATH, "//p[text()='Black Tule Oversized']")
mediumLargeSizedItem = (By.XPATH, "//p[text()='Basic Cactus White T-shirt']")
largeSizedItem = (By.XPATH, "//p[text()='Cropped Stay Groovy off white' or text()='Basic Cactus White T-shirt' or text()='Black Batman T-shirt' or text()='Blue T-Shirt' or text()='Loose Black T-shirt' or text()='Ringer Hall Pass' or text()='Grey T-shirt' or text()='Black T-shirt with white stripes' or text()='Turtles Ninja T-shirt' or text()='Tropical Wine T-shirt' or text()='Marine Blue T-shirt']")
extraLargeSizedItem = (By.XPATH, "//p[text()='Cropped Stay Groovy off white' or text()='Basic Cactus White T-shirt' or text()='Skater Black Sweatshirt' or text()='Black Batman T-shirt' or text()='Blue T-Shirt' or text()='Loose Black T-shirt' or text()='Ringer Hall Pass' or text()='Grey T-shirt' or text()='Black T-shirt with white stripes' or text()='Turtles Ninja T-shirt' or text()='Slim black T-shirt' or text()='White T-shirt Gucci' or text()='Tropical Wine T-shirt' or text()='Marine Blue T-shirt']")
doubleExtraLargedSizedItem = (By.XPATH, "//p[text()='Cropped Stay Groovy off white']")
doubleExtraLargedSizedItem2 = (By.XPATH, "//p[text()='Loose Black T-shirt']")
doubleExtraLargedSizedItem3 = (By.XPATH, "//p[text()='Ringer Hall Pass']")
doubleExtraLargedSizedItem4 = (By.XPATH, "//p[text()='Slim black T-shirt']")

# Product elements
freeShippingProducts = (By.XPATH, "//div[text()='Free shipping']/following-sibling::div[@alt]")
productAddToCart = (By.XPATH, "(//p[text()='product_name']/following::button[text()='Add to cart'])[1]")
freeShippingAddToCart = (By.XPATH, "(//div[text()='Free shipping']/following::p[text()='product_name']/following::button[text()='Add to cart'])[1]")
allProducts = (By.XPATH, "//button[text()='Add to cart']/preceding-sibling::p")
cartIcon = (By.XPATH, "//div[@title='Products in cart quantity']")

# Cart elements
closeCartIcon = (By.XPATH, "//span[text()='X']")
totalCountInCart = (By.XPATH, "//span[text()='Cart']/preceding-sibling::*/div")
itemInCart = (By.XPATH, "//span[text()='Cart']//following::p[text()='product_name']")
increaseDecreaseItemInCart = (By.XPATH, "//span[text()='Cart']//following::p[text()='product_name']/following::button[text()='plusminus']")
quantityOfItemInCart = (By.XPATH, "//p[text()='product_name']/following-sibling::p[contains(., 'Quantity')]")
priceOfItemInCart = (By.XPATH, "(//p[text()='product_name'])[last()]/following::p[contains(text(),'$')]")
removeIconInCart = (By.XPATH, "//button[@title='remove product from cart']")
removeItemFromCart = (By.XPATH, "//p[text()='product_name']/preceding::button[@title='remove product from cart']")
subTotalText = (By.XPATH, "//p[text()='SUBTOTAL']")
subTotalPrice = (By.XPATH, "//p[text()='SUBTOTAL']/following::p[contains(text(),'$')]")
checkoutBtn = (By.XPATH, "//button[text()='Checkout']")
inorderedProducts = (By.XPATH, "(//p[contains(.,'Quantity: ')])[order]/preceding-sibling::p[text()='product_name']")
emptyCartMessage = (By.XPATH, "//p[text()='Add some products in the cart ']")
removeMaxPriceItem = (By.XPATH, "(//p[contains(text(),'price')]/preceding::button[@title='remove product from cart'])[last()]")