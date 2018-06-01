from taxii2client import Collection

base_url = 'https://flarecloud-2127152721.us-east-1.elb.amazonaws.com:443/v0.0.1/'
user = 'client1'
password = 'password'
verify = False
collection_id = '8c99d7d2-8a6c-4196-b216-c1692d0126f2'

print("\n\n Collection 1 info:")
collection = Collection(base_url + 'api1/collections/' + collection_id + '/',
                        user=user, password=password, verify=verify)
print("\t Collection: \t" + collection.title)
print("\t Can read/write: \t" + str(collection.can_read) + ", " + str(collection.can_write))
print("\n")


def print_results(bundle):
    count = 0
    for o in bundle['objects']:
        print(o)
        count += 1
    print("Count: " + str(count))


# params = dict([('match[id]', 'identity--323cae45-86ef-4b78-a82e-c69f8a1ef06a'), ('match[version]', 'all')])
params = {'match[id]': 'identity--323cae45-86ef-4b78-a82e-c69f8a1ef06a', 'match[version]': 'all'}
# print_results(collection.get_objects())
# print_results(collection.get_objects(filter_kwargs=params))

# Manifest may not be part of plugfest testing
# print(collection.get_manifest())
# print(collection.get_manifest(filter_kwargs=params))
