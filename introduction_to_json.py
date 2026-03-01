

import json

### TASK 1


user_profile = {
    "name": "Alex Honnold",
    "age": "40",
    "email": "dummyemail@gmail.com",
    "is_active": True,
    "skills": ["Rock Climbing", "Intense Focus", "Strong Grip"]
}

print(f"############# TASK 1 #############")
json_string = json.dumps(user_profile, indent=2)
print(json_string)

### TASK 2

api_response = '{"status": "success", "data": {"user_id": 101, "username": "alex99", "score": 87.5}}'

api_dict = json.loads(api_response)

username = api_dict["data"]["username"]
score = api_dict["data"]["score"]
print(f"\n\n############# TASK 2 #############")
print(f"User {username} scored {score} points")


### TASK 3

nested_json = {
  "name": "Priya",
  "address": {
    "city": "Bengaluru",
    "state": "Karnataka",
    "zip": "560001"
  }
}


nested_json["address"]["country"] = "India"


print(f"\n\n############# TASK 3 #############")
json_string = json.dumps(nested_json, indent=2)
print(json_string)
