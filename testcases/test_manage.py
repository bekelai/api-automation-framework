from api import post_api

def test_create_post(session):
    r = post_api.create_post(session,"学习测试","今天学requests",1)
    assert r.status_code == 201
    data = r.json()
    assert data["title"] == "学习测试"
    assert "id" in data

def test_update_post(session):
    r = post_api.update_post(session, 1, "更新后的标题", "更新后的内容", 1)
    assert r.status_code == 200
    assert r.json()["title"] == "更新后的标题"

def test_delete_post(session):
    r = post_api.delete_post(session, 1)
    assert r.status_code == 200
    assert r.json() == {}  # 删除后响应是空 dict
