project-2 Recommendation System
===============================
author Chengchang Qian

== Features ==
Complete Features:
1. User registration
2. User login/logout
3. Setup email verification and password recovery
4. Explore and rate movies

Developing Features:
1. Provide recommendations
2. Improve the recommendation result

== Structure ==
App
	- data (saved data)
		- movielens (movielens data)
		- data.csv (clean up movie data)
		- sim.csv (similarity matrix)
		
	- static (static fiels)
		- css (styling sheets)
		- fonts (customized fonts)
		- images (static images)
		- js (scripts)
		- less (less files)
		- scss (scss files)
		- favicon.icon (favicon icon)

	- views (html templates)
		- main.html (base template with sidebar)
		- main_nonav.html (base template without sidebar)
		- home.html (home / movie explore template)
		- recommend.html (recommendations template)
		- login.html (login template)
		- signup.html (signup template)
		- resetpassword.html (reset password template)
		- forget.html (recover password template)
		- message.html (display message template)

	- data.py (data manipulation script)

	- recommendations.py (recommendation algorithm)

	- main.py (primary logic controller)

	- models.py (structure of models)

	- app.yaml (app config file)

	- README.md (readme file)
