from yoomoney import Client, Quickpay
from uuid import uuid4
from Config.config import token_yoomoney

client = Client(token_yoomoney)


#создание запроса на платёж
def bill():
       quickpay = Quickpay(
       receiver=123456789,
       quickpay_form='shop',
       targets='pay',
       paymentType='5B',
       sum=2,
       label=str(uuid4())
       )
       return quickpay.base_url