"""
--- НЕ РОБОЧИЙ ---
проектування програмного коду, коли починаємо з ідеї - draw_house(),
потім декомпозуємо ідею на ф-ції: 
draw_house_foundation()
draw_house_walls()
draw_house_roof()
"""


def main():
    x, y = 100, 100
    width, height = 20, 40

    draw_house(x, y, width, height)


def draw_house(x, y, width, height):
    """
    Mалюємо будинок шириною width, висотою height від опорної точки (x,y),
    яка знаходиться в нижній точці фундаменту.
    Args:
        x (int): координата x
        y (int): кордината y
        width (int): ширина будинку
        height (int): висота будинку
    """
    print("малюємо будинок")
    #  висота фундаменту
    foundation_height = 0.05 * height
    #  ширина стіни
    walls_width = 0.1 * width
    #  висота стіни
    walls_height = 0.5 * height
    #  висота даху
    roof_height = height - foundation_height - walls_height

    def draw_house_foundation(x, y, width, foundation_height):
        """
         Mалюємо фундамент будинку шириною width, 
        висотою foundation_height від опорної точки (x,y),
        яка знаходиться посередині в нижній точці фундаменту.
        Args:
            x (int): координата x середини фундаменту
            y (int): кордината y низу фундаменту
            width (int): ширина фундаменту
            foundation_height (int): висота фундаменту.
        """

        print("малюю фундамент", x, y, width, foundation_height)

    def draw_house_walls(x, y-foundation_height, walls_width, walls_height):
        """малюємо стіни."""
        print("малюємо стіни", x, y-foundation_height, walls_width)
        pass

    def draw_house_roof(x, y - foundation_height - walls_height, width, roof_height):
        """малюємо дах будинку."""
        pass


main()
