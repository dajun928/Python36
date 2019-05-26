from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tmt.v20180321 import tmt_client, models
'''
腾讯翻译接口封装
https://console.cloud.tencent.com/tmt/manage
https://github.com/TencentCloud/tencentcloud-sdk-python
'''
try:
    cred = credential.Credential("AKIDShgQukxejY7QTVDyMUN0OWP7ZooYbLMA", "mKdhX8UaQ5UdXBaqrdJn34qOimbQ0MTL")
    httpProfile = HttpProfile()
    httpProfile.endpoint = "tmt.tencentcloudapi.com"


    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = tmt_client.TmtClient(cred, "ap-guangzhou", clientProfile)

    req = models.TextTranslateRequest()
    params = '{"SourceText":"hello world","Source":"en","Target":"zh","ProjectId":10177715}'
    req.from_json_string(params)

    resp = client.TextTranslate(req)
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)