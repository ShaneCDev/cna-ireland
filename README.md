# cna-ireland
This is an E-Commerce website I made for a fictional business that will be selling CBD Products and sharing blog posts related to CBD and its benefits. The main purpose is to get customers thinking about and considering about alternative health routes that holistic and not modern medicine for lack of a better term.
![AmIResponsive](/docs/readmeimgs/amiresponsive%20image.png)
The website can be viewed here. [MGSR](https://reddjango.herokuapp.com/)

# Index - Table of Contents

- [User Experience (UX)](https://github.com/ShaneCDev/reddango#user-experience-ux)
- [Features](https://github.com/ShaneCDev/reddango#features)
- [Technologies Used](https://github.com/ShaneCDev/reddango#technologies-used)
- [Testing](https://github.com/ShaneCDev/reddango#testing)
- [Deployment](https://github.com/ShaneCDev/reddango#deployment)
- [Credits](https://github.com/ShaneCDev/reddango#credits)
- [Acknowledgments](https://github.com/ShaneCDev/reddango#acknowledgments)

# User Experience (UX)

## User Stories

- ## As a website owner I want:
1. The website allows users to purchase products that are listed on the webstore.
2. The website gives users a great experience while they are visting the site.
3. The website allows users buy products as either a registered user or a guest.
4. The website allows users to check their order history.
5. The website allows users to save their profile data for faster checkouts should they use the site in the future.

- ## As a website user I want:
1. To view and search for products.
2. To filter products based on criteria.
3. To be able to create an account.
4. To be able to edit profile data.
5. To be able to add products to the shopping bag and make purchases.
6. Contact the site owner/customer service.

- ## As a returning website user I want:
1. To check out other people's reviews.
2. Change my review and review score if my opinion should change.

# 1. Strategy
- The main purpose of the site is to provide people with place to purchase CBD products whether it be for medical reasons or recreational ones.

# 2. Scope
- The multipage design is simple and the information provided is clear and concise.
- The information can be accessed on all devices.

# 3. Structure
- Users will find themselves on the homepage where they will be met by a background image and a "Shop Now" button and clicking this button will take users to the products page. Users will also see a navigation bar at the top of the screen.
- The fixed nav bar has a logo on the left search bar in the centre and the navigation items positioned slightly below the search bar, to the right of the search bar you can check your bag or register for an account or login.
- The are all layed out different depending on what screen you are using to visit the site.
- If you click on any of these products you will be brought to the product detail page and from there you can see the product description and add the product to your bag if you wish or click the other button to be redirected back to the products page.
- On the products page there is also a sort menu where you can filter the products accordingly for example you can filter them by price highest to lowest and vice versa and more options are available too.
- For admin users on the products page they will see two buttons "Edit" and "Delete" these buttons are pretty self explanatory, clicking on edit will bring you to the edit product page where you can change the name, category, description, price and image. Clicking the delete button will make a modal pop up which will ask you to confirm your action.
- Clicking on the "Leave A Review" button will take you to the review page which displays a form to the user to fill out upon submitting the form the user will be redirected to the page they just came from and their review will be displayed there.
- There is also an edit button on the reviews that the user wrote, upon clicking on that button it will bring you to the edit-review page where the user can edit their review as they see fit and upon submitting the form the review will be updated and the user redirected back to the page they just came from.
- The footer sections provides the user with social media links to follow the hosts of the 
site.

# 4. Skeleton
## Wireframes
The wireframes were made using Balsamiq.
- [Home](docs/wireframes/homepagewireframe.png)
- [Movies, Games, Shows](docs/wireframes/mgs%20pages%20wireframes.png)
- [Detail Page](docs/wireframes/detailpageswireframe.png)
- [Review, Edit Review](docs/wireframes/reviewwireframe.png)
- [Register](docs/wireframes/signupwireframe.png)
- [Login](docs/wireframes/signinwireframe.png)
- [Signout](docs/wireframes/signoutwireframe.png)

# 5. Surface
- ## Colour
![Colour Pallette](docs/readmeimgs/colourpalette.png)

The colour palette is basic enough but I think its clean and nice, it consists of a whtie and black. Its simple but effective in my opinion.

- ## Font
---
'Lato' font is used for this website.

# Features
## Existing Features

## Navigation Bar
![Navigation Bar](/docs/readmeimgs/navbar.png)
- The navigation bar is fixed for this multi-paged website.
- There is a very simple "MGS | Reviews" logo located to the left of the navigation bar, located slightly to the right of the logo is each page and depending on if the user is logged in or not this will look different. If the user is logged in then the navbar links will be "Home, Movies, Games, Shows, Logout" if they are not logged in then it will be as follows "Home, Movies, Games, Shows, Register, Login".
- The logo acts as a button also and clicking on it will redirect you back to the home page.
- The navbar is responsive as on smaller devices it will turn into a hamburger menu that holds all the links and the logo.
- Upon clicking on any navigation link the website will redirect you to the respective page.

## Home Page
![Home Page](docs/readmeimgs/homepage.png)
- The home page is made up of three carousels which I think is a nice way of displaying different media.
- The page is evenly divided into three rows, each image in the carousel is clickable and clicking on any of them will bring the user to the detail page for whatever they clicked on for example if the user clicks on Sekiro they will be brought to the Sekiro detail page.

## Movies
![Movies](docs/readmeimgs/moviespage.png)
- This is the movies page and it is a 4x4 grid of twelve movies posters which are easily recognisable and upon clicking on them the user will be brought to the detail page.
- This layout is shared across the Games, and Shows pages also to keep things consistent.

## Movie Detail
![Movie Detail](docs/readmeimgs/moviesdetail.png)
- This detail page is also shared across Games, and Shows with some minor details in the data that is displayed to the user.
- There is also a "Leave A Review" button that will be on this page if the user is logged in and has not yet left a review.
- If there are no reviews for the movie then "No reviews for this movie yet" will be displayed.
- If the user has already left a review the review will be displayed here in a little card and at the bottom of the card will be an edit button should they wish to edit their review.

## Games
![Games](docs/readmeimgs/gamespage.png)

## Games Detail
![Games Detail](docs/readmeimgs/gamesdetail.png)

## Shows
![Shows](docs/readmeimgs/showspage.png)

## Shows Detail
![Shows Detail](docs/readmeimgs/showsdetail.png)

## Review
![Review](docs/readmeimgs/reviewpage.png)
- This is the page the user will be brought to upon clicking the "Leave A Review" button.
- This page consists of a form for the user to fill out which upon submitting will redirect them back to the page they just came from and post their review for all users to see.
- I implemented pagination as to not clutter the page too much so there is only three reviews showing at a time.
- This design is shared with the "edit review" page. The only difference being is that instead of the form being blank it is already filled out with your review that can be edited to your liking.

## Edit Review
![Edit Review](docs/readmeimgs/editreviewpage.png)

# Technologies Used

- ## Languages / Frameworks
1. [HTML5](https://en.wikipedia.org/wiki/HTML5)
2. [CSS3](https://en.wikipedia.org/wiki/CSS)
3. [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
4. [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
5. [Django](https://www.djangoproject.com/)
6. [Bootstrap](https://getbootstrap.com/)

- ## Misc Software
- [Balsamiq](https://balsamiq.com/) : Wireframes built using Balsamiq.
- [GitHub](https://github.com/) : GitHub is used as a repository storage for the project.
- [VSCode](https://code.visualstudio.com/) : VSCode was used as a development environment, and code was pushed to GitHub. It is used for version control as well as it allows you to commit code at different stages of development as required.

# Testing
- ## HTML Validator
    At various stages HTML Validation was done.
    - [Home Page HTML Validation]()
    - [Detailed Page HTML Validation]()
    - [Movies Page HTML Validation]()
    - [Games Page HTML Validation]()
    - [Shows Page HTML Validation]()
    - [Review Page HTML Validation]()
    - [Signout Page HTML Validation]()
    - [Signup Page HTML Validation]()
    - [Login Page HTML Validation]()

- ## CSS Validator
    At various stages CSS Validation was done.
    ![CSS Validation](docs/validation/css-validation.png)

- ## Lighthouse
    At various stages Lighthouse testing was done.
    ![Lighthouse](docs/validation/lighthouse.png)

- ## Browser Compatibility
The website was tested on the following browsers:
- Google Chrome: Version 111.0.5563.147 (Official Build) (64-bit)
- Mozilla Firefox: Version 104.0.2 (64-bit)
- OperaGX: Version 90.0.4480.100

- # Manual Testing
The following was manually tested and resulted in a pass:
- ## Navigation Bar
    - The "CNA Ireland" logo takes you back to the homepage when clicked.
    - The navigation links take the user to their respective pages when clicked.
    - The navbar is responsive so on smaller screens it turns into a hamburger menu.
    - For admin users the "My Account" section of the navbar opens up on hover and there is a tab called "Site Management" upon hovering on this another menu will open and that is where store owners can add a product, category, blog post, and logout.
- ## Home Page
    - The home page is responsive on smaller devices.
- ## Products Page
    - Each item on the products page is clickable and takes you to the correct page.
    - For admin users they will see an "Edit" and "Delete" button under the products and clicking these buttons works as intended.
- ## Products Detail
    - Clicking on the "Add To Bag" button adds the product to the users bag and a message pops up.
    - Clicking on the "Keep Shopping" button will redirect users back to the products page.
- ## Review Page
    - Upon submitting the review form the user is redirected back to the page they just came from and their review is there on display.
    - Users can only leave one review, so there is no double posts instead if they have already left a review they can edit the one they posted.
- ## Register Page
    - Filling out this form allows users to register an account so that they can buy products after clicking the confirmation email link that will be sent upon registration.
    - If a user already exists for example (Shane101) and a new user goes to sign up with the same username (Shane101) there is a message shown saying that a user with that username already exists and the form is not submitted.
- ## Sign in Page
    - Upon entering in your credentials you will be logged in to the website and an alert message displays letting you know that you logged in successfully.
- ## Sign out Page
    - Upon clicking the sign out button the user is logged out and an alert message letting the user know that they signed out is displayed.
- ## Blog Page
    - Blogs are stacked on top of eachother using Bootstrap cards to contain their image, title and author, also there is a "Read More" button at the end of the blog card that when clicked will take them to the blog detail view where they can read the blog post in its entirety.
---
# Future Implementation
- I would like to add a newsletter.
- Add "like" button functionality to products.
- Add a "wishlist" for users.
- Maybe add reviews to the products but I am not sure if that would suit a site that sells these kind of products.
- Add a fully functional stripe checkout instead of the card element, I tried to do this but it completely broke the whole site so I decided to scrap it in order to get the project submitted in time.

# Deployment
The website was deployed using Heroku. To deploy to Heroku:
1. To successfully deploy on Heroku you first need to create a requirements.txt file and a Procfile.
2. The requirements.txt file contains all the applications and dependencies that are required to run your application. To create this file run the following command in the terminal:
```bash
pip3 freeze --local > requirements.txt    
```
3. The Procfile lets Heroku know which files run the app and how to run it. Create a `Procfile` in the root directory and add the following to the file (note: you must install gunicorn, you can do this by running this command. `pip3 install gunicorn`):
```Procfile
web: gunicorn yourappname.wsgi
```
4. Log in to the Heroku CLI in the terminal and run this command to disable collectstatic. (You don't have to do this in the CLI you can go to your config vars via the Heroku Dashboard and add this config var `DISABLE_COLLECTSTATIC 1`):
```bash
heroku config:set DISABLE_COLLECTSTATIC=1 --app heroku-app-name-here
```
5. We also need to add the Heroku app and localhost to ALLOWED_HOSTS = [] in settings.py:
```python
ALLOWED_HOSTS = ['{heroku app URL here}', 'localhost']
```
6. Push these changes to GitHub. You can then initialise the Heroku git remote in the terminal and push to Heroku with:
```bash
heroku git:remote -a {app name here}
git push heroku master
```
7. You should now be able to see your deployed site (without any static files).
8. To enable automatic deployments on Heroku, go to the deploy tab and click the connect to GitHub button. Search for your projects repo and then click connect. Click enable automatic deploys at the bottom of the page. Now everytime you push code to GitHub Heroku will take that code and deploy the site again with the updated code you just added.
9. To enable stylesheets just remove the `DISABLE_COLLECTSTATIC` config var and your site will have all its styling.

### Local Development
#### How to Fork
To fork the repo:
1. Log in to GitHub.
2. Go to the repo for this project.
3. Click on the fork button in the top right.

#### How to Clone
To clone the repo:
1. Log in to GitHub
2. Go to the repo for this project.
3. Click the Code button, select whether you would like to clone with HTTPS, SSH or the GitHub CLI and copy the link given.
4. Open the terminal in any IDE of your choosing and change the current working directory to the location you would like to use for the cloned repo.
5. Type the following command into the terminal `git clone` followed by the link you copied in step 3.
6. Set up a virtual environment.
7. Install the packages that are required from the requirements.txt file by running the following command in the terminal:
```bash
pip3 install -r requirements.txt
```

The website can be viewed here. [MGSR](https://reddjango.herokuapp.com/)

# Credits
- ## Images
- All images were taken from [Google Images](https://www.google.ie/imghp?hl=en-GB&tab=ri&ogbl).
- [Am I Responsive](https://ui.dev/amiresponsive) was used to generate the website responsive image used here in the README.md.
- [Ezgif](https://ezgif.com/) for converting some images from webp to jpg.

- ## Coding
- [Bootstrap Docs](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- [Django Docs](https://docs.djangoproject.com/en/4.2/)
