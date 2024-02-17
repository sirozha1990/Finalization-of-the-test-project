import requests
import yaml
import logging

with open("testdata.yaml", "r") as f:
    data = yaml.safe_load(f)


def get_post(token):
    resource = requests.get("https://test-stand.gb.ru/api/posts",
                            headers={"X-Auth-Token": token},
                            params={"owner": "notMe"})

    return resource.json()


def test_1(login, send_email):
    logging.info('Test1: API start loging')
    result = get_post(login)['data']
    lst = []
    for item in result:
        lst.append(item['id'])
    print(lst)
    logging.debug(f"get request return: {result}")
    assert 98509 in lst, "test_1 fail"


def test_2(login, send_email):
    logging.info("Test2: API Create post")
    result1 = requests.post(data['address'],
                            headers={"X-Auth-Token": login},
                            params={'title': data['title'], 'description': data['description'],
                                    'content': data['content']})
    result2 = requests.get(data['address'], headers={"X-Auth-Token": login},
                           params={'description': data['description']})

    assert result1 and result2, "test_2 fail"