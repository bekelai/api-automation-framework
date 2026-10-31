from api import post_api

def test_get_post(session):
    r=post_api.get_post(session,1)
    assert r.status_code == 200
    data = r.json()
    assert "userId" in data
    assert data["userId"] == 1
    assert data["id"] == 1


def test_get_posts(session):
    r = post_api.get_posts(session, user_id=2)
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) == 10

