post1 = {
"user_id":101,
"message":"Hello World",
"lenguage":"python",
"datetime":"20130213",
"location":(44.121234, -102.349813)
}
post2 = dict(user_id = 102,
message = "Wellcome to Python",
lenguage = "pythen",
datetime = "20130213",
location = (44.121234, -102.349813)
)
post2["lenguage"] = "Python"

print(post1)
print(post2)

try:
    print(post1["location"])
except KeyError:
    print("The post doesn't have that key")

location = post1.get("user_id", None)
print(location)

for key in post1.keys():
    print(key, " = ", post1[key])

for key, value in post2.items():
    print(key, " = ", value)
