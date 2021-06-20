import sys
import requests

def main(argv):
    q = argv[0]
    response = requests.get(
        'http://challenge-server.code-check.io/api/hash',
        {'q':f"{q}"})
    print(response.json())


if __name__ == '__main__':
    main(sys.argv[1:])
