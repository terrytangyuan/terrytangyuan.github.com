---
layout:     post
title:      "5 Questions with Uptake Data Scientist and Scikit Flow Co-creator Yuan Tang"
subtitle:   "An Interview with Uptake"
date:       2016-05-05
author:     "Uptake"
header-img: "img/inblog/tensorflow-bg.jpg"
tags:
    - Deep Learning
    - TensorFlow
    - Open Source
    - Machine Learning
    - Python
    - Interview
---

**Note**: This interview was conducted by Uptake team and the original blog was posted [here](https://www.uptake.com/blog/5-questions-with-uptake-data-scientist-and-scikit-flow-co-creator-yuan-tang). Scikit Flow was renamed to be [TensorFlow Estimators](https://arxiv.org/pdf/1708.02637.pdf) and is now part of TensorFlow core. 

Yuan Tang, a data scientist at Uptake and top contributor to TensorFlow. Yuan collaborated with Google researcher and co-creator Illia Polosuhkin, and their contributions are making a significant impact on the data science field.

For the uninitiated, [TensorFlow](https://www.tensorflow.org/) is a machine learning library that’s mostly used to apply deep learning to everything from speech recognition to email filtering. When the library was recently open-sourced by Google Brain, Yuan Tang, a data scientist at Uptake and top contributor to TensorFlow, worked to simplify the library’s interface. The result is [Scikit Flow](https://arxiv.org/pdf/1708.02637.pdf), and it’s making deep learning more accessible than ever before.

Yuan collaborated with Google researcher and co-creator Illia Polosuhkin, and their contributions are making a significant impact on the data science field. They’re combining a cutting-edge technology with much older and trusted libraries and making it easier for other data science teams to use TensorFlow.

We sat down with Yuan to learn more about the project and what it’s doing for the open-source community.


**Could you explain what TensorFlow is for people not in the know?**

Sure, TensorFlow is a numeric computation framework that uses dataflow graphs. Although it has many applications, it’s mostly used for building deep learning systems, which mimic human learning by detecting and deciphering patterns. This allows the system to perform tasks that once only humans could accomplish. For example, the human brain used to be the only “computer” to understand and tell apart very closely related images like a grizzly bear and a panda. With TensorFlow, systems can be easily implemented to differentiate between these similar images.

Even though it was open-sourced less than six months ago, it’s quickly becoming the most popular framework in deep learning based on the number of stars in GitHub. To give you an idea of how significant it is, Google DeepMind completely moved to TensorFlow for their future research. The next-most popular framework is scikit-learn, a machine learning library for the Python programming language commonly used for rapid prototyping.

**Why did you choose TensorFlow to create Scikit Flow?**

We chose to work with TensorFlow because it has a stable, easy-to-use API that Google’s using for research and production. TensorFlow is arguably easier to learn given knowledge of similar libraries, but there is a learning curve to its unfamiliar syntax.

We bring the best of TensorFlow and scikit-learn in Scikit Flow. Scikit Flow combines the concise, well-known scikit-learn interface and the power of TensorFlow’s deep learning library. It’s a simple and familiar interface for data scientists.

**What sparked collaboration with Illia on this project?**

After teaching myself Python, I learned the basics by digging into open-source library code bases and getting familiar with their software architectures. I was hooked and started contributing to Scikit Flow with Illia in the beginning by adding deep learning models and integrations with other libraries. It was one of my first, big projects that I’ve contributed to at an early stage. We had such a great time collaborating together that it eventually became a full partnership.

**What makes you so passionate about contributing to the open-source community?**

I am so grateful for the open-source community because they did everything they could to help me be successful. My first experience with the community was working with the pandas library maintainers. Jeff Reback is a maintainer of pandas and taught me a lot through careful code review and feedback. This was a sort of baby step to Python, and it prepared me to work on TensorFlow.

The spirit of community is inspiring. I truly believe that the more you give, the more you receive, and this idea really applies to the open-source community.

**How do you recommend data scientists get involved in the open-source community?**

Just get started—use the libraries, post issues, and find and fix bugs. To go further, start thinking of enhancements and new features. Community involvement is crucial to the ongoing development of projects like TensorFlow.

We embrace that same sense of collaboration here at Uptake, and it’s played a significant role in our development. We have great culture of open-source software development that’s the lifeblood of how we build software.

Interested learning about TensorFlow from Yuan? He will be discussing TensorFlow for Machine Learning at an upcoming American Statistics Association event at Uptake in March.

<p class="copyright text-muted">
	Copyright &copy; {{ site.title }} {{ site.time | date: '%Y' }}
</p>
