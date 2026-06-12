import json
from dataclasses import dataclass
from typing import List

@dataclass
class Post:
    title: str
    content: str
    community: str

class SearchEngine:
    def __init__(self, posts: List[Post]):
        self.posts = posts

    def search(self, query: str) -> List[Post]:
        results = []
        for post in self.posts:
            if query.lower() in post.title.lower() or query.lower() in post.content.lower():
                results.append(post)
        return results

    def filter_by_relevance(self, results: List[Post], query: str) -> List[Post]:
        results.sort(key=lambda post: post.title.lower().find(query.lower()) if query.lower() in post.title.lower() else float('inf'))
        return results

def main():
    posts = [
        Post("LemmyHub Introduction", "Welcome to LemmyHub!", "LemmyHub"),
        Post("Search Functionality", "Implementing search functionality for LemmyHub.", "LemmyHub Development"),
        Post("Community Guidelines", "Guidelines for the LemmyHub community.", "LemmyHub"),
    ]

    search_engine = SearchEngine(posts)

    query = input("Enter your search query: ")
    results = search_engine.search(query)
    results = search_engine.filter_by_relevance(results, query)

    print("Search results:")
    for post in results:
        print(f"Title: {post.title}")
        print(f"Content: {post.content}")
        print(f"Community: {post.community}")
        print()

if __name__ == "__main__":
    main()
