# **ToolHub**

ToolHub is an eCommerce platform that allows users to browse, purchase, and manage high-quality tools. This application is built using Python, Django, Cloudinary for image storage, PostgreSQL for the database, and is deployed on Heroku.

[**__Link to deployed site here__**](https://tool-hub-f8ebaa947792.herokuapp.com/)
<br><br>

![Am I Responsive](static/readme-img/am-i-responsive.png)
<br><br>

# Contents

* [User Experience](#user-experience)
    * [Owner Goals](#owner-goals)
    * [Visitor Goals](#visitor-goals)
* [Design](#design)
    * [Wireframes](#wireframes)
    * [Database Schema](#database-schema)
    * [Images](#images)
* [Features](#features)
    * [Multi-page Features](#multi-page-features)
    * [All User Features](#all-user-features)
    * [Logged-In Features](#logged-in-features)
    * [CRUD Functionality](#crud-functionality)
* [Technologies](#technologies)
    * [Languages](#languages)
    * [Tools](#tools)
* [Testing](#testing)
* [Deployment](#deployment)
    * [Deployment to Heroku](#deployment-to-heroku)
    * [Forking Repository](#forking-the-github-repository)
    * [Making a Local Clone](#making-a-local-clone)
    * [Version Control](#version-control)
* [Credits](#credits)

<br><br>

# User Experience

ToolHub is designed to allow users to browse and purchase tools, manage their wishlist, and read and leave reviews.

## Owner Goals
- Provide a platform for users to easily browse and purchase tools.
- Enable users to create and manage a personal wishlist.
- Allow users to leave reviews and ratings for tools they have purchased.

## Visitor Goals
As a visitor:
- I want to view a variety of tools available for purchase.
- I want to be able to create an account and manage my tools and wishlist.
- I want to be able to read reviews from other customers.

<br><br>

# Design

## Wireframes

Wireframes created using Miro.

<details>
<summary>Home Desktop</summary>
<br>
<img src="static/readme-img/home-desktop.png">
</details>
<details>
<summary>Home Mobile</summary>
<br>
<img src="static/readme-img/home-mobile.png">
</details>
<details>
<summary>Shop Desktop</summary>
<br>
<img src="static/readme-img/product-detail-desktop.png">
</details>
<details>
<summary>Shop Mobile</summary>
<br>
<img src="static/readme-img/product-detail-mobile.png">
</details>
<details>
<summary>Product detail Desktop</summary>
<br>
<img src="static/readme-img/product-detail-mobile.png">
</details>
<details>
<summary>Product detail Mobile</summary>
<br>
<img src="static/readme-img/product-detail-mobile.png">
</details>
<details>
<summary>Cart Desktop</summary>
<br>
<img src="static/readme-img/product-detail-mobile.png">
</details><details>
<summary>Cart Mobile</summary>
<br>
<img src="static/readme-img/product-detail-mobile.png">
</details>
<details>
<summary>Checkout Desktop</summary>
<br>
<img src="static/readme-img/product-detail-mobile.png">
</details>
<details>
<summary>Checkout Mobile</summary>
<br>
<img src="static/readme-img/product-detail-mobile.png">
</details>
<details>
<summary>Dashboard Desktop</summary>
<br>
<img src="static/readme-img/product-detail-mobile.png">
</details>
<details>
<summary>Dashboard Mobile</summary>
<br>
<img src="static/readme-img/product-detail-mobile.png">
</details>
<details>
<summary>Login Desktop</summary>
<br>
<img src="static/readme-img/product-detail-mobile.png">
</details>
<details>
<summary>Login Mobile</summary>
<br>
<img src="static/readme-img/product-detail-mobile.png">
</details>
<details>
<summary>Signup Desktop</summary>
<br>
<img src="static/readme-img/product-detail-mobile.png">
</details>
<details>
<summary>Signin Mobile</summary>
<br>
<img src="static/readme-img/product-detail-mobile.png">
</details>
<details>
<summary>Logout Desktop</summary>
<br>
<img src="static/readme-img/product-detail-mobile.png">
</details>
<details>
<summary>Logout Mobile</summary>
<br>
<img src="static/readme-img/product-detail-mobile.png">
</details>




<br><br>

## Database Schema

Schema for PostgreSQL database was created on [Draw.io](https://app.diagrams.net/)

<details>
<summary>DB Schema</summary>
<br>
<img src="static/readme-img/db-schema.png">
</details>

<br><br>

# Features

## Multi-page Features

### Navbar

The navbar is displayed on all pages except for the checkout page. On mobile devices, it collapses into a hamburger icon that opens a side navigation menu. The visible links depend on whether the user is logged in or not.

<details>
<summary>Navbar Logged Out</summary>
<br>
<img src="static/readme-img/navbar-logout.png">
</details>
<details>
<summary>Navbar Logged In</summary>
<br>
<img src="static/readme-img/navbar-login.png">
</details>

### Footer

Footer is present on all pages, with a disclaimer and links to social media accounts.

<details>
<summary>Footer</summary>
<br>
<img src="static/readme-img/footer.png">
</details>

<br><br>

## All User Features

### Home Page

On the home page, visitors can see featured products and can search for tools based on categories or keywords and use the filter feature to filter through item tags.

<details>
<summary>Home Page</summary>
<br>
<img src="static/readme-img/homepage.png">
</details>

### Shop

On the shop page users can see all avaliable tools for purchase.

<details>
<summary>Shop</summary>
<br>
<img src="static/readme-img/shop.png">
</details>

### Product Detail Page

On the product detail page, users can view detailed information about the product, read and leave reviews, and add the product to their cart or wishlist.

<details>
<summary>Product Detail Page</summary>
<br>
<img src="static/readme-img/product-detail.png">
</details>

### Log In / Sign Up

Users can sign up or log in to their accounts. Once logged in, they can manage their wishlist and view their previous orders.

<details>
<summary>Log In</summary>
<br>
<img src="static/readme-img/login.png">
</details>

<details>
<summary>Sign Up</summary>
<br>
<img src="static/readme-img/signup.png">
</details>

<br><br>

## Logged In Features

### Dashboard Page

Logged-in users can access their dashboard page to manage their passwod information, view their order history, and view their wishlist.

<details>
<summary>Dashboard</summary>
<br>
<img src="static/readme-img/dashboard.png">
</details>

### Cart Page

Users can view the items in their cart and proceed to checkout.

<details>
<summary>Cart Page</summary>
<br>
<img src="static/readme-img/cart.png">
</details>

### Checkout Page

Users can pay and place an order with stripe payments

<details>
<summary>Checkout Page</summary>
<br>
<img src="static/readme-img/checkout.png">
</details>

### Logout Page

Confermation page for logout

<details>
<summary>Logout Page</summary>
<br>
<img src="static/readme-img/logout.png">
</details>

### Review Feature

Users can leave reviews and ratings for the tools they have purchased in the product detail page, and can also delete their own reviews.

<details>
<summary>Add Review</summary>
<br>
<img src="static/readme-img/review.png">
</details>

<br><br>

## CRUD Functionality

| Page               | Create                                     | Read                                       | Update                                    | Delete                                     |
|--------------------|--------------------------------------------|--------------------------------------------|-------------------------------------------|--------------------------------------------|
| **Login**          |                                            | Read user credentials for authentication |                                           |                                            |
| **Register**       | Create a new user account                  |                                            |                                           |                                            |
| **Home Page**      |                                            | View featured tools and categories        |                                           |                                            |
| **Product Page**   |                           | View individual product details           |                       | Delete product                             |
| **Cart Page**      |                                            | View cart items                           |   Update number of products                                        | Delete item from cart                                           |
| **Product Detail Page** | Add a new review                           | View product details and reviews          |                              | Delete a review                            |
| **Dashboard Page**   |                           | View account details, reviews and wishlist                      | Change password                      |                              |
| **Wishlist (Product Detail Page)** | Add products to wishlist                   |  |                                           | Remove product from wishlist               |

# Technologies

## Languages

* **HTML5** - Used for structuring and organizing content.
* **Bootstrap 5** - Used for responsive design, layout, and styling of the frontend.
* **CSS3** - Used for styling and layout.
* **JavaScript** - Handles frontend interactivity, form validation, and dynamic content rendering.
* **Python** - Manages the backend functionality.
    * Django==5.1.5
    * PostgreSQL==2.9.10
    * Pillow==11.1.0
    * cloudinary==1.36.0
    * crispy-forms==2.3
    * dj-database-url==2.3.0
    * dj-rest-auth==7.0.1
    * dj3-cloudinary-storage==0.0.6
    * gunicorn==20.1.0
    * requests==2.32.3
    * psycopg2-binary==2.9.10

## Tools

* **Cloudinary** - For image and media storage.
* **Heroku** - For deploying the app.
* **PostgreSQL** - For database management.
* **Git/GitHub** - For version control and storage.
* **Django** - For building the backend functionality.
* **Django REST Framework** - For building the API.
* **FontAwesome** - For icons.
* **Whitenoise** - For serving static files in production.
* **Stripe** - For handling payments and transactions.

## Testing

For testing, please refer to the [Testing Documentation](TESTING.md).

<br><br>

## Deployment

### Deployment to Heroku

To deploy to Heroku:
1. In GitPod CLI, the root directory of the project, run:
    pip3 freeze --local > requirements.txt
    to create a requirements.txt file containing project dependencies.
2. In the Gitpod project workspace root directory, create a new file called Procfile, with capital 'P'.
    Open the Procfile. Inside the file, check that web: python3 app.py has been added when creating the file
    Save the file.
3. Push the 2 new files to the GitHub repository
4. Login to Heroku, select Create new app, add the name for your app and choose your closest region.
5. Navigate to the Deploy tab on Heroku dashboard and select Github, search for your repository and click 'connect'.
6. Navigate to the settings tab, click reveal config vars and input the following:

| Key               | Value                                                                                               |
| ----------------- | --------------------------------------------------------------------------------------------------- |
| **DATABASE_URL**   | Your PostgreSQL database URL                         
| **SECRET_KEY**     | Your Secret key                                                                                   |
| **CLOUDINARY_URL** | Your Cloudinary URL                                                                              |

7. Deploy the app by selecting **Deploy Branch** under the **Deploy** tab.

### Forking the GitHub Repository
<br>

By forking the **FlavourVault** GitHub repository, you make a personal copy of the repository to explore and make changes without affecting the original repository. To fork the repository:

1. Log in to GitHub and go to the [FlavourVault Repository](https://github.com/Rand-Jelo/ToolHub).
2. At the top of the repository page, just above the "Settings" button, click the **Fork** button.
3. You should now have your own copy of the repository in your GitHub account.
<br><br>

### Making a Local Clone
<br>

To clone the repository locally, follow these steps:

1. Log in to GitHub and go to the [FlavourVault Repository](https://github.com/Rand-Jelo/ToolHub).
2. Under the repository name, click the **Clone or download** button.
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/Rand-Jelo/ToolHub
```
7. Press Enter. Your local clone will be created.
<br><br>

### Version Control

We use **Git** and **GitHub** for version control. Git helps us track the history of the project and collaborate with others. It enables us to manage different versions of the code and helps us to roll back changes when necessary.

- **git add**: Stage the changes for commit.
- **git commit**: Commit the staged changes with a message describing them.
- **git push**: Push the changes to the remote GitHub repository.

Once your changes are committed, you can push them to GitHub to make them available to collaborators and for deployment.
<br><br>

# **Credits**

## **Code**
- User authentication and management implemented using [Django Allauth](https://django-allauth.readthedocs.io/en/latest/).
- User password reset functionality powered by [Django Rest Auth](https://dj-rest-auth.readthedocs.io/en/latest/).
- Recipe submission, editing, and CRUD functionality built with [Django](https://www.djangoproject.com/).
- Cloud storage for images and media handled via [Cloudinary](https://cloudinary.com/) integration.
- Database interactions optimized with [Django ORM](https://docs.djangoproject.com/en/stable/topics/db/queries/).
- Search and filtering logic based on [Django documentation](https://docs.djangoproject.com/en/stable/topics/db/search/).
- Payments integrated using [Stripe](https://stripe.com/) for seamless transactions.

## **Media**
- Icons provided by [Font Awesome](https://fontawesome.com/).
- Responsive design mockups made with [Am I Responsive](https://ui.dev/amiresponsive).
- UI wireframes designed using [Miro](https://miro.com/).
- Images sourced from [Freepik](https://www.freepik.com/).

## **Tutorials and Resources**
- Django authentication setup guidance from [Django Allauth official documentation](https://django-allauth.readthedocs.io/en/latest/installation.html).
- Payment integration with [Stripe documentation](https://stripe.com/docs).
- API request handling in Django REST Framework based on [DRF official documentation](https://www.django-rest-framework.org/tutorial/quickstart/).
- PostgreSQL integration references from [Heroku documentation](https://devcenter.heroku.com/categories/heroku-postgres).
- Frontend styling and components from [Bootstrap documentation](https://getbootstrap.com/docs/).

## **Acknowledgements**
- A big thank you to my mentor, **Mitko Bachvarov**, for his continuous guidance and feedback throughout the project.
- Special thanks to the [Stack Overflow](https://stackoverflow.com/) community for providing solutions to technical challenges.
- Appreciation to the **Open Source contributors** behind Django, DRF, PostgreSQL, and Stripe for their valuable frameworks.