<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
<meta content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no" name="viewport"/>
<meta content="zh-cn" http-equiv="content-language"/>
<meta content="13 典型案例 3：十分钟搭建弹性可扩展的 Web API" name="description"/>
<link href="/static/favicon.png" rel="icon"/>
<title>13 典型案例 3：十分钟搭建弹性可扩展的 Web API </title>
<link href="/static/index.css" rel="stylesheet"/>
<link href="/static/highlight.min.css" rel="stylesheet"/>
<script src="/static/highlight.min.js"></script>
<meta content="Hexo 4.2.0" name="generator"/>

</head>
<body>
<div class="book-container">
<div class="book-sidebar">
<div class="book-brand">
<a href="/">
<img src="/static/favicon.png"/>
<span>技术文章摘抄</span>
</a>
</div>
<div class="book-menu uncollapsible">
<ul class="uncollapsible">
<li><a class="current-tab" href="/">首页</a></li>
<li><a href="../">上一级</a></li>
</ul>
<ul class="uncollapsible">
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/01%20%e6%9e%b6%e6%9e%84%e7%9a%84%e6%bc%94%e8%bf%9b.md" id="01 架构的演进.md">01 架构的演进.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/02%20Serverless%20%e7%9a%84%e4%bb%b7%e5%80%bc.md" id="02 Serverless 的价值.md">02 Serverless 的价值.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/03%20%e5%b8%b8%e8%a7%81%20Serverless%20%e6%9e%b6%e6%9e%84%e6%a8%a1%e5%bc%8f.md" id="03 常见 Serverless 架构模式.md">03 常见 Serverless 架构模式.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/04%20Serverless%20%e6%8a%80%e6%9c%af%e9%80%89%e5%9e%8b.md" id="04 Serverless 技术选型.md">04 Serverless 技术选型.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/05%20%e5%87%bd%e6%95%b0%e8%ae%a1%e7%ae%97%e7%ae%80%e4%bb%8b.md" id="05 函数计算简介.md">05 函数计算简介.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/06%20%e5%87%bd%e6%95%b0%e8%ae%a1%e7%ae%97%e6%98%af%e5%a6%82%e4%bd%95%e5%b7%a5%e4%bd%9c%e7%9a%84%ef%bc%9f.md" id="06 函数计算是如何工作的？.md">06 函数计算是如何工作的？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/07%20%e5%87%bd%e6%95%b0%e7%b2%98%e5%90%88%e4%ba%91%e6%9c%8d%e5%8a%a1%e6%8f%90%e4%be%9b%e7%ab%af%e5%88%b0%e7%ab%af%e8%a7%a3%e5%86%b3%e6%96%b9%e6%a1%88.md" id="07 函数粘合云服务提供端到端解决方案.md">07 函数粘合云服务提供端到端解决方案.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/08%20%e5%87%bd%e6%95%b0%e8%ae%a1%e7%ae%97%e7%9a%84%e5%bc%80%e5%8f%91%e4%b8%8e%e9%85%8d%e7%bd%ae.md" id="08 函数计算的开发与配置.md">08 函数计算的开发与配置.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/09%20%e5%87%bd%e6%95%b0%e7%9a%84%e8%b0%83%e8%af%95%e4%b8%8e%e9%83%a8%e7%bd%b2.md" id="09 函数的调试与部署.md">09 函数的调试与部署.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/10%20%e8%87%aa%e5%8a%a8%e5%8c%96%20CI&amp;CD%20%e4%b8%8e%e7%81%b0%e5%ba%a6%e5%8f%91%e5%b8%83.md" id="10 自动化 CI&amp;CD 与灰度发布.md">10 自动化 CI&amp;CD 与灰度发布.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/11%20%e5%87%bd%e6%95%b0%e8%ae%a1%e7%ae%97%e7%9a%84%e5%8f%af%e8%a7%82%e6%b5%8b%e6%80%a7.md" id="11 函数计算的可观测性.md">11 函数计算的可观测性.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/12%20%e5%85%b8%e5%9e%8b%e6%a1%88%e4%be%8b%201%ef%bc%9a%e5%87%bd%e6%95%b0%e8%ae%a1%e7%ae%97%e5%9c%a8%e9%9f%b3%e8%a7%86%e9%a2%91%e5%9c%ba%e6%99%af%e5%ae%9e%e8%b7%b5.md" id="12 典型案例 1：函数计算在音视频场景实践.md">12 典型案例 1：函数计算在音视频场景实践.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/13%20%e5%85%b8%e5%9e%8b%e6%a1%88%e4%be%8b%203%ef%bc%9a%e5%8d%81%e5%88%86%e9%92%9f%e6%90%ad%e5%bb%ba%e5%bc%b9%e6%80%a7%e5%8f%af%e6%89%a9%e5%b1%95%e7%9a%84%20Web%20API.md" id="13 典型案例 3：十分钟搭建弹性可扩展的 Web API.md">13 典型案例 3：十分钟搭建弹性可扩展的 Web API.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/14%20Serverless%20Kubernetes%20%e5%ae%b9%e5%99%a8%e6%9c%8d%e5%8a%a1%e4%bb%8b%e7%bb%8d.md" id="14 Serverless Kubernetes 容器服务介绍.md">14 Serverless Kubernetes 容器服务介绍.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/15%20Serverless%20Kubernetes%20%e5%ba%94%e7%94%a8%e9%83%a8%e7%bd%b2%e5%8f%8a%e6%89%a9%e7%bc%a9%e5%ae%b9.md" id="15 Serverless Kubernetes 应用部署及扩缩容.md">15 Serverless Kubernetes 应用部署及扩缩容.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/16%20%e4%bd%bf%e7%94%a8%20Spot%20%e4%bd%8e%e6%88%90%e6%9c%ac%e8%bf%90%e8%a1%8c%20Job%20%e4%bb%bb%e5%8a%a1.md" id="16 使用 Spot 低成本运行 Job 任务.md">16 使用 Spot 低成本运行 Job 任务.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/17%20%e4%bd%8e%e6%88%90%e6%9c%ac%e8%bf%90%e8%a1%8c%20Spark%20%e6%95%b0%e6%8d%ae%e8%ae%a1%e7%ae%97.md" id="17 低成本运行 Spark 数据计算.md">17 低成本运行 Spark 数据计算.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/18%20GPU%20%e6%9c%ba%e5%99%a8%e5%ad%a6%e4%b9%a0%e5%bc%80%e7%ae%b1%e5%8d%b3%e7%94%a8.md" id="18 GPU 机器学习开箱即用.md">18 GPU 机器学习开箱即用.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/19%20%e5%9f%ba%e4%ba%8e%20Knative%20%e4%bd%8e%e6%88%90%e6%9c%ac%e9%83%a8%e7%bd%b2%e5%9c%a8%e7%ba%bf%e5%ba%94%e7%94%a8%ef%bc%8c%e7%81%b5%e6%b4%bb%e8%87%aa%e5%8a%a8%e4%bc%b8%e7%bc%a9.md" id="19 基于 Knative 低成本部署在线应用，灵活自动伸缩.md">19 基于 Knative 低成本部署在线应用，灵活自动伸缩.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/20%20%e5%bf%ab%e9%80%9f%e6%9e%84%e5%bb%ba%20JenkinsGitlab%20%e6%8c%81%e7%bb%ad%e9%9b%86%e6%88%90%e7%8e%af%e5%a2%83.md" id="20 快速构建 JenkinsGitlab 持续集成环境.md">20 快速构建 JenkinsGitlab 持续集成环境.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/21%20%e5%9c%a8%e7%ba%bf%e5%ba%94%e7%94%a8%e7%9a%84%20Serverless%20%e5%ae%9e%e8%b7%b5.md" id="21 在线应用的 Serverless 实践.md">21 在线应用的 Serverless 实践.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/22%20%e9%80%9a%e8%bf%87%20IDEMaven%20%e9%83%a8%e7%bd%b2%20Serverless%20%e5%ba%94%e7%94%a8%e5%ae%9e%e8%b7%b5.md" id="22 通过 IDEMaven 部署 Serverless 应用实践.md">22 通过 IDEMaven 部署 Serverless 应用实践.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/23%20%e4%bc%81%e4%b8%9a%e7%ba%a7%20CICD%20%e5%b7%a5%e5%85%b7%e9%83%a8%e7%bd%b2%20Serverless%20%e5%ba%94%e7%94%a8%e7%9a%84%e8%90%bd%e5%9c%b0%e5%ae%9e%e8%b7%b5.md" id="23 企业级 CICD 工具部署 Serverless 应用的落地实践.md">23 企业级 CICD 工具部署 Serverless 应用的落地实践.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/24%20Serverless%20%e5%ba%94%e7%94%a8%e5%a6%82%e4%bd%95%e7%ae%a1%e7%90%86%e6%97%a5%e5%bf%97&amp;%e6%8c%81%e4%b9%85%e5%8c%96%e6%95%b0%e6%8d%ae.md" id="24 Serverless 应用如何管理日志&amp;持久化数据.md">24 Serverless 应用如何管理日志&amp;持久化数据.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/25%20Serverless%20%e5%ba%94%e7%94%a8%e5%bc%95%e6%93%8e%e4%ba%a7%e5%93%81%e7%9a%84%e6%b5%81%e9%87%8f%e8%b4%9f%e8%bd%bd%e5%9d%87%e8%a1%a1%e5%92%8c%e8%b7%af%e7%94%b1%e7%ad%96%e7%95%a5%e9%85%8d%e7%bd%ae%e5%ae%9e%e8%b7%b5.md" id="25 Serverless 应用引擎产品的流量负载均衡和路由策略配置实践.md">25 Serverless 应用引擎产品的流量负载均衡和路由策略配置实践.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/26%20Spring%20CloudDubbo%20%e5%ba%94%e7%94%a8%e6%97%a0%e7%bc%9d%e8%bf%81%e7%a7%bb%e5%88%b0%20Serverless%20%e6%9e%b6%e6%9e%84.md" id="26 Spring CloudDubbo 应用无缝迁移到 Serverless 架构.md">26 Spring CloudDubbo 应用无缝迁移到 Serverless 架构.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/27%20SAE%20%e5%ba%94%e7%94%a8%e5%88%86%e6%89%b9%e5%8f%91%e5%b8%83%e4%b8%8e%e6%97%a0%e6%8d%9f%e4%b8%8b%e7%ba%bf%e7%9a%84%e6%9c%80%e4%bd%b3%e5%ae%9e%e8%b7%b5.md" id="27 SAE 应用分批发布与无损下线的最佳实践.md">27 SAE 应用分批发布与无损下线的最佳实践.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/28%20%e5%a6%82%e4%bd%95%e9%80%9a%e8%bf%87%e5%8e%8b%e6%b5%8b%e5%b7%a5%e5%85%b7+%20SAE%20%e5%bc%b9%e6%80%a7%e8%83%bd%e5%8a%9b%e8%bd%bb%e6%9d%be%e5%ba%94%e5%af%b9%e5%a4%a7%e4%bf%83.md" id="28 如何通过压测工具+ SAE 弹性能力轻松应对大促.md">28 如何通过压测工具+ SAE 弹性能力轻松应对大促.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Serverless%20%e6%8a%80%e6%9c%af%e5%85%ac%e5%bc%80%e8%af%be%ef%bc%88%e5%ae%8c%ef%bc%89/29%20SAE%20%e6%9e%81%e8%87%b4%e5%ba%94%e7%94%a8%e9%83%a8%e7%bd%b2%e6%95%88%e7%8e%87.md" id="29 SAE 极致应用部署效率.md">29 SAE 极致应用部署效率.md</a>
</li>
<li><a href="/assets/捐赠.md">捐赠</a></li>
</ul>
</div>
</div>
<div class="sidebar-toggle" onclick="sidebar_toggle()" onmouseleave="remove_inner()" onmouseover="add_inner()">
<div class="sidebar-toggle-inner"></div>
</div>
<div class="off-canvas-content">
<div class="columns">
<div class="column col-12 col-lg-12">
<div class="book-navbar">
<header class="navbar">
<section class="navbar-section">
<a onclick="open_sidebar()">
<i class="icon icon-menu"></i>
</a>
</section>
</header>
</div>
<div class="book-content" style="max-width: 960px; margin: 0 auto;
    overflow-x: auto;
    overflow-y: hidden;">
