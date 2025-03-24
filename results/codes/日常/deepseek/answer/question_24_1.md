以下是一个实现HTTP请求工具类的Python代码示例，使用`requests`库处理网络请求，并支持多种请求方法、参数、请求头和数据：

```python
import requests
from urllib.parse import urljoin

class HttpClient:
    def __init__(self, base_url='', default_params=None, default_headers=None):
        """
        初始化HTTP客户端
        :param base_url: 基础URL，后续请求的路径会基于此URL拼接
        :param default_params: 默认查询参数（所有请求携带）
        :param default_headers: 默认请求头（所有请求携带）
        """
        self.base_url = base_url
        self.default_params = default_params or {}
        self.default_headers = default_headers or {}

    def send_request(self, method, url, params=None, headers=None, data=None, json=None, **kwargs):
        """
        发送HTTP请求
        :param method: 请求方法（GET/POST/PUT/DELETE等）
        :param url: 请求路径（若base_url不为空，则会与其拼接）
        :param params: 本次请求的查询参数（合并到默认参数）
        :param headers: 本次请求的请求头（合并到默认头）
        :param data: 表单数据
        :param json: JSON数据
        :param kwargs: 其他requests支持的参数（如timeout、files等）
        :return: 包含响应信息的字典或错误信息
        """
        # 拼接完整URL
        final_url = urljoin(self.base_url, url)
        
        # 合并默认参数和传入参数
        final_params = {**self.default_params, **(params or {})}
        final_headers = {**self.default_headers, **(headers or {})}

        try:
            response = requests.request(
                method=method.upper(),
                url=final_url,
                params=final_params,
                headers=final_headers,
                data=data,
                json=json,
                **kwargs
            )
            response.raise_for_status()  # 自动处理4xx/5xx错误
        except requests.exceptions.RequestException as e:
            # 返回错误信息（可根据需求调整）
            return {
                'error': True,
                'message': str(e),
                'status_code': getattr(e.response, 'status_code', None)
            }
        else:
            # 返回标准响应信息
            return {
                'status_code': response.status_code,
                'headers': dict(response.headers),
                'content': response.text,
                'json': self._safe_json_parse(response)
            }

    @staticmethod
    def _safe_json_parse(response):
        """安全解析JSON响应"""
        try:
            return response.json()
        except ValueError:
            return None

# 使用示例
if __name__ == "__main__":
    # 初始化客户端（可设置全局默认参数）
    client = HttpClient(
        base_url="https://jsonplaceholder.typicode.com",
        default_headers={"User-Agent": "MyHTTPClient/1.0"}
    )

    # 发送GET请求
    get_response = client.send_request(
        method="GET",
        url="/posts/1",
        params={"verbose": "true"}  # 合并到默认参数
    )
    print("GET Response:", get_response)

    # 发送POST请求
    post_response = client.send_request(
        method="POST",
        url="/posts",
        json={
            "title": "foo",
            "body": "bar",
            "userId": 1
        },
        headers={"X-Custom-Header": "test"}  # 合并到默认头
    )
    print("POST Response:", post_response)
```

### 主要特性：
1. **灵活的参数管理**：
   - 支持在初始化时设置`base_url`、`default_params`和`default_headers`
   - 每次请求时传入的参数会与默认参数合并（传入参数优先级更高）

2. **请求方法支持**：
   - 支持所有HTTP方法（GET/POST/PUT/DELETE等）
   - 自动处理参数类型（查询参数、表单数据、JSON数据）

3. **异常处理**：
   - 自动捕获网络请求异常
   - 返回包含错误信息的字典（而非直接抛出异常）
   - 可扩展为抛出异常（移除`try-except`块）

4. **响应标准化**：
   - 返回包含状态码、响应头、文本内容和JSON解析结果的字典
   - 自动安全解析JSON内容

### 使用场景示例：
```python
# 在其他文件中导入并使用
from http_client import HttpClient

# 创建实例（可复用）
client = HttpClient(base_url="https://api.yourservice.com")

# 发送带鉴权头的请求
response = client.send_request(
    method="GET",
    url="/user/data",
    headers={"Authorization": "Bearer your_token"}
)

if 'error' in response:
    print("请求失败:", response['message'])
else:
    print("响应数据:", response['json'])
```

可根据实际需求扩展以下功能：
- 添加文件上传支持（通过`files`参数）
- 增加请求重试机制
- 添加SSL证书验证选项
- 支持异步请求