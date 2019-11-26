# 2. 禮物與邀請碼 API
---

## 2.1 列出所有禮物種類
描述： 取得禮物所有種類的類型名稱對應表

### 接口定義

| HTTP | Endpoint 路徑                     |
| :--- | :-------------------------------- |
| GET | `host`/v1.0/gift-types |

### Response 回傳資訊
```json
{
    "success": true,
    "data": [
        {
            "name": string, //顯示的名稱 e.g: 加息券
            "type": int //類型值 e.g: 0, 1, 2, 3, 4
        },
        ...
    ]
}
```


## 2.2 列出該會員所有可以使用的禮物與邀請碼
描述： 列出該會員所有的禮物邀請碼，其中 `type` 的數值可以透過 `/gift-types` 對應。

### 接口定義

| HTTP | Endpoint 路徑                     |
| :--- | :-------------------------------- |
| GET | `host`/v1.0/members/`member_id`/gifts |

### Response 回傳資訊
```json
{
    "success": true,
    "data": [
        {
            "type": int, //禮物所許的類型值 e.g: 0, 1, 2, 3, 4
            "description": string, //禮物的介紹描述
            "gitf_id": string, // 禮物的 ID
            "invitation": {
                "code": string, //禮物的邀請碼
                "url": string //禮物的邀請轉發連結
            }
        },
        ...
    ]
}
```