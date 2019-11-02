# Malicious Payload Indentification

## With machine learning !

Rest API for malicious payload validation using machine learning

# Examples

## Request

    POST /predict
    Content-type: application/json

    {
        "data": "payload_here"
    }

## Response

    {
        "data":"Xss"
    }

![alt text](docs/payloads.png)

![alt text](docs/payload2.png)

![alt text](docs/payload3.png)
