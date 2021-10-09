#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask import Flask

# Instantiate the Flask app
app = Flask(__name__)

@app.route('/') # Home Directory
def hello():
    return "Hello DS C25 NLP DL Track learners. Welcome to the session on ML Model Deployment"

# If you want to run this app, you must call the run()
if __name__ == '__main__':
    app.run(debug=True)


# In[3]:


# 1-1

