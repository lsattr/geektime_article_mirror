<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
<meta content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no" name="viewport"/>
<meta content="zh-cn" http-equiv="content-language"/>
<meta content="04 ZooKeeper 如何保证数据一致性？" name="description"/>
<link href="/static/favicon.png" rel="icon"/>
<title>04 ZooKeeper 如何保证数据一致性？ </title>
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
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/00%20%e5%bc%80%e7%af%87%e8%af%8d%ef%bc%9a%e6%90%ad%e5%bb%ba%e5%88%86%e5%b8%83%e5%bc%8f%e7%9f%a5%e8%af%86%e4%bd%93%e7%b3%bb%ef%bc%8c%e6%8c%91%e6%88%98%e9%ab%98%e8%96%aa%20Offer.md" id="00 开篇词：搭建分布式知识体系，挑战高薪 Offer.md">00 开篇词：搭建分布式知识体系，挑战高薪 Offer.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/01%20%e5%a6%82%e4%bd%95%e8%af%81%e6%98%8e%e5%88%86%e5%b8%83%e5%bc%8f%e7%b3%bb%e7%bb%9f%e7%9a%84%20CAP%20%e7%90%86%e8%ae%ba%ef%bc%9f.md" id="01 如何证明分布式系统的 CAP 理论？.md">01 如何证明分布式系统的 CAP 理论？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/02%20%e4%b8%8d%e5%90%8c%e6%95%b0%e6%8d%ae%e4%b8%80%e8%87%b4%e6%80%a7%e6%a8%a1%e5%9e%8b%e6%9c%89%e5%93%aa%e4%ba%9b%e5%ba%94%e7%94%a8%ef%bc%9f.md" id="02 不同数据一致性模型有哪些应用？.md">02 不同数据一致性模型有哪些应用？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/03%20%e5%a6%82%e4%bd%95%e9%80%8f%e5%bd%bb%e7%90%86%e8%a7%a3%20Paxos%20%e7%ae%97%e6%b3%95%ef%bc%9f.md" id="03 如何透彻理解 Paxos 算法？.md">03 如何透彻理解 Paxos 算法？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/04%20ZooKeeper%20%e5%a6%82%e4%bd%95%e4%bf%9d%e8%af%81%e6%95%b0%e6%8d%ae%e4%b8%80%e8%87%b4%e6%80%a7%ef%bc%9f.md" id="04 ZooKeeper 如何保证数据一致性？.md">04 ZooKeeper 如何保证数据一致性？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/05%20%e5%85%b1%e8%af%86%e9%97%ae%e9%a2%98%ef%bc%9a%e5%8c%ba%e5%9d%97%e9%93%be%e5%a6%82%e4%bd%95%e7%a1%ae%e8%ae%a4%e8%ae%b0%e8%b4%a6%e6%9d%83%ef%bc%9f.md" id="05 共识问题：区块链如何确认记账权？.md">05 共识问题：区块链如何确认记账权？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/06%20%e5%a6%82%e4%bd%95%e5%87%86%e5%a4%87%e4%b8%80%e7%ba%bf%e4%ba%92%e8%81%94%e7%bd%91%e5%85%ac%e5%8f%b8%e9%9d%a2%e8%af%95%ef%bc%9f.md" id="06 如何准备一线互联网公司面试？.md">06 如何准备一线互联网公司面试？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/07%20%e5%88%86%e5%b8%83%e5%bc%8f%e4%ba%8b%e5%8a%a1%e6%9c%89%e5%93%aa%e4%ba%9b%e8%a7%a3%e5%86%b3%e6%96%b9%e6%a1%88%ef%bc%9f.md" id="07 分布式事务有哪些解决方案？.md">07 分布式事务有哪些解决方案？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/08%20%e5%af%b9%e6%af%94%e4%b8%a4%e9%98%b6%e6%ae%b5%e6%8f%90%e4%ba%a4%ef%bc%8c%e4%b8%89%e9%98%b6%e6%ae%b5%e5%8d%8f%e8%ae%ae%e6%9c%89%e5%93%aa%e4%ba%9b%e6%94%b9%e8%bf%9b%ef%bc%9f.md" id="08 对比两阶段提交，三阶段协议有哪些改进？.md">08 对比两阶段提交，三阶段协议有哪些改进？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/09%20MySQL%20%e6%95%b0%e6%8d%ae%e5%ba%93%e5%a6%82%e4%bd%95%e5%ae%9e%e7%8e%b0%20XA%20%e8%a7%84%e8%8c%83%ef%bc%9f.md" id="09 MySQL 数据库如何实现 XA 规范？.md">09 MySQL 数据库如何实现 XA 规范？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/10%20%e5%a6%82%e4%bd%95%e5%9c%a8%e4%b8%9a%e5%8a%a1%e4%b8%ad%e4%bd%93%e7%8e%b0%20TCC%20%e4%ba%8b%e5%8a%a1%e6%a8%a1%e5%9e%8b%ef%bc%9f.md" id="10 如何在业务中体现 TCC 事务模型？.md">10 如何在业务中体现 TCC 事务模型？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/11%20%e5%88%86%e5%b8%83%e5%bc%8f%e9%94%81%e6%9c%89%e5%93%aa%e4%ba%9b%e5%ba%94%e7%94%a8%e5%9c%ba%e6%99%af%e5%92%8c%e5%ae%9e%e7%8e%b0%ef%bc%9f.md" id="11 分布式锁有哪些应用场景和实现？.md">11 分布式锁有哪些应用场景和实现？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/12%20%e5%a6%82%e4%bd%95%e4%bd%bf%e7%94%a8%20Redis%20%e5%bf%ab%e9%80%9f%e5%ae%9e%e7%8e%b0%e5%88%86%e5%b8%83%e5%bc%8f%e9%94%81%ef%bc%9f.md" id="12 如何使用 Redis 快速实现分布式锁？.md">12 如何使用 Redis 快速实现分布式锁？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/13%20%e5%88%86%e5%b8%83%e5%bc%8f%e4%ba%8b%e5%8a%a1%e8%80%83%e7%82%b9%e6%a2%b3%e7%90%86%20+%20%e9%ab%98%e9%a2%91%e9%9d%a2%e8%af%95%e9%a2%98.md" id="13 分布式事务考点梳理 + 高频面试题.md">13 分布式事务考点梳理 + 高频面试题.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/14%20%e5%a6%82%e4%bd%95%e7%90%86%e8%a7%a3%20RPC%20%e8%bf%9c%e7%a8%8b%e6%9c%8d%e5%8a%a1%e8%b0%83%e7%94%a8%ef%bc%9f.md" id="14 如何理解 RPC 远程服务调用？.md">14 如何理解 RPC 远程服务调用？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/15%20%e4%b8%ba%e4%bb%80%e4%b9%88%e5%be%ae%e6%9c%8d%e5%8a%a1%e9%9c%80%e8%a6%81%20API%20%e7%bd%91%e5%85%b3%ef%bc%9f.md" id="15 为什么微服务需要 API 网关？.md">15 为什么微服务需要 API 网关？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/16%20%e5%a6%82%e4%bd%95%e5%ae%9e%e7%8e%b0%e6%9c%8d%e5%8a%a1%e6%b3%a8%e5%86%8c%e4%b8%8e%e5%8f%91%e7%8e%b0%ef%bc%9f.md" id="16 如何实现服务注册与发现？.md">16 如何实现服务注册与发现？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/17%20%e5%a6%82%e4%bd%95%e5%ae%9e%e7%8e%b0%e5%88%86%e5%b8%83%e5%bc%8f%e8%b0%83%e7%94%a8%e8%b7%9f%e8%b8%aa%ef%bc%9f.md" id="17 如何实现分布式调用跟踪？.md">17 如何实现分布式调用跟踪？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/18%20%e5%88%86%e5%b8%83%e5%bc%8f%e4%b8%8b%e5%a6%82%e4%bd%95%e5%ae%9e%e7%8e%b0%e9%85%8d%e7%bd%ae%e7%ae%a1%e7%90%86%ef%bc%9f.md" id="18 分布式下如何实现配置管理？.md">18 分布式下如何实现配置管理？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/19%20%e5%ae%b9%e5%99%a8%e5%8c%96%e5%8d%87%e7%ba%a7%e5%af%b9%e6%9c%8d%e5%8a%a1%e6%9c%89%e5%93%aa%e4%ba%9b%e5%bd%b1%e5%93%8d%ef%bc%9f.md" id="19 容器化升级对服务有哪些影响？.md">19 容器化升级对服务有哪些影响？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/20%20ServiceMesh%ef%bc%9a%e6%9c%8d%e5%8a%a1%e7%bd%91%e6%a0%bc%e6%9c%89%e5%93%aa%e4%ba%9b%e5%ba%94%e7%94%a8%ef%bc%9f.md" id="20 ServiceMesh：服务网格有哪些应用？.md">20 ServiceMesh：服务网格有哪些应用？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/21%20Dubbo%20vs%20Spring%20Cloud%ef%bc%9a%e4%b8%a4%e5%a4%a7%e6%8a%80%e6%9c%af%e6%a0%88%e5%a6%82%e4%bd%95%e9%80%89%e5%9e%8b%ef%bc%9f.md" id="21 Dubbo vs Spring Cloud：两大技术栈如何选型？.md">21 Dubbo vs Spring Cloud：两大技术栈如何选型？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/22%20%e5%88%86%e5%b8%83%e5%bc%8f%e6%9c%8d%e5%8a%a1%e8%80%83%e7%82%b9%e6%a2%b3%e7%90%86%20+%20%e9%ab%98%e9%a2%91%e9%9d%a2%e8%af%95%e9%a2%98.md" id="22 分布式服务考点梳理 + 高频面试题.md">22 分布式服务考点梳理 + 高频面试题.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/23%20%e8%af%bb%e5%86%99%e5%88%86%e7%a6%bb%e5%a6%82%e4%bd%95%e5%9c%a8%e4%b8%9a%e5%8a%a1%e4%b8%ad%e8%90%bd%e5%9c%b0%ef%bc%9f.md" id="23 读写分离如何在业务中落地？.md">23 读写分离如何在业务中落地？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/24%20%e4%b8%ba%e4%bb%80%e4%b9%88%e9%9c%80%e8%a6%81%e5%88%86%e5%ba%93%e5%88%86%e8%a1%a8%ef%bc%8c%e5%a6%82%e4%bd%95%e5%ae%9e%e7%8e%b0%ef%bc%9f.md" id="24 为什么需要分库分表，如何实现？.md">24 为什么需要分库分表，如何实现？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/25%20%e5%ad%98%e5%82%a8%e6%8b%86%e5%88%86%e5%90%8e%ef%bc%8c%e5%a6%82%e4%bd%95%e8%a7%a3%e5%86%b3%e5%94%af%e4%b8%80%e4%b8%bb%e9%94%ae%e9%97%ae%e9%a2%98%ef%bc%9f.md" id="25 存储拆分后，如何解决唯一主键问题？.md">25 存储拆分后，如何解决唯一主键问题？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/26%20%e5%88%86%e5%ba%93%e5%88%86%e8%a1%a8%e4%bb%a5%e5%90%8e%ef%bc%8c%e5%a6%82%e4%bd%95%e5%ae%9e%e7%8e%b0%e6%89%a9%e5%ae%b9%ef%bc%9f.md" id="26 分库分表以后，如何实现扩容？.md">26 分库分表以后，如何实现扩容？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/27%20NoSQL%20%e6%95%b0%e6%8d%ae%e5%ba%93%e6%9c%89%e5%93%aa%e4%ba%9b%e5%85%b8%e5%9e%8b%e5%ba%94%e7%94%a8%ef%bc%9f.md" id="27 NoSQL 数据库有哪些典型应用？.md">27 NoSQL 数据库有哪些典型应用？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/28%20ElasticSearch%20%e6%98%af%e5%a6%82%e4%bd%95%e5%bb%ba%e7%ab%8b%e7%b4%a2%e5%bc%95%e7%9a%84%ef%bc%9f.md" id="28 ElasticSearch 是如何建立索引的？.md">28 ElasticSearch 是如何建立索引的？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/29%20%e5%88%86%e5%b8%83%e5%bc%8f%e5%ad%98%e5%82%a8%e8%80%83%e7%82%b9%e6%a2%b3%e7%90%86%20+%20%e9%ab%98%e9%a2%91%e9%9d%a2%e8%af%95%e9%a2%98.md" id="29 分布式存储考点梳理 + 高频面试题.md">29 分布式存储考点梳理 + 高频面试题.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/30%20%e6%b6%88%e6%81%af%e9%98%9f%e5%88%97%e6%9c%89%e5%93%aa%e4%ba%9b%e5%ba%94%e7%94%a8%e5%9c%ba%e6%99%af%ef%bc%9f.md" id="30 消息队列有哪些应用场景？.md">30 消息队列有哪些应用场景？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/31%20%e9%9b%86%e7%be%a4%e6%b6%88%e8%b4%b9%e5%92%8c%e5%b9%bf%e6%92%ad%e6%b6%88%e8%b4%b9%e6%9c%89%e4%bb%80%e4%b9%88%e5%8c%ba%e5%88%ab%ef%bc%9f.md" id="31 集群消费和广播消费有什么区别？.md">31 集群消费和广播消费有什么区别？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/32%20%e4%b8%9a%e5%8a%a1%e4%b8%8a%e9%9c%80%e8%a6%81%e9%a1%ba%e5%ba%8f%e6%b6%88%e8%b4%b9%ef%bc%8c%e6%80%8e%e4%b9%88%e4%bf%9d%e8%af%81%e6%97%b6%e5%ba%8f%e6%80%a7%ef%bc%9f.md" id="32 业务上需要顺序消费，怎么保证时序性？.md">32 业务上需要顺序消费，怎么保证时序性？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/33%20%e6%b6%88%e6%81%af%e5%b9%82%e7%ad%89%ef%bc%9a%e5%a6%82%e4%bd%95%e4%bf%9d%e8%af%81%e6%b6%88%e6%81%af%e4%b8%8d%e8%a2%ab%e9%87%8d%e5%a4%8d%e6%b6%88%e8%b4%b9%ef%bc%9f.md" id="33 消息幂等：如何保证消息不被重复消费？.md">33 消息幂等：如何保证消息不被重复消费？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/34%20%e9%ab%98%e5%8f%af%e7%94%a8%ef%bc%9a%e5%a6%82%e4%bd%95%e5%ae%9e%e7%8e%b0%e6%b6%88%e6%81%af%e9%98%9f%e5%88%97%e7%9a%84%20HA%ef%bc%9f.md" id="34 高可用：如何实现消息队列的 HA？.md">34 高可用：如何实现消息队列的 HA？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/35%20%e6%b6%88%e6%81%af%e9%98%9f%e5%88%97%e9%80%89%e5%9e%8b%ef%bc%9aKafka%20%e5%a6%82%e4%bd%95%e5%ae%9e%e7%8e%b0%e9%ab%98%e6%80%a7%e8%83%bd%ef%bc%9f.md" id="35 消息队列选型：Kafka 如何实现高性能？.md">35 消息队列选型：Kafka 如何实现高性能？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/36%20%e6%b6%88%e6%81%af%e9%98%9f%e5%88%97%e9%80%89%e5%9e%8b%ef%bc%9aRocketMQ%20%e9%80%82%e7%94%a8%e5%93%aa%e4%ba%9b%e5%9c%ba%e6%99%af%ef%bc%9f.md" id="36 消息队列选型：RocketMQ 适用哪些场景？.md">36 消息队列选型：RocketMQ 适用哪些场景？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/37%20%e6%b6%88%e6%81%af%e9%98%9f%e5%88%97%e8%80%83%e7%82%b9%e6%a2%b3%e7%90%86%20+%20%e9%ab%98%e9%a2%91%e9%9d%a2%e8%af%95%e9%a2%98.md" id="37 消息队列考点梳理 + 高频面试题.md">37 消息队列考点梳理 + 高频面试题.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/38%20%e4%b8%8d%e6%ad%a2%e4%b8%9a%e5%8a%a1%e7%bc%93%e5%ad%98%ef%bc%8c%e5%88%86%e5%b8%83%e5%bc%8f%e7%b3%bb%e7%bb%9f%e4%b8%ad%e8%bf%98%e6%9c%89%e5%93%aa%e4%ba%9b%e7%bc%93%e5%ad%98%ef%bc%9f.md" id="38 不止业务缓存，分布式系统中还有哪些缓存？.md">38 不止业务缓存，分布式系统中还有哪些缓存？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/39%20%e5%a6%82%e4%bd%95%e9%81%bf%e5%85%8d%e7%bc%93%e5%ad%98%e7%a9%bf%e9%80%8f%e3%80%81%e7%bc%93%e5%ad%98%e5%87%bb%e7%a9%bf%e3%80%81%e7%bc%93%e5%ad%98%e9%9b%aa%e5%b4%a9%ef%bc%9f.md" id="39 如何避免缓存穿透、缓存击穿、缓存雪崩？.md">39 如何避免缓存穿透、缓存击穿、缓存雪崩？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/40%20%e7%bb%8f%e5%85%b8%e9%97%ae%e9%a2%98%ef%bc%9a%e5%85%88%e6%9b%b4%e6%96%b0%e6%95%b0%e6%8d%ae%e5%ba%93%ef%bc%8c%e8%bf%98%e6%98%af%e5%85%88%e6%9b%b4%e6%96%b0%e7%bc%93%e5%ad%98%ef%bc%9f.md" id="40 经典问题：先更新数据库，还是先更新缓存？.md">40 经典问题：先更新数据库，还是先更新缓存？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/41%20%e5%a4%b1%e6%95%88%e7%ad%96%e7%95%a5%ef%bc%9a%e7%bc%93%e5%ad%98%e8%bf%87%e6%9c%9f%e9%83%bd%e6%9c%89%e5%93%aa%e4%ba%9b%e7%ad%96%e7%95%a5%ef%bc%9f.md" id="41 失效策略：缓存过期都有哪些策略？.md">41 失效策略：缓存过期都有哪些策略？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/42%20%e8%b4%9f%e8%bd%bd%e5%9d%87%e8%a1%a1%ef%bc%9a%e4%b8%80%e8%87%b4%e6%80%a7%e5%93%88%e5%b8%8c%e8%a7%a3%e5%86%b3%e4%ba%86%e5%93%aa%e4%ba%9b%e9%97%ae%e9%a2%98%ef%bc%9f.md" id="42 负载均衡：一致性哈希解决了哪些问题？.md">42 负载均衡：一致性哈希解决了哪些问题？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/43%20%e7%bc%93%e5%ad%98%e9%ab%98%e5%8f%af%e7%94%a8%ef%bc%9a%e7%bc%93%e5%ad%98%e5%a6%82%e4%bd%95%e4%bf%9d%e8%af%81%e9%ab%98%e5%8f%af%e7%94%a8%ef%bc%9f.md" id="43 缓存高可用：缓存如何保证高可用？.md">43 缓存高可用：缓存如何保证高可用？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/44%20%e5%88%86%e5%b8%83%e5%bc%8f%e7%bc%93%e5%ad%98%e8%80%83%e7%82%b9%e6%a2%b3%e7%90%86%20+%20%e9%ab%98%e9%a2%91%e9%9d%a2%e8%af%95%e9%a2%98.md" id="44 分布式缓存考点梳理 + 高频面试题.md">44 分布式缓存考点梳理 + 高频面试题.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/45%20%e4%bb%8e%e5%8f%8c%e5%8d%81%e4%b8%80%e7%9c%8b%e9%ab%98%e5%8f%af%e7%94%a8%e7%9a%84%e4%bf%9d%e9%9a%9c%e6%96%b9%e5%bc%8f.md" id="45 从双十一看高可用的保障方式.md">45 从双十一看高可用的保障方式.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/46%20%e9%ab%98%e5%b9%b6%e5%8f%91%e5%9c%ba%e6%99%af%e4%b8%8b%e5%a6%82%e4%bd%95%e5%ae%9e%e7%8e%b0%e7%b3%bb%e7%bb%9f%e9%99%90%e6%b5%81%ef%bc%9f.md" id="46 高并发场景下如何实现系统限流？.md">46 高并发场景下如何实现系统限流？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/47%20%e9%99%8d%e7%ba%a7%e5%92%8c%e7%86%94%e6%96%ad%ef%bc%9a%e5%a6%82%e4%bd%95%e5%a2%9e%e5%bc%ba%e6%9c%8d%e5%8a%a1%e7%a8%b3%e5%ae%9a%e6%80%a7%ef%bc%9f.md" id="47 降级和熔断：如何增强服务稳定性？.md">47 降级和熔断：如何增强服务稳定性？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/48%20%e5%a6%82%e4%bd%95%e9%80%89%e6%8b%a9%e9%80%82%e5%90%88%e4%b8%9a%e5%8a%a1%e7%9a%84%e8%b4%9f%e8%bd%bd%e5%9d%87%e8%a1%a1%e7%ad%96%e7%95%a5%ef%bc%9f.md" id="48 如何选择适合业务的负载均衡策略？.md">48 如何选择适合业务的负载均衡策略？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/49%20%e7%ba%bf%e4%b8%8a%e6%9c%8d%e5%8a%a1%e6%9c%89%e5%93%aa%e4%ba%9b%e7%a8%b3%e5%ae%9a%e6%80%a7%e6%8c%87%e6%a0%87%ef%bc%9f.md" id="49 线上服务有哪些稳定性指标？.md">49 线上服务有哪些稳定性指标？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/50%20%e5%88%86%e5%b8%83%e5%bc%8f%e4%b8%8b%e6%9c%89%e5%93%aa%e4%ba%9b%e5%a5%bd%e7%94%a8%e7%9a%84%e7%9b%91%e6%8e%a7%e7%bb%84%e4%bb%b6%ef%bc%9f.md" id="50 分布式下有哪些好用的监控组件？.md">50 分布式下有哪些好用的监控组件？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/51%20%e5%88%86%e5%b8%83%e5%bc%8f%e4%b8%8b%e5%a6%82%e4%bd%95%e5%ae%9e%e7%8e%b0%e7%bb%9f%e4%b8%80%e6%97%a5%e5%bf%97%e7%b3%bb%e7%bb%9f%ef%bc%9f.md" id="51 分布式下如何实现统一日志系统？.md">51 分布式下如何实现统一日志系统？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e5%88%86%e5%b8%83%e5%bc%8f%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e4%b8%8e%e5%ae%9e%e6%88%9845%e8%ae%b2-%e5%ae%8c/52%20%e5%88%86%e5%b8%83%e5%bc%8f%e8%b7%af%e6%bc%ab%e6%bc%ab%ef%bc%8c%e5%8e%9a%e7%a7%af%e8%96%84%e5%8f%91%e6%89%8d%e6%98%af%e7%8e%8b%e9%81%93.md" id="52 分布式路漫漫，厚积薄发才是王道.md">52 分布式路漫漫，厚积薄发才是王道.md</a>
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
<h1 class="title" data-id="04 ZooKeeper 如何保证数据一致性？" id="title">04 ZooKeeper 如何保证数据一致性？</h1>
<div><p>在分布式场景中，ZooKeeper 的应用非常广泛，比如数据发布和订阅、命名服务、配置中心、注册中心、分布式锁等。</p>
<p>ZooKeeper 提供了一个类似于 Linux 文件系统的数据模型，和基于 Watcher 机制的分布式事件通知，这些特性都依赖 ZooKeeper 的高容错数据一致性协议。</p>
<p>那么问题来了，在分布式场景下，ZooKeeper 是如何实现数据一致性的呢？</p>
<h2 id="zab-一致性协议">Zab 一致性协议</h2>
<p>ZooKeeper 是通过 Zab 协议来保证分布式事务的最终一致性。Zab（ZooKeeper Atomic Broadcast，ZooKeeper 原子广播协议）支持崩溃恢复，基于该协议，ZooKeeper 实现了一种主备模式的系统架构来保持集群中各个副本之间数据一致性。</p>
<p>系统架构可以参考下面这张图：</p>
<p><img alt="img" src="assets/Ciqah16O5QyAB4rJAAEiJ-4T3bE046.png"/></p>
<p>在 ZooKeeper 集群中，所有客户端的请求都是写入到 Leader 进程中的，然后，由 Leader 同步到其他节点，称为 Follower。在集群数据同步的过程中，如果出现 Follower 节点崩溃或者 Leader 进程崩溃时，都会通过 Zab 协议来保证数据一致性。</p>
<p>Zab 协议的具体实现可以分为以下两部分：</p>
<ul>
<li>消息广播阶段</li>
</ul>
<p>Leader 节点接受事务提交，并且将新的 Proposal 请求广播给 Follower 节点，收集各个节点的反馈，决定是否进行 Commit，在这个过程中，也会使用上一课时提到的 Quorum 选举机制。</p>
<ul>
<li>崩溃恢复阶段</li>
</ul>
<p>如果在同步过程中出现 Leader 节点宕机，会进入崩溃恢复阶段，重新进行 Leader 选举，崩溃恢复阶段还包含数据同步操作，同步集群中最新的数据，保持集群的数据一致性。</p>
<p>整个 ZooKeeper 集群的一致性保证就是在上面两个状态之前切换，当 Leader 服务正常时，就是正常的消息广播模式；当 Leader 不可用时，则进入崩溃恢复模式，崩溃恢复阶段会进行数据同步，完成以后，重新进入消息广播阶段。</p>
<h2 id="zab-协议中的-zxid">Zab 协议中的 Zxid</h2>
<p>Zxid 在 ZooKeeper 的一致性流程中非常重要，在详细分析 Zab 协议之前，先来看下 Zxid 的概念。</p>
<p>Zxid 是 Zab 协议的一个事务编号，Zxid 是一个 64 位的数字，其中低 32 位是一个简单的单调递增计数器，针对客户端每一个事务请求，计数器加 1；而高 32 位则代表 Leader 周期年代的编号。</p>
<p>这里 Leader 周期的英文是 epoch，可以理解为当前集群所处的年代或者周期，对比另外一个一致性算法 Raft 中的 Term 概念。在 Raft 中，每一个任期的开始都是一次选举，Raft 算法保证在给定的一个任期最多只有一个领导人。</p>
<p><img alt="img" src="assets/Cgq2xl6O5QyAeZqMAAB5C-BWbeI425.png"/></p>
<p>Zab 协议的实现也类似，每当有一个新的 Leader 选举出现时，就会从这个 Leader 服务器上取出其本地日志中最大事务的 Zxid，并从中读取 epoch 值，然后加 1，以此作为新的周期 ID。总结一下，高 32 位代表了每代 Leader 的唯一性，低 32 位则代表了每代 Leader 中事务的唯一性。</p>
<h2 id="zab-流程分析">Zab 流程分析</h2>
<p>Zab 的具体流程可以拆分为消息广播、崩溃恢复和数据同步三个过程，下面我们分别进行分析。</p>
<p><img alt="img" src="assets/Ciqah16O5QyADv0LAAA84x9hlQc078.png"/></p>
<h3 id="消息广播">消息广播</h3>
<p>在 ZooKeeper 中所有的事务请求都由 Leader 节点来处理，其他服务器为 Follower，Leader 将客户端的事务请求转换为事务 Proposal，并且将 Proposal 分发给集群中其他所有的 Follower。</p>
<p>完成广播之后，Leader 等待 Follwer 反馈，当有过半数的 Follower 反馈信息后，Leader 将再次向集群内 Follower 广播 Commit 信息，Commit 信息就是确认将之前的 Proposal 提交。</p>
<p>这里的 Commit 可以对比 SQL 中的 COMMIT 操作来理解，MySQL 默认操作模式是 autocommit 自动提交模式，如果你显式地开始一个事务，在每次变更之后都要通过 COMMIT 语句来确认，将更改提交到数据库中。</p>
<p>Leader 节点的写入也是一个两步操作，第一步是广播事务操作，第二步是广播提交操作，其中过半数指的是反馈的节点数 &gt;=N/2+1，N 是全部的 Follower 节点数量。</p>
<p>消息广播的过程描述可以参考下图：</p>
<p><img alt="img" src="assets/Cgq2xl6O5Q2ASjMpAAHdAdF67vE736.png"/></p>
<ul>
<li>客户端的写请求进来之后，Leader 会将写请求包装成 Proposal 事务，并添加一个递增事务 ID，也就是 Zxid，Zxid 是单调递增的，以保证每个消息的先后顺序；</li>
<li>广播这个 Proposal 事务，Leader 节点和 Follower 节点是解耦的，通信都会经过一个先进先出的消息队列，Leader 会为每一个 Follower 服务器分配一个单独的 FIFO 队列，然后把 Proposal 放到队列中；</li>
<li>Follower 节点收到对应的 Proposal 之后会把它持久到磁盘上，当完全写入之后，发一个 ACK 给 Leader；</li>
<li>当 Leader 收到超过半数 Follower 机器的 ack 之后，会提交本地机器上的事务，同时开始广播 commit， Follower 收到 commit 之后，完成各自的事务提交。</li>
</ul>
<p>分析完消息广播，我们再来看一下崩溃恢复。</p>
<h3 id="崩溃恢复">崩溃恢复</h3>
<p>消息广播通过 Quorum 机制，解决了 Follower 节点宕机的情况，但是如果在广播过程中 Leader 节点崩溃呢？</p>
<p>这就需要 Zab 协议支持的崩溃恢复，崩溃恢复可以保证在 Leader 进程崩溃的时候可以重新选出 Leader，并且保证数据的完整性。</p>
<p>崩溃恢复和集群启动时的选举过程是一致的，也就是说，下面的几种情况都会进入崩溃恢复阶段：</p>
<ul>
<li>初始化集群，刚刚启动的时候</li>
<li>Leader 崩溃，因为故障宕机</li>
<li>Leader 失去了半数的机器支持，与集群中超过一半的节点断连</li>
</ul>
<p>崩溃恢复模式将会开启新的一轮选举，选举产生的 Leader 会与过半的 Follower 进行同步，使数据一致，当与过半的机器同步完成后，就退出恢复模式， 然后进入消息广播模式。</p>
<p>Zab 中的节点有三种状态，伴随着的 Zab 不同阶段的转换，节点状态也在变化：
<img alt="img" src="assets/Cgq2xl6O5-SASu1cAABBzFJh3s0114.png"/>
我们通过一个模拟的例子，来了解崩溃恢复阶段，也就是选举的流程。</p>
<p>假设正在运行的集群有五台 Follower 服务器，编号分别是 Server1、Server2、Server3、Server4、Server5，当前 Leader 是 Server2，若某一时刻 Leader 挂了，此时便开始 Leader 选举。</p>
<p>选举过程如下：</p>
<p><strong>1</strong><strong>.各个节点</strong><strong>变更状态</strong><strong>，变更为</strong> <strong>Looking</strong></p>
<p>ZooKeeper 中除了 Leader 和 Follower，还有 Observer 节点，Observer 不参与选举，Leader 挂后，余下的 Follower 节点都会将自己的状态变更为 Looking，然后开始进入 Leader 选举过程。</p>
<p><strong>2</strong><strong>.各个</strong> <strong>Server</strong> <strong>节点都</strong><strong>会发出一个投票</strong><strong>，参与选举</strong></p>
<p>在第一次投票中，所有的 Server 都会投自己，然后各自将投票发送给集群中所有机器，在运行期间，每个服务器上的 Zxid 大概率不同。</p>
<p><strong>3</strong><strong>.</strong><strong>集群接收来自各个服务器的投票，开始处理投票和选举</strong></p>
<p>处理投票的过程就是对比 Zxid 的过程，假定 Server3 的 Zxid 最大，Server1 判断 Server3 可以成为 Leader，那么 Server1 就投票给 Server3，判断的依据如下：</p>
<blockquote>
<p>首先选举 epoch 最大的</p>
<p>如果 epoch 相等，则选 zxid 最大的</p>
<p>若 epoch 和 zxid 都相等，则选择 server id 最大的，就是配置 zoo.cfg 中的 myid</p>
</blockquote>
<p>在选举过程中，如果有节点获得超过半数的投票数，则会成为 Leader 节点，反之则重新投票选举。</p>
<p><img alt="img" src="assets/Ciqah16O5Q2AL03bAADZjhkw3ys031.png"/></p>
<p><strong>4</strong><strong>.</strong><strong>选举成功，改变服务器的状态</strong><strong>，参考上面这张图的状态变更</strong></p>
<h3 id="数据同步">数据同步</h3>
<p>崩溃恢复完成选举以后，接下来的工作就是数据同步，在选举过程中，通过投票已经确认 Leader 服务器是最大Zxid 的节点，同步阶段就是利用 Leader 前一阶段获得的最新Proposal历史，同步集群中所有的副本。</p>
<p>上面分析了 Zab 协议的具体流程，接下来我们对比一下 Zab 协议和 Paxos 算法。</p>
<h2 id="zab-与-paxos-算法的联系与区别">Zab 与 Paxos 算法的联系与区别</h2>
<p>Paxos 的思想在很多分布式组件中都可以看到，Zab 协议可以认为是基于 Paxos 算法实现的，先来看下两者之间的联系：</p>
<ul>
<li>都存在一个 Leader 进程的角色，负责协调多个 Follower 进程的运行</li>
<li>都应用 Quorum 机制，Leader 进程都会等待超过半数的 Follower 做出正确的反馈后，才会将一个提案进行提交</li>
<li>在 Zab 协议中，Zxid 中通过 epoch 来代表当前 Leader 周期，在 Paxos 算法中，同样存在这样一个标识，叫做 Ballot Number</li>
</ul>
<p>两者之间的区别是，Paxos 是理论，Zab 是实践，Paxos 是论文性质的，目的是设计一种通用的分布式一致性算法，而 Zab 协议应用在 ZooKeeper 中，是一个特别设计的崩溃可恢复的原子消息广播算法。</p>
<p>Zab 协议增加了崩溃恢复的功能，当 Leader 服务器不可用，或者已经半数以上节点失去联系时，ZooKeeper 会进入恢复模式选举新的 Leader 服务器，使集群达到一个一致的状态。</p>
<h2 id="总结">总结</h2>
<p>这一课时的内容分享了 ZooKeeper 一致性实现，包括 Zab 协议中的 Zxid 结构，Zab 协议具体的流程实现，以及 Zab 和原生 Paxos 算法的区别和联系。</p>
<p>Zab 协议在实际处理中有很多的实现细节，由于篇幅原因，这里只分享了核心的流程，若对该协议感兴趣的话，可以在课后继续找些书籍或者资料来学习：</p>
<ul>
<li><a href="https://book.douban.com/subject/26292004/" target="_blank">《从Paxos到Zookeeper》</a></li>
<li><a href="https://book.douban.com/subject/26766807/" target="_blank">《ZooKeeper:分布式过程协同技术详解》</a></li>
</ul>
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
<p>© 2019 - 2023 <a href="/cdn-cgi/l/email-protection#8de1e1e1b4b9bcbcbdbacdeae0ece4e1a3eee2e0" target="_blank">Liangliang Lee</a>.
                    Powered by <a href="https://github.com/gin-gonic/gin" target="_blank">gin</a> and <a href="https://github.com/kaiiiz/hexo-theme-book" target="_blank">hexo-theme-book</a>.</p>
</div>
</div>
<a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script>(function(){function c(){var b=a.contentDocument||a.contentWindow.document;if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'8f0c48f37d2b85a0',t:'MTczMzk5MTUxOS4wMDAwMDA='};var a=document.createElement('script');a.nonce='';a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();</script></body>

<script src="/static/index.js"></script>
</head></html>