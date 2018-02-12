---
layout:     post
title:      "autoplotly - Automatic Generation of Interactive Visualizations for Popular Statistical Results"
subtitle:   ""
date:       2018-02-12
author:     "Yuan Tang"
tags:
    - Visualization
    - Open Source
    - R
---

Hi there!

<link rel="stylesheet" href="/css/custom.css">

```
p <- autoplotly(prcomp(iris[c(1, 2, 3, 4)]), data = iris,
  colour = 'Species', label = TRUE, label.size = 3, frame = TRUE)
p
```

<div class="myIframe"><iframe src="/data/plots/autoplotly/pca-ggplot2-composable.html"></iframe></div>


```
p +
  ggplot2::ggtitle("Principal Components Analysis") +
  ggplot2::labs(y = "Second Principal Components", x = "First Principal Components")
```

<div class="myIframe"><iframe src="/data/plots/autoplotly/pca-ggplot2-composable-2.html"></iframe></div>


```
p <- autoplotly(prcomp(iris[c(1, 2, 3, 4)]), data = iris,
  colour = 'Species', frame = TRUE)

p %>% plotly::layout(annotations = list(
  text = "Example Text",
  font = list(
    family = "Courier New, monospace",
    size = 18,
    color = "black"),
  x = 0,
  y = 0,
  showarrow = TRUE))
```

<div class="myIframe"><iframe src="/data/plots/autoplotly/pca-plotly-composable.html"></iframe></div>

```
library(changepoint)
autoplotly(cpt.meanvar(AirPassengers))
```

<div class="myIframe"><iframe src="/data/plots/autoplotly/changepoint.html"></iframe></div>


```
library(dlm)
form <- function(theta){
  dlmModPoly(order = 1, dV = exp(theta[1]), dW = exp(theta[2]))
}
model <- form(dlmMLE(Nile, parm = c(1, 1), form)$par)
filtered <- dlmFilter(Nile, model)
autoplotly(filtered)
```

<div class="myIframe"><iframe src="/data/plots/autoplotly/dlm.html"></iframe></div>

```
library(strucchange)
autoplotly(breakpoints(Nile ~ 1), ts.colour = "blue", ts.linetype = "dashed",
           cpt.colour = "dodgerblue3", cpt.linetype = "solid")
```
<div class="myIframe"><iframe src="/data/plots/autoplotly/strucchange.html"></iframe></div>

```
library(splines)
autoplotly(ns(diamonds$price, df = 6))
```
<div class="myIframe"><iframe src="/data/plots/autoplotly/splines.html"></iframe></div>

```
library(splines)
subplot(
  autoplotly(ns(diamonds$price, df = 6)),
  autoplotly(ns(diamonds$price, df = 3)), nrows = 2, margin = 0.03)
```
<div class="myIframe"><iframe src="/data/plots/autoplotly/splines-subplots.html"></iframe></div>
