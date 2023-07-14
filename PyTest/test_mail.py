import pytest


def test_sending_mail_1(set_up,some):
    print("Письмо отправлено")
@pytest.mark.run(order=1)
def test_sending_mail_2(set_up):
    print("Письмо отправлено")
