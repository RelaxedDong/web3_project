#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2022/6/13 3:09 PM
# @Author  : donghao
import requests
import time

ALERT_RULES = {
    '-3m': 5,
    '-5m': 8,
    '-30m': 15,
}

ALERT_TIME_CNN = {
    '-3m': "3分钟",
    '-5m': "5分钟",
    '-30m': "30分钟",
}

alerted_slugs = []


def main():
    while True:
        print('请求排行榜数据...')
        url = "https://rarity.mycointool.com/api/minting/rankv2"
        response = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0',
            'origin': 'https://mycointool.com',
            'referer': 'https://mycointool.com/',
        })
        resp = response.json()
        if resp.get("result") != "Success":
            print('请求error')
            return

        json_data_list = resp['data']
        for time_key, data_list in json_data_list.items():
            if time_key not in ALERT_RULES:
                continue

            mint_alert_cnt = ALERT_RULES[time_key]
            for data in data_list:
                total_mint = data['mint_total']
                if total_mint < mint_alert_cnt:
                    continue
                collection = data['collection']
                info = data['collection']['info']
                data_info = {
                    "dc": info['discord_url'],
                    "web": info['external_url'],
                    "eth_addr": f"https://etherscan.io/address/{data['contract']}",
                }
                if info.get("slug"):
                    data_info['opensea_url'] = f"https://opensea.io/collection/{info['slug']}"
                if collection['symbol'] in alerted_slugs:
                    continue

                alerted_slugs.append(collection['symbol'])
                print(f'{collection["symbol"]} {ALERT_TIME_CNN[time_key]} mint了{total_mint}次，快去mint...')
                print(data_info)
                print('*'*10)

        time.sleep(30)


if __name__ == '__main__':
    main()
