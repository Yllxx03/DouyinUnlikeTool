import requests
import re


# 获取关注列表
def get_follow(get_follow_url, headers):
    final_list = []
    res = requests.get(url=get_follow_url, headers=headers, verify=False)
    # print(res.text)
    if res.status_code == 200:
        # 处理第一页
        following_list = re.findall(r'"uid":"(\d+)",', res.text)
        # print(following_list)
        # print(len(following_list))
        final_list += following_list
        # 处理后面的页
        total = int(re.findall(r'"total":(\d+),', res.text)[0])
        page = total // 20
        for i in range(1, page + 1):
            get_follow_url = get_follow_url.replace("offset=0", f"offset={20 * page}")
            res = requests.get(url=get_follow_url, headers=headers, verify=False)
            if res.status_code == 200:
                following_list = re.findall(r'"uid":"(\d+)",', res.text)
                # print(following_list)
                # print(len(following_list))
                final_list += following_list
            else:
                print(f"获取第{page * 20}后的关注列表失败")
        return final_list
    else:
        print("获取关注列表失败")


# 关注或取消关注
def following(operate_type, user_list, headers):
    action = {1: "关注", 0: "取消关注"}
    print(f"开始处理关注事件，此次处理类型为：{action[operate_type]}")
    following_url = "https://www-hj.douyin.com/aweme/v1/web/commit/follow/user/?device_platform=webapp&aid=6383&channel=channel_pc_web&pc_client_type=1&pc_libra_divert=Windows&update_version_code=170400&support_h265=0&support_dash=0&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1707&screen_height=960&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=136.0.0.0&browser_online=true&engine_name=Blink&engine_version=136.0.0.0&os_name=Windows&os_version=10&cpu_core_num=20&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=100"
    for user_id in user_list:
        res = requests.post(url=following_url, headers=headers, data={
            "type": f"{type}",
            "user_id": f"{user_id}"
        })
        if res.status_code == 200:
            print(res.text)
            print(f"user_id: {user_id}{action[operate_type]}成功")
        else:
            print(f"user_id: {user_id}{action[operate_type]}失败")
    print(f"{action[operate_type]}事件处理完成")

