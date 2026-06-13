import json
from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Post:
    id: int
    title: str
    content: str
    topic: str
    date: str

class LemmyHub:
    def __init__(self, posts: List[Post]):
        self.posts = posts

    def search(self, query: str, topic: str = None, date: str = None, page: int = 1, per_page: int = 10):
        results = [post for post in self.posts if query.lower() in post.title.lower() or query.lower() in post.content.lower()]
        if topic:
            results = [post for post in results if post.topic == topic]
        if date:
            results = [post for post in results if post.date == date]
        results = sorted(results, key=lambda x: x.id)
        start = (page - 1) * per_page
        end = start + per_page
        return results[start:end]

    def save(self, filename: str):
        data = [{"id": post.id, "title": post.title, "content": post.content, "topic": post.topic, "date": post.date} for post in self.posts]
        with open(filename, "w") as f:
            json.dump(data, f)

    @classmethod
    def load(cls, filename: str):
        with open(filename, "r") as f:
            data = json.load(f)
        posts = [Post(**post) for post in data]
        return cls(posts)
