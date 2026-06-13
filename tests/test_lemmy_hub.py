from lemmy_hub import LemmyHub, Post
import pytest

def test_search():
    posts = [
        Post(1, "Hello World", "This is a test post", "test", "2022-01-01"),
        Post(2, "Foo Bar", "This is another test post", "test", "2022-01-02"),
        Post(3, "Baz Qux", "This is yet another test post", "example", "2022-01-03"),
    ]
    hub = LemmyHub(posts)
    results = hub.search("test", topic="test")
    assert len(results) == 2
    assert results[0].title == "Hello World"
    assert results[1].title == "Foo Bar"

def test_search_topic():
    posts = [
        Post(1, "Hello World", "This is a test post", "test", "2022-01-01"),
        Post(2, "Foo Bar", "This is another test post", "test", "2022-01-02"),
        Post(3, "Baz Qux", "This is yet another test post", "example", "2022-01-03"),
    ]
    hub = LemmyHub(posts)
    results = hub.search("test", topic="test")
    assert len(results) == 2
    assert results[0].title == "Hello World"
    assert results[1].title == "Foo Bar"

def test_search_date():
    posts = [
        Post(1, "Hello World", "This is a test post", "test", "2022-01-01"),
        Post(2, "Foo Bar", "This is another test post", "test", "2022-01-02"),
        Post(3, "Baz Qux", "This is yet another test post", "example", "2022-01-03"),
    ]
    hub = LemmyHub(posts)
    results = hub.search("test", date="2022-01-01", topic="test")
    assert len(results) == 1
    assert results[0].title == "Hello World"

def test_search_pagination():
    posts = [
        Post(1, "Hello World", "This is a test post", "test", "2022-01-01"),
        Post(2, "Foo Bar", "This is another test post", "test", "2022-01-02"),
        Post(3, "Baz Qux", "This is yet another test post", "example", "2022-01-03"),
        Post(4, "Qux Foo", "This is yet another test post", "test", "2022-01-04"),
        Post(5, "Bar Baz", "This is yet another test post", "test", "2022-01-05"),
    ]
    hub = LemmyHub(posts)
    results = hub.search("test", topic="test", page=1, per_page=2)
    assert len(results) == 2
    assert results[0].title == "Hello World"
    assert results[1].title == "Foo Bar"
    results = hub.search("test", topic="test", page=2, per_page=2)
    assert len(results) == 2
    assert results[0].title == "Qux Foo"
    assert results[1].title == "Bar Baz"
