# Rafael CookBook - Milestone Project 

Collection of Various kinds of recipes.
This project is dedicated to users who are willing to learn cooking.
It contains various kinds of recipes and user can upload their own recipes too.
 
## UX
 
This website consists of a user friendly layout. 

It's built for two kind of users:

1. One who wants learn Cooking (To be a chef)
2. One who wants to teach Cooking (Wants to share their talent)

Some Users will visit the site to learn new recipes whereas others visit to upload their recipies so that other users can learn and appreciate their talent.

## Features

- User can add new recipies using their name and email.
- User can view all kind of recipes in website uploaded by him or other users
- User can edit recipe uploaded by him
- User can delete already added recipe uploaded by him
- User can filter recipies uploaded by him only. 

### Features Left to Implement
We can implement various features to improve the site like:

- Comment section
So that users can post a comment to clear their doubts or to appreciate the work.

- Ratings
So that users can rate the recipes to help others whether this recipe is good or bad.

- Categorize the Data 
So that users can easily get/filter whatever they want out of thousand of recipes.


## Technologies Used

- [Python](https://www.python.org/doc/)
    - The project uses **Python** as backend.
    
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    - The project uses **Flask** framework to built a website.
  
 - [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
   
 - [Bootstrap](https://getbootstrap.com/docs/4.1/getting-started/introduction/)
    - The project uses **Bootstrap** to build responsive and creative site.
    
- [MONGO DB](https://docs.mongodb.com/)
    - The project uses **Mongo DB** to store and retrieve the data.
   

### Testing

1. Home Page: 
  - It contains **The best Recipes** section to visit the most popular recipes.
  - **All Receipes** section to view all kinds of recipes present in website uploaded by all users along with their name and emails.

  If you **click on any recipe card** it will take you to the recipe detail page showing all details(steps to cook, ingredients, cooking time etc)  of that specific dish. 

  If you click on button present at top named **My Recipes** will take you to the page which will show you filtered recipes uploaded by specific user.

2. RecipeView: To View

    - Recipe Description
    - Images 
    - Steps to cook
    - Ingredients required
    - cook time needed
    - preparation time needed
    
3. My Recipe Page:
   **User needs to enter their name and email** to view all recipes uploaded by him.
   After entering email and name, click **show my recipes** button.
   - It displays all recipes uploaded by you. If no recipe was uploaded by you it will show message "No Data Found".
   - It displays **Add Recipe** button at top. You can add a new recipe on clicking that button.
   - There are three buttons with each recipe uploaded by you(View, Edit,Delete). 
   You can **View complete recipe details** by clicking on **View** button present below that recipe.
   You can **Edit your recipe details** by clicking on **Edit** button present below that recipe.
   You can **Delete your recipe** by clicking on **Delete** button present below that recipe.
   
   
#### Deployment

This app is deployed on heroku
Heroku is a cloud platform as a service supporting several programming languages. 

**Here are pros/benefits of using Heroku:**

- Allows the developer to focus on code instead of infrastructure
- Enhance the productivity of cloud app development team
- Offers single billing for all projects broken down by team
- Monitor and enhance performance though rich application monitoring
- Helps your development, QA, and business stakeholders create a unified dashboard.
- Simple Horizontal & Vertical Scalability
- Heroku operation and security team is instantly ready to help you 24/7
- Leading Platform tools and Services Ecosystem
- Helps you to focus on innovation, not operations
- The Heroku Enterprise architecture offers minimal or no downtime during the system updates.
- Fast application lifecycle management and permissions
- Allows you to remove friction from the development
- Offers a powerful dashboard and CLI
- Integrates with familiar developer workflows
- Predictability and insight into the cost of application development and maintenance
- A bunch of supportive tools
- Beginner and startup-friendly
- It allows you to create a new server in just 10 seconds by using the interface of Heroku Command Line.
- The deployed version is available here: https://rafael-cookbook.herokuapp.com/

## PLUS POINTS
- Using Heroku Config Vars: 
An app’s environment-specific configuration should be stored in environment variables (not in the app’s source code). This lets you modify each environment’s configuration in isolation, and prevents secure credentials from being stored in version control. So here i use heroku config vars.

- App is running in two different environments
On local machine (i.e. development).
Deployed to the Heroku platform (i.e., production)

for running the app’s test suite safely in isolation
Staging, for running a new build of the app in a production-like setting before promoting it

- Different Git branch(my_cook_book)

### RUN LOCALLY

1. clone the project using command :
      git clone https://github.com/Assugeni/Rafael-CookBook
      
2. create and activate virtualenv in project directory using commands:

    For Windows :
      virtualenv venv
      source venv/Scripts/activate
      
    For Linux :
      virtualenv venv
      source venv/bin/activate
      
3 install Requirements from requirements.txt file. Run command:
    pip install -r requirements.txt
    
4 After successfull installation run app using command:
    python app.py
    
Open link : http://127.0.0.1:5000/

## Credits

### Content
- The text for home section was copied from the [Blog Cooking quotes]https://littleraesbakery.com/2020/02/19/12-quotes-about-cooking-from-the-heart/

### Media
- The photos used in this site were obtained from [GOOGLE]https://www.google.com/

### Acknowledgements

