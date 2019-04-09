
class Config(object):
    SECRET_KEY = "CantStopAddictedToTheShinDigChopTopHeSaysImGonnaWinBig"
    HOST = "manage-new-products-shopify.herokuapp.com"

    SHOPIFY_CONFIG = {
        'API_KEY': '9a00f82de7096c4315be9f630d07a8b9',
        'API_SECRET': '67924e4d4f48952f5e2f8ebaca9a9a0b',

        'STORE_KEY': '118f73631eb4b65793d6fee119a4eb5b',
        'STORE_SECRET': '2bc9696b41d504697f555f423fd881dc',
        'STORE_SHOP' : 'dropshipvapes.myshopify.com',
        'STORE_URL' : 'www.dropshipvapes.com',

        'STORE_KEY_OLD': '1ee6a39b0a15483fb1e8946868892330',
        'STORE_SECRET_OLD': '7efc33cb1e0ae43ae9e6913e482ccef4',
        'STORE_SHOP_OLD' : 'eightcig.myshopify.com',
        'STORE_URL_OLD' : 'www.eightvape.com',

        'TESTSTORE_KEY' : '85c697024104edb3130ca519d8dc7601',
        'TESTSTORE_PASSWORD' : 'ee201ec8dfd38edcf24baee582c34071',
        'TESTSTORE_SECRET': '3a3449ddbf79d6b4b0d0ba77471f1d06',
        'TESTSTORE_STOREFRONT_TOKEN': 'b72263fb62e8716b4bddb69524f8447d',

        'APP_HOME': 'https://' + HOST,
        'CALLBACK_URL': 'https://' + HOST + '/install',
        'REDIRECT_URI': 'https://' + HOST + '/connect',
        'SCOPE': 'read_products, write_products'
    }
