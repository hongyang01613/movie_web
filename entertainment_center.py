# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 09:10:31 2017

@author: admin
"""

import media
import fresh_tomatoes

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://list.youku.com/show/id_zde0eef689fa311df97c0.html")
movies = [avatar]
fresh_tomatoes.open_movies_page(movies)
