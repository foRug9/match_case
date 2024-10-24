"""
Пример работы с match case.
"""
def http_errors(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with Internet"


if __name__ == '__main__':
    print(http_errors(418))
    print(http_errors(400))
    print(http_errors(401))
