
# [Luxury Shoes](https://luxury-shoes-00974b0f1528.herokuapp.com/ "Click to view the deployed site")

- Luxury Shoes is an ecommerce website designed to sell womens shoes and accessories.
- Luxury Shoes is an ecommerce website designed to be easily navigated using standard ecommerce conventions.
- Luxury Shoes is an ecommerce website that allows users to browse products through categories, ratings, price and via a search bar using key words.
- Luxury Shoes has a crisp and clear aesthetic that makes it easy for the user to see the products and their details.
- Luxury Shoes allows users to add products to a shopping basket and purchase them, creating an order.
- In order to make a test purchase on Luxury Shoes please use the following details:
Card Number: 4242 4242 4242 4242 Exp: 02/25 Zip Code: 24242

## Table of Contents

<details>
<summary>Click here for Table of Contents</summary>

[Mockup Screenshots](#mockup-screenshots)

[UX](#ux)

- [Colour Scheme](#colour-scheme)
- [Typography](#typography)
[User Stories](#user-stories)

- [New site Users](#new-site-users)
- [Returning Site Users](#returning-site-users)
- [Use Case Diagram](#use-case-diagram)
- [Database Schema](#database-schema)
- [Database Details](#database-details)

[Wireframes](#wireframes)

[Features](#features)

- [Existing Features](#existing-features)
- [Future Features](#future-features)

[Testing](#testing)

[Deployment](#deployment)

[Credits](#credits)

- [Content and Code](#content-and-code)

- [Acknowledgments](#acknowledgements)

</details>

## Mockup Screenshots

Below is a mockup image of the Luxury Shoes ecommerce application created using the "Am I Responsive" website.

| Screenshot 1 |
| :---: |
| ![screenshot]() |

## UX

- The design for Luxury Shoes was created as a series of wireframes covering mobile, tablet and desktop to determine the initial design and layout of the site.
- Luxury Shoes is designed to be simple and easy to navigate using standard user conventions for ecommerce websites.
- The applications display the homepage, product pages, product details pages, shopping basket and checkout confirmation.
- Toasts appear in the top right of the page to let the user know that they have 'added to bag', 'removed from bag' and 'updated the bag', as well as a shopping bag toast that shows the user the products in their bag as well as the cost.

### Colour Scheme

- I decided to go with a clean and crisp colour scheme with a white background using black as the main colour for text/icons and a taupe accent to provide a pop of colour to the screen. This colour complements the background image used on the homepage.
- The colours used are as follows:-

- `#ffffff` used for primary text and buttons.
- `#000000` used for the background and secondary text.
- `#8C7D75` used for banner, buttons and other details.

I have used CSS `:root` variables to easily update the global colour scheme by changing only one value, instead of everywhere in the CSS file.

```css
:root {
    --black: #000;
    --white: #fff;
    --taupe: #8C7D75;
}
```

### Typography

- I used the Google Fonts called 'Baskervville SC' and 'Raleway' for the Luxury Shoes website.

- [Baskervville SC](https://fonts.google.com/specimen/Baskervville+SC) was used for the main text on the site such as the navbar.
- [Raleway](https://fonts.google.com/specimen/Raleway) was used for product, product/details and shopping bag pages.
- [Font Awesome](https://fontawesome.com) icons were used in the Luxury Shoes site.

## User Stories

### New Site Users (General)

- As a new site user, I need to understand clearly what the purpose of the website is for.
- As a new site user, I need to be able to navigate the product categories easily.
- As a new site user, I need to be able to search for keywords in a search bar.
- As a new site user, I need to be able to sort the products by rating, price and category.
- As a new site user, I need to be able to see the product details clearly, such as price, rating and description.
- As a new site user, I need to be able to add products to the basket and see that I have added them.
- As a new site user, I need to be able to view my shopping bag and make adjustments such as update and remove from the basket.
- As a new site user, I need the checkout process to be clear to understand and simple. Making me want to return to the website.

| **Viewing & Navigation** |
|-------------|

| **ID** | **As A** | **I Want To Be Able To** | **So That I Can** |
|-------------|------------|---------------------|-------------------|
| 1 | Shopper | View the products | To select what I want to purchase |
| 2 | Shopper | View products via specific categories | Quickly find the products I want to purchase |
| 3 | Shopper | View individual product details | See how much the item costs, read the description  and see what sizes are available |
| 4 | Shopper | View the total of my shopping bag | Be aware of how much money I am spending |

| **Registration & User Accounts** |
|-------------|

| **ID** | **As A** | **I Want To Be Able To** | **So That I Can** |
|-------------|------------|---------------------|-------------------|
| 5 | Site User | Register an account | Keep my details/orders saved |
| 6 | Site User | Login or Logout | Access my personal account information securely and prevent unwanted access |
| 7 | Site User | Recover my password if i forget it | Recover access to my account |
| 8 | Site User | Receive a confirmation email after registering | Verify that my account registration was successful |
| 9 | Site User | Have a user profile specific to me | See my order history and presaved shipping address |

| **Sorting & Searching** |
|-------------|

| **ID** | **As A** | **I Want To Be Able To** | **So That I Can** |
|-------------|------------|---------------------|-------------------|
| 10 | Shopper | Save my shopping bag when I leave the site  | Easily make the purchase when I am ready |
| 11 | Shopper | Sort the products available on the site | Easily find the products I am interested in |
| 12 | Shopper | Sort a specific category of product | Easily find the products according to rating, price, category and name |
| 13 | Shopper | Search for a product using keywords | Find products relevant to my needs |
| 14 | Shopper | See the results of what i've searched for | Decide whether the product is suitable for what I want |

| **Purchasing & Checkout** |
|-------------|

| **ID** | **As A** | **I Want To Be Able To** | **So That I Can** |
|-------------|------------|---------------------|-------------------|
| 15 | Shopper | Select the size and quantity of a product I want to purchase | Make a purchase that fulfills my needs |
| 16 | Shopper | View items that are in my shopping bag | To check that my shopping bag contains what I want and view a detailed price breakdown showing the total costs |
| 17 | Shopper | Adjust the quantity of individual items in my bag | Make changes to the quantity without navigating away from the checkout |
| 18 | Shopper | Enter my payment information | Check out quickly and with no hassle |
| 19 | Shopper | Checkout securely with no risk | Provide the sensitive information needed to purchase the products |
| 20 | Shopper | See an order confirmation | Check that the order is correct |
| 21 | Shopper | Receive an email confirmation | To safely store the order in my mail as reference |

| **Admin & Store Management** |
|-------------|

| **ID** | **As A** | **I Want To Be Able To** | **So That I Can** |
|-------------|------------|---------------------|-------------------|
| 22 | Store Owner | Add a product | Add new products to the store for customers to shop |
| 23 | Store Owner | Edit/Update a product | Edit/Update details of products such as price, description, image, rating etc |
| 24 | Store Owner | Delete a product | Remove products that are no longer available for sale |
| 25 | Store Owner | Manage products in one place | Easily make necessary amendments without navigating to different areas of the site |
| 26 | Store Owner | Send marketing emails to users | To send promotional emails to registered users and drive sales |

### Use Case Diagram
| UML Use Case Diagram |
| :---: |
| ![screenshot](README/media/UML-Use-Case-Diagram.png) | 

### Database Schema
| Database Schema |
| :---: |
| ![screenshot](README/media/Database-Schema-Model.png) | 

## Database Details
- The website has been built using HTML, Javascript (JQuery) and CSS using Bootstrap for the frontend.
- The backend has been developed using Django Frameworks and Python.
- SQLite was used for the local database.
- Postgres was used for the deployed Heroku database.

## Database Models
- The following are the models used in the creation of the Luxury Shoes ecommerce website.

#### User Model
- The User model contains information about the user. It is a part of the Django Allauth library.
- The User model contains username, password, first_name, last_name, email, is_staff, is_active, is_superuser, last_login, data_joined as defaults.

#### User Profile Model
- The User Profile model has a one to one relationship with the User.
- The User Profile model contains default_full_name, default_email, default_street_address1, default_street_address2, default_town_or_city, default_county, default_postcode, default_country and default_phone_number.

#### Order Model
- The Order model contains information about the orders made by customers.
- The Order model has UserProfile as a ForeignKey.
- The Order model contains order_number, user_profile, full_name, email, street_address1, street_address2, town_or_city, county, postcode, country, phone_number, date, delivery_cost, vat_total, order_total, grand_total, original_bag and stripe_pid.

#### OrderLineItem Model
- The OrderLineItem model contains information about an entry in an order placed on the website.
- The OrderLineItem model contains Order and Product as ForeignKeys.
- The OrderLineItem model contains order, product, product_size, quantity, lineitem_total.

#### Product Model
- The Product model contains information of the products and their details.
- The Product model contains Category as a ForeignKey.
- The Product model contains category, sku, name, description, has_shoesizes, price, rating, image_url and image.

#### Category Model
- The Category model contains information of the products categories.
- The Category model contains name and friendly_name.

#### Marketing Model
- The Marketing model contains information to build a form for admin to send emails.
- The Marketing model contains subject, message and sent_at.

#### EmailLog
- The EmailLog model contains information that logs when emails are sent and to whom.
- The EmailLog model contains user, email and sent_at.


## Wireframes

Each wireframe image below contains two images, one for desktop and one for mobile.
Balsamiq was used to create the wireframes
_ _ _

<details><summary>Home</summary>
<img src="README/media/wireframe-home.png">
</details>
<details><summary>Products</summary>
<img src="README/media/wireframe-products.png">
</details>
<details><summary>Shopping Bag</summary>
<img src="README/media/wireframe-shopping-bag.png">
</details>
<details><summary>Checkout</summary>
<img src="README/media/wireframe-checkout.png">
</details>


## Features

### Existing Features

| Feature | Description | Screenshot |
| :---: | :---: | :---: |
| **Navigation Bar** | The user can clearly see the navigation bar at the top of the screen. This includes account, basket, homepage, all products, shoes and accessories. On mobile devices, these are accessed through a hamburger menu. | ![screenshot]() |
| **Search Box** | The search box is located at the top of the main page for users to be able to search the website with specific queries. They can search for categories and specific products. | ![screenshot]() |
| **Product Sorting** | The user can view products by selecting their order preference in the dropdown, for example by rating, category, price and name.| ![screenshot]() |
| **Product Details** | A user can see further details of a product within the product details page which inclues a description, an option to choose a size (if applicable) and can add to bag or return to the products page.| ![screenshot]() |
| **Shopping Bag** | Users can access the shopping bag whether it is empty or not. They can see details of the products within the bag including a breakdown of the prices that contribute to the order grand total (including VAT). | ![screenshot]() | !
| **Toasts Add To Basket** | When a user adds a product to the basket a popup appears on the screen to let the user know they successfully added the product to the basket. It also shows the user the product and its size(if applicable) and forms a snapshot of the shopping bag. | ![screenshot]() |
| **Toasts Update/Remove From Basket** | When a user removes a product or updates the quantity in the basket, a popup appears to notify them of the change. | ![screenshot]() |
| **Checkout Form** | When the user is ready to make a purchase they can checkout securely by filling in the checkout form with their details and submitting it.  | ![screenshot]() |
| **Checkout Success** | When the user has submitted the checkout form a new screen loads with a summary of the details of their order and lets them know that an email has been sent to the email address they provided in the form.| ![screenshot]() |
| **Account Profile** | Users who are registered can access their profile where they can see/update their shipping address as well as see previous orders they've placed.| ![screenshot]() |
| **Product Management** | Admins have access to product management within their account. They can add, edit and remove items from the store all from the product management page.| ![screenshot]() |
| **Modals** | Modals have been built into the product management of admins meaning they are prompted to confirm the change they are doing. This is a defensive program to prevent accidental changes/deletions to the shop.| ![screenshot]() |

### Future Features

- Future Feature
  - For users to be able to pay with multiple methods such as Apple Pay and Klarna.
- Future Feature
  - A carousel on the homepage highlighting products to help increase sales.
- Future Feature
  - To restrict the sales of products via an inventory system.
- Future Feature
  - For product pages to have a 'quick add to basket' feature rather than going into the individual product page.

## Tools & Technologies Used

- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [CSS :root variables](https://www.w3schools.com/css/css3_variables.asp) used for reusable styles throughout the site.
- [JQuery](https://www.jquery.com) used for user interaction on the site.
- [GitHub](https://gitpod.io) used for secure online code storage.
- [Heroku](https://heroku.com) used for hosting the deployed front-end site.
- [Flaticon](https://www.flaticon.com/) used for the favicon.
- [Google Fonts](https://fonts.google.com/) used to search a suitable font and obtain a download link for that font.
- [Font Awesome](https://fontawesome.com/) used to add GitHub icon to the footer and modal and search icon to the search button.
- [Amazon Web Services](https://amazonaws.com/) used to load the static files to the deployed site and hold order information.
- [Stripe](https://stripe.com/) used to process payments in the checkout page.

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The site was deployed to Heroku. The steps to deploy are as follows:

- After pushing all content to the repository, navigate to Heroku.
- In the [Heroku Dashboard](https://heroku.com/dashboard), navigate to the Project that you're working on.
- Click on the 'Deploy' button located near the top left of the page.
- Deployment method: Github > then select the repository to connect to.
- Enable automatic deploys.
- Deploy branch.

The live link can be found [here](https://luxury-shoes-00974b0f1528.herokuapp.com/).

Amazon Web Service bucket has been used to provide the static files to the deployed website.

## Credits

The following are credits to various people and technologies that have directly or otherwise assisted in the creation of the Luxury Shoes site.

### Content and Code

| Source | Purpose | Notes |
| --- | --- | --- |
| [Code Institute](https://codeinstitute.net) | Main Application | Walkthrough used as a guide to create application. |
| [borderg](https://github.com/boderg/your-weather/blob/main/README.md) | README and TESTING| Used as a template for README and TESTING |
| [Github](https://www.github.com) | Repository | Used to store work in repository. |
| [Gitpod](https://www.gitpod.io) | Code Creation | Used to develop and write the application. |
| [Heroku](https://www.heroku.com) | Deployment | Used to deploy the application. |
| [Flaticon](https://www.flaticon.com/free-icons/sports-and-competition) | Favicon | Used as the favicon for the application. |
| [Udacity](https://www.udacity.com/blog/2021/03/creating-an-html-404-error-web-page.html) | 404 Page | Used to create an Error 404 page. |
| [LucidChart](https://www.lucid.app) | README | Used to create a Use Case & Database Schema Diagram. |
| [Jaclyn Moy](https://unsplash.com/photos/womens-seven-assorted-color-footwear-on-surface-ugZxwLQuZec) | Homepage| Used as the background image on the homepage |
| [1017043463441](https://www.vecteezy.com/photo/46562243-3d-rendering-pair-of-women-s-high-heels) | Products | Used as an image for black heels. |
| [Jack_Buu](https://www.vecteezy.com/photo/10098606-woman-shoes-isolated-on-white) | Products | Used as an image for black ballet flat shoes. |
| [rysak](https://www.vecteezy.com/photo/48162162-black-leather-ankle-boots) | Products | Used as an image for black boots. |
| [saddhavisual](https://www.vecteezy.com/photo/51443511-plain-white-sneakers-with-minimalist-design-isolated-on-white-background) | Products | Used as an image for white trainers.  |
| [107284640629537](https://www.vecteezy.com/photo/24496898-photo-of-softening-shea-butter-lip-balm-ai-generated) | Products | Used as an image for leather balm. |
| [thatphichai.ys27](https://www.vecteezy.com/photo/2901818-black-crew-socks-isolated-on-white-background-with-clipping-path) | Products | Used as an image for black socks. |


### Acknowledgements

- I would like to thank Ethan Peters and Tyrone Tuazon, my course buddies, for their continued support throughout the year during this course.
