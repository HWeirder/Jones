import requests
import execjs
import json

session = requests.session()
index_url = 'https://fanyi.baidu.com/'
lang_url = 'https://fanyi.baidu.com/langedetect'
translate_api = 'https://fanyi.baidu.com/v2transapi'


def translate(text):
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Acs-Token": "1672387555244_1672392541716_axD0w9xqZ7RgZA0Drk4pgJTfcQM5zhIAeimx0kG6imXXQlONrK5c1lSprHlQgX9Pa5KLNwLaZsjDPnWhW6QMJS539qhk+PnvlsS9GslZ4iJe6NGElq/4dwKcAxOCKM3lSSkPcvI1OfXbIUf+T4hdmASPEX1m1LfTosdvv01l8hn28LStNUw8sQ4+HgyyHi8oowFq7RPpudn8auPxoZdGzlRMYr8+dvL4zFGUVfBJq4NcDZscwmIH6wwqpAm73Zf8/KeC+4jJMThdWooD9lcINUkhsw4ojxB9IG3NptB5PZjrQukzBEYhhvFwq1yI1uo/UlEl9rNvSPtcFl9qlK4dK5K+c38OUyInut8md5fLZh6cebCpxjtp0k1MUXDD58BoIcOyLovh0BIIpYVUPaX/TUCEIblgJ2qePXoyFxdJtek=",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://fanyi.baidu.com",
        "Pragma": "no-cache",
        "Referer": "https://fanyi.baidu.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": "^\\^Not?A_Brand^^;v=^\\^8^^, ^\\^Chromium^^;v=^\\^108^^, ^\\^Google",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\\^Windows^^"
    }
    cookies = {
        "BIDUPSID": "6CBD52B5DB6850D6A366A299896E5085",
        "PSTM": "1667901834",
        "BAIDUID": "6CBD52B5DB6850D6627F2143CB633DD7:FG=1",
        "MCITY": "-289^%^3A",
        "BDORZ": "B490B5EBF6F3CD402E515D22BCDA1598",
        "delPer": "0",
        "BAIDUID_BFESS": "6CBD52B5DB6850D6627F2143CB633DD7:FG=1",
        "BA_HECTOR": "0la5a5ak8l0gag2k2l250l8l1hqsmbt1i",
        "ZFY": "XO7qZM8BqEw5kOfWpGv1mpvex7f4LVIhpiUZ9QPU5E0:C",
        "Hm_lvt_64ecd82404c51e03dc91cb9e8c025574": "1672380449",
        "APPGUIDE_10_0_2": "1",
        "REALTIME_TRANS_SWITCH": "1",
        "FANYI_WORD_SWITCH": "1",
        "HISTORY_SWITCH": "1",
        "SOUND_SPD_SWITCH": "1",
        "SOUND_PREFER_SWITCH": "1",
        "BCLID": "10905596353326518066",
        "BCLID_BFESS": "10905596353326518066",
        "BDSFRCVID": "l48OJeC62lwJFSRjGArswN6sGeVJyboTH6aoODUHrqA5xCpTCU2WEG0P5f8g0Kub5ayWogKK0eOTHvkF_2uxOjjg8UtVJeC6EG0Ptf8g0M5",
        "BDSFRCVID_BFESS": "l48OJeC62lwJFSRjGArswN6sGeVJyboTH6aoODUHrqA5xCpTCU2WEG0P5f8g0Kub5ayWogKK0eOTHvkF_2uxOjjg8UtVJeC6EG0Ptf8g0M5",
        "H_BDCLCKID_SF": "tJAq_Dt-tC83fP36q47o5JFt-UQ0atFXKKOLVb42fp7keq8CD4vbyxK90x6x3Rjeb2_qQh3HQqcBHR72y5jHhU4v3t7Hbx_tMg7j-pOGtf3psIJMjtDWbT8U5fKt5RcUaKviaKJHBMb1fRvDBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTDMFhe4tX-NFtqTkftMK",
        "H_BDCLCKID_SF_BFESS": "tJAq_Dt-tC83fP36q47o5JFt-UQ0atFXKKOLVb42fp7keq8CD4vbyxK90x6x3Rjeb2_qQh3HQqcBHR72y5jHhU4v3t7Hbx_tMg7j-pOGtf3psIJMjtDWbT8U5fKt5RcUaKviaKJHBMb1fRvDBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTDMFhe4tX-NFtqTkftMK",
        "PSINO": "5",
        "H_PS_PSSID": "36551_37647_37907_38015_37623_36920_37990_37800_37936_37904_26350_37284_37881",
        "Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574": "1672392530",
        "ab_sr": "1.0.1_Y2YzMmRmZTE4N2Q5MzlmOTBiZWE1OTgwODIzNGNhNmE0MzU1ZDVkZjgxNGZlYjkzYWI5MTJhYzFkMzZiMmNkODVkNjZjYzYzNTczMGRmZDE3YTliMzUwY2IyMzUxYjIyZTE0NGFhM2ZmYjMyMTkzN2RlMTczMDViMTkzN2NiMGNiNjAzY2Q2YzU2ZDAyNTU2Yzc2MWNmYWYwODVhNTY0OA=="
    }
    url = "https://fanyi.baidu.com/v2transapi"
    params = {
        "from": "zh",
        "to": "en"
    }
    data = {
        "from": "zh",
        "to": "en",
        "query": text,
        "transtype": "realtime",
        "simple_means_flag": "3",
        "sign": execjs.compile(read_js("signa.js")).call("e", text),
        "token": "b1f6c07ffe99d382a2faaa129698ca30",
        "domain": "common"
    }
    response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)

    print(json.loads(response.text)["trans_result"]['data'][0]['dst'])


def read_js(path):
    with open(path, "r")as f:
        f = f.read()
    return f


if __name__ == '__main__':
    try:
        print("百度翻译(输入 `exit` 退出)")
        while True:
            input_text = input("请输入翻译字符:")
            if input_text == 'exit':
                break
            translate(input_text)
        input('Press Enter to exit...')
    except Exception as ex:
        print("出现如下异常%s" % ex)
    finally:
        input('程序执行失败，按任意键退出：')
