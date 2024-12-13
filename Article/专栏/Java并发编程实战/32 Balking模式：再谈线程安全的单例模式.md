<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
<meta content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no" name="viewport"/>
<meta content="zh-cn" http-equiv="content-language"/>
<meta content="32 Balking模式：再谈线程安全的单例模式" name="description"/>
<link href="/static/favicon.png" rel="icon"/>
<title>32 Balking模式：再谈线程安全的单例模式 </title>
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
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/00%20%e5%ad%a6%e4%b9%a0%e6%94%bb%e7%95%a5%20%e5%a6%82%e4%bd%95%e6%89%8d%e8%83%bd%e5%ad%a6%e5%a5%bd%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%ef%bc%9f.md" id="00 学习攻略 如何才能学好并发编程？.md">00 学习攻略 如何才能学好并发编程？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/00%20%e5%bc%80%e7%af%87%e8%af%8d%20%e4%bd%a0%e4%b8%ba%e4%bb%80%e4%b9%88%e9%9c%80%e8%a6%81%e5%ad%a6%e4%b9%a0%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%ef%bc%9f.md" id="00 开篇词 你为什么需要学习并发编程？.md">00 开篇词 你为什么需要学习并发编程？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/01%20%e5%8f%af%e8%a7%81%e6%80%a7%e3%80%81%e5%8e%9f%e5%ad%90%e6%80%a7%e5%92%8c%e6%9c%89%e5%ba%8f%e6%80%a7%e9%97%ae%e9%a2%98%ef%bc%9a%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8bBug%e7%9a%84%e6%ba%90%e5%a4%b4.md" id="01 可见性、原子性和有序性问题：并发编程Bug的源头.md">01 可见性、原子性和有序性问题：并发编程Bug的源头.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/02%20Java%e5%86%85%e5%ad%98%e6%a8%a1%e5%9e%8b%ef%bc%9a%e7%9c%8bJava%e5%a6%82%e4%bd%95%e8%a7%a3%e5%86%b3%e5%8f%af%e8%a7%81%e6%80%a7%e5%92%8c%e6%9c%89%e5%ba%8f%e6%80%a7%e9%97%ae%e9%a2%98.md" id="02 Java内存模型：看Java如何解决可见性和有序性问题.md">02 Java内存模型：看Java如何解决可见性和有序性问题.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/03%20%e4%ba%92%e6%96%a5%e9%94%81%ef%bc%88%e4%b8%8a%ef%bc%89%ef%bc%9a%e8%a7%a3%e5%86%b3%e5%8e%9f%e5%ad%90%e6%80%a7%e9%97%ae%e9%a2%98.md" id="03 互斥锁（上）：解决原子性问题.md">03 互斥锁（上）：解决原子性问题.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/04%20%e4%ba%92%e6%96%a5%e9%94%81%ef%bc%88%e4%b8%8b%ef%bc%89%ef%bc%9a%e5%a6%82%e4%bd%95%e7%94%a8%e4%b8%80%e6%8a%8a%e9%94%81%e4%bf%9d%e6%8a%a4%e5%a4%9a%e4%b8%aa%e8%b5%84%e6%ba%90%ef%bc%9f.md" id="04 互斥锁（下）：如何用一把锁保护多个资源？.md">04 互斥锁（下）：如何用一把锁保护多个资源？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/05%20%e4%b8%80%e4%b8%8d%e5%b0%8f%e5%bf%83%e5%b0%b1%e6%ad%bb%e9%94%81%e4%ba%86%ef%bc%8c%e6%80%8e%e4%b9%88%e5%8a%9e%ef%bc%9f.md" id="05 一不小心就死锁了，怎么办？.md">05 一不小心就死锁了，怎么办？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/06%20%e7%94%a8%e2%80%9c%e7%ad%89%e5%be%85-%e9%80%9a%e7%9f%a5%e2%80%9d%e6%9c%ba%e5%88%b6%e4%bc%98%e5%8c%96%e5%be%aa%e7%8e%af%e7%ad%89%e5%be%85.md" id="06 用“等待-通知”机制优化循环等待.md">06 用“等待-通知”机制优化循环等待.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/07%20%e5%ae%89%e5%85%a8%e6%80%a7%e3%80%81%e6%b4%bb%e8%b7%83%e6%80%a7%e4%bb%a5%e5%8f%8a%e6%80%a7%e8%83%bd%e9%97%ae%e9%a2%98.md" id="07 安全性、活跃性以及性能问题.md">07 安全性、活跃性以及性能问题.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/08%20%e7%ae%a1%e7%a8%8b%ef%bc%9a%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e7%9a%84%e4%b8%87%e8%83%bd%e9%92%a5%e5%8c%99.md" id="08 管程：并发编程的万能钥匙.md">08 管程：并发编程的万能钥匙.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/09%20Java%e7%ba%bf%e7%a8%8b%ef%bc%88%e4%b8%8a%ef%bc%89%ef%bc%9aJava%e7%ba%bf%e7%a8%8b%e7%9a%84%e7%94%9f%e5%91%bd%e5%91%a8%e6%9c%9f.md" id="09 Java线程（上）：Java线程的生命周期.md">09 Java线程（上）：Java线程的生命周期.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/10%20Java%e7%ba%bf%e7%a8%8b%ef%bc%88%e4%b8%ad%ef%bc%89%ef%bc%9a%e5%88%9b%e5%bb%ba%e5%a4%9a%e5%b0%91%e7%ba%bf%e7%a8%8b%e6%89%8d%e6%98%af%e5%90%88%e9%80%82%e7%9a%84%ef%bc%9f.md" id="10 Java线程（中）：创建多少线程才是合适的？.md">10 Java线程（中）：创建多少线程才是合适的？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/11%20Java%e7%ba%bf%e7%a8%8b%ef%bc%88%e4%b8%8b%ef%bc%89%ef%bc%9a%e4%b8%ba%e4%bb%80%e4%b9%88%e5%b1%80%e9%83%a8%e5%8f%98%e9%87%8f%e6%98%af%e7%ba%bf%e7%a8%8b%e5%ae%89%e5%85%a8%e7%9a%84%ef%bc%9f.md" id="11 Java线程（下）：为什么局部变量是线程安全的？.md">11 Java线程（下）：为什么局部变量是线程安全的？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/12%20%e5%a6%82%e4%bd%95%e7%94%a8%e9%9d%a2%e5%90%91%e5%af%b9%e8%b1%a1%e6%80%9d%e6%83%b3%e5%86%99%e5%a5%bd%e5%b9%b6%e5%8f%91%e7%a8%8b%e5%ba%8f%ef%bc%9f.md" id="12 如何用面向对象思想写好并发程序？.md">12 如何用面向对象思想写好并发程序？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/13%20%e7%90%86%e8%ae%ba%e5%9f%ba%e7%a1%80%e6%a8%a1%e5%9d%97%e7%83%ad%e7%82%b9%e9%97%ae%e9%a2%98%e7%ad%94%e7%96%91.md" id="13 理论基础模块热点问题答疑.md">13 理论基础模块热点问题答疑.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/14%20Lock%e5%92%8cCondition%ef%bc%88%e4%b8%8a%ef%bc%89%ef%bc%9a%e9%9a%90%e8%97%8f%e5%9c%a8%e5%b9%b6%e5%8f%91%e5%8c%85%e4%b8%ad%e7%9a%84%e7%ae%a1%e7%a8%8b.md" id="14 Lock和Condition（上）：隐藏在并发包中的管程.md">14 Lock和Condition（上）：隐藏在并发包中的管程.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/15%20Lock%e5%92%8cCondition%ef%bc%88%e4%b8%8b%ef%bc%89%ef%bc%9aDubbo%e5%a6%82%e4%bd%95%e7%94%a8%e7%ae%a1%e7%a8%8b%e5%ae%9e%e7%8e%b0%e5%bc%82%e6%ad%a5%e8%bd%ac%e5%90%8c%e6%ad%a5%ef%bc%9f.md" id="15 Lock和Condition（下）：Dubbo如何用管程实现异步转同步？.md">15 Lock和Condition（下）：Dubbo如何用管程实现异步转同步？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/16%20Semaphore%ef%bc%9a%e5%a6%82%e4%bd%95%e5%bf%ab%e9%80%9f%e5%ae%9e%e7%8e%b0%e4%b8%80%e4%b8%aa%e9%99%90%e6%b5%81%e5%99%a8%ef%bc%9f.md" id="16 Semaphore：如何快速实现一个限流器？.md">16 Semaphore：如何快速实现一个限流器？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/17%20ReadWriteLock%ef%bc%9a%e5%a6%82%e4%bd%95%e5%bf%ab%e9%80%9f%e5%ae%9e%e7%8e%b0%e4%b8%80%e4%b8%aa%e5%ae%8c%e5%a4%87%e7%9a%84%e7%bc%93%e5%ad%98%ef%bc%9f.md" id="17 ReadWriteLock：如何快速实现一个完备的缓存？.md">17 ReadWriteLock：如何快速实现一个完备的缓存？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/18%20StampedLock%ef%bc%9a%e6%9c%89%e6%b2%a1%e6%9c%89%e6%af%94%e8%af%bb%e5%86%99%e9%94%81%e6%9b%b4%e5%bf%ab%e7%9a%84%e9%94%81%ef%bc%9f.md" id="18 StampedLock：有没有比读写锁更快的锁？.md">18 StampedLock：有没有比读写锁更快的锁？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/19%20CountDownLatch%e5%92%8cCyclicBarrier%ef%bc%9a%e5%a6%82%e4%bd%95%e8%ae%a9%e5%a4%9a%e7%ba%bf%e7%a8%8b%e6%ad%a5%e8%b0%83%e4%b8%80%e8%87%b4%ef%bc%9f.md" id="19 CountDownLatch和CyclicBarrier：如何让多线程步调一致？.md">19 CountDownLatch和CyclicBarrier：如何让多线程步调一致？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/20%20%e5%b9%b6%e5%8f%91%e5%ae%b9%e5%99%a8%ef%bc%9a%e9%83%bd%e6%9c%89%e5%93%aa%e4%ba%9b%e2%80%9c%e5%9d%91%e2%80%9d%e9%9c%80%e8%a6%81%e6%88%91%e4%bb%ac%e5%a1%ab%ef%bc%9f.md" id="20 并发容器：都有哪些“坑”需要我们填？.md">20 并发容器：都有哪些“坑”需要我们填？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/21%20%e5%8e%9f%e5%ad%90%e7%b1%bb%ef%bc%9a%e6%97%a0%e9%94%81%e5%b7%a5%e5%85%b7%e7%b1%bb%e7%9a%84%e5%85%b8%e8%8c%83.md" id="21 原子类：无锁工具类的典范.md">21 原子类：无锁工具类的典范.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/22%20Executor%e4%b8%8e%e7%ba%bf%e7%a8%8b%e6%b1%a0%ef%bc%9a%e5%a6%82%e4%bd%95%e5%88%9b%e5%bb%ba%e6%ad%a3%e7%a1%ae%e7%9a%84%e7%ba%bf%e7%a8%8b%e6%b1%a0%ef%bc%9f.md" id="22 Executor与线程池：如何创建正确的线程池？.md">22 Executor与线程池：如何创建正确的线程池？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/23%20Future%ef%bc%9a%e5%a6%82%e4%bd%95%e7%94%a8%e5%a4%9a%e7%ba%bf%e7%a8%8b%e5%ae%9e%e7%8e%b0%e6%9c%80%e4%bc%98%e7%9a%84%e2%80%9c%e7%83%a7%e6%b0%b4%e6%b3%a1%e8%8c%b6%e2%80%9d%e7%a8%8b%e5%ba%8f%ef%bc%9f.md" id="23 Future：如何用多线程实现最优的“烧水泡茶”程序？.md">23 Future：如何用多线程实现最优的“烧水泡茶”程序？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/24%20CompletableFuture%ef%bc%9a%e5%bc%82%e6%ad%a5%e7%bc%96%e7%a8%8b%e6%b2%a1%e9%82%a3%e4%b9%88%e9%9a%be.md" id="24 CompletableFuture：异步编程没那么难.md">24 CompletableFuture：异步编程没那么难.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/25%20CompletionService%ef%bc%9a%e5%a6%82%e4%bd%95%e6%89%b9%e9%87%8f%e6%89%a7%e8%a1%8c%e5%bc%82%e6%ad%a5%e4%bb%bb%e5%8a%a1%ef%bc%9f.md" id="25 CompletionService：如何批量执行异步任务？.md">25 CompletionService：如何批量执行异步任务？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/26%20Fork_Join%ef%bc%9a%e5%8d%95%e6%9c%ba%e7%89%88%e7%9a%84MapReduce.md" id="26 Fork_Join：单机版的MapReduce.md">26 Fork_Join：单机版的MapReduce.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/27%20%e5%b9%b6%e5%8f%91%e5%b7%a5%e5%85%b7%e7%b1%bb%e6%a8%a1%e5%9d%97%e7%83%ad%e7%82%b9%e9%97%ae%e9%a2%98%e7%ad%94%e7%96%91.md" id="27 并发工具类模块热点问题答疑.md">27 并发工具类模块热点问题答疑.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/28%20Immutability%e6%a8%a1%e5%bc%8f%ef%bc%9a%e5%a6%82%e4%bd%95%e5%88%a9%e7%94%a8%e4%b8%8d%e5%8f%98%e6%80%a7%e8%a7%a3%e5%86%b3%e5%b9%b6%e5%8f%91%e9%97%ae%e9%a2%98%ef%bc%9f.md" id="28 Immutability模式：如何利用不变性解决并发问题？.md">28 Immutability模式：如何利用不变性解决并发问题？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/29%20Copy-on-Write%e6%a8%a1%e5%bc%8f%ef%bc%9a%e4%b8%8d%e6%98%af%e5%bb%b6%e6%97%b6%e7%ad%96%e7%95%a5%e7%9a%84COW.md" id="29 Copy-on-Write模式：不是延时策略的COW.md">29 Copy-on-Write模式：不是延时策略的COW.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/3%20%e4%b8%aa%e7%94%a8%e6%88%b7%e6%9d%a5%e4%bf%a1%20%e6%89%93%e5%bc%80%e4%b8%80%e4%b8%aa%e6%96%b0%e7%9a%84%e5%b9%b6%e5%8f%91%e4%b8%96%e7%95%8c.md" id="3 个用户来信 打开一个新的并发世界.md">3 个用户来信 打开一个新的并发世界.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/30%20%e7%ba%bf%e7%a8%8b%e6%9c%ac%e5%9c%b0%e5%ad%98%e5%82%a8%e6%a8%a1%e5%bc%8f%ef%bc%9a%e6%b2%a1%e6%9c%89%e5%85%b1%e4%ba%ab%ef%bc%8c%e5%b0%b1%e6%b2%a1%e6%9c%89%e4%bc%a4%e5%ae%b3.md" id="30 线程本地存储模式：没有共享，就没有伤害.md">30 线程本地存储模式：没有共享，就没有伤害.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/31%20Guarded%20Suspension%e6%a8%a1%e5%bc%8f%ef%bc%9a%e7%ad%89%e5%be%85%e5%94%a4%e9%86%92%e6%9c%ba%e5%88%b6%e7%9a%84%e8%a7%84%e8%8c%83%e5%ae%9e%e7%8e%b0.md" id="31 Guarded Suspension模式：等待唤醒机制的规范实现.md">31 Guarded Suspension模式：等待唤醒机制的规范实现.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/32%20Balking%e6%a8%a1%e5%bc%8f%ef%bc%9a%e5%86%8d%e8%b0%88%e7%ba%bf%e7%a8%8b%e5%ae%89%e5%85%a8%e7%9a%84%e5%8d%95%e4%be%8b%e6%a8%a1%e5%bc%8f.md" id="32 Balking模式：再谈线程安全的单例模式.md">32 Balking模式：再谈线程安全的单例模式.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/33%20Thread-Per-Message%e6%a8%a1%e5%bc%8f%ef%bc%9a%e6%9c%80%e7%ae%80%e5%8d%95%e5%ae%9e%e7%94%a8%e7%9a%84%e5%88%86%e5%b7%a5%e6%96%b9%e6%b3%95.md" id="33 Thread-Per-Message模式：最简单实用的分工方法.md">33 Thread-Per-Message模式：最简单实用的分工方法.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/34%20Worker%20Thread%e6%a8%a1%e5%bc%8f%ef%bc%9a%e5%a6%82%e4%bd%95%e9%81%bf%e5%85%8d%e9%87%8d%e5%a4%8d%e5%88%9b%e5%bb%ba%e7%ba%bf%e7%a8%8b%ef%bc%9f.md" id="34 Worker Thread模式：如何避免重复创建线程？.md">34 Worker Thread模式：如何避免重复创建线程？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/35%20%e4%b8%a4%e9%98%b6%e6%ae%b5%e7%bb%88%e6%ad%a2%e6%a8%a1%e5%bc%8f%ef%bc%9a%e5%a6%82%e4%bd%95%e4%bc%98%e9%9b%85%e5%9c%b0%e7%bb%88%e6%ad%a2%e7%ba%bf%e7%a8%8b%ef%bc%9f.md" id="35 两阶段终止模式：如何优雅地终止线程？.md">35 两阶段终止模式：如何优雅地终止线程？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/36%20%e7%94%9f%e4%ba%a7%e8%80%85-%e6%b6%88%e8%b4%b9%e8%80%85%e6%a8%a1%e5%bc%8f%ef%bc%9a%e7%94%a8%e6%b5%81%e6%b0%b4%e7%ba%bf%e6%80%9d%e6%83%b3%e6%8f%90%e9%ab%98%e6%95%88%e7%8e%87.md" id="36 生产者-消费者模式：用流水线思想提高效率.md">36 生产者-消费者模式：用流水线思想提高效率.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/37%20%e8%ae%be%e8%ae%a1%e6%a8%a1%e5%bc%8f%e6%a8%a1%e5%9d%97%e7%83%ad%e7%82%b9%e9%97%ae%e9%a2%98%e7%ad%94%e7%96%91.md" id="37 设计模式模块热点问题答疑.md">37 设计模式模块热点问题答疑.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/38%20%e6%a1%88%e4%be%8b%e5%88%86%e6%9e%90%ef%bc%88%e4%b8%80%ef%bc%89%ef%bc%9a%e9%ab%98%e6%80%a7%e8%83%bd%e9%99%90%e6%b5%81%e5%99%a8Guava%20RateLimiter.md" id="38 案例分析（一）：高性能限流器Guava RateLimiter.md">38 案例分析（一）：高性能限流器Guava RateLimiter.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/39%20%e6%a1%88%e4%be%8b%e5%88%86%e6%9e%90%ef%bc%88%e4%ba%8c%ef%bc%89%ef%bc%9a%e9%ab%98%e6%80%a7%e8%83%bd%e7%bd%91%e7%bb%9c%e5%ba%94%e7%94%a8%e6%a1%86%e6%9e%b6Netty.md" id="39 案例分析（二）：高性能网络应用框架Netty.md">39 案例分析（二）：高性能网络应用框架Netty.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/40%20%e6%a1%88%e4%be%8b%e5%88%86%e6%9e%90%ef%bc%88%e4%b8%89%ef%bc%89%ef%bc%9a%e9%ab%98%e6%80%a7%e8%83%bd%e9%98%9f%e5%88%97Disruptor.md" id="40 案例分析（三）：高性能队列Disruptor.md">40 案例分析（三）：高性能队列Disruptor.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/41%20%e6%a1%88%e4%be%8b%e5%88%86%e6%9e%90%ef%bc%88%e5%9b%9b%ef%bc%89%ef%bc%9a%e9%ab%98%e6%80%a7%e8%83%bd%e6%95%b0%e6%8d%ae%e5%ba%93%e8%bf%9e%e6%8e%a5%e6%b1%a0HiKariCP.md" id="41 案例分析（四）：高性能数据库连接池HiKariCP.md">41 案例分析（四）：高性能数据库连接池HiKariCP.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/42%20Actor%e6%a8%a1%e5%9e%8b%ef%bc%9a%e9%9d%a2%e5%90%91%e5%af%b9%e8%b1%a1%e5%8e%9f%e7%94%9f%e7%9a%84%e5%b9%b6%e5%8f%91%e6%a8%a1%e5%9e%8b.md" id="42 Actor模型：面向对象原生的并发模型.md">42 Actor模型：面向对象原生的并发模型.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/43%20%e8%bd%af%e4%bb%b6%e4%ba%8b%e5%8a%a1%e5%86%85%e5%ad%98%ef%bc%9a%e5%80%9f%e9%89%b4%e6%95%b0%e6%8d%ae%e5%ba%93%e7%9a%84%e5%b9%b6%e5%8f%91%e7%bb%8f%e9%aa%8c.md" id="43 软件事务内存：借鉴数据库的并发经验.md">43 软件事务内存：借鉴数据库的并发经验.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/44%20%e5%8d%8f%e7%a8%8b%ef%bc%9a%e6%9b%b4%e8%bd%bb%e9%87%8f%e7%ba%a7%e7%9a%84%e7%ba%bf%e7%a8%8b.md" id="44 协程：更轻量级的线程.md">44 协程：更轻量级的线程.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/45%20CSP%e6%a8%a1%e5%9e%8b%ef%bc%9aGolang%e7%9a%84%e4%b8%bb%e5%8a%9b%e9%98%9f%e5%91%98.md" id="45 CSP模型：Golang的主力队员.md">45 CSP模型：Golang的主力队员.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/%e7%94%a8%e6%88%b7%e6%9d%a5%e4%bf%a1%20%e7%9c%9f%e5%a5%bd%ef%bc%8c%e9%9d%a2%e8%af%95%e8%80%83%e5%88%b0%e8%bf%99%e4%ba%9b%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%ef%bc%8c%e6%88%91%e9%83%bd%e7%ad%94%e5%af%b9%e4%ba%86%ef%bc%81.md" id="用户来信 真好，面试考到这些并发编程，我都答对了！.md">用户来信 真好，面试考到这些并发编程，我都答对了！.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%e5%ae%9e%e6%88%98/%e7%bb%93%e6%9d%9f%e8%af%ad%20%e5%8d%81%e5%b9%b4%e4%b9%8b%e5%90%8e%ef%bc%8c%e5%88%9d%e5%bf%83%e4%be%9d%e6%97%a7.md" id="结束语 十年之后，初心依旧.md">结束语 十年之后，初心依旧.md</a>
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
<h1 class="title" data-id="32 Balking模式：再谈线程安全的单例模式" id="title">32 Balking模式：再谈线程安全的单例模式</h1>
<div><p>上一篇文章中，我们提到可以用“多线程版本的if”来理解Guarded Suspension模式，不同于单线程中的if，这个“多线程版本的if”是需要等待的，而且还很执着，必须要等到条件为真。但很显然这个世界，不是所有场景都需要这么执着，有时候我们还需要快速放弃。</p>
<p>需要快速放弃的一个最常见的例子是各种编辑器提供的自动保存功能。自动保存功能的实现逻辑一般都是隔一定时间自动执行存盘操作，存盘操作的前提是文件做过修改，如果文件没有执行过修改操作，就需要快速放弃存盘操作。下面的示例代码将自动保存功能代码化了，很显然AutoSaveEditor这个类不是线程安全的，因为对共享变量changed的读写没有使用同步，那如何保证AutoSaveEditor的线程安全性呢？</p>
<pre><code>class AutoSaveEditor{
  //文件是否被修改过
  boolean changed=false;
  //定时任务线程池
  ScheduledExecutorService ses = 
    Executors.newSingleThreadScheduledExecutor();
  //定时执行自动保存
  void startAutoSave(){
    ses.scheduleWithFixedDelay(()-&gt;{
      autoSave();
    }, 5, 5, TimeUnit.SECONDS);  
  }
  //自动存盘操作
  void autoSave(){
    if (!changed) {
      return;
    }
    changed = false;
    //执行存盘操作
    //省略且实现
    this.execSave();
  }
  //编辑操作
  void edit(){
    //省略编辑逻辑
    ......
    changed = true;
  }
}
</code></pre>
<p>解决这个问题相信你一定手到擒来了：读写共享变量changed的方法autoSave()和edit()都加互斥锁就可以了。这样做虽然简单，但是性能很差，原因是锁的范围太大了。那我们可以将锁的范围缩小，只在读写共享变量changed的地方加锁，实现代码如下所示。</p>
<pre><code>//自动存盘操作
void autoSave(){
  synchronized(this){
    if (!changed) {
      return;
    }
    changed = false;
  }
  //执行存盘操作
  //省略且实现
  this.execSave();
}
//编辑操作
void edit(){
  //省略编辑逻辑
  ......
  synchronized(this){
    changed = true;
  }
}  
</code></pre>
<p>如果你深入地分析一下这个示例程序，你会发现，示例中的共享变量是一个状态变量，业务逻辑依赖于这个状态变量的状态：当状态满足某个条件时，执行某个业务逻辑，其本质其实不过就是一个if而已，放到多线程场景里，就是一种“多线程版本的if”。这种“多线程版本的if”的应用场景还是很多的，所以也有人把它总结成了一种设计模式，叫做<strong>Balking模式</strong>。</p>
<h2 id="balking模式的经典实现">Balking模式的经典实现</h2>
<p>Balking模式本质上是一种规范化地解决“多线程版本的if”的方案，对于上面自动保存的例子，使用Balking模式规范化之后的写法如下所示，你会发现仅仅是将edit()方法中对共享变量changed的赋值操作抽取到了change()中，这样的好处是将并发处理逻辑和业务逻辑分开。</p>
<pre><code>boolean changed=false;
//自动存盘操作
void autoSave(){
  synchronized(this){
    if (!changed) {
      return;
    }
    changed = false;
  }
  //执行存盘操作
  //省略且实现
  this.execSave();
}
//编辑操作
void edit(){
  //省略编辑逻辑
  ......
  change();
}
//改变状态
void change(){
  synchronized(this){
    changed = true;
  }
}
</code></pre>
<h2 id="用volatile实现balking模式">用volatile实现Balking模式</h2>
<p>前面我们用synchronized实现了Balking模式，这种实现方式最为稳妥，建议你实际工作中也使用这个方案。不过在某些特定场景下，也可以使用volatile来实现，但<strong>使用volatile的前提是对原子性没有要求</strong>。</p>
<p>在<a href="https://time.geekbang.org/column/article/93154" target="_blank">《29 | Copy-on-Write模式：不是延时策略的COW》</a>中，有一个RPC框架路由表的案例，在RPC框架中，本地路由表是要和注册中心进行信息同步的，应用启动的时候，会将应用依赖服务的路由表从注册中心同步到本地路由表中，如果应用重启的时候注册中心宕机，那么会导致该应用依赖的服务均不可用，因为找不到依赖服务的路由表。为了防止这种极端情况出现，RPC框架可以将本地路由表自动保存到本地文件中，如果重启的时候注册中心宕机，那么就从本地文件中恢复重启前的路由表。这其实也是一种降级的方案。</p>
<p>自动保存路由表和前面介绍的编辑器自动保存原理是一样的，也可以用Balking模式实现，不过我们这里采用volatile来实现，实现的代码如下所示。之所以可以采用volatile来实现，是因为对共享变量changed和rt的写操作不存在原子性的要求，而且采用scheduleWithFixedDelay()这种调度方式能保证同一时刻只有一个线程执行autoSave()方法。</p>
<pre><code>//路由表信息
public class RouterTable {
  //Key:接口名
  //Value:路由集合
  ConcurrentHashMap&lt;String, CopyOnWriteArraySet&lt;Router&gt;&gt; 
    rt = new ConcurrentHashMap&lt;&gt;();    
  //路由表是否发生变化
  volatile boolean changed;
  //将路由表写入本地文件的线程池
  ScheduledExecutorService ses=
    Executors.newSingleThreadScheduledExecutor();
  //启动定时任务
  //将变更后的路由表写入本地文件
  public void startLocalSaver(){
    ses.scheduleWithFixedDelay(()-&gt;{
      autoSave();
    }, 1, 1, MINUTES);
  }
  //保存路由表到本地文件
  void autoSave() {
    if (!changed) {
      return;
    }
    changed = false;
    //将路由表写入本地文件
    //省略其方法实现
    this.save2Local();
  }
  //删除路由
  public void remove(Router router) {
    Set&lt;Router&gt; set=rt.get(router.iface);
    if (set != null) {
      set.remove(router);
      //路由表已发生变化
      changed = true;
    }
  }
  //增加路由
  public void add(Router router) {
    Set&lt;Router&gt; set = rt.computeIfAbsent(
      route.iface, r -&gt; 
        new CopyOnWriteArraySet&lt;&gt;());
    set.add(router);
    //路由表已发生变化
    changed = true;
  }
}
</code></pre>
<p>Balking模式有一个非常典型的应用场景就是单次初始化，下面的示例代码是它的实现。这个实现方案中，我们将init()声明为一个同步方法，这样同一个时刻就只有一个线程能够执行init()方法；init()方法在第一次执行完时会将inited设置为true，这样后续执行init()方法的线程就不会再执行doInit()了。</p>
<pre><code>class InitTest{
  boolean inited = false;
  synchronized void init(){
    if(inited){
      return;
    }
    //省略doInit的实现
    doInit();
    inited=true;
  }
}
</code></pre>
<p>线程安全的单例模式本质上其实也是单次初始化，所以可以用Balking模式来实现线程安全的单例模式，下面的示例代码是其实现。这个实现虽然功能上没有问题，但是性能却很差，因为互斥锁synchronized将getInstance()方法串行化了，那有没有办法可以优化一下它的性能呢？</p>
<pre><code>class Singleton{
  private static
    Singleton singleton;
  //构造方法私有化  
  private Singleton(){}
  //获取实例（单例）
  public synchronized static 
  Singleton getInstance(){
    if(singleton == null){
      singleton=new Singleton();
    }
    return singleton;
  }
}
</code></pre>
<p>办法当然是有的，那就是经典的<strong>双重检查</strong>（Double Check）方案，下面的示例代码是其详细实现。在双重检查方案中，一旦Singleton对象被成功创建之后，就不会执行synchronized(Singleton.class){}相关的代码，也就是说，此时getInstance()方法的执行路径是无锁的，从而解决了性能问题。不过需要你注意的是，这个方案中使用了volatile来禁止编译优化，其原因你可以参考<a href="https://time.geekbang.org/column/article/83682" target="_blank">《01 | 可见性、原子性和有序性问题：并发编程Bug的源头》</a>中相关的内容。至于获取锁后的二次检查，则是出于对安全性负责。</p>
<pre><code>class Singleton{
  private static volatile 
    Singleton singleton;
  //构造方法私有化  
  private Singleton() {}
  //获取实例（单例）
  public static Singleton 
  getInstance() {
    //第一次检查
    if(singleton==null){
      synchronize(Singleton.class){
        //获取锁后二次检查
        if(singleton==null){
          singleton=new Singleton();
        }
      }
    }
    return singleton;
  }
}
</code></pre>
<h2 id="总结">总结</h2>
<p>Balking模式和Guarded Suspension模式从实现上看似乎没有多大的关系，Balking模式只需要用互斥锁就能解决，而Guarded Suspension模式则要用到管程这种高级的并发原语；但是从应用的角度来看，它们解决的都是“线程安全的if”语义，不同之处在于，Guarded Suspension模式会等待if条件为真，而Balking模式不会等待。</p>
<p>Balking模式的经典实现是使用互斥锁，你可以使用Java语言内置synchronized，也可以使用SDK提供Lock；如果你对互斥锁的性能不满意，可以尝试采用volatile方案，不过使用volatile方案需要你更加谨慎。</p>
<p>当然你也可以尝试使用双重检查方案来优化性能，双重检查中的第一次检查，完全是出于对性能的考量：避免执行加锁操作，因为加锁操作很耗时。而加锁之后的二次检查，则是出于对安全性负责。双重检查方案在优化加锁性能方面经常用到，例如<a href="https://time.geekbang.org/column/article/88909" target="_blank">《17 | ReadWriteLock：如何快速实现一个完备的缓存？》</a>中实现缓存按需加载功能时，也用到了双重检查方案。</p>
<h2 id="课后思考">课后思考</h2>
<p>下面的示例代码中，init()方法的本意是：仅需计算一次count的值，采用了Balking模式的volatile实现方式，你觉得这个实现是否有问题呢？</p>
<pre><code>class Test{
  volatile boolean inited = false;
  int count = 0;
  void init(){
    if(inited){
      return;
    }
    inited = true;
    //计算count的值
    count = calc();
  }
}  
</code></pre>
<p>欢迎在留言区与我分享你的想法，也欢迎你在留言区记录你的思考过程。感谢阅读，如果你觉得这篇文章对你有帮助的话，也欢迎把它分享给更多的朋友。</p>
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
<p>© 2019 - 2023 <a href="/cdn-cgi/l/email-protection#d1bdbdbde8e5e0e0e1e691b6bcb0b8bdffb2bebc" target="_blank">Liangliang Lee</a>.
                    Powered by <a href="https://github.com/gin-gonic/gin" target="_blank">gin</a> and <a href="https://github.com/kaiiiz/hexo-theme-book" target="_blank">hexo-theme-book</a>.</p>
</div>
</div>
<a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script>(function(){function c(){var b=a.contentDocument||a.contentWindow.document;if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'8f0b0295ea8b07aa',t:'MTczMzk3ODE1MS4wMDAwMDA='};var a=document.createElement('script');a.nonce='';a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();</script></body>

<script src="/static/index.js"></script>
</head></html>