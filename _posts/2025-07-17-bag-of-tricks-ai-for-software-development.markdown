---
layout:     post
title:      "Bag of Tricks: Using AI for Software Development"
subtitle:   ""
date:       2025-07-17
author:     "Yuan Tang"
tags:
    - Leadership
---

Other potential angles:
* AI for experienced developers

Outline
* Write good instructions, designs, like an architect and product manager. AI tends to generate more than what you asked. Be specific
* Small refactorings/optimizations instead of big ones. 
* Generate tests and make sure they run before major refactoring. Also note that code may be modified incorrectly to pass tests. 
* Provide debugging hints if you ever run into infinite loop of iterations and AI gets stuck easily and run out of ideas
* Security is important. AI can help patches but don’t underestimate any generated code that might be insecure.
* AI to write CI workflows - can generate boiler templates but have a lot of things to tweak manually. Have to copy paste error messages from GitHub Actions to locally.
* If you already have scripts to auto generate code, e.g. common in Golang and Kubernetes controller development, tell AI explicitly that you'd like to reuse the existing tools. Otherwise, your output tokens can be expensive

