# MSDS 498 Data Engineering Capstone
Model used to recommend products to customers

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
