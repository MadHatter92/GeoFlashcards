## A Geography Quiz Web App

- Idea
  - A website that has questions on maps
  - Students select the correct option out of 4
  
- App Organization
  - Layout
    - Sidebar - Login, Quiz Sections, About, Contact - ***[EASY]***
    - Main Area - Questions and options on the left, map on the right - ***[EASY]***
  - User Registration
    - Probably will have to have some sort of database integration - **check if this can be done in Dash in an integrated manner** - ***[HARD]***
  - Monetization
    - Need to figure out how to integrate a payment gateway with the user registration - ***[MEDIUM]***
    - Can look at ad support at a later stage if needed ***[OPTIONAL]***

- Distribution
  - Looking at only Word of Mouth for now

- Challenges
  - Integration between user registration and payment processor is proving to be a challenge
  - If every user gets assigned a username, what is ensuring non-sharing of username and password?
  - If authentication can be shared, why have it at all?
  - This can probably be eliminated by ensuring connect with Google account / facebook account
  - If authenticated by Google account, is it smoother to integrate with Google Pay?
  - Google pay is actually preferred, given that it is mobile first

  - However, a more current challenge is to make sure the layout works properly on mobile devices

- Decisions
  - Decided to focus on creating a responsive app as the primary objective
  - Testing to be done in a live environment, with URL redirect etc
  - Decided on interesting homepage and about page as the secondary objective
  - Decided to postpone monetization and implement a simple donation system for now
  - When all the above done, and the site has some traction, may think of creating a banner ad at the bottom

- Content
  - Add more write up / image content
  - India Biosphere Reserves
  - World Heritage Sites in India
  - List of Intangible Cultural Heritage
  - National Geological Monuments of India
  - Eyecandy
    - Creating a logo
    - Creating a banner

- Services and Components
  - Google Analytics - has been setup
    - TBD - try to do it pagewise
  - Google Adwords
  - Google Authentication/Any other authentication
  - Payment gateway set up

- Issues
  - Have to expose heroku link in pro version, as responsiveness does not work when using URL redirect
  - Passwords are still in code and plain text
  - Have separate Google Analytics tracking on trial and pro versions to check traffic on both and see if passwords are being shared
  - Sections "EIC Treaties" and "Indian Freedom Struggle" not getting highlighted on sidebar

- Ideas to Extend
  - Create a quiz based on material on the website, so that people can gauge their knowledge, realize the gaps in it and buy subscriptions to fill that gap