from enum import Enum


class Color(Enum):

    RED = (1, '赤')
    GREEN = (2, '緑')

    def __init__(self, id, ja):
        self.id = id
        self.ja = ja

    # tagとしてidとjaを連結した文字列を取得する
    @property
    def tag(self):
        return "{}_{}".format(self.id, self.ja)

    # 全メンバーを取得する
    @classmethod
    def get_all(cls):
        # Order dictionary -> list
        return [*cls.__members__.values()]

    # idを指定して取得する
    @classmethod
    def get_by_id(cls, id):
        for c in cls.get_all():
            if id == c.id:
                return c
        # default
        return Color.RED


if __name__ == "__main__":
    print('#=== members ===#')
    print(Color.get_all())

    print('#=== enum ===#')
    for c in Color.get_all():
        print(c)

    print('#=== id ===#')
    for c in Color.get_all():
        print(c.id)

    print('#=== ja ===#')
    for c in Color.get_all():
        print(c.ja)

    print('#=== tag ===#')
    for c in Color.get_all():
        print(c.tag)
