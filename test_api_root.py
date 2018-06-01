from taxii2client import Server, ApiRoot, Collection, Status

base_url = 'https://a3e8833e4e03711e782c912400ee178b-1362315974.us-east-1.elb.amazonaws.com:8001/v0.0.1/'
user = 'client1'
password = 'password'
verify = False

print("\n\n API Root 1 info:")
api_root = ApiRoot(base_url + 'api1/',
                   user=user, password=password, verify=verify)
print("API Root title: \t" + api_root.title)
print("API Root description: \t" + api_root.description)
for collection in api_root.collections:
    print("\t Collection: \t" + collection.title)
    print("\t ID: \t" + collection.id)
    print("\t Description: \t" + collection.description)
    print("\t Can read/write: \t" + str(collection.can_read) + ", " + str(collection.can_write))
    print("\n")
