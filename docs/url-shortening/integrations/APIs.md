# Shortening service APIs

---

## Header Parameters

The following header parameters are required across all APIs:

|  Parameter  |  Type  | Required |          Description           |
|:-----------:|:------:|:--------:|:------------------------------:|
| X-User-Code | String |   Yes    | Unique identifier for the user |

---
## List of APIs

1. [Add Url](#get-categories)
2. [Get Url](#add-category)



# Add Category

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

---
