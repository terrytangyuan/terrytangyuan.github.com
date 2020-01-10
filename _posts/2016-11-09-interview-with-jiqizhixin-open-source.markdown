---
layout:     post
title:      "机器之心专访：关于开源，我们和谷歌开源奖获得者、DMLC成员唐源聊了聊"
subtitle:   "An Interview with Synced (www.jiqizhixin.com) on Open-source"
date:       2016-11-09
author:     "Synced"
tags:
    - Open Source
    - Interview
    - Deep Learning
    - Machine Learning
---

<select onchange= "onLanChange(this.options[this.options.selectedIndex].value)">
    <option value="0" selected> 中文 Chinese </option>
    <option value="1"> 英语 English </option>
</select>


<!-- Chinese Version -->
<div class="zh post-container">
	{% capture interview-with-jiqizhixin-open-source %}{% include posts/interview-with-jiqizhixin-open-source-chinese.md %}{% endcapture %}
	{{ interview-with-jiqizhixin-open-source | markdownify }}
</div>


<!-- English Version -->
<div class="en post-container">
	{% capture interview-with-jiqizhixin-open-source %}{% include posts/interview-with-jiqizhixin-open-source-english.md %}{% endcapture %}
	{{ interview-with-jiqizhixin-open-source | markdownify }}
</div>



<!-- Handle Language Change -->
<script type="text/javascript">
    // get nodes
    var $zh = document.querySelector(".zh");
    var $en = document.querySelector(".en");
    var $select = document.querySelector("select");
    // bind hashchange event
    window.addEventListener('hashchange', _render);
    // handle render
    function _render(){
        var _hash = window.location.hash;
        // en
        if(_hash == "#en"){
            $select.selectedIndex = 1;
            $en.style.display = "block";
            $zh.style.display = "none";
        // zh by default
        }else{
            // not trigger onChange, otherwise cause a loop call.
            $select.selectedIndex = 0;
            $zh.style.display = "block";
            $en.style.display = "none";
        }
    }
    // handle select change
    function onLanChange(index){
        if(index == 0){
            window.location.hash = "#zh"
        }else{
            window.location.hash = "#en"
        }
    }
    // init
    _render();
</script>