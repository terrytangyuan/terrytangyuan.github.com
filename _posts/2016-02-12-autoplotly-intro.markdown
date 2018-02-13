---
layout:     post
title:      "autoplotly - One Line of R Code to Build Interactive Visualizations for Popular Statistical Results"
subtitle:   "Automatic Generation of Interactive Visualizations in ggplot2 and plotly Styles"
date:       2018-02-12
author:     "Yuan Tang"
tags:
    - Visualization
    - Open Source
    - R
---

<h><b>Note: this is NOT ready on mobile yet. Please switch to use a desktop browser.</b></h>

<link rel="stylesheet" href="/css/custom.css">

## Background

Often times users only want to quickly iterate the process of exploring data, building statistical models, and visualizing the model results, especially the models that focus on common tasks such as clustering and time series analysis. Some of these packages provide default visualizations for the data and models they generate. However, they look out-of-fashion and these components require additional transformation and clean-up before using them in [ggplot2](http://ggplot2.tidyverse.org/) and each of those transformation steps must be replicated by others when they wish to produce similar charts in their analyses. Creating a central repository for common/popular transformations and default plotting idioms would reduce the amount of effort needed by all to create compelling, consistent and informative charts.

The [ggfortify package](https://CRAN.R-project.org/package=ggfortify) provides a unified interface with one single `autoplot()` function for plotting many statistics and machine learning packages and functions in order to help these users achieve reproducibility goals with minimal effort. `ggfortify` package has a very easy-to-use and uniform programming interface that enables users to use one line of code to visualize statistical results of many popular R packages using `ggplot2` as building blocks. This helps statisticians, data scientists, and researchers avoid both repetitive work and the need to identify the correct `ggplot2` syntax to achieve what they need. Users are able to generate beautiful visualizations of their statistical results produced by popular packages with minimal effort.

The [autoplotly package](https://github.com/terrytangyuan/autoplotly) is an extension built on top of `ggplot2`, [plotly](https://plot.ly/), and `ggfortify` to provide functionalities to automatically generate interactive visualizations for many popular statistical results supported by `ggfortify` package in `plotly` and `ggplot2` styles. The generated visualizations can also be easily extended using `ggplot2` and `plotly` syntax while staying interactive.


## Get Started

You can either try out the following examples in your RStudio or play around with the interactive visualizations embedded on this post.

A couple hints for you to facilitate your exploration:

* Simply drag and draw to zoom in your area of interest
* Double-click to zoom back out
* Hover your mouse over to see more options, e.g. lasso/box select, download as PNG, etc.

### Installation

Install the latest stable release from CRAN:

```
install.packages('autoplotly')
```

### Examples


The `autoplotly()` function works for the two essential classes of objects for principal component analysis (PCA) obtained from `stats` package: `stats::prcomp` and `stats::princomp`, for example:

```
p <- autoplotly(prcomp(iris[c(1, 2, 3, 4)]), data = iris,
  colour = 'Species', frame = TRUE)
p
```

<div class="myIframe"><iframe src="/data/plots/autoplotly/pca-ggplot2-composable.html"></iframe></div>



Visualization of the change points with optimal positioning for the `AirPassengers` data set
found in the `changepoint` package using the `cpt.meanvar` function:

```
library(changepoint)
autoplotly(cpt.meanvar(AirPassengers))
```

<div class="myIframe"><iframe src="/data/plots/autoplotly/changepoint.html"></iframe></div>



Visualization of the original and smoothed line from Kalman filter function in `dlm` package:

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



Visualization of optimal break points where possible structural changes happen in the
regression models built by `strucchange::breakpoints`:

```
library(strucchange)
autoplotly(breakpoints(Nile ~ 1), ts.colour = "blue", ts.linetype = "dashed",
           cpt.colour = "dodgerblue3", cpt.linetype = "solid")
```
<div class="myIframe"><iframe src="/data/plots/autoplotly/strucchange.html"></iframe></div>



B-spline basis points visualization for natural cubic spline with boundary knots produced
from `splines::ns`:

```
library(splines)
autoplotly(ns(diamonds$price, df = 6))
```
<div class="myIframe"><iframe src="/data/plots/autoplotly/splines.html"></iframe></div>

You can find a complete list of supported objects by `autoplotly` [here](https://github.com/sinhrks/ggfortify#coverage).

## Extensibility and Composability

The plots generated using `autoplotly()` can be easily extended by applying additional
`ggplot2` elements or components. For example, we can add title and axis labels to the
originally generated plot using `ggplot2::ggtitle` and `ggplot2::labs`:

```
autoplotly(
  prcomp(iris[c(1, 2, 3, 4)]), data = iris, colour = 'Species', frame = TRUE) +
  ggplot2::ggtitle("Principal Components Analysis") +
  ggplot2::labs(y = "Second Principal Components", x = "First Principal Components")
```

<div class="myIframe"><iframe src="/data/plots/autoplotly/pca-ggplot2-composable-2.html"></iframe></div>

Similarly, we can add additional interactive components using `plotly`. The following
example adds a custom `plotly` annotation element placed to the center of the plot with an arrow:


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

We can also stack multiple plots generated from `autoplotly()` together in a single view
using `subplot()`, two interactive splines visualizations with different degree of freedom
are stacked into one single view in the following example:

```
library(splines)
subplot(
  autoplotly(ns(diamonds$price, df = 6)),
  autoplotly(ns(diamonds$price, df = 3)), nrows = 2, margin = 0.03)
```
<div class="myIframe"><iframe src="/data/plots/autoplotly/splines-subplots.html"></iframe></div>

The snapshots of the interactive visualizations generated via `autoplotly()` can be exported using
a simple `export()` function, for example:
```
export(p, "/tmp/result.png")
```

It builds on top of `RSelenium` package for exporting WebGL plots and uses `webshot` package for non-WebGL formats such as JPEG, PNG, PDF, etc.


## Future Development

This package is still in an early development stage. Some details in the visualizations may not
look as perfect yet. I highly encourage you to use this package for exploratory analysis only.
If you ever decide to use the visualization in your publications, please consider changing
`autoplotly()` to `ggfortify::autoplot()` to get a better static plots or taking snapshots
of your `autoplotly` visualization.

We welcome suggestions and contributions from others. With this package, researchers will hopefully
spend less time focusing on learning `ggplot2` syntax or interactive visualization packages like `plotly`.
Instead they can spend more time on their work and research. The source code of the package is located on
 [Github](https://github.com/terrytangyuan/autoplotly) where users can test out development versions of
 the package and provide feature requests, feedback and bug reports. We encourage you to submit your
 issues and pull requests to help us make this package better for the R community.
 In the future, we'll try to support a much wider range of objects through a larger coverage in `ggfortify`.
 If you find any new use cases, please don't hesitate to submit an issue on Github and join us in the development!

## Additional Resources

* [autoplotly Github repository](https://github.com/terrytangyuan/autoplotly)
* [ggfortify Github repository](https://github.com/sinhrks/ggfortify)
* [ggfortify R Journal paper](https://journal.r-project.org/archive/2016-2/tang-horikoshi-li.pdf)
* [一行R代码实现繁琐的可视化](https://terrytangyuan.github.io/2015/11/24/ggfortify-intro/)


<!-- <script>

var src = new Array();
var list = document.getElementsByClassName("myIframe");
for (var i = 0; i < list.length; i++) {
    var url = list[i].getElementsByTagName("iframe")[0].getAttribute('src');
    src.push(url);
};
$(window).load(function() {
    for (var i = 0; i < src.length; i++) {
        var theIframe = $('.myIframe')[i].getElementsByTagName("iframe")[0]
        theIframe.setAttribute('onload', function() {
          setTimeout(function doSomething() {
              alert("it should have wait 10000 milliseconds, instead it triggers immediately");
          }, 10000)
          theIframe.setAttribute('src', src[i]);
        });
    };
});
</script> -->
