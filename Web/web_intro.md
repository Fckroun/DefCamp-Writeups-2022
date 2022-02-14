## web_intro


<img src="../images/web_intro.png" allign="center" alt="Logo">


The challenge's description :

<img src="../images/widesc.png">

The website responded with Access denied.

<img src="../images/1.png">

We try this with Burp:

<img src="../images/2.png" width="120%">

We can notice an indication that it's a python server and a cute cookie in the response's headers :

```eyJsb2dnZWRfaW4iOmZhbHNlfQ.YglxiQ.sMMeYTTrGhfxV4A0hLMxWrG1WS0 ```

So probably this is a flask cookie, let's try to decode it using:

```flask-unsign --decode --cookie 'eyJsb2dnZWRfaW4iOmZhbHNlfQ.YglxiQ.sMMeYTTrGhfxV4A0hLMxWrG1WS0'```

<img src="../images/3.png">

Changing the "logged_in" parameter to True is possible but we should sign the cookie with a secret we don't know yet.

I tried first to bruteforce it with the rockyou dictionary using the same tool and luckily, we got the secret:

<img src="../images/4.png">

We are now two steps away from getting access to the web app.
First we decode the cookie, change the value of "logged_in" to True and sign it again with our cracked secret.

<img src="../images/5.png">

Passing our innocent cookie to the web app we get the flag :

<img src="../images/6.png">


Made By Fckroun with <3