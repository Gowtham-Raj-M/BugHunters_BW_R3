"""
This page consists of Generic and Login page xpaths and constants
"""
from os.path import join, dirname

# Xpaths #
ZARA_URL = "https://www.zara.com/in/"
ZARA_SEARCH_BAR = "//span[contains(text(),'Search')]"
ZARA_DRESS_TEXT = "//button[contains(text(),'dress')]"
ZARA_MAN = "//button[contains(text(),'Man')]"
ZARA_MAN_PRODUCTS = "//*[@class='product-grid-product__info-wrapper']"
SELECT_PRODUCT_ZARA_MEN = "(//span[contains(text(),'STRETCH SHIRT')])[1]"
ZARA_ADD_TO_CART_BUTTON = "//span[contains(text(),'Add to bag')]"
ZARA_CLOSE_BUTTON = "//span[contains(text(),'CLOSE')]"
VALIDATE_ERROR_MSG = "//*[contains(text(),'YOU MUST SELECT A SIZE')]"
SIZE_L = "//span[contains(text(),'L (UK L)')]"
POPUP_CLOSE_BUTTON = "//*[@class='header__close-icon']"
FILTERS = "//span[contains(text(),'Filters')]"
PLUS_BUTTON = "//*[@class='plus-icon-horizontal-path']"
SELECT_SIZE_WOMEN = "//*[contains(text(),'XXS')]"
FIRST_PRODUCT = "//*[contains(text(),'DRAPED DRESS')]"
FIRST_SIZE_FOR_WOMEN = "(//*[@class='product-detail-size-info__size'])[1]"
# Constants #
WAIT_TIME = 100
ERROR_MSG= "YOU MUST SELECT A SIZE"


# Path #
DATA_FOLDER_PATH = join(dirname(dirname(dirname(__file__))), 'web_automation\\test\\Data\\{}')
DOWNLOAD_FOLDER_PATH = join(dirname(dirname(dirname(__file__))), 'web_automation/downloads/{}')
REPORT_FOLDER_PATH = join(dirname(dirname(dirname(__file__))), 'web_automation\\report')
