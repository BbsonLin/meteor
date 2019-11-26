# NextBank - IBMB API 規格文件
---
該文件包含了 IBMB 中台的 API 傳輸規則、連線環境設定、 API 路由的定義與錯誤訊息。

## API 傳輸風格

### 1. 請求的網域名
以下為測試或正式連線 API 的網域環境，透過此方式區分測試資料或正式資料:

| 環境                 | API 網域                   |
| :-------------------- | :-------------------------- |
| 開發環境測試 | https://ncb.ap.ngrok.io  |

註：上述網域在後續的 API Endpoint 文件中不會直接呈現，而會以代號 `host` 表示。



### 2. 呼叫 API 方式

採用 HTTP Restful Style 風格，以 GET, POST, PATCH, DELTE 方式呼叫 API 來請求結果，透過上以下四種做 CRUD 的操作。

* **GET** ：取得指定的單一資源或列表資源
* **POST** ：新增資源（資料)，或取得資源。
* **PATCH**：更新指定的資源內容。
* **DELETE**：刪除指定的資源 (硬刪除使用，軟刪除採用 PATCH)

### 3. Response 回傳格式

#### 3.1 請求成功，回傳正常的結果
請求成功，且回傳正常的結果，回傳 HTTP Status code 為 200。

以下為請求成功後回傳的格式：

```json
{
    "success": boolean, // true 表示請求結果返回成功, false 表示錯誤，回傳錯誤結果。
    "data": [ 
         {
            //  回傳的資料內容
         },
         ...
    ]
}
```

註： `data` 的欄位，無論多筆或單筆資料，皆採用 Array 方式回傳呈現。


#### 3.2 請求成功，發生預期的例外錯誤
請求成功，但發生可預期的錯誤，回傳 HTTP Status code 為 200，但內部會透過 `error` 參數來取得錯誤代碼與訊息，可以透過 `success` 判斷有無 `error`。


```json
{
    "success": boolean, // true 表示請求結果返回成功, false 表示錯誤，回傳錯誤結果。
    "error": {
        "code": string, //例外代碼，以 大寫與底線命名 e.g: "ORDER_NOT_FOUND" or "10001"
        "message": string //代碼的描述訊息， e.g: "The member does not found"
    }
}
```

#### 3.3 請求成功，發生未預期的例外錯誤

*關於 Server 內部「無法預期」的例外產生的錯誤顯示格式，後續再討論*


## 透過 Postman 工具測試
[Postman](https://www.getpostman.com/) 是一套 API 的測試工具，可以透過圖形化介面與參數來測試 API 是否可以執行。

建議先使用此套工具，並透過匯入（Import）程式碼中的 Postmain API 文件檔 (`NextBank IBMB Dev API.postman_collection.json`) 與環境 (`NextBank Local Dev Env.postman_environment.json`) 檔：


## API 文件版本更新資訊

| 版本號                 | 日期                   | 修改描述                   |
| :-------------------- | :-------------------------- |:-------------------------- |
| 1.0.0 | 2019/11/25  | 初版文件撰寫，撰寫 Gift 與 Member 兩組功能 API |
