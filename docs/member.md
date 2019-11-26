# 1. 會員與登入 API
---

## 1.1 會員登入
描述： 透過 `mobile` 手機登入 *(目前先不考慮 Auth Token )*

### 接口定義

| HTTP | Endpoint 路徑                     |
| :--- | :-------------------------------- |
| POST | `host`/v1.0/login |


### Request 請求參數
```json
{
    "mobile": string, // 會員手機號碼
}
```

### Response 回傳資訊
```json
{
    "success": true,
    "data": [
        {
            "member_id": string //會員的唯一 ID
        }
    ]
}
```