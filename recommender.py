def get_rule_based_recommendations(books_list, selected_genre, selected_mood, selected_length):
    """
    Applies rule filters using list comprehensions and sorts by rating using Python's sorted().
    """
    filtered = []
    
    for book in books_list:
        match_genre = (selected_genre == "Any" or book["genre"] == selected_genre)
        match_mood = (selected_mood == "Any" or book["mood"] == selected_mood)
        match_length = (selected_length == "Any" or book["length"] == selected_length)
        
        if match_genre and match_mood and match_length:
            filtered.append(book)
            
    # Sort results by highest rating (descending)
    recommended = sorted(filtered, key=lambda x: x["rating"], reverse=True)
    
    return recommended