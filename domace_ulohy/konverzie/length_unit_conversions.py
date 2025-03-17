import json

class LengthUnitConversions:
    def __init__(self):
        try:
            with open('length_units.json', 'r', encoding='utf-8') as f:
                self.__ratio = json.load(f)
        except json.JSONDecodeError:
            raise ValueError('File with unit coefficients (length_units.json) is corrupted')
        except FileNotFoundError:
            raise ValueError('File with unit coefficients (length_units.json) does not exist')

    def units(self):
        return list(self.__ratio.keys())

    def convert(self, value, from_unit, to_unit):
        if not isinstance(value, (int, float)):
            raise TypeError(f'Distance must by a number.')
        if value < 0:
            raise ValueError(f'Distance must by positive, not "{value}".')
        try:
            result = value * self.__ratio[from_unit] / self.__ratio[to_unit]
        except KeyError as error:
            raise ValueError(f'Unknown unit: {error}')
        else:
            return result

if __name__ == '__main__':
    try:
        convertor = LengthUnitConversions()  # can raise an exception ValueError
        print(convertor.units())  # ['mm', 'cm', 'dm', 'm', 'km', 'ly']
        print(convertor.convert(0.5, 'km', 'm'))  # 500.0
        print(convertor.convert(1500, 'm', 'km'))  # 1.5
        # print(convertor.convert(-1500, 'm', 'km'))  # raise ValueError
        # print(convertor.convert('distance', 'm', 'km'))  # raise TypeError
        # print(convertor.convert(1500, 'm', 'mi'))  # raise ValueError

    except ValueError as error:
        print(error)
    except TypeError as error:
        print(error)