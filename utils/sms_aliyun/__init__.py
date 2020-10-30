#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

def send_msg_to_phone(phone_num, content):
    """
    将阿里云提供的发送短信demo，封装为函数，方便使用
    :param phone_num:
    :param content:
    :return:
    """
    client = AcsClient('LTAI4G1oysXZpEyYbZ7QpquM', 'tmF4XN5qBPI0fao2MhczdtLco7UeaK', 'cn-hangzhou')

    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', phone_num)
    request.add_query_param('SignName', "flask项目")
    request.add_query_param('TemplateCode', "SMS_204286300")
    request.add_query_param('TemplateParam', "{\"code\":\"%s\"}" % content)

    response = client.do_action(request)
    # python2:  print(response)
    print(str(response, encoding='utf-8'))


if __name__ == "__main__":
    send_msg_to_phone("19852744199","123123")
