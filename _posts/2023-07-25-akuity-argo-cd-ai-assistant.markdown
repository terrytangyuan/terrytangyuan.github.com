---
layout:     post
title:      "Introducing the AI Assistant for Argo CD inside Akuity Platform"
subtitle:   "Argo CD extension to help developers quickly analyze any issues in your Argo CD Applications"
date:       2023-07-25
author:     "Yuan Tang and Alexander Matyushentsev"
tags:
    - Open Source
    - Kubernetes
    - Argo
    - Machine Learning
---

*Originally posted on [Akuity Blog](https://akuity.io/blog/akuity-argo-ai-assistant/). Also mentioned on [Business Wire](https://www.businesswire.com/news/home/20230725088248/en/Akuity-Launches-an-AI-Assistant-for-Argo-CD-to-Help-Troubleshoot-Common-Kubernetes-Deployment-Issues) and [Venture Beat](https://venturebeat.com/business/akuity-launches-an-ai-assistant-for-argo-cd-to-help-troubleshoot-common-kubernetes-deployment-issues/).*

We are thrilled to announce that the AI Assistant for Argo CD is now available inside the [Akuity Platform](https://akuity.io/akuity-platform/). It integrates cutting-edge AI functionality into our product, powered by GPT (Generative Pre-trained Transformer).

## What's the AI Assistant for Argo CD?

The AI Assistant is an Argo CD extension to help developers quickly analyze any issues with the Kubernetes resources and Argo CD Application tracks. Users can interact with the assistant by asking custom questions, clicking pre-defined prompts, and triggering Argo CD actions.

![assistant-hello](../../../../../img/inblog/akuity-argo-cd-ai-assistant/assistant-hello.png)


### Why Did We Do This?

Developers spend a tremondous amount of time trying to figure out why their Argo CD Applications are unhealthy. They often need to identify root causes for each of the Kubernetes resources that are failing, which requires a lot of manual inspection on the live K8s manifests, events, logs, etc.

With the rapid advancements in artificial intelligence, GPT revolutionizes the way we interact with technology. We'd like to leverage the GPT model's immense knowledge and contextual understanding to figure out the issues beforehand instead of wasting developers' valuable time and making them inspect each unhealthy resource manually.

This addition marks a significant milestone in our continuous efforts to enhance the developer experiences to facilitate the every-day use of Argo CD with intelligent assistance.


### Examples

The AI Assistant can help analyze logs from Pods, Deployments, etc. Below is an example of the analysis of Pod logs. The assistant found that the Pod is not ready and experiencing a `CrashLooDBackOff` due to a missing binary.

![binary-logs](../../../../../img/inblog/akuity-argo-cd-ai-assistant/binary-logs.png)

Similarly, the AI Assistant can also detect the issue in init containers:

![init-container-logs](../../../../../img/inblog/akuity-argo-cd-ai-assistant/init-container-logs.png)

The AI Assistant can also detect issues from Kubernetes events associated with the resource. For example, in the screenshot below, the AI Assistant summarizes the events into 3 categories and successfully identifies the root cause: the liveness probe is failing and causing the container to restart continuously. It also provides recommendations on what we should do to fix the problem. For example, making
necessary adjustments to ensure that the container responds successfully to the specified HTTP path.

![liveness-probe-events](../../../../../img/inblog/akuity-argo-cd-ai-assistant/liveness-probe-events.png)

The analysis of the logs provides additional details on what is happening in the Pod. The Apache server in the container is starting up, but the liveness probe is failing because it cannot find the expected path, which is "/bad-url" that we intentionally specified to see whether the AI Assistant can correctly identify the issue.

![liveness-probe-logs](../../../../../img/inblog/akuity-argo-cd-ai-assistant/liveness-probe-logs.png)

Similarly, the AI Assistant successfully detects issues with readiness probe based on events and logs:

![readiness-probe-logs-events](../../../../../img/inblog/akuity-argo-cd-ai-assistant/readiness-probe-logs-events.png)

There are also pre-built prompts displayed at the bottom of the dialogue for the resource the AI Assistant is analyzing, including specific actions that the AI Assistant can perform. Below is an example where the AI Assistant restarts the Deployment.

![action-restart](../../../../../img/inblog/akuity-argo-cd-ai-assistant/action-restart.png)

You can also ask additional questions in the dialogue box. For example, asking the AI Assistant to check the status of the Deployment after the restart as shown below.

![custom-question](../../../../../img/inblog/akuity-argo-cd-ai-assistant/custom-question.png)


### Is It Safe to Use?

We understand that introducing AI functionality can raise questions about data privacy and security. Rest assured, we have taken rigorous measures to safeguard your information and maintain the highest standards of data protection. Our commitment to privacy and ethical use of AI remains unwavering, ensuring your trust and peace of mind. Our AI Assistant feature leverages OpenAI API, check out its [API data usage policies](https://openai.com/policies/api-data-usage-policies). You can also read our [Trust Report](https://trust.akuity.io/) and [Privacy Policy](https://akuity.io/privacy-policy/).

## What's Next?

After using AI Assistant internally, our first thought was: "Wow, this is too good to be true!". The combination of the AI functionality with the in-depth knowledge of the application state provided by the Akuity Platform enables an extremely powerful feature. Clearly, we are just scratching the surface of what is possible, and it does not make sense to stop here.

We've started from use cases around a single Kubernetes resource, however, Akuity Platform and Argo CD have so much more information about the application state. We can go one level up and analyze the state of the application as a whole. Here are some ideas we are considering:

* Analyze the information powering Argo CD Network View and help troubleshoot network issues.
* Analyze application workloads' resource requests and detect over- or under-provisioning.
* Inspect application manifests security posture and detect potential vulnerabilities.

The use cases are not necessarily limited to summarizing and advising. The AI Assistant can perform actions as well. For example, it could trigger application synchronization, apply suggested changes to the resource manifest, and much more. I could go on and on since imagination is the only limit here.

So what are we waiting for? We recognize that AI is an emerging technology and needs to be used responsibly. Instead of rushing, we want to validate our ideas carefully and need your feedback to do it! 

Please give the AI Assistant for Argo CD a try and let us know what you think. It is an awesome opportunity to shape the tool that will revolutionize how engineers interact with Kubernetes. We are looking forward to hearing from you!
