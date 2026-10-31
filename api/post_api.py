# 接口封装层：一个接口=一个函数，参数进、响应出。所有 URL 和请求细节只住在这个文件里。
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_posts(session, user_id=None):
    params = {}
    if user_id is not None:
        params["userId"] = user_id
    return session.get(BASE_URL + "/posts", params=params, timeout=5)


def get_post(session, post_id):
    return session.get(BASE_URL + "/posts/" + str(post_id), timeout=5)


def create_post(session, title, body, user_id):
    return session.post(BASE_URL + "/posts",
                        json={"title": title, "body": body, "userId": user_id},
                        timeout=5)


def update_post(session, post_id, title, body, user_id):
    return session.put(BASE_URL + "/posts/" + str(post_id),
                       json={"id": post_id, "title": title, "body": body, "userId": user_id},
                       timeout=5)


def delete_post(session, post_id):
    return session.delete(BASE_URL + "/posts/" + str(post_id), timeout=5)
