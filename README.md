
# [Luxe Shoes](https://luxe-shoes-84842264eb1e.herokuapp.com/ "Click to view the deployed site")

- Luxe Shoes is an ecommerce website designed to sell womens shoes and accessories.
- Luxe Shoes is an ecommerce website designed to be easily navigated using standard ecommerce conventions.
- Luxe Shoes is an ecommerce website that allows users to browse products through categories, ratings, price and via a search bar using key words.
- Luxe Shoes has a crisp and clear aesthetic that makes it easy for the user to see the products and their details.
- Luxe Shoes allows users to add products to a shopping basket and purchase them, creating an order.

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

Below is a mockup image of the Luxe Shoes ecommerce application created using the "Am I Responsive" website.

| Screenshot 1 |
| :---: |
| ![screenshot]() |

## UX

- The design for Luxe Shoes was created as a series of wireframes covering mobile, tablet and desktop to determine the initial design and layout of the site.
- Luxe Shoes is designed to be simple and easy to navigate using standard user conventions for ecommerce websites.
- The applications display the homepage, product pages, product details pages, shopping basket and checkout confirmation.
- Toasts appear in the top right of the page to let the user know that they have 'added to bag', 'removed from bag' and 'updated the bag'.

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

- I used the Google Fonts called 'Baskervville SC' and 'Raleway' for the Luxe Shoes website.

- [Baskervville SC](https://fonts.google.com/specimen/Baskervville+SC) was used for the main text on the site such as the navbar.
- [Raleway](https://fonts.google.com/specimen/Raleway) was used for product, product/details and shopping bag pages.
- [Font Awesome](https://fontawesome.com) icons were used in the Luxe Shoes site.

## User Stories

### New Site Users

- As a new site user, I need to understand clearly what the purpose of the website is for.
- As a new site user, I need to be able to navigate the product categories easily.
- As a new site user, I need to be able to search for keywords in a search bar.
- As a new site user, I need to be able to sort the products by rating, price and category.
- As a new site user, I need to be able to see the product details clearly, such as price, rating and description.
- As a new site user, I need to be able to add products to the basket and see that I have added them.
- As a new site user, I need to be able to view my shopping bag and make adjustments such as update and remove from the basket.
- As a new site user, I need the checkout process to be clear to understand and simple. Making me want to return to the website.

### Returning Site Users

- As a returning site user, I want all the features that a new user needs.
- As a returning site user, I want to be able to have a speedy checkout process without inputting all my details again.
- As a returning site user, if I am registered I want to be able to see my orders.

### Use Case Diagram
| UML Use Case Diagram |
| :---: |
| ![screenshot]() | 

### Database Schema
| Database Schema |
| :---: |
| ![screenshot]() | 

## Wireframes

| Main page |
| :---: |
| ![screenshot]() | 


## Features

### Existing Features

| Feature | Description | Screenshot |
| :---: | :---: | :---: |
| **Navigation Bar** | The user can clearly see the navigation bar at the top of the screen. This includes account, basket, homepage, all products, shoes and accessories. On mobile devices, these are accessed through a hamburger menu. | ![screenshot]() |
| **Search Box** | The search box is located at the top of the main page for users to be able to search the website with specific queries. They can search for categories and specific products. | ![screenshot]() |
| **Shopping Bag** | Users can access the shopping bag whether it is empty or not. | ![screenshot]() | !
| **Toasts Add To Basket** | When a user adds a product to the basket a popup appears on the screen to let the user know they successfully added the product to the basket. It also shows the user the product and its size(if applicable) and forms a snapshot of the shopping bag. | ![screenshot]() |
| **Toasts Update/Remove From Basket** | When a user removes a product or updates the quantity in the basket, a popup appears to notify them of the change. | ![screenshot]() |
| **Checkout Form** | When the user is ready to make a purchase they can checkout securely by filling in the checkout form with their details and submitting it.  | ![screenshot]() |
| **Checkout Success** | When the user has submitted the checkout form a new screen loads with a summary of the details of their order and lets them know that an email has been sent to the email address they provided in the form.| ![screenshot]() |

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

The live link can be found [here](https://luxe-shoes-84842264eb1e.herokuapp.com/).

## Credits

The following are credits to various people and technologies that have directly or otherwise assisted in the creation of the Luxe Shoes site.

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
- I would like to thank 
- I would like to thank 
