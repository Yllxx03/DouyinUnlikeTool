from time import sleep
import random
import requests
import re


# 获取抖音喜欢列表
def get_favorite(headers, f_url):
    res = requests.get(url=f_url, headers=headers, verify=False)
    if res.status_code == 200:
        # print(res.text)
        video_list = re.findall('"aweme_id":"(\d+)",', res.text)
        print("成功获取到下面视频aweme_id：")
        print(video_list)
        return video_list
    else:
        print("获取点赞列表失败")


# 点赞操作函数
def favorite(operate_type, video_list, headers):
    action = {1: "点赞", 0: "取消点赞"}
    print(f"开始处理点赞事件，此次处理类型为：{action[operate_type]}")
    favorite_url = "https://www-hj.douyin.com/aweme/v1/web/commit/item/digg/?device_platform=webapp&aid=6383&channel=channel_pc_web&pc_client_type=1&pc_libra_divert=Windows&update_version_code=170400&support_h265=1&support_dash=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1707&screen_height=960&browser_language=zh-CN&browser_platform=Win32&browser_name=Firefox&browser_version=137.0&browser_online=true&engine_name=Gecko&engine_version=137.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=&platform=PC"
    for video_id in video_list:
        res = requests.post(url=favorite_url, headers=headers, data={
            "aweme_id": f"{video_id}",
            "item_type": "0",
            "type": f"{operate_type}"
        })
        if res.status_code == 200:
            print(res.text)
            print(f"video_id: {video_id}{action[operate_type]}成功")
            sleep(random.uniform(0.5, 1.0))
        else:
            print(f"video_id: {video_id}{action[operate_type]}失败")
    print(f"{action[operate_type]}事件处理完成")


# 整合函数
def operate_favorite(operate_type, header, f_url):
    video_list = get_favorite(header, f_url)
    while len(video_list) > 0:
        favorite(operate_type, video_list, header)
        video_list = get_favorite(header, f_url)
    print("检测到点赞列表已为0，程序结束")
