# The-Twitter-Thing
Hi there!

Okay, let's cut the "Intro" talk and get into it. In this post I will explain you how to collect the twitter tweets in 3 steps. 

# Step 1: Connecting to Twitter API

We need to create an app, to gain access to the Twitter API, to access the tweets. Start here: https://developer.twitter.com - documentation helps. 

Once you create an app, note the consumer key, consumer secret, access token and access token secret. We need these credentials for authorization. 

# Step 2: Mining the Tweets 

Use the credentials for authorization. Then access the tweets according to your requirements using the Twitter's Search API. You can check the current trends in the world or in a specific location, you can search for tweets about a specific #hashtag and a lot more. The API reference can be found at https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets.html, customize it according to your needs,  but watch out for the rate limits - you don't want to make twitter angry. 

I have used the twitter package in python for this. My ipython notebook file "twitter_data_collection. ipynb" can be found on my github page. 

# Step 3: Save the Tweets 

Once you collect the tweets, save them to analyze later or even if you want to go ahead and analyze them right away, it’s always good to have a copy of original raw data. Corresponding code to save can be found on my github page. 

# References:
I have used the book:  Mining the Social Web by Matthew A. Russell - it's a good book. He explains everything from scratch. I would recommend reading it, if you want to know more about mining the social web. If you prefer watching to reading, there is also a video tutorial, explaining the same, at safari books https://www.safaribooksonline.com/library/view/mining-the-social/9781491989784 by Mikhail Klassen. 

# So, what is next?

Share your data analysis in comments and stay tuned for my next posts to analyze the collected tweets data at https://digitaldatastory.wordpress.com/

