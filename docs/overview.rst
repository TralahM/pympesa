***********
Overview
***********

Why this Library ?
===================
This project was motivated by the need and frustration faced by my colleagues and myself
when developing software that interfaced and intergrated with  `Mpesa's Daraja API
<https://developer.safaricom.co.ke>`_ , A
popular mobile money platform that is widely used in Africa.

A lot of developers, and that may include you, as you are reading this, face some trouble
when interfacing with the daraja api especially the messy parts of authenticating and
obtaining an Oauth Token from the api that expires quickly even when you keep the token
for 30 days.

For python developers,even when using the awesome *requests* library to do the work, you
will often need to manually prepare the request headers, the payload which varies
depending on the api you are interfacing with and still parse the request response to
extract the information you need.

That is why i developed this library, to abstract away those messy, repetitive tasks you
will often do in your code as you intergrate Mpesa into your software solution.
This is to help you focus on the business logic implementation and not on the unimportant
third party payment gateway.

This will result in cleaner, shorter, and beautiful code that is easy to refactor and
maintain.

Now head over to the `getting started section <getting_started.html>`_ ..... and happy coding!!
