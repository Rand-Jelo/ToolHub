# Testing Documentation for ToolHub Web Application

![ToolHub Testing](static/readme-img/am-i-responsive.png)

<br><br>

# Contents

* [Validation](#validation)
    * [HTML Validation](#html-validation)
    * [CI Python Linter](#ci-python-linter)
    * [Lighthouse](#lighthouse)
* [User Story Testing](#user-story-testing)
    * [General](#general)
    * [Logged Out](#logged-out)
    * [Logged In User](#logged-in-user)
    * [Admin](#admin)
* [Manual Testing](#manual-testing)

<br><br>
# Validation

## HTML Validation

All pages pass HTML Validation at [W3C markup validation service](https://validator.w3.org/)

<details>
<summary>Home page</summary>
<br>
<img src="static/testing-img/home-html-validation.png">
</details>
<details>
<summary>Store</summary>
<br>
<img src="static/testing-img/store-html-validation.png">
</details>
<details>
<summary>Product detail page</summary>
<br>
<img src="static/testing-img/product-detail-html-validation.png">
</details>
<details>
<summary>Cart page</summary>
<br>
<img src="static/testing-img/cart-html-validation.png">
</details>
<details>
<summary>Dashboard page</summary>
<br>
<img src="static/testing-img/Dashboard-html-validation.png">
</details>
<details>
<summary>Checkout page</summary>
<br>
<img src="static/testing-img/checkout-html-validation.png">
</details>
<details>
<summary>Login page</summary>
<br>
<img src="static/testing-img/login-html-validation.png">
</details>
<details>
<summary>Signup page</summary>
<br>
<img src="static/testing-img/signup-html-validation.png">
</details>
<details>
<summary>Logout page</summary>
<br>
<img src="static/testing-img/logout-html-validation.png">
</details>
<br><br>

## CI Python Linter

All Python files are run through the CI PEP8 Linter.

### Cart app

<details>
<summary>models.py</summary>
<br>
<img src="static/testing-img/cart-models-validation.png">
</details>
<details>
<summary>views.py</summary>
<br>
<img src="static/testing-img/cart-views-validation.png">
</details>

### Core app

<details>
<summary>views.py</summary>
<br>
<img src="static/testing-img/core-views-validation.png">
</details>

### Orders app

<details>
<summary>models.py</summary>
<br>
<img src="static/testing-img/orders-models-validation.png">
</details>
<details>
<summary>views.py</summary>
<br>
<img src="static/testing-img/orders-views-validation.png">
</details>

### Payments app

<details>
<summary>models.py</summary>
<br>
<img src="static/testing-img/payments-models-validation.png">
</details>
<details>
<summary>views.py</summary>
<br>
<img src="static/testing-img/payments-views-validation.png">
</details>

### Product Wishlist app

<details>
<summary>models.py</summary>
<br>
<img src="static/testing-img/product_wishlist-models-validation.png">
</details>
<details>
<summary>views.py</summary>
<br>
<img src="static/testing-img/product_wishlist-views-validation.png">
</details>
<details>
<summary>context_processors.py</summary>
<br>
<img src="static/testing-img/product_wishlist-context-validation.png">
</details>

### Products app

<details>
<summary>models.py</summary>
<br>
<img src="static/testing-img/product-models-validation.png">
</details>
<details>
<summary>views.py</summary>
<br>
<img src="static/testing-img/product-views-validation.png">
</details>
<details>
<summary>filters.py</summary>
<br>
<img src="static/testing-img/product-filters-validation.png">
</details>

### Reviews app

<details>
<summary>models.py</summary>
<br>
<img src="static/testing-img/review-models-validation.png">
</details>
<details>
<summary>views.py</summary>
<br>
<img src="static/testing-img/review-views-validation.png">
</details>
<details>
<summary>forms.py</summary>
<br>
<img src="static/testing-img/review-forms-validation.png">
</details>

### User Profile app

<details>
<summary>views.py</summary>
<br>
<img src="static/testing-img/user-views-validation.png">
</details>

## Lighthouse

### Desktop

<details>
<summary>Home page</summary>
<br>
<img src="static/testing-img/home-lighthouse-desktop.png">
</details>
<details>
<summary>Shop page</summary>
<br>
<img src="static/testing-img/shop-lighthouse-desktop.png">
</details>
<details>
<summary>Product detail page</summary>
<br>
<img src="static/testing-img/product-detail-lighthouse-desktop.png">
</details>
<details>
<summary>Dashboard page</summary>
<br>
<img src="static/testing-img/dashboard-lighthouse-desktop.png">
</details>
<details>
<summary>Cart page</summary>
<br>
<img src="static/testing-img/cart-lighthouse-desktop.png">
</details>
<details>
<summary>Checkout page</summary>
<br>
<img src="static/testing-img/checkout-lighthouse-desktop.png">
</details>
<details>
<summary>Login page</summary>
<br>
<img src="static/testing-img/login-lighthouse-desktop.png">
</details>
<details>
<summary>Signup page</summary>
<br>
<img src="static/testing-img/signup-lighthouse-desktop.png">
</details>
<details>
<summary>Logout page</summary>
<br>
<img src="static/testing-img/logout-lighthouse-desktop.png">
</details>
<br><br>

### Mobile

<details>
<summary>Home page</summary>
<br>
<img src="static/testing-img/home-lighthouse-mobile.png">
</details>
<details>
<summary>Shop page</summary>
<br>
<img src="static/testing-img/shop-lighthouse-mobile.png">
</details>
<details>
<summary>Product detail page</summary>
<br>
<img src="static/testing-img/product-detail-lighthouse-mobile.png">
</details>
<details>
<summary>Dashboard page</summary>
<br>
<img src="static/testing-img/dashboard-lighthouse-mobile.png">
</details>
<details>
<summary>Cart page</summary>
<br>
<img src="static/testing-img/cart-lighthouse-mobile.png">
</details>
<details>
<summary>Checkout page</summary>
<br>
<img src="static/testing-img/checkout-lighthouse-mobile.png">
</details>
<details>
<summary>Login page</summary>
<br>
<img src="static/testing-img/login-lighthouse-mobile.png">
</details>
<details>
<summary>Signup page</summary>
<br>
<img src="static/testing-img/signup-lighthouse-mobile.png">
</details>
<details>
<summary>Logout page</summary>
<br>
<img src="static/testing-img/logout-lighthouse-mobile.png">
</details>
<br><br>

# User Story Testing

## General

| User Story                                                                                        | Feature                                                                                     |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| I want to immediately identify the purpose of the site.                                           | Logo in header displaying app name, and the homepage featuring a welcome message and CTA.  |
| I want navigation to be simple and intuitive.                                                     | Navigation links are placed logically with a responsive navbar (Hamburger menu for mobile). |
| I want to be able to view the site on any device.                                                 | The site is fully responsive and mobile-friendly, designed using the Bootstrap framework.   |

<br><br>

## Logged Out

| User Story                                         | Feature                                                            |
| -------------------------------------------------- | ------------------------------------------------------------------ |
| I want to be able to log in/signup to the service.  | Both login and register features available on the homepage.       |

<br><br>

## Logged In User

| User Story                                                                 | Feature                                                              |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| I want to be able to manage my cart and checkout process.                  | Cart page allows viewing, updating, and removing items. Checkout page for entering shipping information. |
| I want to be able to manage my orders and track them.                       | Order history and order tracking available on the account page.     |
| I want to be able to leave reviews for products.                            | Product pages allow users to leave reviews and ratings.             |

<br><br>

## Admin

| User Story                                                                  | Feature                                                              |
| --------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| I want to be able to manage all user accounts.                              | Admin can view, edit, and delete users from the admin panel.         |
| I want to be able to manage all products listed in the shop.                | Admin can add, edit, and delete products from the admin panel.       |
| I want to be able to see and manage orders placed by users.                 | Admin can view, update, and delete orders from the admin panel.      |
| I want to be able to remove any inappropriate reviews left by users.        | Admin can remove reviews via the admin panel.                        |

<br><br>

# Manual Testing

| Feature/Test                                         | Expected Outcome                                                        | Result |
| ---------------------------------------------------- | ----------------------------------------------------------------------- | ------ |
| Logo in Navbar.                                       | Redirects to Homepage.                                                  | Pass   |
| Nav Links.                                           | Redirect to relevant pages.                                              | Pass   |
| Cart Update Button.                                  | Allows updating the number of items in the cart.                        | Pass   |
| Footer Links                                         | Opens relevant external sites in new tabs.                              | Pass   |
| Login Form - Empty                                   | Form will not submit if fields are empty.                               | Pass   |
| Login Form - Incorrect Username                      | Form submits, but does not log in, displays an error message.           | Pass   |
| Login Form - Correct Username and Password           | Form submits and redirects to the dashboard.                            | Pass   |
| Logout Button                                        | Logs user out and redirects to Homepage.                                | Pass   |
| Product Page - Add to Cart                           | Product is added to cart successfully.                                  | Pass   |
| Product Page - Add Review                           | Review is added and visible under the product detail page.              | Pass   |
| Cart - Update Quantity                              | Quantity of items in cart can be updated.                              | Pass   |
| Checkout Form - Missing Information                  | Displays error messages for missing required fields.                   | Pass   |
| Checkout Form - Correct Information                  | Successfully processes order and displays confirmation.                | Pass   |
| Admin Panel - Manage Products                        | Admin can add, edit, and delete products.                               | Pass   |
| Admin Panel - Manage Orders                         | Admin can view and manage orders.                                       | Pass   |
| Admin Panel - Manage Users                          | Admin can view, edit, and delete users.                                 | Pass   |