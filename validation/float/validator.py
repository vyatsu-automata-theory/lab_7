from validation.params import ValidationParams


class FloatValidator:
    def __init__(self, params: ValidationParams):
        self.params = params

    def start(self, inp: str):
        for i in range(len(inp)):
            if inp[i] == self.params.space:
                continue
            elif inp[i] in self.params.signs:
                return self.__sign(inp[i + 1:])
            elif inp[i] in self.params.numbers:
                return self.__num(inp[i + 1:])

            return self.__err('symbol ' + inp[i] + ' not a number or sign')

    def __sign(self, inp: str):
        for i in range(len(inp)):
            if inp[i] not in self.params.numbers:
                return self.__err('not number after sign')
            return self.__num(inp[i + 1:])

    def __err(self, reason: str):
        raise BaseException('error: ' + reason)

    def __num(self, inp: str):
        for i in range(len(inp)):
            if inp[i] in self.params.numbers:
                continue
            if inp[i] == self.params.enter:
                return self.__end()
            return self.__err('symbol ' + inp[i] + ' not a number')

    def __end(self):
        print('number validate success')
