---
layout:     post
title:      "Open source AI at Red Hat: Our journey in the Kubeflow community"
subtitle:   ""
date:       2024-03-19
author:     "Yuan Tang"
tags:
    - Open Source
    - Kubernetes
    - Kubeflow
---


**Authors: Jeremy Eder, Yuan Tang, Ricardo Martinelli de Oliveira**

*This blogpost was originally posted [here](https://www.redhat.com/en/blog/open-source-ai-red-hat-our-journey-kubeflow-community).*

Red Hat has been involved in AI and data projects for many years, and while many support the modernization journey, none tell the whole user journey to bring artificial intelligence (AI) and machine learning (ML) to production. This is why we launched [Open Data Hub](http://opendatahub.io/)–to help develop and support open source projects dedicated to data and AI/ML, like [Kubeflow](https://www.kubeflow.org/) and [KServe](https://github.com/kserve/kserve).

## Open Data Hub and Kubeflow

Open Data Hub started with a simple operator that deploys AI/ML and data software on Red Hat OpenShift clusters with some level of integration between them. However, when we began to hit roadblocks when looking for supportability, we turned to Kubeflow–a new project focused on simplifying and scaling ML workload deployments on Kubernetes. By rewriting Open Data Hub on top of Kubeflow code, we were able to create a new support matrix of features.  Red Hat has increased our involvement with the Kubeflow community over the past year to not only contribute code, but to assist the community in achieving higher levels of maturity and user acceptance.  Below is an overview of the work we are currently engaged in the Kubeflow community.

## Kubeflow 1.9 release

After joining the Kubeflow community,  Ricardo Martinelli, Red Hat senior software engineer, volunteered to work on the Kubeflow 1.9 release as release manager, collaborating with fellow Kubeflow contributors to create a roadmap for the release. As a result, Red Hat contributed several features to Kubeflow 1.9.

## Model registry

Model registry, an [in-demand feature](https://blog.kubeflow.org/kubeflow-user-survey-2023/), became one of Red Hat’s primary contributions to Kubeflow 1.9. Model registry integrates with Kubeflow’s pipelines and serving components to create a catalog of artifacts, including models, datasets, metrics and more, and deploy models from the artifact storage. Other key features of the model registry include operator/helm chart deployment, RBAC, multi-tenancy, and others. To support the new model registry feature, the Kubeflow community developed a new working group.

## Kubeflow Pipelines 2.0

Red Hat also began contributing to Kubeflow Pipelines 2.0 by facilitating their upgrade to [Argo Workflows](https://github.com/argoproj/argo-workflows) 3.4, addressing issues regarding MinIO security and licensing and developing performance improvements in both Argo and Tekton implementations.

## Notebooks 2.0

With the Kubeflow 1.9 release, the community decided to start their plans for Kubeflow Notebooks 2.0, which would bring a new set of custom resource definitions (Workspace and WorkspaceKind). These CRDs provide the administrator with more control over the workspaces, including the ability to update an existing notebook configuration. This work started in the design phase at the beginning of 2024, and the Notebooks working group is driving its design architecture. Red Hat engineers Andriana Theodorakopoulou, Ramakrishna Pattnaik, Jiri Petrlik and Harshad Reddy Nalla are in the midst of developing the design document and targeting future code contributions.

## KServe

[KServe](https://github.com/kserve/kserve) has been a standalone project after graduating from Kubeflow Incubation. The KServe community has been working closely with the Kubeflow community as part of the Kubeflow serving working group to integrate KServe with Kubeflow while developing KServe’s own rapidly growing community and driving innovative features. We’ve been working closely with the community to lead efforts in various areas, including adding HuggingFace and vLLM out-of-the-box runtimes, adding pluggable explainer runtime, enhancements and bug fixes to RawDeployment mode, optimizing oversized KServe CRDs, harnessing security, improving release process and more. Edgar Hernandez Garcia, Jooho Lee, Filippe Spolti, and Yuan Tang are among the major KServe contributors from Red Hat. Notably, Yuan Tang and Edgar Hernandez Garcia got promoted to KServe reviewers recently.

## What’s next for Kubeflow?

Red Hat and other community members are working towards developing Kubeflow into a Cloud Native Computing Foundation (CNCF) graduated project.  Some of the requirements to qualify Kubeflow as a CNCF graduated project  includes revisiting Kubeflow materials for filling the CNCF graduation requirements, which expanded the work in other areas, including security and IP policy.

Red Hat’s product security and open source program office teams engaged with the Kubeflow community to address questions around security vulnerability processes when they arise in Kubeflow components. Sean Pryor is leading an effort to prevent releasing Kubeflow images with unhandled CVEs by proposing the use of security scanners, and a workflow to fix these security issues. Owen Watkins from the Red Hat product security team is working on general guidance for taking action when a security issue is reported.

Another area in which Red Hat is contributing to Kubeflow is in governance, where Yuan Tang,  Red Hat principal software engineer, was elected as a member of the [Kubeflow Steering Committee](https://blog.kubeflow.org/election/2024/01/31/kubeflow-project-steering-committee-announced.html) (KSC), the "root" level governance body of Kubeflow. Yuan is an experienced author and maintainer of many popular open-source projects, including Argo and KServe, and has been a tech lead on various Kubeflow sub-projects for the past six years. His contributions have built trust in the Kubeflow community in his technical and leadership skills and have helped drive the community topics that arose when Kubeflow started the CNCF graduation process.

Since the beginning of our contributions to the Kubeflow project, Red Hat knew that the idea of a "certified distribution" would be an important subject to address, and with the new Steering Committee, and the CNCF Graduation process on track, Kubeflow could revisit the plan to create a conformance test to certify Kubeflow Distributions.

There is more work to be done in Kubeflow to achieve CNCF graduation, and Red Hat is committed to contributing even more towards this goal.

## Kubeflow and Google Summer of Code

Following our commitment to the Kubeflow community and our experience with working on open-source projects, we stepped in to create a proposal on behalf of the Kubeflow community to Google Summer of Code. We proposed more than projects in collaboration with other Kubeflow contributors that covered LLM API development, Github issues and PR triage, documentation tasks and many others. Red Hat has been participating in Google Summer of Code for several years, including work across our multiple middleware projects, and that experience led us to get approval to join the event with the help of the Kubeflow community. We are very excited to mentor students and teach them how open source collaboration enlightens innovation and enhances education and careers with real-world development experience.

Red Hat’s engagement and relationship with the Kubeflow community exemplifies how communities can build and deliver better software together.  We look forward to many years of continued success and thank the Kubeflow community for welcoming us with open arms.