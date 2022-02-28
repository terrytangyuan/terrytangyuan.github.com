---
layout:     post
title:      "Argo Security Automation with OSS-Fuzz"
subtitle:   "Continuous Fuzzing Integration in Argo"
date:       2022-02-28
author:     "Yuan Tang"
tags:
    - Open Source
    - DevOps
    - Kubernetes
    - Argo
    - Security
---


**Authors: [Yuan Tang](https://twitter.com/TerryTangYuan) (Akuity), [Adam Korczynski](https://twitter.com/AdamKorcz4) and [David Korczynski](https://twitter.com/Davkorcz) (Ada Logics), Jann Fischer (Red Hat), [Henrik Blixt](https://twitter.com/khblixt) (Intuit)**

![argo-security](../../../../../img/inblog/argo-security.png)

Security is a key priority for the Argo project. In an effort to improve security, the Argo maintainers from [Akuity](https://akuity.io/), [Red Hat](https://www.redhat.com), and [Intuit](https://www.intuit.com/) recently joined forces with [Ada Logics](https://adalogics.com/) in a project commissioned by the [Cloud Native Computing Foundation](https://www.cncf.io/) on setting up fuzzing for the Argo project. In summary, this engagement set up a continuous fuzzing infrastructure that now runs as part of the project’s recurring jobs. A total of 41 fuzzers were developed and 10 bugs were found. All found bugs have been fixed (with exception of two issues found at the end of the engagement) and are available in the latest project patchsets. In this blog post we will outline the process and results of this engagement while full details are available in [the Argo fuzzing report](https://github.com/argoproj/argoproj/blob/dd7cae43d81c5a11f21ff4ea0a4afadcae4799c7/docs/audit_fuzzer_adalogics_2022.pdf).

Fuzzing is a common technique to automate the process of identifying reliability and security issues. It is commonly used by security researchers to find vulnerabilities in systems and the technique has been successfully used on various [CNCF projects](https://github.com/cncf/cncf-fuzzing#cncf-projects-and-fuzzing), such as Kubernetes, Envoy, Helm, Linkerd2-proxy, and Fluent-bit. The general approach of fuzzing is to use genetic algorithms in combination with sophisticated program analysis and software instrumentation techniques to generate inputs that achieve a high level of code coverage in the target software. In the context of Argo the purpose of this is identifying inputs that trigger system faults of various kinds, such as crashes, panics, out-of-bounds memory issues, and hangs.

![argo-oss-fuzz](../../../../../img/inblog/argo-oss-fuzz.png)

Ada Logics set up a fuzzing infrastructure and implemented fuzzers with a large coverage across various subprojects of the Argo ecosystem. This is the first step in fuzzing Argo as we did not have any fuzzers in place before. One of the goals of this collaboration was to create a meaningful and sustainable fuzzing infrastructure that the maintainers and contributors of the Argo Project can use to observe results and adopt into the development lifecycle and release process.

## Fuzzer Integration

Ada Logics developed a total of 41 fuzzers as part of this engagement. The Argo projects focused on are Argo Workflows, Argo CD, Argo Events, Argo Rollouts, and GitOps Engine. The fuzzers were set up to run continuously by way of OSS-fuzz and 10 bugs were reported. By the end of the engagement, all issues have been fixed except for two issues which were found in the final days of the engagement. The bugs found by the fuzzers are divided into the following groups:
* 4 nil-dereferences
* 1 Slice bounds out of range
* 3 Index out of range
* 1 Interface conversion issue
* 1 Out of memory

The details of these issues and their root cause analysis are listed in the “Issues found” section in [the Argo fuzzing report](https://github.com/argoproj/argoproj/blob/dd7cae43d81c5a11f21ff4ea0a4afadcae4799c7/docs/audit_fuzzer_adalogics_2022.pdf).

All fuzzers developed in this engagement were committed to the [CNCF-Fuzzing repository](https://github.com/cncf/cncf-fuzzing). OSS-fuzz was then instructed to get the fuzzers from there and build them against the latest master branch of each of the five repositories.

Most fuzzers will run at least 3-4 times per week. This frequency helps Argo catch issues in new or modified code as well as the parts of the code that have not been touched for longer periods of time. The fuzzers are rebuilt daily to get the latest updates from each project and test for any recent breaking changes that could block the fuzzers from running. Failing builds will be reported to the maintainers. 

Issues are reported by OSS-fuzz. When an issue is found, Argo maintainers are notified with an email containing a link to a detailed report. The report includes details such as stack trace, name of the fuzzer that triggered the crash as well as the exact test case that caused the crash. This test case can be used to reproduce the issue locally. All findings on OSS-fuzz have a 90 day grace period after which they become public. If an issue is fixed within the 90 days, OSS-fuzz verifies this and automatically closes the issue and makes it public. 

Issues reported by the fuzzers are publicly available [here](https://bugs.chromium.org/p/oss-fuzz/issues/list?q=argo) and the OSS-Fuzz set up is available [here](https://github.com/google/oss-fuzz/tree/6b6196001560b3ab5d5ac33e73cc958ac2530c30/projects/argo) and the Argo fuzzers are available in the CNCF-Fuzzing repository [here](https://github.com/cncf/cncf-fuzzing/tree/789eea5ef9aff72fab52e9cb9070552baa3cd261/projects/argo).

## Future Plans

Going forward, we would like to continue improving the coverage of the existing fuzzers to include additional areas and subprojects from the Argo ecosystem. Writing fuzzers for new code will be included in the checklist when contributors submit the PRs to help contributors and maintainers develop a habit of writing fuzzers in addition to other familiar testing procedures.

Fuzzing will be supported natively in Go 1.18 and this has potential to ease the maintenance effort in the fuzzers. OSS-Fuzz infrastructure already supports fuzzers written for the native fuzzing engine in Go 1.18 and, therefore, we plan to transition into using this type of set up. 

In addition, the current fuzzers are located in the [CNCF-fuzzing repository](https://github.com/cncf/cncf-fuzzing). The Argo maintainers will discuss whether the fuzzers should be moved to the upstream subprojects. In the event we rewrite the fuzzers for the Go 1.18 native fuzzing engine, the fuzzers can be placed close to the tested code similarly to how Argo’s Go unit tests are handled.

## Acknowledgement

We would like to thank Ada Logics for setting up the fuzzing infrastructure for the Argo ecosystem and implementing an extensive fuzzing suite. The work has already paid off in terms of finding bugs in the codebase.

We would also like to thank CNCF for commissioning this engagement.

Last but not least, we are grateful to the Argo maintainers and contributors who helped fix all the identified issues.
