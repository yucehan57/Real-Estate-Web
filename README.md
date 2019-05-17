# Real-Estate-Web

Real Estate web app uses Django's built-in User Authentication system to allow users to register, login, and logout. Database I chose to incorporate with the project is PostgreSQL.
BT Real Estate company web app lets users define their search based on keyword, city, state, number of bedrooms desired, and ideal price range the property hunter is willing to pay. 
Home page fetches three featured listings from the database on which user can click on 'More Info' button to see the details of the listing. 
About page fetches all realtors from the database one of whom is the 'Seller of the Month'.
Users are allowed to make an inquiry for a listing. If user inquired for a listing, an inquiry can't be made again, and user will be prompted with a message stating an inquiry has already been made for that very listing.


#### Disclaimer: Front-end was not built by me. However, I have full proficiency to understand and change the code to my liking, as I did for the admin panel. 


### Requirements

* Python 3.6+
* Django 2.1+

### Installation

Clone the repo, create virtual environment:

    $ git clone https://github.com/yucehan57/Real-Estate-Web.git
    $ virtualenv env
    $ source /env/bin/activate
    
Environment is set up. To proceed, you begin by making necessary migrations:

    $ python manage.py makemigrations
    $ python manage.py migrate
    
And, run the server:

    $ python manage.py runserver
