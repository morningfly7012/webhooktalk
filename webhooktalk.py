from discord import SyncWebhook

webhooklink = input('請輸入你的webhooks：')
webhook = SyncWebhook.from_url(webhooklink)
while True:
    i = input('輸入您要說的話：')
    webhook.send(i)
