'''
Author: Travis CI travis@travis-ci.org
Date: 2022-06-06 10:04:41
LastEditors: Travis CI travis@travis-ci.org
LastEditTime: 2022-06-06 14:25:13
FilePath: \c:Users\morni\OneDrive - 晨飛\桌面\test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from discord import SyncWebhook

webhooklink = input('請輸入你的webhooks：')
webhook = SyncWebhook.from_url(webhooklink)
while True:
    i = input('輸入您要說的話：')
    webhook.send(i)