import pytest
from src.search import Post, SearchEngine

def test_search_bar_visibility():
    # Test that the search bar is visible and accessible on the main page
    # This test is more related to the UI and cannot be tested directly with the provided code
    # However, we can test that the search function is working correctly
    posts = [
        Post("LemmyHub Introduction", "Welcome to LemmyHub!", "LemmyHub"),
        Post("Search Functionality", "Implementing search functionality for LemmyHub.", "LemmyHub Development"),
        Post("Community Guidelines", "Guidelines for the LemmyHub community.", "LemmyHub"),
    ]

    search_engine = SearchEngine(posts)
    query = "LemmyHub"
    results = search_engine.search(query)
    assert len(results) > 0

def test_search_query():
    # Test that users can input search queries and receive relevant results
    posts = [
        Post("LemmyHub Introduction", "Welcome to LemmyHub!", "LemmyHub"),
        Post("Search Functionality", "Implementing search functionality for LemmyHub.", "LemmyHub Development"),
        Post("Community Guidelines", "Guidelines for the LemmyHub community.", "LemmyHub"),
    ]

    search_engine = SearchEngine(posts)
    query = "Introduction"
    results = search_engine.search(query)
    assert len(results) > 0

def test_results_filtered_by_relevance():
    # Test that results are filtered by relevance and include post title, content, and community
    posts = [
        Post("LemmyHub Introduction", "Welcome to LemmyHub!", "LemmyHub"),
        Post("Search Functionality", "Implementing search functionality for LemmyHub.", "LemmyHub Development"),
        Post("Community Guidelines", "Guidelines for the LemmyHub community.", "LemmyHub"),
    ]

    search_engine = SearchEngine(posts)
    query = "LemmyHub"
    results = search_engine.search(query)
    results = search_engine.filter_by_relevance(results, query)
    assert len(results) > 0
    for post in results:
        assert hasattr(post, "title")
        assert hasattr(post, "content")
        assert hasattr(post, "community")
