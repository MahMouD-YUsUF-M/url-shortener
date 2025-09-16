# Shortening service APIs

---

## Header Parameters

The following header parameters are required across all APIs:

|  Parameter  |  Type  | Required |          Description           |
|:-----------:|:------:|:--------:|:------------------------------:|
| X-User-Code | String |   Yes    | Unique identifier for the user |

---
## List of APIs

1. [Add Url](#add-url)
2. [Get Url info](#get-url-info)
3. [Get Url](#get-url)



# Add Url

- This API creates a new short url for the user.
- The url  must be valid and secure.
- A unique short code is automatically generated.

### Endpoint

```http request
POST /v1/url
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
    "url_code": "fx82nk",
    "expires_at": "9/16/2025, 2:48:30 PM"
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

## Get  Urls

- This API returns basic information about any short URL


### End Point

```http request
GET /v1/info/urls
```

##### For Specific url

```http request
GET /v1/info/urls/{code}
```
### Path Parameters

| Parameter  |  Type  | Required |       Description       |
|:----------:|:------:|:--------:|:-----------------------:|
|  url_code  | String |    No    | Unique code of the  url |


### Path Parameters For Specific url
| Parameter |  Type  | Required |      Description       |
|:---------:|:------:|:--------:|:----------------------:|
|   code    | String |   Yes    | Unique code of the url |

### Response

#### For all urls

```json

{
  "success": true,
  "code": 200,
  "message": "",
  "data": [
    {
      "code": "fx82nk",
      "target_url": "www.google.com",
      "expires_at": "9/16/2025, 2:48:30 PM",
      "clicks": 1
    },
    {
      "code": "dsg33asf",
      "target_url": "www.atcoder.com",
      "expires_at": "9/12/2025, 2:38:31 PM",
      "clicks": 6
    }
  ]
}
```

#### For specific url

```json
{
  "success": true,
  "code": 200,
  "message": "",
  "data": [
    {
      "code": "fx82nk",
      "target_url": "www.google.com",
      "expires_at": "9/16/2025, 2:48:30 PM",
      "clicks": 1
    }
  ]
}
```

### Error Response

#### For specific url

```json
{
  "success": false,
  "code": 403,
  "message": "Sorry, url not found"
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
GET /v1/url/{code}
```
### Path Parameters
| Parameter |  Type  | Required |      Description       |
|:---------:|:------:|:--------:|:----------------------:|
|   code    | String |   Yes    | Unique code of the url |

### Response

```json
{
  "success": true,
  "code": 302,
  "message": "",
  "data": [
   {
   "target_url": "https://www.google.com"
   }
  ]
}
```
### Error Response


```json
{
  "success": false,
  "code": 403,
  "message": "Sorry, url not found"
}
```