# **Its4kids - Project Portfolio 4**

Its4kids is an environment to get and share play ideas for children by people interested in contributing to a more playing world, such as parents, educators, as well as future education professionals... 

Welcome to the live site here: <a href="https://its4kids.herokuapp.com/" target="_blank">Its4kids</a>


# Contents

* [**Objective**](<#objective>)
* [**User Experience UX**](<#user-experience-ux>)
    * [Target Audience](<#target-audience>)
     [Wireframes](<#wireframes>)
    * [Site Structure](<#site-structure>)
    * [Design Choices](<#design-choices>)
        *  [Typography](<#typography>)
        *  [Colour Scheme](<#colour-scheme>)
* [**Data Model**](<#data-model>)
* [**Features**](<#features>)
    * [**Existing Features**](<#existing-features>)
    * [**Home**](<#home-page>)
        * [Navigation bar](<#navigation-bar>)
        * [Gallery Carousel](<#gallery-carousel>)
        * [About-us](<#about-us>)
        * [Footer](<#footer>)
        * [**Browse Ideas**](<#browse-page>)
        * [**User Profile**](<#user-page>)
        * [**Contact**](<#contact-page>)
            * [Contact details](<#contact-details>)
            * [Contact Form](<#contact-form>)
            * [Testimonials](<#testimonials>)
            * [Location Map](<#location-map>)
        * [**Admin Page**](<#admin-page>)
        * [**Future Features**](<#future-features>)
* [**Technologies Used**](<#technologies-used>)
* [**Testing**](<#testing>)
* [**Deployment**](<#deployment>)
* [**Credits**](<#credits>)
    * [**Code**](<#code>)
*  [**Acknowledgements**](<#acknowledgements>)


## User Stories







## Design Choices

 * ### Logo

 The logo was designed on [Canva](https://www.canva.com/en_gb/) version Pro. A painted children hands icon was chosen to convey the core concept of children playing and also a community ethos. 

![Its4kids logo](./static/images/readme/its4kids-logo.png) 

 * ### Typography
 
 The typography used throughout the site is Montserrat, as it is a nice font, elegant and, also conveys confidence and professionalism. It is very good for UX/UI for having good readability on any device, large x-heigh and, is also good for accessibility. 

 * ### Colour Scheme

Colour Palette image

<img src="./static/images/readme/color-palette.jpg" alt="Colour Palette image">


### Data Model



#### Post Model

| Key | Name | Type
|-----|----------------|------------------|
| foreign key | author | User Model
| | title (unique) | Char[200]
| | created_date | DateTime
| | updated_date | DateTime
| | content | TextField
| | featured_image | Cloudinary_image
| | excerpt | TextField
| many-to-many | likes | User Model
| label for url | slug (unique) | SlugField
| | status | Integer

#### Comment model


#### Profile model

## Deployment

### **Forking this repository on GitHub**

A fork of this repository can be made which will allow you to make changes to this project without affecting the original repository. 

The steps below should be followed to ***fork*** the respository:

1. Log in to ***GitHub*** and find the [repository](https://github.com/fmstacco/its4kids-blog).

2. Click on the button ***fork*** on the right-hand side of the page to create a copy of the original repository in your GitHub account.

See the image below:

![GitHub pages - to fork a depository](./static/images/readme/fork.jpg)

[Back to top](<#contents>)

# Credits

* [I Think therefore I Blog](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/fe4299adcd6743328183aab4e7ec5d13/) - this project was created based on the walkthrough I think therefore I Blog.
* [Tasty Blog](https://github.com/PedroCristo/portfolio_project_4) - this project inspired me and I borrow some of the code for the hero section carousel.
* [Location Blog](https://github.com/DionneMaguire/locationblog) - this project also inspired me.
* [Unplash](https://unsplash.com/) - I got pictures for hero carousel and the blog posts.


# Acknowledgements

Its4kids was designed and developed for Portfolio 4 project, a requirement of Full Stack Software Developer Diploma Course (Eccommerce) at the [Code Institute](https://codeinstitute.net/). I would like to thank my mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/), my Cohort facilitators, my Cohort colleagues, the Slack community, the Tutor Support and a big thanks to Bethany from the Student care for all support during this journey. I am also thankful to the ***Mayo, Sligo and Leitrim Education Training Board (msletb)*** for this opportunity. I  would also like to say thank you to my family, my husband Michel and, my children, Alanna, and Peter who is just 11 months old at the time of this project submission. 

Fabiana Tacco (2023)

[Back to top](<#contents>)
