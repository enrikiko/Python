#Device Registry Service

##Usage

All responses will have the form

```json
{
  "data":"Mixed type holding the content of the response",
  "message":"Description of what happened"
}
```
Subsequent response definitions will only detail the expected value of the `data field`
###List all devices

**Definition**

`GET /devices`

**Response**

-`200 OK` on success

```json

{
  "identifier":"watering",
  "name":"Watering",
  "device-type":"boolean",
  "controller-gateway":"192.1.0.2"
}
