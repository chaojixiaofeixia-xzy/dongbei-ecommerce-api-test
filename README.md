## Bing 搜索功能自动化测试

### 项目描述
本项目使用 Python + Selenium 实现对 Bing 搜索核心功能的自动化测试，验证搜索结果中是否包含目标关键词。

### 技术栈
- 语言：Python 3.10
- 自动化框架：Selenium WebDriver
- 浏览器：Microsoft Edge
- 断言验证：Python assert

### 测试场景
1. 打开 Bing 搜索首页
2. 定位搜索框，输入"东北大学"
3. 执行搜索
4. 验证搜索结果页面包含"东北大学"

### 如何运行
1. 克隆代码：`git clone https://github.com/超极小霞霞-XZY/selenium-bing-test.git`
2. 安装依赖：`pip install selenium`
3. 确保已安装 Edge 浏览器，并将 msedgedriver.exe 放在项目目录下
4. 运行脚本：`python test_baidu.py`

### 运行结果
终端输出：`✅ 测试通过！脚本运行成功，搜索结果包含了'东北大学'。`
