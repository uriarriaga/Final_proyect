Sentwitment: We are the best Marketing Insights trough Machine Learning Agency!
What a week, huh? #Bootcamp #Tec

Companies around the world strugle to get users real feedback around their products and services. Users will always complain when something is not working, but what are they excited about? It is very rare for a consumer to contact Customer Service to congratulate a company around a service. Customer Obsessed companies need to know the customers sentiment without the usual Customer Service filters. Twitter is one of the most used & popular platforms worldwide to share feelings around any situation. With this in mind, Sentwitment uses machine learning to translate tweets into sentiment information from users towards any product or service and use data science to provide marketing insights to any industry.

Our goal is to apply Sentiment Analysis Models to translate Twitter posts and identify market trends and insights in the spanish speaking social media market.

It all starts with the appropiate keyword selection to filter and collect tweets. Then, the model classifies them into positive, neutral, or negative. With the sorted information, we calculate a Net Satisfaction score (NSAT) which we use to plot the analysis and share valuable conclusions through visualization.

ETL Process                               
The main source for our project is Twitter API. Using it requires special controlled accesses due to it's sensitive information
The library used to download the information was Tweepy, which allows for easir manipulation of tweets.
Transform                           
We used <strong>Pandas</strong> to manipulate and clean data.
Then we performed machine learning analyis trough an existing model <strong>Sentimet Analyis Spanish</strong> was used. This model, which allows to analyze text in spanish
The databases were stored in Amazon Web Services.
The data was imported into <strong>Postgres</strong>, and consulted trough queries. The queries were parsed using <strong>Flask and SQL Alchemy</strong>, then were used to deploy visualizations in <strong>Plotly</strong>

Machine Learning Analysis
We decided to use an existing python library (sentiment-spanish) that uses convolutional neural networks to predict the sentiment of spanish sentences to analyze our tweets. This model was trained using over 800000 reviews of users from the pages: eltenedor, decathlon, tripadvisor, filmaffinity and ebay. The model was then trained using Keras and Tensorflow libraries. The model has a 88% validation accuracy over fresh data (not used for training).

Sentwitment Metrics
We used the results from the analysis to create a Net Satisfaction Score (NSAT) which summarizes the sentiment towards the service/product analyzed. In this example we can see the evolution trough time of the NSAT and the popularity gained by the Tokyo Olympic games as we approach the Opening Ceremony

Streaming Services
We performed a business case study using our Sentiment Model Analysis to provide examples on the business insights it can generate.
Tweet Share as a Popularity measure: Using the amount of identified tweets over a period of time related to the keywords for each streaming service in Mexico we calculated a Popularity share.
Sentiments towards each streaming platform: Prior to calculating the NSAT score we graphed the user's sentiments towards each streaming platform. Paramount+ has the biggest amount of Positive sentiments (probably because it launche in March'21).
NSAT: Net Satisfaction Score: We agregate all sentiment information in one score, making it more easy to read and summarize sentiment in order to create more complex charts to detect trends.
NSAT evolution trough time: We see that the NSAT score tends to decrease over time. It is more normal for users to post negative comments. Amazon Prime Video has the highest satisfaction score in 2021.
Negative words are around specific movies/series and account related issues, while positive comments tend to be more on soon to be released products.

Streaming Services relevance over time: The 2020 COVID19 pandemics had a strong impact on Streaming Services popularity probably related to lockdowns.
Netflix mocks Televisa's Blim in 2016: BLIM vs NETFLIX. Even when Twitter users evaluated Blim better than Netflix (NSAT score higher), Netflix was the big winner of the whole battle with a higher tweet share.

Disney+ Simpson's launch fiasco: Disney launched in Nov 2017 but only with 2 Seasons from "The Simpsons"
Disney had a huge tweeter share during the platform launch, however it was mostly filled with users complaining on a miss to include all the "The Simpsons" seasons (driven by a previous agreement with TV AZTECA that removed this content from MX).
