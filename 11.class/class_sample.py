class Shop(object):
    description = 'Python Shop class'

    def __init__(self, name, shop_type, address):
        self.name = name
        self.shop_type = shop_type
        self.address = address

    def show_info(self):
        print(f'상점 ({self.name})')
        print(f'  유형: {self.shop_type}')
        print(f'  주소: {self.address}')

    def change_type(self, new_shop_type):
        self.shop_type = new_shop_type


