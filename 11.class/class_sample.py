class Shop(object):
    description = 'Python Shop class'

    def __init__(self, name, shop_type, address):
        self.name = name
        self._shop_type = shop_type
        self.address = address

    def _get_show_info_text(self):
        return f'''상점 ({self.name})
  유형: {self._shop_type}
  주소: {self.address}'''

    def show_info(self):
        print(self._get_show_info_text())

    @property
    def info(self):
        return '상점(%s)' % self._name

    @classmethod
    def make_dummy(cls):
        """
        name: untitled
        shop_type: undefined
        address: unknown
        의 속성을 갖는 Shop객체를 생성해 리턴
        """
        return cls('untitled', 'undefined', 'unknown')

    @property
    def shop_type(self):
        return self._shop_type

    @shop_type.setter
    def shop_type(self, new_shop_type):
        if new_shop_type not in ['패스트푸드', 'PC방']:
            print('해당 상점유형은 사용할 수 없습니다')
        else:
            self._shop_type = new_shop_type

    def show_object_log(self, obj):
        print(obj.log)

    def multi(x):
        return x * x



class Restaurant(Shop):
    def __init__(self, name, shop_type, address, rating=5.0):
        super().__init__(name, shop_type, address)
        self.rating = rating

    def _get_show_info_text(self):
        ori = super()._get_show_info_text()
        ret = ori.replace('상점', '식당')
        ret += f'\n  점수: {self.rating}'
        return ret

