# DelWeibo
批量删除微博

## 使用方法：
1. 将 st 参数的值替换，将 UID 替换为自己的微博数字 id    
2. 在浏览器中登陆微博，将 cookie 替换为当前 cookie
3. 在已安装相应依赖包的 Python 3.x 环境下运行 delweibo.py

## 注意：
- 多线程删除过多会触发删除微博的 rate limit。    
- 如使用注释内的匹配方法而非正则匹配，则需将解析器参数由 'html5lib' 改为 'lxml'。