<div class="book-post">

<p align="center" id="tip"></p>
<h1 class="title" data-id="13 典型案例 3：十分钟搭建弹性可扩展的 Web API" id="title">13 典型案例 3：十分钟搭建弹性可扩展的 Web API</h1>
<div><h3 id="基本概念">基本概念</h3>
<p><img alt="幻灯片 3.PNG" src="assets/2020-09-21-060728.png"/></p>
<p>常见的 WebAPI 架构如上图所示，主要包括客户端（浏览器）、服务器、数据库，WebAPI 由服务器提供，同时服务器要完成负载均衡、登录鉴权的相关操作。</p>
<p>当客户端流量快速增大时，服务器端只能通过水平扩展加机器的方式来增加提高服务能力。</p>
<p>这种常规模式主要有两点局限性：</p>
<ul>
<li>技术同学除了开发业务代码，有大量的服务器运维成本，来保证服务的稳定性、可用性，技术同学要花费很多时间进行运维工作，占用开发时间，降低项目研发效率。</li>
<li>流量突然增加时，需要水平扩展加机器，弹性的响应能力差，扩容速度往往要数十分钟，无法实现秒级极速扩容，导致一段时间内的服务能力不足。同时当流量变少时，难以做到及时缩容，造成机器的成本浪费。</li>
</ul>
<p><img alt="幻灯片 4.PNG" src="assets/2020-09-21-060730.png"/></p>
<p>基于函数计算的 WebAPI 架构如上图所示，与常规的 WebAPI 架构相比，客户端和数据库未发生变化，但服务器变化巨大，主要体现在：</p>
<ul>
<li>之前需要开发团队维护的路由模块以及鉴权模块都将接入服务商提供的 API 网关系统以及鉴权系统，开发团队无须再维护这两部分的业务代码，只需要持续维护相关规则即可。</li>
<li>在这个结构下，业务代码也被拆分成了函数粒度，不同函数表示不同的功能。</li>
<li>我们已经看不到服务器的存在，是因为 Serverless 的目的是让使用者只关注自己的业务逻辑即可，所以一部分安全问题、资源调度问题（例如用户量暴增、如何实现自动扩容等）全都交给云厂商负责。</li>
<li>相对于传统项目而言，传统项目无论是否有用户访问，服务都在运行中，都是有成本支出，而 Serverless 而言，只有在用去发起请求时，函数才会被激活并执行，且会按量收费，可以实现在有流量的时候才有支持，没有流量的时候就没有支出，相对来说，成本会进一步降低。</li>
</ul>
<h3 id="开发流程">开发流程</h3>
<h4 id="1-登录函数计算控制台-创建应用">1. 登录函数计算控制台，创建应用</h4>
<p><img alt="3.png" src="assets/2020-09-21-60731.png"/></p>
<p>可以通过两种方式来创建应用，如果是已有的 Web 项目，可以选择上图中的第一种方式：“常见 Web 应用”；对于新项目则推荐使用第二种方式：“基于模板创建应用”。我们这里使用模板方式，选择基于 Python 的 Web 应用。</p>
<p>模板可以当做应用脚手架，选择适合的模板，可以自动完成相关依赖资源的创建，如角色、OSS、域名网关等，降低开发成本。</p>
<h4 id="2-新建函数">2. 新建函数</h4>
<p><img alt="4.png" src="assets/2020-09-21-060733.png"/></p>
<p>在应用下，创建函数，我们是开发 WebAPI，所以选择“HTTP”函数，这种函数会将指定的 http 请求作为触发器，来调度对应函数的执行。</p>
<p>函数新建好之后，是个返回 helloWorld 的 demo，我们在此基础上来开发我们的业务逻辑。</p>
<p><img alt="image.png" src="assets/2020-09-21-060734.png"/></p>
<p>首先介绍下上图代码中的 handler 函数，这个函数是入口函数，http 触发器接收到调用后会通过这个入口来启动整个函数。函数有两个入参，environ 和 start_response：</p>
<ul>
<li>environ</li>
</ul>
<p>environ 中主要包含两部分内容：http 请求的入参和函数执行上下文 fcContext，函数上下文参数中包含一些函数运行时的信息（例如 request id 、 临时 AK ），您在代码中可以使用这些信息。信息类型是 FCContext。</p>
<ul>
<li>start_response</li>
</ul>
<p>该参数主要用于生成 http 请求的 response。</p>
<h4 id="3-配置触发器-绑定域名">3. 配置触发器，绑定域名</h4>
<p><img alt="image.png" src="assets/2020-09-21-060736.png"/></p>
<p>在新建函数时会自动创建一个 http 触发器，这个触发器的路径是“aliyun.com”的一个测试路径，只能用于测试，真实的应用需要通过自定义域名将真实域名与函数绑定，这样访问指定域名时，对应函数就会被触发执行。</p>
<h4 id="4-日志与监控">4. 日志与监控</h4>
<p>在每个函数编辑页面，日志和监控服务，函数的每次执行都会生成唯一的 requestId，日志中通过 requestId 进行查询，看到本次函数执行的所有日志。</p>
<p><img alt="image.png" src="assets/2020-09-21-060739.png"/></p>
<h3 id="操作演示">操作演示</h3>
<p>点击链接即可观看演示视频：<a href="https://developer.aliyun.com/lesson_2024_18999" target="_blank">https://developer.aliyun.com/lesson*2024*18999</a></p>
</div>
</div>
<div>
<div id="prePage" style="float: left">
</div>
<div id="nextPage" style="float: right">
</div>
</div>
</div>
</div>
</div>
<div class="copyright">
<hr/>
<p>© 2019 - 2023 <a href="/cdn-cgi/l/email-protection#b9d5d5d5808d8888898ef9ded4d8d0d597dad6d4" target="_blank">Liangliang Lee</a>.
                    Powered by <a href="https://github.com/gin-gonic/gin" target="_blank">gin</a> and <a href="https://github.com/kaiiiz/hexo-theme-book" target="_blank">hexo-theme-book</a>.</p>
</div>
</div>
<a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script>(function(){function c(){var b=a.contentDocument||a.contentWindow.document;if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'8f0baa09eea68515',t:'MTczMzk4NTAxMC4wMDAwMDA='};var a=document.createElement('script');a.nonce='';a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();</script></body>

<script src="/static/index.js"></script>
</head></html>