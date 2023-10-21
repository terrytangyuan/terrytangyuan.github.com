---
layout:     post
title:      "What's new in Argo Workflows v3.5"
subtitle:   "Exciting New Features with Improved User Experience and Performance"
date:       2023-08-14
author:     "Yuan Tang"
tags:
    - Open Source
    - Kubernetes
    - Argo
---


We are thrilled to announce that [Argo Workflows v3.5](https://github.com/argoproj/argo-workflows/releases/tag/v3.5.0) is now available!


We have rolled out a long list of exciting new features, ranging from improvements to existing UI/UX, CLI, controller performance optimizations, additional fields and parameters in workflow/template spec, authentication, monitoring, and more. 

Some quick statistics about this release:

* 66 new features
* 237 bug fixes
* 182 documentation updates
* 18 build and 24 improvements
* from 63 contributors

## Overview of New Features

We'd like to highlight some of the new features in each area in the following sections. You can find the complete changelog [here](https://github.com/argoproj/argo-workflows/blob/master/CHANGELOG.md).

### UI

In this release, we removed the archived workflow list view from the UI. There's now a unified workflow list view to see both live workflow custom resource objects and the archived workflows that are persisted in the database. The additional "archived" column indicates whether a particular workflow has been archived and persisted in the database. Thanks to [#11121](https://github.com/argoproj/argo-workflows/pull/11121) by [Yuan Tang](https://github.com/terrytangyuan) and a couple of important bug fixes by [Tomoki Yamaguchi](https://github.com/toyamagu-2021).

![unified-workflows](../../../../../img/inblog/argo-workflows-v3.5/unified-workflows.png)


Users can also resubmit workflows with parameters. Thanks again to [Tomoki Yamaguchi](https://github.com/toyamagu-2021)'s work on [#11083](https://github.com/argoproj/argo-workflows/pull/11083)!

![submit-with-params](../../../../../img/inblog/argo-workflows-v3.5/submit-with-params.png)


Ever wanted to add title and description for your workflows so that your teammates can get a sense of what you are experimenting? This is now possible in the new release! Thanks to [#9805](https://github.com/argoproj/argo-workflows/pull/9805) by [Jason Meridth](https://github.com/jmeridth).

![wf-title-description](../../../../../img/inblog/argo-workflows-v3.5/wf-title-description.png)

Users no longer need to manually check and uncheck individual checkboxes in workflow DAG filter. Thanks to the new "Check All" checkbox added in [#11132](https://github.com/argoproj/argo-workflows/pull/11132) by [Jason Meridth](https://github.com/jmeridth).

![check-all](../../../../../img/inblog/argo-workflows-v3.5/check-all.png)


In this release, users can also add customized navigation links and columns. Thanks to [#10808](https://github.com/argoproj/argo-workflows/pull/10808) by [Remington Breeze](https://github.com/rbreeze) and [#10677](https://github.com/argoproj/argo-workflows/pull/10677) by [Jiacheng Xu](https://github.com/jiachengxu). For example, with a simple configuratio in controller's configmap like the following:

```
data: 
  links: |
    - name: Completed Workflows
      scope: workflow-list
      url: http://workflows?label=workflows.argoproj.io/completed=true
  columns: |
    - name: Workflow Completed
      type: label
      key: workflows.argoproj.io/completed
```

We can see additional link to the list of completed workflows and a new column "Workflows Completed":

![customized-links](../../../../../img/inblog/argo-workflows-v3.5/customized-links.png)

Additionally, thanks to [#10145](https://github.com/argoproj/argo-workflows/pull/10145) by [Isitha Subasinghe](https://github.com/isubasinghe), the Argo Workflows UI can parse JSON structured logs.

User information in suspended nodes when resuming is also available. Thanks to [Tomoki Yamaguchi](https://github.com/toyamagu-2021) via [#11763](https://github.com/argoproj/argo-workflows/pull/11763).

Search functionality has been added for WorkflowTemplates page in [#11684](https://github.com/argoproj/argo-workflows/pull/11684) by [sunyeongchoi](https://github.com/sunyeongchoi).

We'll be continuously improving the UI/UX. If you are interested in contributing, please check out the [UI/UX improvements project board](https://github.com/orgs/argoproj/projects/29).



### CLI

A new argument `--query-chunk-size` is added to `argo delete` to be consistent with `argo list`. Thanks to [#10813](https://github.com/argoproj/argo-workflows/pull/10813) by [Oliver Skånberg-Tippen](https://github.com/oskanberg). The value supplied in this argument will be applied when the command is fetching the workflows to delete. Note that the name `query-chunk-size` is different from `chunk-size` argument to avoid the implication that it will delete based on the specified chunk.

A new argument `--selector` flag is added to `argo cron list` command to support selectively querying Cron workflows based on labels defined under objects' `metadata`, similar to the `--selector` field in `kubectl`. Thanks to [#11202](https://github.com/argoproj/argo-workflows/pull/11202) by [Dylan Bragdon](https://github.com/dbragdon1).

`argo retry` now allows users to retry successful workflows if `--node-field-selector` is set, instead of only allowing to retry failed  or errored workflows. Thanks to [#11409](https://github.com/argoproj/argo-workflows/pull/11409) by [Or Shachar](https://github.com/or-shachar).


### Workflow/Template Spec

Users can configure whether to force remove the finalizer if artifact GC fails. Thanks to [#10810](https://github.com/argoproj/argo-workflows/pull/10810) by [Julie Vogelman](https://github.com/juliev0).

Users can access additional variables:

* `steps.<TASKNAME>.hostNodeName`: the host node name where the task ran. Thanks to [#10950](https://github.com/argoproj/argo-workflows/pull/10950) by [Amit Oren](https://github.com/amit-o).
* `lastRetry.message`: the message output from the last retry via [#10987](https://github.com/argoproj/argo-workflows/pull/10987) by [Alan Clucas](https://github.com/Joibel).
* `workflow.mainEntrypoint`: workflow's initial entrypoint via [#11151](https://github.com/argoproj/argo-workflows/pull/11151) by [Alan Clucas](https://github.com/Joibel).

We also added cross-namespace locking for semaphore and mutex via [#11096](https://github.com/argoproj/argo-workflows/pull/11096) by [Lukas Wöhrl](https://github.com/woehrl01). This enhances the semaphore configuration with a namespace property to enable better resource management in environments with shared resources across multiple namespaces.

Workflow-level `DeleteDelayDuration` is added to this release. Thanks to [#11325](https://github.com/argoproj/argo-workflows/pull/11325) by [Anton Gilgur](https://github.com/agilgur5).

The creator labels of a `CronWorkflow` are now propogated to the scheduled workflows. Thanks to [#11407](https://github.com/argoproj/argo-workflows/pull/11407) by [Jinsu Park](https://github.com/umi0410).


### Authentication

Support for `name` field in claim for RBAC SSO is added. Thanks to [#10927](https://github.com/argoproj/argo-workflows/pull/10927) by [Anton Gilgur](https://github.com/agilgur5).

We also improved the logging in OAuth2 callback handler so that it's easier to identify errors and misconfigurations related to SSO. Thanks to [#11370](https://github.com/argoproj/argo-workflows/pull/11370) by [Jinsu Park](https://github.com/umi0410). For example, we'll see the following detailed error message when the client secret value is incorrectly set. Prior to this release, we would only see a `401` status.

```txt
time="2023-07-16T12:20:25.064Z" level=error msg="failed to get oauth2Token by using code from the oauth2 server" error="oauth2: \"unauthorized_client\" \"Invalid client secret\""
time="2023-07-16T12:20:25.064Z" level=info duration=9.112831ms method=GET path=/oauth2/callback size=0 status=401
```

We also added support for filtering SSO groups based on regex. Thanks to [Basanth Jenu H B](https://github.com/basanthjenuhb) in [#11774](https://github.com/argoproj/argo-workflows/pull/11774).

### Monitoring

Users can specify an operation, e.g. `Add`, `Set`, and `Sub`, to gauge metric's value. Thanks to [#10774](https://github.com/argoproj/argo-workflows/pull/10774) by [Eduardo Rodrigues](https://github.com/eduardodbr).
```yaml
metrics:
    prometheus:
      - name: custom_gauge_sub
        labels:
          - key: name
            value: random-int
        gauge:
          operation: Sub
          value: "5"
```

### Controller

We switched to use `WorkflowTemplate` and `ClusterWorkflowTemplate` informers when validating CronWorkflows to improve the CronWorkflow controller's performance. Prior to this release, there is a large number of unnecessary K8s API requests for "GET WorkflowTemplate". Thanks to [#11470](https://github.com/argoproj/argo-workflows/pull/11470) by [Julie Vogelman](https://github.com/juliev0).

We also exposed a new argument `--cron-workflow-workers` to specify the number of CronWorkflows workers, which would be useful when running a large number of CronWorkflows. Thanks to [#11457](https://github.com/argoproj/argo-workflows/pull/11457) by [Saravanan Balasubramanian](https://github.com/sarabala1979).

Client-side throttling logging has been improved by [@Jack-R-lantern](https://github.com/Jack-R-lantern) in [#11437](https://github.com/argoproj/argo-workflows/pull/11437).

The controller has also added checks to protect users against infinite recursion for calls to templates. Thanks to [Alan Clucas](https://github.com/Joibel) in [#11646](https://github.com/argoproj/argo-workflows/pull/11646).


### Artifacts

Artifact streaming download for HTTP/Artifactory artifact driver has been added by [Yuan Tang](https://github.com/terrytangyuan) in [#11823](https://github.com/argoproj/argo-workflows/pull/11823). Previously, when a user would click the button to download an artifact in the UI, the artifact would need to be written to the Argo Server’s disk first before downloading. If many users tried to download simultaneously, they would take up disk space and fail the download. After this release, S3, Azure Blob, HTTP, and Artifactory all support streaming download so artifacts don’t need to be first saved to disk.

Artifactory artifact also supports keyFormat now to be consistent with other artifact types. Thanks to [Yuan Tang](https://github.com/terrytangyuan) via [#11798](https://github.com/argoproj/argo-workflows/pull/11798).

We also added custom CA support in S3 artifact repository. Thanks to [Niklas Simons](https://github.com/nsimons) via [#11161](https://github.com/argoproj/argo-workflows/pull/11161).


### Local Development

Developers of Argo Workflows can now use [Nix](https://nixos.org/) to make the local development easier. Nix is a package manager and build tool which focuses on reproducible build environments. Check out how to use it [here](https://github.com/argoproj/argo-workflows/blob/master/docs/running-nix.md). Thanks to [#10999](https://github.com/argoproj/argo-workflows/pull/10999) by [Isitha Subasinghe](https://github.com/isubasinghe).


## Join Our Growing Community

Thanks to everyone who filed issues or helped resolve them, asked and answered questions, and were part of inspiring discussions. You are welcome to [join our growing Slack community](https://argoproj.github.io/community/join-slack/). 

We also host monthly community meetings where we and the community showcase demos and discuss the current and future state of the project. Feel free to [join us](https://github.com/argoproj/argo-workflows#community-meetings).

Check out the curated list of awesome projects and resources related to Argo [here](https://github.com/akuity/awesome-argo)!

