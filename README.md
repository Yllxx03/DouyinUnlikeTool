## 使用

```CMD
python main.py
```

## Cookie导入

需要使用PC端的浏览器登录抖音，再按F12，点击网络，随机点击某音含有Cookie的数据包，将Cookie复制到提示输入的地方即可

## 批量取消点赞

要求输入请求路径为`/aweme/v1/web/aweme/favorite`的完整请求信息

打开浏览器F12，打开抖音的喜欢页面，在F12页面的筛选器输入`/aweme/v1/web/aweme/favorite`就能筛选出需要的请求数据包了，点击任意一个请求路径为`/aweme/v1/web/aweme/favorite`的数据包，将标头的完整URL复制即可

批量取消关注同理