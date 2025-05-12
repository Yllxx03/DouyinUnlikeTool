from Favorite import operate_favorite
from Follow import get_follow
from Follow import following


def favorite_fun():
    # 输入含有a_bogus的获取喜欢列表的url参数
    print(
        "请输入请求路径为/aweme/v1/web/aweme/favorite的完整请求信息，如https://xxx.com/aweme/v1/web/aweme/favorite/?device_platform=webapp&此处省略&a_bogus=")
    f_url = input()
    print("获取到的点赞列表路径为："+f_url)
    # 取消点赞
    operate_favorite(0, headers, f_url)


def follower_fun():
    print("请输入请求路径为aweme/v1/web/user/following/list的完整请求信息，如https://xxx.com/aweme/v1/web/user/following/list/?device_platform=webapp&aid=6383&此处省略后续部分")
    f_url = input()
    print("获取到的关注列表路径为：" + f_url)
    result = get_follow(f_url, headers)
    print(result)
    following(0, result, headers)


if __name__ == '__main__':
    logo = r"""
     _    _ _       _      
    | |  | (_)     | |     
    | |  | |_  __ _| | ___ 
    | |  | | |/ _` | |/ _ \
    | |__| | | (_| | |  __/
     \____/|_|\__, |_|\___|
                __/ |      
               |___/   Unlike-Tool
     声明：此工具仅用于个人学习使用，禁止非法使用，任何非法使用均与创作者本人无关
    """
    print(logo)

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Cookie": "",
        "Host": "www-hj.douyin.com",
        "Origin": "https://www.douyin.com",
        "Referer": "https://www.douyin.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
        "bd-ticket-guard-web-sign-type": "1",
        "bd-ticket-guard-web-version": "1",
        "sec-ch-ua": "\"Chromium\";v=\"136\", \"Microsoft Edge\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }

    # 输入Cookie
    Cookie = input("请输入Cookie:")
    headers["Cookie"] = Cookie

    option = 1
    while option:
        print("1：批量取消点赞")
        print("2：批量取消关注")
        print("0：退出脚本")
        option = int(input())
        if option == 1:
            favorite_fun()
        elif option == 2:
            follower_fun()
        else:
            option = 0






