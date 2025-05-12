import requests
import re


# 获取关注列表
def get_follow(get_follow_url, header):
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
def following(operate_type, user_list, header):
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


if __name__ == '__main__':
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Cookie": "SEARCH_RESULT_LIST_TYPE=%22multi%22; ttwid=1%7CQBvDmxyFWLUd27E3-ydf0z2nnF7lr8nO7Wy6WhpkTLM%7C1746890961%7C36bf76e45fd84cc3dea3026f0515611e874d1bd9cf26537c0c69fd1aea1f536e; home_can_add_dy_2_desktop=%220%22; hevc_supported=true; IsDouyinActive=true; WallpaperGuide=%7B%22showTime%22%3A1746891026372%2C%22closeTime%22%3A1746891037366%2C%22showCount%22%3A1%2C%22cursor1%22%3A41%2C%22cursor2%22%3A12%2C%22hoverTime%22%3A1746891121874%7D; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; SearchMultiColumnLandingAbVer=2; SearchColumnSwitchLog=%5B%7B%22date%22%3A%222025-05-10%22%2C%22latestColumnType%22%3A%22multi%22%7D%5D; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; is_dash_user=1; odin_tt=198b5c62f8da057be8d236278fa5c9c25fef9faeed324a140d174c1be39e1b491361b832d2b2cb670375b8896e5461a48ffe4795a8a7f1a7a97c5e5cc2825ee7d0424eb79f5f18b1d206acff55558e82; passport_csrf_token=b4e49497de49b596667d74ce93ee6f82; passport_csrf_token_default=b4e49497de49b596667d74ce93ee6f82; __security_mc_1_s_sdk_crypt_sdk=d6c8cbb9-42a6-bd8a; __security_mc_1_s_sdk_cert_key=5f364371-4371-bb1d; __security_mc_1_s_sdk_sign_data_key_web_protect=e0785acc-40f7-bab4; bd_ticket_guard_client_web_domain=2; passport_mfa_token=CjgDE%2BYrV6g6ygzInJVac3DzZlTEAX1r11irTpvBraNAivJKDkK5cjnPmFQY4b720BppDJGpVlnpCBpKCjwAAAAAAAAAAAAATvqCtxO4yOYodJLT9zqaPrtwzFbomWixoCac1DYLph603x0ku%2FLL26M%2FkG2y67SvZqMQwYPxDRj2sdFsIAIiAQOa7q%2FS; d_ticket=dbd23ec8fc71a25b919f61c6bb66ec0377c90; passport_assist_user=Ck599li7xMD4ZvhPILD9QihxXKuUC2U7JU2vUp4buOWsAqo3rJEwpgbFKox_PPMx7TONmzweOqDiiN8CnEbKTBzvFll6oxwFMRts_17WMaMaSgo8AAAAAAAAAAAAAE76QtW1zlZ6UM82ewC5avUobj9G0xP0n4Aet_nQeGBmxWnf0ObmGZWFmoh1PqH5yHKXEKuE8Q0Yia_WVCABIgEDSwQYTA%3D%3D; n_mh=9-mIeuD4wZnlYrrOvfzG3MuT6aQmCUtmr8FxV8Kl8xY; sid_guard=cd1968c68be84d793b9b0444041b7813%7C1746902964%7C5183950%7CWed%2C+09-Jul-2025+18%3A48%3A34+GMT; uid_tt=4ae42c21a66f1cff9dedb58282b39715ecedb3aa91680387cf09e882101a88e8; uid_tt_ss=4ae42c21a66f1cff9dedb58282b39715ecedb3aa91680387cf09e882101a88e8; sid_tt=cd1968c68be84d793b9b0444041b7813; sessionid=cd1968c68be84d793b9b0444041b7813; sessionid_ss=cd1968c68be84d793b9b0444041b7813; is_staff_user=false; sid_ucp_v1=1.0.0-KDk5MmM5YjM1YmMxMmQ4YjEzYzExZDA5ZDYxNTMxN2IwNzdhNjU2YmUKHAi5iODst8PksmcQtL_-wAYY7zEgDDgGQPQHSAQaAmhsIiBjZDE5NjhjNjhiZTg0ZDc5M2I5YjA0NDQwNDFiNzgxMw; ssid_ucp_v1=1.0.0-KDk5MmM5YjM1YmMxMmQ4YjEzYzExZDA5ZDYxNTMxN2IwNzdhNjU2YmUKHAi5iODst8PksmcQtL_-wAYY7zEgDDgGQPQHSAQaAmhsIiBjZDE5NjhjNjhiZTg0ZDc5M2I5YjA0NDQwNDFiNzgxMw; login_time=1746891144669; SelfTabRedDotControl=%5B%5D; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAACo6h_5TPrDRZsgKWcWAXZOvpyB2mEvPA3PdR2ybcnrnNRA9Z45QyU7SI6EnfN3LW%2F1747065600000%2F0%2F1747034358210%2F0%22; publish_badge_show_info=%220%2C0%2C0%2C1746891176670%22; _bd_ticket_crypt_cookie=0c4b59b0285865654ebbff50e74c007b; __security_server_data_status=1; UIFID=d0e230a07fa0d9d6cc843b2a6f3839e84e72c08555f437f7b0bc997f277818341482f29fdda2377cd94e0a14abba00a0f1f4d4bbea6be944f00e93d8472f1621cc793924732a8131ecbd6578a21871c151cf5c2e6b17bcc51961bd8c19cf18d2eb2e7b70825b30145110daf9c7fa9d04a7294ddb8b2463557c36d6444d4a37130ab56c4ec1c04212862cce44826a751d7402a5e16652d04512c86446bce3d4e135ea35ee1e05684f627b3fea70813805128ef282a66856d70fd6e1ff9d6d2b84; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1707%2C%5C%22screen_height%5C%22%3A960%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A0%2C%5C%22downlink%5C%22%3A%5C%22%5C%22%2C%5C%22effective_type%5C%22%3A%5C%22%5C%22%2C%5C%22round_trip_time%5C%22%3A0%7D%22; my_rd=2; download_guide=%223%2F20250510%2F1%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAACo6h_5TPrDRZsgKWcWAXZOvpyB2mEvPA3PdR2ybcnrnNRA9Z45QyU7SI6EnfN3LW%2F1746892800000%2F0%2F1746892190666%2F0%22; EnhanceDownloadGuide=%220_0_1_1746900061_0_0%22; __security_mc_1_s_sdk_sign_data_key_sso=431e2d11-444c-ba34; sso_uid_tt=f73b1a5a890fd95b5739a5c6363d90644fe53d1f653562426d2d5a9a45a6a369; sso_uid_tt_ss=f73b1a5a890fd95b5739a5c6363d90644fe53d1f653562426d2d5a9a45a6a369; toutiao_sso_user=611e1f307db1c47a1430094c1116ee9d; toutiao_sso_user_ss=611e1f307db1c47a1430094c1116ee9d; sid_ucp_sso_v1=1.0.0-KDY4MGY4OGQ2ZmUyYjc1ZWQwMzIxMjNjZmZkZGMyMzUzODcxNWM4M2IKIgi5iODst8PksmcQ_77-wAYY7zEgDDCAs5a7BjgGQPQHSAYaAmxmIiA2MTFlMWYzMDdkYjFjNDdhMTQzMDA5NGMxMTE2ZWU5ZA; ssid_ucp_sso_v1=1.0.0-KDY4MGY4OGQ2ZmUyYjc1ZWQwMzIxMjNjZmZkZGMyMzUzODcxNWM4M2IKIgi5iODst8PksmcQ_77-wAYY7zEgDDCAs5a7BjgGQPQHSAYaAmxmIiA2MTFlMWYzMDdkYjFjNDdhMTQzMDA5NGMxMTE2ZWU5ZA; passport_auth_status=1723f7c4876a90f0eb985ea3a84764c6%2C; passport_auth_status_ss=1723f7c4876a90f0eb985ea3a84764c6%2C; _bd_ticket_crypt_doamin=2; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; strategyABtestKey=%221747034106.811%22; DiscoverFeedExposedAd=%7B%7D; biz_trace_id=97376ed4; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCRzB6UG5MQ1orTmZ0MnFrV2N4RVcySFZYbEFNeUVrN2F1SGNySGlUeElrRkgyWGRUem9tVERRK3lzanlITW4vZmx4UmQ3UGZjRXRpd1JBU1EzSEVjSmc9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D",
        "Host": "www-hj.douyin.com",
        "Origin": "https://www.douyin.com",
        "Referer": "https://www.douyin.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
        "bd-ticket-guard-web-version": "1",
        "sec-ch-ua": "\"Chromium\";v=\"136\", \"Microsoft Edge\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    url = "https://www-hj.douyin.com/aweme/v1/web/user/following/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&user_id=7450521805323240505&offset=0&min_time=0&max_time=0&count=20&source_type=4&gps_access=0&address_book_access=0&is_top=1&update_version_code=170400&pc_client_type=1&pc_libra_divert=Windows&support_h265=0&support_dash=0&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1707&screen_height=960&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=136.0.0.0&browser_online=true&engine_name=Blink&engine_version=136.0.0.0&os_name=Windows&os_version=10&cpu_core_num=20&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=100"
    result = get_follow(url, headers)
    print(result)
    print(len(result))
    following(0, result, headers)
