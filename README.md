# JBD-Sprint3-Day3

İki Proyekt yaradın.

## Assignment 1: Birinci proyekt:

Bu proyektdə iki səhifədən ibarət olmalıdı birinci səhifədə Bloglar yaradılmalı. İkinci səhifədə isə yaradılmış bloglar siyahı şəklində çıxmalıdır. Blogların `id`, `title`, `description` kimi xüsusiyyətləri olmalıdır.


Database olaraq `Mysql` istifadə olunmalıdır.



## Assignment 2: İkinci proyekt:

Bu proyektdə 4 səhifədən ibarət olmalıdı birinci səhifədə Bloglar yaradılmalı. İkinci səhifədə isə yaradılmış bloglar siyahı şəklində çıxmalıdır. Bu səhifədə hər hansı bir blog-a click etdikdə onun ətraflı səhifəsinə keçid etməlidir. (Yəni, bizim 3-cü səhifəyə)
3-cü səhifədə Blogların ətraflı səhifəsi açılmalı burada id-nə görə 1 blog haqqında məlumat və onun kommentləri görünməlidir.
4-cü səhifədə commentlər yaradılmalıdır.
Blogların `id`, `title`, `description` kimi xüsusiyyətləri olmalıdır. Commentlərin isə `id`, `contect` kimi xüsusiyyətləri olmalıdır.


Database olaraq Postgresql istifadə olunmalıdır.

## Qeyd:
  - Hər iki proyekt `dockerizasiya` edilməlidir.
  - Proyektlərdə olan servislər (Flask, Database) `docker-compose` vasitəsi quraşdırılmalıdır.
  - Proyektlərdə `Flask SQLAlchemy` istifadə edilməlidir.



## Bonus

Birinci proyektin bazasına yazılan bloglar avtomatik şəkildə ikinci proyektin bazasına əlavə edilməlidir.
  - Bunun üçün redis publish subscribe xüsusiyyətlərindən istifadə edilməlidir.