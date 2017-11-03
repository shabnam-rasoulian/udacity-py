import fresh_tomatoes
import media

before_sunrise = media.Movie("Before Surise",
                            """A young man and woman meet on a train in Europe, and
                            wind up spending one evening together in Vienna.""",
                            "https://upload.wikimedia.org/wikipedia/en/d/da/Before_Sunrise_poster.jpg",
                            "https://www.youtube.com/watch?v=25v7N34d5HE")

#print(before_sunrise.storyline)
#before_sunrise.show_trailer()

before_sunset = media.Movie("Before Sunset",
                            """Nine years after Jesse and Celine first met, they encounter each other 
                            again on the French leg of Jesse's book tour.""",
                            "https://upload.wikimedia.org/wikipedia/en/d/d1/Before_Sunset_poster.jpg",
                            "https://www.youtube.com/watch?v=25v7N34d5HE")

#print(before_sunset.storyline)
#before_sunset.show_trailer()

before_midnight = media.Movie("Before Midnight",
                            """We meet Jesse and Celine nine years on in Greece. Almost two decades 
                            have passed since their first meeting on that train bound for Vienna.""",
                            "https://upload.wikimedia.org/wikipedia/en/a/ad/Before_Midnight_poster.jpg",
                            "https://www.youtube.com/watch?v=Kv6JWoVKlGY")

black_book = media.Movie("Black Book",
                        """In the Nazi-occupied Netherlands during World War II, a Jewish singer infiltrates
                        the regional Gestapo headquarters for the Dutch resistance.""",
                        "https://upload.wikimedia.org/wikipedia/en/3/3e/Official_poster_Black_Book.jpg",
                        "https://www.youtube.com/watch?v=DIklvGsU7bM")

notebook = media.Movie("The Notebook",
                       """In a nursing home, resident Duke reads a romance story for an 
                        old woman who has senile dementia with memory loss.""",
                       "https://upload.wikimedia.org/wikipedia/en/8/86/Posternotebook.jpg",
                       "https://www.youtube.com/watch?v=FC6biTjEyZw")

the_holiday = media.Movie("The Holiday",
                            """Two women troubled with guy-problems swap homes in each other's countries, 
                            where they each meet a local guy and fall in love.""",
                            "https://upload.wikimedia.org/wikipedia/en/6/60/Theholidayposter.jpg",
                            "https://www.youtube.com/watch?v=BDi5zH18vxU")

movies = [before_sunrise, before_sunset, before_midnight, black_book, notebook, the_holiday]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
