---
layout:     post
title:      "ArgoCon 2021 Akuity Team Recap"
subtitle:   "Impressive Numbers From This Conference and Recap on the 4 Sessions From the Akuity Team"
date:       2021-12-22
author:     "Yuan Tang"
tags:
    - Open Source
    - DevOps
    - Kubernetes
    - Conferences
    - Argo
---

We just concluded the inaugural ArgoCon! We'd like to share some impressive numbers from this conference and recap on the 4 sessions from the Akuity team.

## The Numbers

First, let's look at some numbers that came out from this conference.

* 3,893 registrants with 1,800 unique attendees over the day from 90 countries and more than 1500 companies.
* 20 sessions from 25 speakers, including 4 sessions from Akuity team.
* 6,200+ live session views and 2,600+ on demand views across all talks.
* 8 corporate sponsors.

These are really impressive numbers and we just got started for this first-ever Argo conference! 

We are proud to be one of the diamond sponsors of ArgoCon and [4 of the talks were given by our team members at Akuity](https://akuity.io/resources)!

![](https://i.imgur.com/etuK5UF.jpg)

Our team consists of the founding members and core maintainers of Argo. We've been involved in every perspective of the Argo projects and we will invest in what’s needed to foster the project’s growth. This includes continuing our contributions to the project, supporting users with their issues, facilitating discussions and meetings, and promoting Argo every chance we get. If this interests you, [please reach out and we are actively hiring](https://akuity.io/careers)!

The Argo community is growing fast and has been leading the chart with a large number of open source contributors and development activities. Argo is ranked as one of the top projects among all the CNCF projects in terms of development velocity, based on activities on GitHub commits/PRs/issues (see the screenshot below).

![](https://i.imgur.com/jOokULF.jpg)


Who's excited for the upcoming ArgoCon 2022? Be on the lookout for the ArgoCon 2022 CFP! In addition, follow us on [LinkedIn](https://www.linkedin.com/company/akuityio) and [Twitter](https://twitter.com/akuityio) to stay tuned for the latest news and development of Argo!

## Akuity Talks Recap

TODO(terry): Embeded YouTube links https://medium.com/embeds/how-to-embed-a-youtube-video-52e8aecd7fd

### Argo: The Present, Past, and Future

Speakers:
* [Kelsey Hightower](https://twitter.com/kelseyhightower) - Principal Engineer at Google Cloud Platform
* [Hong Wang](https://www.linkedin.com/in/hwang8/) - Founder and CEO at Akuity

Hong and Kelsey takes a deep-dive into the Argo project and explores how we got here, and where we’re going.

Recording: https://youtu.be/76iUpAWakIM

### How Scalable is Argo-Rollouts: A Cloud Operator’s Perspective

Speakers:
* Hui Kang - Platform Engineer at Salesforce
* [Jesse Suen](https://www.linkedin.com/in/jessesuen/) - Argo Project Lead, Co-founder and CTO at Akuity


TODO(jesse): More concise summary of the talk and some screenshots

Abstract: Argo-Rollouts enables advanced deployment capabilities to Kubernetes such as blue-green/canary update strategy, automated rollback and promotion, configurable update steps, and fine-grained, weighted traffic control. As Argo-Rollouts reaches its first major release of v1.0, companies are working rapidly to adopt Argo-Rollouts into their continuous deployment infrastructure. Further, work is underway to prove Argo-Rollouts’ scalability.

In this talk, we present our methodology of benchmarking Argo-Rollouts controller to manage the life cycle of a large number of Rollout custom resources in a realistic cloud environment. For this purpose, we developed a load-generation and performance measurement tool argo-rollouts-benchmark to emulate users, making continuous requests using k8s API with defined quantities and concurrency (e.g., create 100 rollouts in the cluster by 10 concurrent users). While the Argo-rollouts controller under test reconciles these Rollout CRs to the desired state, the benchmark tool collects the following metrics: convergence latency (The amount of time between the rollout CR is received by the controller and reaches a conclusive phase such as healthy, degraded, paused) in percentile distribution, timeout error rate (the percentage of degraded rollouts due to timeout), and throughput.

We will share the latest results from our experiments, as well as how these results help improve the overall scalability of Argo-Rollouts. We then looked at ways, such as predetermined t-shirt sizes and autoscaling, to optimize the resource provision of Argo-Rollouts to accommodate various customer demands. Based on these findings, we can define the SLO for our deployment capability offerings built atop Argo-Rollouts. Finally, the talk shows how to evaluate the Argo-Rollouts performance in your own clusters.

Recording: https://youtu.be/rCEhxJ2NSTI

### Bridging into Python Ecosystem with Cloud-Native Distributed Machine Learning Pipelines

Speaker: [Yuan Tang](https://terrytangyuan.github.io/about/) - Founding Engineer at Akuity

In this talk, Yuan provides an overview of the Python scientific system, machine learning frameworks, and workflow orchestration tools. He also presents various best practices and challenges on building large, efficient, scalable, and reliable distributed machine learning pipelines using cloud-native technologies such as Argo Workflows and Kubeflow as well as how they fit into Python ecosystem with cutting-edge distributed machine learning frameworks such as TensorFlow and PyTorch.

![](https://i.imgur.com/VoXuJ6P.png)

Recording: https://youtu.be/muM7IErh1S0

### Maintainer Update on Argo CD and Rollouts

Speaker: [Jesse Suen](https://www.linkedin.com/in/jessesuen/) - Argo Project Lead, Co-founder and CTO at Akuity

TODO(jesse): Summary of the talk (both maintainer update sessions), screenshots

Jesse provided an update on ..

If you are interested in updates on Argo Workflows, check out xxx
TODO: Perhaps change this to just maintainer update.

Recording: https://youtu.be/wn6OOLoHvQg

workflows update: https://youtu.be/FUekn40l9-A

## Additional Resources

You can find all the past and upcoming talks at various conferences from our team [here](https://akuity.io/resources). If you missed any of the ArgoCon sessions, [all the recordings are available on GitHub](https://www.youtube.com/playlist?list=PLGHfqDpnXFXKwNGO_8usFuTO-rIHNyefC)!

In addition, there's also a [curated list of projects and resources related to Argo](https://github.com/terrytangyuan/awesome-argo) if you'd like to learn more about the Argo core projects and ecosystem projects.

Join our growing Argo community by [finding us at regular community meetings, conferences, and Slack](https://github.com/terrytangyuan/awesome-argo#community)!


<p class="copyright text-muted">
	Copyright &copy; {{ site.title }} {{ site.time | date: '%Y' }}
</p>

