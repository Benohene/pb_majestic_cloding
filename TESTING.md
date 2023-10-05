# Testing

Back to [README.md](README.md)

## Validator Testing

### HTML Validator:

Since this project employs Django templates, the HTML validation process involved a manual verification procedure. This entailed navigating through the application pages, duplicating the source code of the displayed pages, and subsequently validating this HTML rendition using the W3C Validator [Link](https://validator.w3.org/). To ensure the HTML files were validated correctly, all Django template tags were meticulously eliminated. The HTML code was then extracted and integrated into the base template, and the navigation and footer templates were manually added to all pages during testing.

![models](docs/testing/html-valid.jpg)

### PEP 8 Python Linter:

The PEP 8 Python Linter by CI was used to test the validity of the python code. [PEP( PYTHON CI LINTER](https://pep8ci.herokuapp.com/) Below are the results of the test.

| FILE | IMAGE | REMARK |
| --- | --- | --- |
| Blog - admin.py | ![blog admin](docs/testing/blog.admin.png) | No Errors detected - PASS |
| Blog - forms.py | ![blog forms](docs/testing/blog.forms.png) | No Errors detected - PASS |
| Blog - models.py | ![blog models](docs/testing/blog.model.png) | No Errors detected - PASS |
| Blog - views.py | ![blog views](docs/testing/blog.views.png) | No Errors detected - PASS |
| Blog - widgets.py | ![blog widget](docs/testing/blog.widgets.png) | No Errors detected - PASS |
| Cart - context.py | ![cart-context](docs/testing/cart.context.png) | No Errors detected - PASS |
| Cart - views.py | ![cart-views](docs/testing/cart.view.png) | No Errors detected - PASS |
| Checkout - admin.py | ![checkout-admin](docs/testing/co.admin.png) | No Errors detected - PASS |
| Checkout - forms.py | ![checkout-forms](docs/testing/co.forms.png) | No Errors detected - PASS |
| Checkout - models.py | ![checkout-models](docs/testing/co.models.png) | No Errors detected - PASS |
| Checkout - signals.py | ![checkout-signals](docs/testing/co.signals.png) | No Errors detected - PASS |
| Checkout - views.py | ![checkout-view](docs/testing/co.views.png) | No Errors detected - PASS |
| Checkout - webhooks-handler.py | ![checkout-webhook-handler](docs/testing/co.webhook-handler.png) | No Errors detected - PASS |
| Checkout - webhook.py | ![checkout-webhook](docs/testing/co.webhook.py.png) | No Errors detected - PASS Just a long code error which does not affected the code |
| Contact - admin.py | ![contact admin](docs/testing/contact.admin.png) | No Errors detected - PASS |
| Contact - contact.py | ![contact forms](docs/testing/contact.forms.png) | No Errors detected - PASS |
| Contact - models.py | ![contact models](docs/testing/contact.models.png) | No Errors detected - PASS |
| Contact - views.py | ![contact views](docs/testing/contact.views.png) | No Errors detected - PASS |
| Name | ![Name]() | No Errors detected - PASS |
| Name | ![Name]() | No Errors detected - PASS |
| Name | ![Name]() | No Errors detected - PASS |
| Name | ![Name]() | No Errors detected - PASS |
| Name | ![Name]() | No Errors detected - PASS |
| Name | ![Name]() | No Errors detected - PASS |
| Name | ![Name]() | No Errors detected - PASS |
| Name | ![Name]() | No Errors detected - PASS |
| Name | ![Name]() | No Errors detected - PASS |
| Name | ![Name]() | No Errors detected - PASS |
| Name | ![Name]() | No Errors detected - PASS |

### Javascript Validator:

JSHint was used to validate the JavaScript with no errors highlighted.

![js-custom](docs/testing/js-custom.jpg)

### CSS Validator:

The CSS files within the project were all checked for errors using W3C CSS Validator Services. They all passed the text and displayyed the same message. The CSS files are blog.css , checkout.css and profile.css

![js-custom](docs/testing/css-validator.jpg)

## Lighthouse Report

The Lighthouse report indicated areas where SEO and best practices could be enhanced. We improved the SEO score to 100 by incorporating meta descriptions and keywords. However, we encountered best practice warnings due to the utilization of JavaScript within an embedded iframe. Regrettably, we couldn't find a solution to address this issue since I am not responsible for initializing the Google Map iframe with JavaScript.

![lighthouse](docs/testing/lighthouse.jpg)

## Responsiveness

The Website has been tested and it passed responsiveness for small mediumum and large screens of various devices. All pages have been tested for with a device size of from 320px.

The Responsive design was tested manually with [Chrome DevTools](https://developer.chrome.com/docs/devtools/) and also the Microsoft Dev tools. The Website worked perfectly well.

The Website pass its responsiveness and no responsive issues were seen on the following trial device:

- iPhone SE
- iPhone 12 Pro
- Samsung Galaxy S20/S20 Ultra
- Surface Duo