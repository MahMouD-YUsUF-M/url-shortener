# Shortening service APIs

---

## Header Parameters

The following header parameters are required across all APIs:

|  Parameter  |  Type  | Required |           Description           |
|:-----------:|:------:|:--------:|:-------------------------------:|
| X-Guest-Code| String |   Yes    | Unique identifier for the guest |

---
## List of APIs

1. [short  Url](#add-url)
2. [Get Url info](#get-url-info)
3. [Get Url](#get-url)



# Short  Url

- This API creates a new short url for the user.
- The url  must be valid and secure.
- A unique short code is automatically generated.

### Endpoint

```http request
POST /v1/urls
```

### Request Body Parameters

| Parameter  |  Type  | Required |           Description            |
|:----------:|:------:|:--------:|:--------------------------------:|
| target_url | String |   Yes    |  target_url (must be valid url)  |

### Payload

```json
{
  "target_url": "https://www.google.com"
}
```

### Response

```json
{
  "success": true,
  "code": 200,
  "message": "Url shortening done!",
  "data": {
    "url_code": "https://short.url/fx82nk",
    "expires_at": "2024-07-30T14:30:00.123456"
  }
}
```

### Error Response

```json
{
  "success": false,
  "code": 400,
  "message": "Url must be valid"
}
```
```json
{
  "success": false,
  "code": 400,
  "message": "You reach the limit"
}
```
---

---

## Get  Url info

- This API returns basic information about any short URL


### End Point

```http request
GET /v1/urls
```


### Response

#### For all urls

```json

{
  "success": true,
  "code": 200,
  "message": "",
  "data": [
    {
      "code": "https://short.url/fx82nk",
      "target_url": "www.google.com",
      "expires_at": "2024-07-30T14:30:00.123456",
      "clicks": 1
    },
    {
      "code": "dsg33asf",
      "target_url": "www.atcoder.com",
      "expires_at": "2024-07-30T14:30:00.123456",
      "clicks": 6
    }
  ]
}
```




### Error Response

```json
{
  "success": false,
  "code": 500,
  "message": "Sorry, something went wrong on our side"
}
```

---



## Get Url

- This API  visit a short URL and  redirected user to the original website

### Endpoint

```http request
GET /v1/{code}
```
### Path Parameters
|  Parameter   |  Type  | Required |      Description      |
|:------------:|:------:|:--------:|:---------------------:|
|   url_code   | String |   Yes    | Unique code of the url|

### Response

```http 
HTTP/1.1 302 Found
Location: https://example.com/dashboard
```
### Error Response

```json
{
  "success": false,
  "code": 403,
  "message": "Sorry, url not found"
}
```
