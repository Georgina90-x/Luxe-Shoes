

# Testing

Return back to the [README.md](README.md) file.

## Table of Contents

<details>
<summary>Click here for Table of Contents</summary>

- [Code Validation](#code-validation)
  - [HTML](#html)
  - [CSS](#css)
  - [JavaScript](#javascript)

- [Browser Compatibility](#browser-compatibility)

- [Responsiveness](#responsiveness)

- [Accessibility](#accessibility)

- [Defensive Programming](#defensive-programming)

- [Test Driven Development](#test-driven-development)

- [User Story Testing](#user-story-testing)

- [Bugs](#bugs)

</details>

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.
The validator picked up the ame error for all pages tested, this is due to using Jinja templating.

| Page | Page URL | Screenshot | Notes |
| :---: | :---: | :---: | :---: |
| Home | [W3C]() | ![screenshot]() | Notes |
| Products | [W3C]() | ![screenshot]() | Notes | Notes |
| Product_Details | [W3C]() | ![screenshot]() | Notes |
| Bag | [W3C]() | ![screenshot]() | Notes |
| Checkout | [W3C]() | ![screenshot]() | Notes |
| Checkout Success | [W3C]() | ![screenshot]() | Notes |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Jigsaw URL | Screenshot | Notes |
| :---: | :---: | :---: | :---: |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator) | ![screenshot]() | Pass: No Errors |
| checkout.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator) | ![screenshot]() | Pass: No Errors |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| :---: | :---: | :---: |
| script.js | ![screenshot]() | Notes...|

## Browser Compatibility

I have tested Luxe Shoes on the following browsers to check for compatibility issues.

| Browser | Main | Page 1 | Page 2 | Page 3 | Page 4 | Page 5 | Page 6 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [Chrome](https://www.google.com/chrome) | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | Works as expected |
| [Firefox](https://www.google.com/firefox) | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | Works as expected |
| [Edge](https://www.microsoft.com/en-us/edge/?form=MA13FJ) | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | Works as expected |
| [Safari](https://www.apple.com/safari/) | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | Works as expected |

## Responsiveness

I have tested my deployed project on multiple devices to check for responsiveness issues.

<details>
<summary>Click for report</summary>

| Device | Main | Page 1 | Page 2 | Page 3 | Page 4 | Page 5 | Page 6 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Mobile (iPhone 15 Pro) | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | No issues |
| Tablet (iPad Air) | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | No Issues |
| 13" Macbook Pro| ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | No Issues |
| 15" Windows Laptop | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | No Issues |
| Android Phone | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() |  No Issues  |

</details>

## Accessibility

I have tested my deployed project using the [WAVE](https://wave.webaim.org/) web accessibility evaluation tool to check for any accessibility issues.

| Page | Summary | Details | Contrast | Notes |
| :---: | :---: | :---: | :---: | :---: |
| Main | ![screenshot]() | ![screenshot]() | ![screenshot]() | Notes |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

<details>
<summary>Click for report</summary>

| Page | Expectation | Test | Result | Fix | Screenshot |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Main | | | | | |
| | Luxe Shoes is expected to have a homepage that shows the workouts added by users that can then be previewed as a dropdown by clicking on them. | Tested this by opening the home page and clicking on the workouts. | The feature behaved as expected.| Test passed. | ![screenshot]() |

</details>

## Test Driven Development

<details>
<summary>Click for report</summary>

| Page | Expectation | Test | Result | Fix | Screenshot |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Main | | | | | |
| | Luxe Shoes is expected to have a homepage that shows the workouts added by users that can then be previewed as a dropdown by clicking on them. | Tested this by opening the home page and clicking on the workouts. | The feature behaved as expected.| Test passed. | ![screenshot]() |

</details>

## User Story Testing

| User Story | Screenshot |
| :---: | :---: |
| As a new site user, | ![screenshot]() |
| As a new site user, | ![screenshot]() |
| As a new site user, | ![screenshot]() |
| As a new site user, | ![screenshot]() |
| As a new site user, | ![screenshot]() |
| As a new site user, | ![screenshot]() |

## Bugs

The following are bugs that I have come across while creating the Workout site.

- When clicking on the 'secure checkout' button an error appears that prevents the checkout form page from loading.

| Original image | Bug fixed image |
| :---: | :---: |
| ![screenshot](T/Users/georginakidger/Documents/vscode-projects/Luxe-Shoes/TESTING/media/checkout-access-error.jpg) | ![screenshot](TESTING/media/shoesizes-model.png) |

- To fix this the shoe_sizes model had a character limit of 2, the sizes require more characters, so this was adjusted to 10 and fixed the issue and the checkout form now loads.

- When processing orders in the checkout, the form would not load.

| Original image | Bug fixed image |
| :---: | :---: |
| ![screenshot](/Users/georginakidger/Documents/vscode-projects/Luxe-Shoes/TESTING/media/checkout-access-error.jpg) | ![screenshot](TESTING/media/country-fields-error-fix.png) |

- The country field from Django CountryFields wasn't able to render correctly causing the bug. The dropdown has been removed until a solution is found.

- When filling in the form and trying to process an order an error appears stating an issue with the lineitem.

| Original image | Bug fixed image |
| :---: | :---: |
| ![screenshot](TESTING/media/checkout-lineitem-error.png) | ![screenshot](/Users/georginakidger/Documents/vscode-projects/Luxe-Shoes/TESTING/media/lineitem-error-fix.png) |

- Changed the null value to True, this then generated an error within the settings.py for 'STANDARD_DELIVERY_PRICE', this was fixed by amending a typo.

- When processing orders in the checkout, when accessing orders in the admin, the order details do not show the product details and prices.

| Original image | Bug fixed image |
| :---: | :---: |
| ![screenshot](/Users/georginakidger/Documents/vscode-projects/Luxe-Shoes/TESTING/media/order-admin-issue.png) | ![screenshot](TESTING/media/admin-prices-fix.png) |

- When amending the lineitem issue, the products now appeared in the order, but the price does not show. The prices did not show due to an indentation issue in the model.

- When deploying to heroku the application fails to load in the browser.

| Original image | Bug fixed image |
| :---: | :---: |
| ![screenshot](/Users/georginakidger/Documents/vscode-projects/Luxe-Shoes/TESTING/media/heroku-deployment-error.png) | ![screenshot](/Users/georginakidger/Documents/vscode-projects/Luxe-Shoes/TESTING/media/heroku-deployment-fix.png) |

- Ran through Heroku logs to find the issue and it was with the f strings in the webhook handler python file. These were rewritten and then pushed to the repository.

- When attempting to go throught the checkout process instead of checkout success showing a server error 500 appears.

| Original image | Bug fixed image |
| :---: | :---: |
| ![screenshot](TESTING/media/heroku-deployment-error.png) | ![screenshot](TESTING/media/heroku-deployment-fix.png) |

- Ran through Heroku logs to find the issue and it suggested there was an issue with shoe_size in orderlineitem. Checked this and ran migrations. No fix. Deleted the migration files and ran migrations again, no fix. Renamed all parts of code to align as shoe_sizes including the data items. No fix. 

***

## Unfixed Bugs

| Error | Screenshot | Description |
| :---: | :---: | :---: |
| Error | ![screenshot]() | Description |

There are no remaining bugs that I am aware of.