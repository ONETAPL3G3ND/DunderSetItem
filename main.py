class Server:
    def __init__(self):
        self.users = {}

    def __setitem__(self, key, value):
        self.users[key] = value


if __name__ == "__main__":
    server = Server()
    server['kirill'] = "012345678"
    server["Vasya"] = "0000"
    server["Katya"] = "10111101"
    print(server.users)