from taxii2client import Server, ApiRoot, Collection, Status

base_url = 'https://a3e8833e4e03711e782c912400ee178b-1362315974.us-east-1.elb.amazonaws.com:8001/v0.0.1/'
user = 'client1'
password = 'password'
verify = False

# Basic connectivity checks:
# server = Server('https://a3e8833e4e03711e782c912400ee178b-1362315974.us-east-1.elb.amazonaws.com:8001/v0.0.1/taxii/',
#                 user='admin', password='12qwaszx@#WESDXC', verify=False)
# server = Server('https://a3e8833e4e03711e782c912400ee178b-1362315974.us-east-1.elb.amazonaws.com:8001/v0.0.1/taxii/',
#                 verify=False)

server = Server(base_url + 'taxii/',
                user=user, password=password, verify=verify)

print("Server info: ")

print("Title: \t" + server.title)
print("Description: \t" + server.description)
print("API Roots:")
print("Contact: \t" + server.contact)
print("API Roots:")
print(server.api_roots)
# for api_root in server.api_roots:
#     print(api_root.title)