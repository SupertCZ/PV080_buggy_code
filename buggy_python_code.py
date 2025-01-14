import flask
import yaml
import urllib3
import urllib as urllib2

app = flask.Flask(__name__)


@app.route("/")
def index():
    version = flask.request.args.get("urllib_version")
    url = flask.request.args.get("url")
    return fetch_website(version, url)

        
CONFIG = {"API_KEY": "771df488714111d39138eb60df756e6b"}
class Person():
    def __init__(self, name):
        self.name = name


def print_nametag(format_string, person):
    print(format_string.format(person=person))


def fetch_website(urllib_version, url):
    # Import the requested version (2 or 3) of urllib
    urllib = urllib2 if urllib_version == 2 else urllib3
 
    try: 
        http = urllib.PoolManager()
        return http.request('GET', url)
    except ConnectionError:
        print('ConnectionException')


def load_yaml(filename):
    stream = open(filename)
    deserialized_data = yaml.safe_load(stream, Loader=yaml.Loader) #deserializing data
    return deserialized_data


def authenticate(password):
    # Assert that the password is correct
    if password == "ILoveyou":
        print("Successfully authenticated!")


if __name__ == '__main__':
    print("Vulnerabilities:")
    print("1. Format string vulnerability: use string={person.__init__.__globals__[CONFIG][API_KEY]}")
    print("2. Code injection vulnerability: use string=;print('Own code executed') #")
    print("3. Yaml deserialization vulnerability: use string=file.yaml")
    print("4. Use of assert statements vulnerability: run program with -O argument")
    CHOICE = input("Select vulnerability: ")
    if CHOICE == "1":
        NEW_PERSON = Person("Vickie")  
        print_nametag(input("Please format your nametag: "), NEW_PERSON)
    elif CHOICE == "2":
        URLLIB_VERSION = input("Choose version of urllib: ")
        fetch_website(URLLIB_VERSION, url="https://www.google.com")
    elif CHOICE == "3":
        load_yaml(input("File name: "))
        print("Executed -ls on current folder")
    elif CHOICE == "4":
        PASSWORD = input("Enter master PASSWORD: ")
        authenticate(PASSWORD)

