# MSDS 498 Data Engineering Capstone Project

Project Overview
Kicking off the project in Week 1, our team was focused on finding a technology that we believed would be a disruptor in the field of AI & ML. One technology that we found intriguing, was recommender systems.  Because of their widespread use across the applications we use everyday, we settled on recomender systems because we believe that as AI & ML systems mature in the coming decade, recommender systems will become ingrained in every aspect of our daily lives.  From recommending the next song or video in a playlist, to what product a customer may purchase, recommender systems are becoming an increasingly utilized method for businesses to connect with their customers in a more personalized way then ever before.  

For a gentle introduction into recommender systems:
https://en.wikipedia.org/wiki/Recommender_system


Preview

Installation & Required Packages
To use this project, first clone the repo on your device using the command below:

git init

git clone https://github.com/jgentry10/MSDS498_GroupProject

Contribute






Assignment Instructions:

Your team will make a “bet” on a technique or technology in the free resources you have been exposed to.  Maybe you want to demo step-by-step how to train a Tensorflow model on a TPU on GCP, or how to train an RNN model using AWS Sagemaker.  Pick something you think will “move the needle” in the next two years. Alumni of the program are counting on you to give them a demo of what skills they need to invest in.  Soon, you will be alumni and will be hoping other students will show you a demo of something that you can learn from in the coming years when you graduate.

Deliverables:
1. Github project with source code and README.md explaining the project your group works on.  The README.md should be of professional quality and use a business writing style.
1. Five-minute final demo video showing how it works.  
 - This demo video should be submitted into group discussion for the week it is due.  This will allow other students to learn from each other and exchange ideas.
 - The demo needs to be very technical and show exactly how to accomplish a task, i.e. you need to teach someone step by step.  (Think about a cooking show where a chef demonstrates how to make chocolate chip cookies.  This needs to be at the same level of detail).

(Optional, but recommended:)
1. Publish source code the Northwestern Data Engineering Capstone Github Organization
1. Publish your demo to Northwestern Data Engineering Capstone YouTube channel and your own channel. The video should be at least 1080p with 16:9 aspect ratio.
1. Create a post with a link to source code and video and share via Linkedin.  Add the following hashtags: #northwestern #dataengineering #capstone

---
# Overview
- This project will recommend items to customers based on their purchase history at a grocery store. 


# Engineering Architecture:

(Insert here)


# DS Architecture (Recommendation Model):

- The API will receive a Product_ID (5 digit number) from the user
- It will send this Product_ID to a pre-built recommendation model (item2vec.200d.model) from mlApp.py
- This model is called via "most_similar_readable" function
- From this input, the API will return a JSON payload containing the list of most similar products and their scores
