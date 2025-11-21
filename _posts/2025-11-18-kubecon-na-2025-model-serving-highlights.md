---
layout:     post
title:      "KubeCon North America 2025: Red Hat AI Model Serving Highlights"
subtitle:   ""
date:       2025-11-18
author:     "Yuan Tang"
tags:
    - Open Source
    - Kubernetes
    - Artificial Intelligence
    - Machine Learning
    - KServe
    - Conferences
---

*Originally posted on [InferenceOps Substack newsletter](https://inferenceops.substack.com/p/kubecon-north-america-2025-red-hat)*.


**Time**: Nov 9th \- 13th, 2025  
**Location**: Atlanta, Georgia, USA  
![](../../../../../img/inblog/kubecon-na-2025/image1.png)

# Executive Summary

* **Red Hat AI** had a great presence at KubeCon. Highlights of what we’ve accomplished this week:  
  * Delivered the day 1 sponsored keynote that focuses on security and AI.  
  * Got invited to the opening keynotes to talk about K8s AI Conformance Program. Red Hat has been leading this effort and is among first vendors that are certified.  
  * Co-chaired the two main AI related co-located events: Cloud Native AI Day and Kubeflow Summit.  
  * Showcased our model serving related projects in many demos, breakout sessions, and media interviews.  
  * KServe joined CNCF as an incubating project and many people joined our session and at the booth for questions.  
* **AI on K8s**  
  * The community started collaborating and actively addressing pain points to improve AI workloads on K8s.  
  * Many K8s vendors have adopted the new K8s AI Conformance Program that we’ve been organizing, which was announced at the opening keynote.  
  * Many model serving related initiatives and projects exist but more collaborations would be useful to share solutions to common LLM inference challenges.  
* **Hot topics**  
  * Security and observability for AI agents and workloads are increasingly important.  
  * Kubernetes AI Conformance Program has been announced and many vendors have already adopted it.  
  * Dynamic Resource Allocation (DRA) is now GA and delivers 50-70% GPU efficiency gains.  
  * The EU Cyber Resilience Act and AI sovereign drive compliance-first infrastructure decisions.  
* **Event statistics**  
  * 9,000+ attendees  
  * 19+ co-located events  
  * 270 vendor booths  
  * 67 project booths  
  * 34 Red Hat sessions

Red Hat Booth  
![](../../../../../img/inblog/kubecon-na-2025/image2.png)

Red Hat AI team members and Kubeflow \+ KServe community members  
![](../../../../../img/inblog/kubecon-na-2025/image3.jpeg)
![](../../../../../img/inblog/kubecon-na-2025/image4.png)

# Keynotes

## Sponsored Keynote (Security \+ AI)

Session title: *Anchoring Trust in the Age of AI: Identities Across Humans, Machines, and Models*

Yuan Tang from Red Hat AI and Anjali Telang from OpenShift team have delivered a sponsored keynote on main KubeCon on day 1 in front of more than 9,000 attendees.This keynote focuses on trust and identity in the AI era and how KServe (integrates with llm-d, vLLM, etc.) connects seamlessly with security-focused technologies (SPIFFE/SPIRE, Keycloak, OAuth, OIDC, etc.) in the cloud-native ecosystem.

We also announced that KServe has joined CNCF as part of the keynote. Announcement blogs:

* CNCF: [https://www.cncf.io/blog/2025/11/11/kserve-becomes-a-cncf-incubating-project/](https://www.cncf.io/blog/2025/11/11/kserve-becomes-a-cncf-incubating-project/)   
* Red Hat: [https://www.redhat.com/en/blog/kserve-joins-cncf-incubating-project](https://www.redhat.com/en/blog/kserve-joins-cncf-incubating-project)

Recording: [https://www.youtube.com/watch?v=Sw5uT4VkCHA](https://www.youtube.com/watch?v=Sw5uT4VkCHA) 

Huge thanks to Josh Berkus and Laura Santamaria for their incredible speaker training, and to Andrew Block, Christopher Nuland, Jennifer Vargas, Sean Rickerd, and Stuart Miniman for their support.

![](../../../../../img/inblog/kubecon-na-2025/image5.png)
![](../../../../../img/inblog/kubecon-na-2025/image6.png)

## Opening Keynote (Kubernetes AI Conformance)

The CNCF leadership invited the co-chairs of the Kubernetes WG AI Conformance, including Yuan Tang (Red Hat), Rita Zhang (Microsoft), Janet Kuo (Google), and Mario Fahlandt (Kubermatic), to share their experiences and vision of the Kubernetes AI Conformance Program. 

Special thanks to Laura Santamaria, Derek Carr, and Mrunal Patel for offering insights from both community and technical perspectives as well as Jessica Forrester and Jason Greene for their support throughout the journey.

* Recording: [https://www.youtube.com/watch?v=cQvtT2vRhok\&t=1462s](https://www.youtube.com/watch?v=cQvtT2vRhok&t=1462s)   
* CNCF announcement: [https://www.cncf.io/announcements/2025/11/11/cncf-launches-certified-kubernetes-ai-conformance-program-to-standardize-ai-workloads-on-kubernetes/](https://www.cncf.io/announcements/2025/11/11/cncf-launches-certified-kubernetes-ai-conformance-program-to-standardize-ai-workloads-on-kubernetes/) 

Red Hat has been leading this effort and is among first vendors that are certified:  
![](../../../../../img/inblog/kubecon-na-2025/image7.png)

Yuan on the keynote stage, together with other program co-chairs of K8s WG AI Conformance:  
![](../../../../../img/inblog/kubecon-na-2025/image8.png)
![](../../../../../img/inblog/kubecon-na-2025/image9.png)

# Other sessions

## llm-d 

Sponsored demo on llm-d by Christopher Nuland at the demo theater located in solutions showcase area:  
![](../../../../../img/inblog/kubecon-na-2025/image10.png)

llm-d: Multi-Accelerator LLM Inference on Kubernetes by Erwan Gallen: [https://sched.co/27Fee](https://sched.co/27Fee)  
![](../../../../../img/inblog/kubecon-na-2025/image11.png)

## Intelligent routing

[Intelligent LLM Routing: A New Paradigm for Multi-Model AI Orchestration in Kubernetes](https://sched.co/27FaI) by Chen Wang (IBM Research) and Huamin Chen (Red Hat)  
![](../../../../../img/inblog/kubecon-na-2025/image12.png)

[You got a match\! LLM Prefix Aware Routing with Kubernetes](https://sched.co/28D0y) by Ricardo Noriega (Red Hat) and Cong Liu (Google) 

[Routing Stateful AI Workloads in Kubernetes](https://kccncna2025.sched.com/event/27FX6/routing-stateful-ai-workloads-in-kubernetes-maroon-ayoub-ibm-michey-mehta-red-hat) by Maroon Ayoub (IBM) and Michey Mehta (Red Hat)   
![](../../../../../img/inblog/kubecon-na-2025/image13.png)

## Benchmarking

Samuel Monson (Red Hat) and Jing Chen (IBM Research) delivered a tutorial on distributed LLM inference benchmarking with Junchen Jiang (University of Chicago), Ganesh Kudleppanavar (NVIDIA), and Jason Kramberger (Google).

Session: [https://sched.co/27FXL](https://sched.co/27FXL)   
![](../../../../../img/inblog/kubecon-na-2025/image14.png)

## KServe

Yuan Tang (Red Hat) and Dan Sun (Co-founder of KServe, Bloomberg) shared the project's current state and future direction.

Session: [https://sched.co/28D4J](https://sched.co/28D4J)  
![](../../../../../img/inblog/kubecon-na-2025/image15.png)

## K8s WG Serving

Yuan Tang (Red Hat) shared the current state of model inference on Kubernetes with Rita Zhang (Microsoft), Jiaxin Shan (Bytedance), and Sergey Kanzhelev (Google) as well as efforts and initiatives from K8s WG Serving.

Session: [https://sched.co/27Nlv](https://sched.co/27Nlv)  
![](../../../../../img/inblog/kubecon-na-2025/image16.png)

## Media interview (KServe and vLLM Semantic Router)

Huamin Chen and Yuan Tang joined a media interview to discuss KServe joining CNCF and the new vLLM semantic router project.  
![](../../../../../img/inblog/kubecon-na-2025/image17.png)

## Other relevant sessions

* [Kubeflow Ecosystem: Navigating the Cloud-Native AI/ML and LLMOps Frontier](https://sched.co/27Nm7)  
* [Gateway API: Table Stakes](https://sched.co/27No3)  
* [Introducing TAG Workloads Foundation: Advancing the Core of Cloud Native Execution](https://sched.co/27NnE)  
* [RAG and Fine Tuning With Kubeflow](https://sched.co/27FY7)  
* [High-Performance AI Workloads in KubeVirt VMs With NVIDIA GPUs: Challenges and Real-World Solutions](https://kccncna2025.sched.com/event/27Fd3/high-performance-ai-workloads-in-kubevirt-vms-with-nvidia-gpus-challenges-and-real-world-solutions-ezra-silvera-ibm-michael-hrivnak-red-hat)

Full list of sessions from Red Hat: [https://kccncna2025.sched.com/?searchstring=red+hat](https://kccncna2025.sched.com/?searchstring=red+hat) 

# Relevant events

**Cloud Native & Kubernetes AI Day**

* 300+ attendees  
* Yuan Tang co-chaired the event to ensure the event ran smoothly from start to finish and delivered the closing remarks

**Kubernetes SIGs Lunch and Learn**

* Representation for AI related WGs: WG Serving and WG AI Conformance

**Red Hat Time Machine**

* Invited community members and collaborators to join this event and had great discussions

**Kubeflow Summit and project booth**

* Valentina Rodriguez Sosa Co-chaired Kubeflow Summit and helped coordinate booth schedules for the Kubeflow project and ensured our presence at the booth through the week

# Upcoming KubeCons

Dates and locations for upcoming KubeCons in 2026 were announced during the opening keynote:

* KubeCon Europe in Amsterdam, Netherlands (March 23–26)  
* KubeCon India in Mumbai (June 18 \- 19\)  
* KubeCon Japan in Yokohama (July 29 \- 30\)  
* KubeCon China in Shanghai (September 8 \- 9\)  
* KubeCon North America in Salt Lake City, Utah (November 9 \- 12\)

**See you in 2026\!**
