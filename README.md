# Bike Builder

The website is deployed [here](https://bike-builder.herokuapp.com/).

It is a Stream 3 project for the Code Institute Full Stack Diploma in Software Development.

## Purpose

The website is aimed at people who work on their own motorcycles, or are considering doing so in the future. This may be modifying their bike, restoring an old bike, building a bike from scratch or simply learning how to maintain their bike rather than paying someone else to do it for them. It provides inspiration and information for the biking community, from deciding on what to use as the basis for the next project to overcoming the pitfalls of creating a dream motorcycle.

## Features

The site uses a Django framework with each page created in a separate app.

A Bootstrap theme (Sandstone from bootswatch.com) has been used to change the appearance of certain elements.

A Bootstrap navigation bar is used with a custom collapse point and the current tab is highlighted. A sticky footer is displayed at the foot of the page.

Images: images used as part of the site are either copyright-free, downloaded from Pixabay.com, or the source is referenced below the images. It is recognised that images uploaded by users may be subject to copyright. If this is the case, images will be removed at the request of the copyright-holder.

#### Home

Uses a Bootstrap carousel with background images, scrolling through overlaid text introducing each section of the website in turn.

#### Registration

Guest users can access all parts of the website, but full functionality can only be accessed by registering or logging in.

The app is based on LMS code but changes have been made. Code associated with taking payments at registration has been removed. Added functionality includes an enhanced Profile page with additional information being displayed regarding the user, plus the ability to upload a profile image which is displayed in certain parts of the site. A public name is also taken at registration to identify a user on the site. It was felt that this was more appropriate, in terms of user privacy and security, than displaying a user's full email address.

#### Gallery

This page displays motorcycle images and is intended as inspiration to users. Guests can view the images but only registered users can upload them. If an image is clicked, a modal window opens showing the full-size image. The modal incorporates a carousel so that users can scroll through the full-size images with a description included beneath each image. A significant number of images will increase page loading time so pagination has been incorporated here.

#### Project bike selector

This is intended to identify motorcycles which may provide the basis of a project for a user. It allows users to select criteria from drop-down menus and then retrieves a list of bikes from the database which match the given criteria.

The criteria are currently limited to manufacturer, engine layout and number of cylinders although this could be updated in the future. For instance, adding in a dates of manufacture field might assist someone who wants to restore a bike from a certain decade, perhaps one they remember from when they were growing up and aspired to own. However, I feel that the current criteria are very relevant and, with a database currently holding details of over 200 motorcycles, this should be a useful tool without any further development. Regarding the database entries, I have only included pre-1950 motorcycles if I felt it was appropriate, and I have also omitted models made in very limited numbers.

#### How-to guides

This section lists links to how-to articles from other websites. They can be posted by registered users of the site with recognition being given to the poster. How-to guides are invaluable to people working on motorcycles and it was felt that this means of access would allow them to be listed succinctly and provide credit to the original source without any plagiarism or copyright infringement.

#### Forum

The forum contains a number of subjects with threads and posts and has the functionality to conduct polls. All users can view the forum but only registered users are able to contribute.

The LMS code was used as a basis for the app but has been enhanced in a number of ways, including, but not limited to, the following: the layout and appearance has been updated to be in keeping with the rest of the site; more information is provided, such as the latest post for each subject, and the number of posts and views for each thread; users have avatars and their total number of posts is displayed; forms for creating, editing and deleting posts have Cancel buttons; users who edit posts are returned to the page they were previously on, and even the correct pagination page, if applicable; threads are displayed in order of latest posts; navigation has been improved with a forum navigation bar.

Thanks to [hipsum](https://hipsum.co/) for the hipster-style lorem ipsum text.

#### Merchandise

This provides users with the opportunity to purchase a number of items branded with the Bike Builder logo. Payments are taken using Stripe.

It uses LMS code as a basis but has been amended to suit, with users completing a payment form after selecting an item rather than providing details up-front when they register with the site. Merchandise items also have images.

This section satisfies the requirement for some kind of e-commerce functionality on the site, but would require further work before being usable on a live site. The lack of sizing selection and a shopping cart to enable multiple purchases are just two issues which would need to be addressed.

## Technologies used

* Django: full-stack framework

* HTML5 and CSS3: website content and appearance

* Python: backend coding

* Javascript (jQuery): payment validation and displaying active navbar tab

* SQLite: database

* Python libraries: including pillow (allowing use of images), arrow (to display readable, human-friendly dates and times), and tinymce (a Javascript HTML WYSIWYG editor used for writing posts in the forum). A complete list of Python libraries can be found in the requirements.txt file.

* Bootstrap: navbar, modal, carousel, forms, responsiveness.

* Font Awesome: for a variety of icons.

## Testing

Extensive manual testing has taken place throughout the development of the site. Every time some new functionality was added or existing functionality amended, testing took place. A number of browsers have been used for the testing, including Google Chrome, Microsoft Edge and Mozilla Firefox.

There is also a suite of tests which was written to test certain functionality of the site, but coverage is not 100%. I would have liked to spend more time writing test scripts but ran out of time at the end of the project. Testing is certainly an area I would like to develop in the future and I intend to return to this project and extend the test coverage to as close to 100% as I can.

The site is fully responsive through use of Bootstrap and media queries and is designed to operate well on screen widths down to 320px.

## Issues/shortcomings

Gallery: I’m not completely happy with the appearance of this page, with the rows of images only being left-justified. I would prefer left-and right-justification and managed to achieve this using flexbox. However, it created large gaps between images and left the page looking worse, especially on smaller screen sizes. In the end I felt that the left-justification, though not perfect, was the best way to go.

Image files: Image files are served by Heroku. Testing showed that this limits the functionality of the deployed site as users cannot upload images. The database can be updated, so new users can be created and new posts written, but their profile images won’t be saved and neither will any images uploaded to the Gallery or Forum. Functionality could be improved by using an online storage service such as Amazon S3 but this was outside the scope of this project and is something which may be added in the future.

## Deployment

The site has been deployed to the hosting platform Heroku (link at the top of the page) and ClearDB.

Separate environments were created with different settings and requirements files. Base files contain settings and requirements shared across all environments. Development files allow for debugging and continue to use the SQLite database used during development, whereas staging files use a MySQL database for the deployed site.

To run the project locally, the settings file must be specified:

`python manage.py runserver --settings=settings.dev` or `python manage.py runserver --settings=settings.staging`

A new Heroku app was created and configured. A migration was run to setup the database tables and a fixture file was used to populate the MySQL database with the data from the SQLite database.
