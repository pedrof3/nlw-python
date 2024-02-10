from cerberus import Validator

body = {
    "data": {
        "elemento1": "abc",
        "elemento2": 123,
        "elemento3": 456,
    }
}

body_validator = Validator({
    "data": {
        "type": "dict",
        "schema": {
            "elemento1": {"type": "float", "required": True, "empty": False},
            "elemento2": {"type": "float", "required": True, "empty": False},
            "elemento3": {"type": "float", "required": True, "empty": False},
        }
    }
})

response = body_validator.validate(body)

print(response)
print(body_validator.errors)
