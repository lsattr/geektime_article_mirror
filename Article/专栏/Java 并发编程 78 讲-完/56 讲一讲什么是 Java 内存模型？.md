<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
<meta content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no" name="viewport"/>
<meta content="zh-cn" http-equiv="content-language"/>
<meta content="56 讲一讲什么是 Java 内存模型？" name="description"/>
<link href="/static/favicon.png" rel="icon"/>
<title>56 讲一讲什么是 Java 内存模型？ </title>
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
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/00%20%e7%94%b1%e7%82%b9%e5%8f%8a%e9%9d%a2%ef%bc%8c%e6%90%ad%e5%bb%ba%e4%bd%a0%e7%9a%84%20Java%20%e5%b9%b6%e5%8f%91%e7%9f%a5%e8%af%86%e7%bd%91.md" id="00 由点及面，搭建你的 Java 并发知识网.md">00 由点及面，搭建你的 Java 并发知识网.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/01%20%e4%b8%ba%e4%bd%95%e8%af%b4%e5%8f%aa%e6%9c%89%201%20%e7%a7%8d%e5%ae%9e%e7%8e%b0%e7%ba%bf%e7%a8%8b%e7%9a%84%e6%96%b9%e6%b3%95%ef%bc%9f.md" id="01 为何说只有 1 种实现线程的方法？.md">01 为何说只有 1 种实现线程的方法？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/02%20%e5%a6%82%e4%bd%95%e6%ad%a3%e7%a1%ae%e5%81%9c%e6%ad%a2%e7%ba%bf%e7%a8%8b%ef%bc%9f%e4%b8%ba%e4%bb%80%e4%b9%88%20volatile%20%e6%a0%87%e8%ae%b0%e4%bd%8d%e7%9a%84%e5%81%9c%e6%ad%a2%e6%96%b9%e6%b3%95%e6%98%af%e9%94%99%e8%af%af%e7%9a%84%ef%bc%9f.md" id="02 如何正确停止线程？为什么 volatile 标记位的停止方法是错误的？.md">02 如何正确停止线程？为什么 volatile 标记位的停止方法是错误的？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/03%20%e7%ba%bf%e7%a8%8b%e6%98%af%e5%a6%82%e4%bd%95%e5%9c%a8%206%20%e7%a7%8d%e7%8a%b6%e6%80%81%e4%b9%8b%e9%97%b4%e8%bd%ac%e6%8d%a2%e7%9a%84%ef%bc%9f.md" id="03 线程是如何在 6 种状态之间转换的？.md">03 线程是如何在 6 种状态之间转换的？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/04%20waitnotifynotifyAll%20%e6%96%b9%e6%b3%95%e7%9a%84%e4%bd%bf%e7%94%a8%e6%b3%a8%e6%84%8f%e4%ba%8b%e9%a1%b9%ef%bc%9f.md" id="04 waitnotifynotifyAll 方法的使用注意事项？.md">04 waitnotifynotifyAll 方法的使用注意事项？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/05%20%e6%9c%89%e5%93%aa%e5%87%a0%e7%a7%8d%e5%ae%9e%e7%8e%b0%e7%94%9f%e4%ba%a7%e8%80%85%e6%b6%88%e8%b4%b9%e8%80%85%e6%a8%a1%e5%bc%8f%e7%9a%84%e6%96%b9%e6%b3%95%ef%bc%9f.md" id="05 有哪几种实现生产者消费者模式的方法？.md">05 有哪几种实现生产者消费者模式的方法？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/06%20%e4%b8%80%e5%85%b1%e6%9c%89%e5%93%aa%203%20%e7%b1%bb%e7%ba%bf%e7%a8%8b%e5%ae%89%e5%85%a8%e9%97%ae%e9%a2%98%ef%bc%9f.md" id="06 一共有哪 3 类线程安全问题？.md">06 一共有哪 3 类线程安全问题？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/07%20%e5%93%aa%e4%ba%9b%e5%9c%ba%e6%99%af%e9%9c%80%e8%a6%81%e9%a2%9d%e5%a4%96%e6%b3%a8%e6%84%8f%e7%ba%bf%e7%a8%8b%e5%ae%89%e5%85%a8%e9%97%ae%e9%a2%98%ef%bc%9f.md" id="07 哪些场景需要额外注意线程安全问题？.md">07 哪些场景需要额外注意线程安全问题？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/08%20%e4%b8%ba%e4%bb%80%e4%b9%88%e5%a4%9a%e7%ba%bf%e7%a8%8b%e4%bc%9a%e5%b8%a6%e6%9d%a5%e6%80%a7%e8%83%bd%e9%97%ae%e9%a2%98%ef%bc%9f.md" id="08 为什么多线程会带来性能问题？.md">08 为什么多线程会带来性能问题？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/09%20%e4%bd%bf%e7%94%a8%e7%ba%bf%e7%a8%8b%e6%b1%a0%e6%af%94%e6%89%8b%e5%8a%a8%e5%88%9b%e5%bb%ba%e7%ba%bf%e7%a8%8b%e5%a5%bd%e5%9c%a8%e5%93%aa%e9%87%8c%ef%bc%9f.md" id="09 使用线程池比手动创建线程好在哪里？.md">09 使用线程池比手动创建线程好在哪里？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/10%20%e7%ba%bf%e7%a8%8b%e6%b1%a0%e7%9a%84%e5%90%84%e4%b8%aa%e5%8f%82%e6%95%b0%e7%9a%84%e5%90%ab%e4%b9%89%ef%bc%9f.md" id="10 线程池的各个参数的含义？.md">10 线程池的各个参数的含义？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/11%20%e7%ba%bf%e7%a8%8b%e6%b1%a0%e6%9c%89%e5%93%aa%204%20%e7%a7%8d%e6%8b%92%e7%bb%9d%e7%ad%96%e7%95%a5%ef%bc%9f.md" id="11 线程池有哪 4 种拒绝策略？.md">11 线程池有哪 4 种拒绝策略？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/12%20%e6%9c%89%e5%93%aa%206%20%e7%a7%8d%e5%b8%b8%e8%a7%81%e7%9a%84%e7%ba%bf%e7%a8%8b%e6%b1%a0%ef%bc%9f%e4%bb%80%e4%b9%88%e6%98%af%20Java8%20%e7%9a%84%20ForkJoinPool%ef%bc%9f.md" id="12 有哪 6 种常见的线程池？什么是 Java8 的 ForkJoinPool？.md">12 有哪 6 种常见的线程池？什么是 Java8 的 ForkJoinPool？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/13%20%e7%ba%bf%e7%a8%8b%e6%b1%a0%e5%b8%b8%e7%94%a8%e7%9a%84%e9%98%bb%e5%a1%9e%e9%98%9f%e5%88%97%e6%9c%89%e5%93%aa%e4%ba%9b%ef%bc%9f.md" id="13 线程池常用的阻塞队列有哪些？.md">13 线程池常用的阻塞队列有哪些？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/14%20%e4%b8%ba%e4%bb%80%e4%b9%88%e4%b8%8d%e5%ba%94%e8%af%a5%e8%87%aa%e5%8a%a8%e5%88%9b%e5%bb%ba%e7%ba%bf%e7%a8%8b%e6%b1%a0%ef%bc%9f.md" id="14 为什么不应该自动创建线程池？.md">14 为什么不应该自动创建线程池？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/15%20%e5%90%88%e9%80%82%e7%9a%84%e7%ba%bf%e7%a8%8b%e6%95%b0%e9%87%8f%e6%98%af%e5%a4%9a%e5%b0%91%ef%bc%9fCPU%20%e6%a0%b8%e5%bf%83%e6%95%b0%e5%92%8c%e7%ba%bf%e7%a8%8b%e6%95%b0%e7%9a%84%e5%85%b3%e7%b3%bb%ef%bc%9f.md" id="15 合适的线程数量是多少？CPU 核心数和线程数的关系？.md">15 合适的线程数量是多少？CPU 核心数和线程数的关系？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/16%20%e5%a6%82%e4%bd%95%e6%a0%b9%e6%8d%ae%e5%ae%9e%e9%99%85%e9%9c%80%e8%a6%81%ef%bc%8c%e5%ae%9a%e5%88%b6%e8%87%aa%e5%b7%b1%e7%9a%84%e7%ba%bf%e7%a8%8b%e6%b1%a0%ef%bc%9f.md" id="16 如何根据实际需要，定制自己的线程池？.md">16 如何根据实际需要，定制自己的线程池？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/17%20%e5%a6%82%e4%bd%95%e6%ad%a3%e7%a1%ae%e5%85%b3%e9%97%ad%e7%ba%bf%e7%a8%8b%e6%b1%a0%ef%bc%9fshutdown%20%e5%92%8c%20shutdownNow%20%e7%9a%84%e5%8c%ba%e5%88%ab%ef%bc%9f.md" id="17 如何正确关闭线程池？shutdown 和 shutdownNow 的区别？.md">17 如何正确关闭线程池？shutdown 和 shutdownNow 的区别？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/18%20%e7%ba%bf%e7%a8%8b%e6%b1%a0%e5%ae%9e%e7%8e%b0%e2%80%9c%e7%ba%bf%e7%a8%8b%e5%a4%8d%e7%94%a8%e2%80%9d%e7%9a%84%e5%8e%9f%e7%90%86%ef%bc%9f.md" id="18 线程池实现“线程复用”的原理？.md">18 线程池实现“线程复用”的原理？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/19%20%e4%bd%a0%e7%9f%a5%e9%81%93%e5%93%aa%e5%87%a0%e7%a7%8d%e9%94%81%ef%bc%9f%e5%88%86%e5%88%ab%e6%9c%89%e4%bb%80%e4%b9%88%e7%89%b9%e7%82%b9%ef%bc%9f.md" id="19 你知道哪几种锁？分别有什么特点？.md">19 你知道哪几种锁？分别有什么特点？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/20%20%e6%82%b2%e8%a7%82%e9%94%81%e5%92%8c%e4%b9%90%e8%a7%82%e9%94%81%e7%9a%84%e6%9c%ac%e8%b4%a8%e6%98%af%e4%bb%80%e4%b9%88%ef%bc%9f.md" id="20 悲观锁和乐观锁的本质是什么？.md">20 悲观锁和乐观锁的本质是什么？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/21%20%e5%a6%82%e4%bd%95%e7%9c%8b%e5%88%b0%20synchronized%20%e8%83%8c%e5%90%8e%e7%9a%84%e2%80%9cmonitor%20%e9%94%81%e2%80%9d%ef%bc%9f.md" id="21 如何看到 synchronized 背后的“monitor 锁”？.md">21 如何看到 synchronized 背后的“monitor 锁”？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/22%20synchronized%20%e5%92%8c%20Lock%20%e5%ad%b0%e4%bc%98%e5%ad%b0%e5%8a%a3%ef%bc%8c%e5%a6%82%e4%bd%95%e9%80%89%e6%8b%a9%ef%bc%9f.md" id="22 synchronized 和 Lock 孰优孰劣，如何选择？.md">22 synchronized 和 Lock 孰优孰劣，如何选择？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/23%20Lock%20%e6%9c%89%e5%93%aa%e5%87%a0%e4%b8%aa%e5%b8%b8%e7%94%a8%e6%96%b9%e6%b3%95%ef%bc%9f%e5%88%86%e5%88%ab%e6%9c%89%e4%bb%80%e4%b9%88%e7%94%a8%ef%bc%9f.md" id="23 Lock 有哪几个常用方法？分别有什么用？.md">23 Lock 有哪几个常用方法？分别有什么用？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/24%20%e8%ae%b2%e4%b8%80%e8%ae%b2%e5%85%ac%e5%b9%b3%e9%94%81%e5%92%8c%e9%9d%9e%e5%85%ac%e5%b9%b3%e9%94%81%ef%bc%8c%e4%b8%ba%e4%bb%80%e4%b9%88%e8%a6%81%e2%80%9c%e9%9d%9e%e5%85%ac%e5%b9%b3%e2%80%9d%ef%bc%9f.md" id="24 讲一讲公平锁和非公平锁，为什么要“非公平”？.md">24 讲一讲公平锁和非公平锁，为什么要“非公平”？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/25%20%e8%af%bb%e5%86%99%e9%94%81%20ReadWriteLock%20%e8%8e%b7%e5%8f%96%e9%94%81%e6%9c%89%e5%93%aa%e4%ba%9b%e8%a7%84%e5%88%99%ef%bc%9f.md" id="25 读写锁 ReadWriteLock 获取锁有哪些规则？.md">25 读写锁 ReadWriteLock 获取锁有哪些规则？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/26%20%e8%af%bb%e9%94%81%e5%ba%94%e8%af%a5%e6%8f%92%e9%98%9f%e5%90%97%ef%bc%9f%e4%bb%80%e4%b9%88%e6%98%af%e8%af%bb%e5%86%99%e9%94%81%e7%9a%84%e5%8d%87%e9%99%8d%e7%ba%a7%ef%bc%9f.md" id="26 读锁应该插队吗？什么是读写锁的升降级？.md">26 读锁应该插队吗？什么是读写锁的升降级？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/27%20%e4%bb%80%e4%b9%88%e6%98%af%e8%87%aa%e6%97%8b%e9%94%81%ef%bc%9f%e8%87%aa%e6%97%8b%e7%9a%84%e5%a5%bd%e5%a4%84%e5%92%8c%e5%90%8e%e6%9e%9c%e6%98%af%e4%bb%80%e4%b9%88%e5%91%a2%ef%bc%9f.md" id="27 什么是自旋锁？自旋的好处和后果是什么呢？.md">27 什么是自旋锁？自旋的好处和后果是什么呢？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/28%20JVM%20%e5%af%b9%e9%94%81%e8%bf%9b%e8%a1%8c%e4%ba%86%e5%93%aa%e4%ba%9b%e4%bc%98%e5%8c%96%ef%bc%9f.md" id="28 JVM 对锁进行了哪些优化？.md">28 JVM 对锁进行了哪些优化？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/29%20HashMap%20%e4%b8%ba%e4%bb%80%e4%b9%88%e6%98%af%e7%ba%bf%e7%a8%8b%e4%b8%8d%e5%ae%89%e5%85%a8%e7%9a%84%ef%bc%9f.md" id="29 HashMap 为什么是线程不安全的？.md">29 HashMap 为什么是线程不安全的？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/30%20ConcurrentHashMap%20%e5%9c%a8%20Java7%20%e5%92%8c%208%20%e6%9c%89%e4%bd%95%e4%b8%8d%e5%90%8c%ef%bc%9f.md" id="30 ConcurrentHashMap 在 Java7 和 8 有何不同？.md">30 ConcurrentHashMap 在 Java7 和 8 有何不同？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/31%20%e4%b8%ba%e4%bb%80%e4%b9%88%20Map%20%e6%a1%b6%e4%b8%ad%e8%b6%85%e8%bf%87%208%20%e4%b8%aa%e6%89%8d%e8%bd%ac%e4%b8%ba%e7%ba%a2%e9%bb%91%e6%a0%91%ef%bc%9f.md" id="31 为什么 Map 桶中超过 8 个才转为红黑树？.md">31 为什么 Map 桶中超过 8 个才转为红黑树？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/32%20%e5%90%8c%e6%a0%b7%e6%98%af%e7%ba%bf%e7%a8%8b%e5%ae%89%e5%85%a8%ef%bc%8cConcurrentHashMap%20%e5%92%8c%20Hashtable%20%e7%9a%84%e5%8c%ba%e5%88%ab.md" id="32 同样是线程安全，ConcurrentHashMap 和 Hashtable 的区别.md">32 同样是线程安全，ConcurrentHashMap 和 Hashtable 的区别.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/33%20CopyOnWriteArrayList%20%e6%9c%89%e4%bb%80%e4%b9%88%e7%89%b9%e7%82%b9%ef%bc%9f.md" id="33 CopyOnWriteArrayList 有什么特点？.md">33 CopyOnWriteArrayList 有什么特点？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/34%20%e4%bb%80%e4%b9%88%e6%98%af%e9%98%bb%e5%a1%9e%e9%98%9f%e5%88%97%ef%bc%9f.md" id="34 什么是阻塞队列？.md">34 什么是阻塞队列？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/35%20%e9%98%bb%e5%a1%9e%e9%98%9f%e5%88%97%e5%8c%85%e5%90%ab%e5%93%aa%e4%ba%9b%e5%b8%b8%e7%94%a8%e7%9a%84%e6%96%b9%e6%b3%95%ef%bc%9fadd%e3%80%81offer%e3%80%81put%20%e7%ad%89%e6%96%b9%e6%b3%95%e7%9a%84%e5%8c%ba%e5%88%ab%ef%bc%9f.md" id="35 阻塞队列包含哪些常用的方法？add、offer、put 等方法的区别？.md">35 阻塞队列包含哪些常用的方法？add、offer、put 等方法的区别？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/36%20%e6%9c%89%e5%93%aa%e5%87%a0%e7%a7%8d%e5%b8%b8%e8%a7%81%e7%9a%84%e9%98%bb%e5%a1%9e%e9%98%9f%e5%88%97%ef%bc%9f.md" id="36 有哪几种常见的阻塞队列？.md">36 有哪几种常见的阻塞队列？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/37%20%e9%98%bb%e5%a1%9e%e5%92%8c%e9%9d%9e%e9%98%bb%e5%a1%9e%e9%98%9f%e5%88%97%e7%9a%84%e5%b9%b6%e5%8f%91%e5%ae%89%e5%85%a8%e5%8e%9f%e7%90%86%e6%98%af%e4%bb%80%e4%b9%88%ef%bc%9f.md" id="37 阻塞和非阻塞队列的并发安全原理是什么？.md">37 阻塞和非阻塞队列的并发安全原理是什么？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/38%20%e5%a6%82%e4%bd%95%e9%80%89%e6%8b%a9%e9%80%82%e5%90%88%e8%87%aa%e5%b7%b1%e7%9a%84%e9%98%bb%e5%a1%9e%e9%98%9f%e5%88%97%ef%bc%9f.md" id="38 如何选择适合自己的阻塞队列？.md">38 如何选择适合自己的阻塞队列？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/39%20%e5%8e%9f%e5%ad%90%e7%b1%bb%e6%98%af%e5%a6%82%e4%bd%95%e5%88%a9%e7%94%a8%20CAS%20%e4%bf%9d%e8%af%81%e7%ba%bf%e7%a8%8b%e5%ae%89%e5%85%a8%e7%9a%84%ef%bc%9f.md" id="39 原子类是如何利用 CAS 保证线程安全的？.md">39 原子类是如何利用 CAS 保证线程安全的？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/40%20AtomicInteger%20%e5%9c%a8%e9%ab%98%e5%b9%b6%e5%8f%91%e4%b8%8b%e6%80%a7%e8%83%bd%e4%b8%8d%e5%a5%bd%ef%bc%8c%e5%a6%82%e4%bd%95%e8%a7%a3%e5%86%b3%ef%bc%9f%e4%b8%ba%e4%bb%80%e4%b9%88%ef%bc%9f.md" id="40 AtomicInteger 在高并发下性能不好，如何解决？为什么？.md">40 AtomicInteger 在高并发下性能不好，如何解决？为什么？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/41%20%e5%8e%9f%e5%ad%90%e7%b1%bb%e5%92%8c%20volatile%20%e6%9c%89%e4%bb%80%e4%b9%88%e5%bc%82%e5%90%8c%ef%bc%9f.md" id="41 原子类和 volatile 有什么异同？.md">41 原子类和 volatile 有什么异同？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/42%20AtomicInteger%20%e5%92%8c%20synchronized%20%e7%9a%84%e5%bc%82%e5%90%8c%e7%82%b9%ef%bc%9f.md" id="42 AtomicInteger 和 synchronized 的异同点？.md">42 AtomicInteger 和 synchronized 的异同点？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/43%20Java%208%20%e4%b8%ad%20Adder%20%e5%92%8c%20Accumulator%20%e6%9c%89%e4%bb%80%e4%b9%88%e5%8c%ba%e5%88%ab%ef%bc%9f.md" id="43 Java 8 中 Adder 和 Accumulator 有什么区别？.md">43 Java 8 中 Adder 和 Accumulator 有什么区别？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/44%20ThreadLocal%20%e9%80%82%e5%90%88%e7%94%a8%e5%9c%a8%e5%93%aa%e4%ba%9b%e5%ae%9e%e9%99%85%e7%94%9f%e4%ba%a7%e7%9a%84%e5%9c%ba%e6%99%af%e4%b8%ad%ef%bc%9f.md" id="44 ThreadLocal 适合用在哪些实际生产的场景中？.md">44 ThreadLocal 适合用在哪些实际生产的场景中？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/45%20ThreadLocal%20%e6%98%af%e7%94%a8%e6%9d%a5%e8%a7%a3%e5%86%b3%e5%85%b1%e4%ba%ab%e8%b5%84%e6%ba%90%e7%9a%84%e5%a4%9a%e7%ba%bf%e7%a8%8b%e8%ae%bf%e9%97%ae%e7%9a%84%e9%97%ae%e9%a2%98%e5%90%97%ef%bc%9f.md" id="45 ThreadLocal 是用来解决共享资源的多线程访问的问题吗？.md">45 ThreadLocal 是用来解决共享资源的多线程访问的问题吗？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/46%20%e5%a4%9a%e4%b8%aa%20ThreadLocal%20%e5%9c%a8%20Thread%20%e4%b8%ad%e7%9a%84%20threadlocals%20%e9%87%8c%e6%98%af%e6%80%8e%e4%b9%88%e5%ad%98%e5%82%a8%e7%9a%84%ef%bc%9f.md" id="46 多个 ThreadLocal 在 Thread 中的 threadlocals 里是怎么存储的？.md">46 多个 ThreadLocal 在 Thread 中的 threadlocals 里是怎么存储的？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/47%20%e5%86%85%e5%ad%98%e6%b3%84%e6%bc%8f%e2%80%94%e2%80%94%e4%b8%ba%e4%bd%95%e6%af%8f%e6%ac%a1%e7%94%a8%e5%ae%8c%20ThreadLocal%20%e9%83%bd%e8%a6%81%e8%b0%83%e7%94%a8%20remove%28%29%ef%bc%9f.md" id="47 内存泄漏——为何每次用完 ThreadLocal 都要调用 remove()？.md">47 内存泄漏——为何每次用完 ThreadLocal 都要调用 remove()？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/48%20Callable%20%e5%92%8c%20Runnable%20%e7%9a%84%e4%b8%8d%e5%90%8c%ef%bc%9f.md" id="48 Callable 和 Runnable 的不同？.md">48 Callable 和 Runnable 的不同？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/49%20Future%20%e7%9a%84%e4%b8%bb%e8%a6%81%e5%8a%9f%e8%83%bd%e6%98%af%e4%bb%80%e4%b9%88%ef%bc%9f.md" id="49 Future 的主要功能是什么？.md">49 Future 的主要功能是什么？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/50%20%e4%bd%bf%e7%94%a8%20Future%20%e6%9c%89%e5%93%aa%e4%ba%9b%e6%b3%a8%e6%84%8f%e7%82%b9%ef%bc%9fFuture%20%e4%ba%a7%e7%94%9f%e6%96%b0%e7%9a%84%e7%ba%bf%e7%a8%8b%e4%ba%86%e5%90%97%ef%bc%9f.md" id="50 使用 Future 有哪些注意点？Future 产生新的线程了吗？.md">50 使用 Future 有哪些注意点？Future 产生新的线程了吗？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/51%20%e5%a6%82%e4%bd%95%e5%88%a9%e7%94%a8%20CompletableFuture%20%e5%ae%9e%e7%8e%b0%e2%80%9c%e6%97%85%e6%b8%b8%e5%b9%b3%e5%8f%b0%e2%80%9d%e9%97%ae%e9%a2%98%ef%bc%9f.md" id="51 如何利用 CompletableFuture 实现“旅游平台”问题？.md">51 如何利用 CompletableFuture 实现“旅游平台”问题？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/52%20%e4%bf%a1%e5%8f%b7%e9%87%8f%e8%83%bd%e8%a2%ab%20FixedThreadPool%20%e6%9b%bf%e4%bb%a3%e5%90%97%ef%bc%9f.md" id="52 信号量能被 FixedThreadPool 替代吗？.md">52 信号量能被 FixedThreadPool 替代吗？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/53%20CountDownLatch%20%e6%98%af%e5%a6%82%e4%bd%95%e5%ae%89%e6%8e%92%e7%ba%bf%e7%a8%8b%e6%89%a7%e8%a1%8c%e9%a1%ba%e5%ba%8f%e7%9a%84%ef%bc%9f.md" id="53 CountDownLatch 是如何安排线程执行顺序的？.md">53 CountDownLatch 是如何安排线程执行顺序的？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/54%20CyclicBarrier%20%e5%92%8c%20CountdownLatch%20%e6%9c%89%e4%bb%80%e4%b9%88%e5%bc%82%e5%90%8c%ef%bc%9f.md" id="54 CyclicBarrier 和 CountdownLatch 有什么异同？.md">54 CyclicBarrier 和 CountdownLatch 有什么异同？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/55%20Condition%e3%80%81object.wait%28%29%20%e5%92%8c%20notify%28%29%20%e7%9a%84%e5%85%b3%e7%b3%bb%ef%bc%9f.md" id="55 Condition、object.wait() 和 notify() 的关系？.md">55 Condition、object.wait() 和 notify() 的关系？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/56%20%e8%ae%b2%e4%b8%80%e8%ae%b2%e4%bb%80%e4%b9%88%e6%98%af%20Java%20%e5%86%85%e5%ad%98%e6%a8%a1%e5%9e%8b%ef%bc%9f.md" id="56 讲一讲什么是 Java 内存模型？.md">56 讲一讲什么是 Java 内存模型？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/57%20%e4%bb%80%e4%b9%88%e6%98%af%e6%8c%87%e4%bb%a4%e9%87%8d%e6%8e%92%e5%ba%8f%ef%bc%9f%e4%b8%ba%e4%bb%80%e4%b9%88%e8%a6%81%e9%87%8d%e6%8e%92%e5%ba%8f%ef%bc%9f.md" id="57 什么是指令重排序？为什么要重排序？.md">57 什么是指令重排序？为什么要重排序？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/58%20Java%20%e4%b8%ad%e7%9a%84%e5%8e%9f%e5%ad%90%e6%93%8d%e4%bd%9c%e6%9c%89%e5%93%aa%e4%ba%9b%e6%b3%a8%e6%84%8f%e4%ba%8b%e9%a1%b9%ef%bc%9f.md" id="58 Java 中的原子操作有哪些注意事项？.md">58 Java 中的原子操作有哪些注意事项？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/59%20%e4%bb%80%e4%b9%88%e6%98%af%e2%80%9c%e5%86%85%e5%ad%98%e5%8f%af%e8%a7%81%e6%80%a7%e2%80%9d%e9%97%ae%e9%a2%98%ef%bc%9f.md" id="59 什么是“内存可见性”问题？.md">59 什么是“内存可见性”问题？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/60%20%e4%b8%bb%e5%86%85%e5%ad%98%e5%92%8c%e5%b7%a5%e4%bd%9c%e5%86%85%e5%ad%98%e7%9a%84%e5%85%b3%e7%b3%bb%ef%bc%9f.md" id="60 主内存和工作内存的关系？.md">60 主内存和工作内存的关系？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/61%20%e4%bb%80%e4%b9%88%e6%98%af%20happens-before%20%e8%a7%84%e5%88%99%ef%bc%9f.md" id="61 什么是 happens-before 规则？.md">61 什么是 happens-before 规则？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/62%20volatile%20%e7%9a%84%e4%bd%9c%e7%94%a8%e6%98%af%e4%bb%80%e4%b9%88%ef%bc%9f%e4%b8%8e%20synchronized%20%e6%9c%89%e4%bb%80%e4%b9%88%e5%bc%82%e5%90%8c%ef%bc%9f.md" id="62 volatile 的作用是什么？与 synchronized 有什么异同？.md">62 volatile 的作用是什么？与 synchronized 有什么异同？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/63%20%e5%8d%95%e4%be%8b%e6%a8%a1%e5%bc%8f%e7%9a%84%e5%8f%8c%e9%87%8d%e6%a3%80%e6%9f%a5%e9%94%81%e6%a8%a1%e5%bc%8f%e4%b8%ba%e4%bb%80%e4%b9%88%e5%bf%85%e9%a1%bb%e5%8a%a0%20volatile%ef%bc%9f.md" id="63 单例模式的双重检查锁模式为什么必须加 volatile？.md">63 单例模式的双重检查锁模式为什么必须加 volatile？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/64%20%e4%bd%a0%e7%9f%a5%e9%81%93%e4%bb%80%e4%b9%88%e6%98%af%20CAS%20%e5%90%97%ef%bc%9f.md" id="64 你知道什么是 CAS 吗？.md">64 你知道什么是 CAS 吗？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/65%20CAS%20%e5%92%8c%e4%b9%90%e8%a7%82%e9%94%81%e7%9a%84%e5%85%b3%e7%b3%bb%ef%bc%8c%e4%bb%80%e4%b9%88%e6%97%b6%e5%80%99%e4%bc%9a%e7%94%a8%e5%88%b0%20CAS%ef%bc%9f.md" id="65 CAS 和乐观锁的关系，什么时候会用到 CAS？.md">65 CAS 和乐观锁的关系，什么时候会用到 CAS？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/66%20CAS%20%e6%9c%89%e4%bb%80%e4%b9%88%e7%bc%ba%e7%82%b9%ef%bc%9f.md" id="66 CAS 有什么缺点？.md">66 CAS 有什么缺点？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/67%20%e5%a6%82%e4%bd%95%e5%86%99%e4%b8%80%e4%b8%aa%e5%bf%85%e7%84%b6%e6%ad%bb%e9%94%81%e7%9a%84%e4%be%8b%e5%ad%90%ef%bc%9f.md" id="67 如何写一个必然死锁的例子？.md">67 如何写一个必然死锁的例子？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/68%20%e5%8f%91%e7%94%9f%e6%ad%bb%e9%94%81%e5%bf%85%e9%a1%bb%e6%bb%a1%e8%b6%b3%e5%93%aa%204%20%e4%b8%aa%e6%9d%a1%e4%bb%b6%ef%bc%9f.md" id="68 发生死锁必须满足哪 4 个条件？.md">68 发生死锁必须满足哪 4 个条件？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/69%20%e5%a6%82%e4%bd%95%e7%94%a8%e5%91%bd%e4%bb%a4%e8%a1%8c%e5%92%8c%e4%bb%a3%e7%a0%81%e5%ae%9a%e4%bd%8d%e6%ad%bb%e9%94%81%ef%bc%9f.md" id="69 如何用命令行和代码定位死锁？.md">69 如何用命令行和代码定位死锁？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/70%20%e6%9c%89%e5%93%aa%e4%ba%9b%e8%a7%a3%e5%86%b3%e6%ad%bb%e9%94%81%e9%97%ae%e9%a2%98%e7%9a%84%e7%ad%96%e7%95%a5%ef%bc%9f.md" id="70 有哪些解决死锁问题的策略？.md">70 有哪些解决死锁问题的策略？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/71%20%e8%ae%b2%e4%b8%80%e8%ae%b2%e7%bb%8f%e5%85%b8%e7%9a%84%e5%93%b2%e5%ad%a6%e5%ae%b6%e5%b0%b1%e9%a4%90%e9%97%ae%e9%a2%98.md" id="71 讲一讲经典的哲学家就餐问题.md">71 讲一讲经典的哲学家就餐问题.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/72%20final%20%e7%9a%84%e4%b8%89%e7%a7%8d%e7%94%a8%e6%b3%95%e6%98%af%e4%bb%80%e4%b9%88%ef%bc%9f.md" id="72 final 的三种用法是什么？.md">72 final 的三种用法是什么？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/73%20%e4%b8%ba%e4%bb%80%e4%b9%88%e5%8a%a0%e4%ba%86%20final%20%e5%8d%b4%e4%be%9d%e7%84%b6%e6%97%a0%e6%b3%95%e6%8b%a5%e6%9c%89%e2%80%9c%e4%b8%8d%e5%8f%98%e6%80%a7%e2%80%9d%ef%bc%9f.md" id="73 为什么加了 final 却依然无法拥有“不变性”？.md">73 为什么加了 final 却依然无法拥有“不变性”？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/74%20%e4%b8%ba%e4%bb%80%e4%b9%88%20String%20%e8%a2%ab%e8%ae%be%e8%ae%a1%e4%b8%ba%e6%98%af%e4%b8%8d%e5%8f%af%e5%8f%98%e7%9a%84%ef%bc%9f.md" id="74 为什么 String 被设计为是不可变的？.md">74 为什么 String 被设计为是不可变的？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/75%20%e4%b8%ba%e4%bb%80%e4%b9%88%e9%9c%80%e8%a6%81%20AQS%ef%bc%9fAQS%20%e7%9a%84%e4%bd%9c%e7%94%a8%e5%92%8c%e9%87%8d%e8%a6%81%e6%80%a7%e6%98%af%e4%bb%80%e4%b9%88%ef%bc%9f.md" id="75 为什么需要 AQS？AQS 的作用和重要性是什么？.md">75 为什么需要 AQS？AQS 的作用和重要性是什么？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/76%20AQS%20%e7%9a%84%e5%86%85%e9%83%a8%e5%8e%9f%e7%90%86%e6%98%af%e4%bb%80%e4%b9%88%e6%a0%b7%e7%9a%84%ef%bc%9f.md" id="76 AQS 的内部原理是什么样的？.md">76 AQS 的内部原理是什么样的？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/77%20AQS%20%e5%9c%a8%20CountDownLatch%20%e7%ad%89%e7%b1%bb%e4%b8%ad%e7%9a%84%e5%ba%94%e7%94%a8%e5%8e%9f%e7%90%86%e6%98%af%e4%bb%80%e4%b9%88%ef%bc%9f.md" id="77 AQS 在 CountDownLatch 等类中的应用原理是什么？.md">77 AQS 在 CountDownLatch 等类中的应用原理是什么？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/Java%20%e5%b9%b6%e5%8f%91%e7%bc%96%e7%a8%8b%2078%20%e8%ae%b2-%e5%ae%8c/78%20%e4%b8%80%e4%bb%bd%e7%8b%ac%e5%ae%b6%e7%9a%84%20Java%20%e5%b9%b6%e5%8f%91%e5%b7%a5%e5%85%b7%e5%9b%be%e8%b0%b1.md" id="78 一份独家的 Java 并发工具图谱.md">78 一份独家的 Java 并发工具图谱.md</a>
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
<h1 class="title" data-id="56 讲一讲什么是 Java 内存模型？" id="title">56 讲一讲什么是 Java 内存模型？</h1>
<div><p>本课时我们主要介绍什么是 Java 内存模型？</p>
<p>从本课时开始，我们会进入到 Java 内存模型的学习。如果你想了解 Java 并发的底层原理，那么 Java 内存模型的知识非常重要，同时也是一个分水岭，可以区分出我们是仅停留在如何使用并发工具，还是能更进一步，知其所以然。</p>
<h2 id="容易混淆-jvm-内存结构-vs-java-内存模型"><strong>容易混淆：JVM 内存结构 VS Java 内存模型</strong></h2>
<p>Java 作为一种面向对象的语言，有很多概念，从名称上看起来比较相似，比如 JVM 内存结构、Java 内存模型，这是两个截然不同的概念，但是很容易混淆。网络上也有不少讲 Java 内存模型的文章，其实写的是 JVM 内存结构。</p>
<p>所以我们就先从整体上概括一下这两者的主要作用：</p>
<ul>
<li>JVM 内存结构和 Java 虚拟机的运行时区域有关；</li>
<li>Java 内存模型和 Java 的并发编程有关。</li>
</ul>
<p>所以可以看出，这两个概念其实是有很大区别的。下面我们先来简要介绍一下 JVM 内存结构。</p>
<h3 id="jvm-内存结构"><strong>JVM 内存结构</strong></h3>
<p>我们都知道，Java 代码是要运行在虚拟机上的，而虚拟机在执行 Java 程序的过程中会把所管理的内存划分为若干个不同的数据区域，这些区域都有各自的用途。在《Java 虚拟机规范（Java SE 8）》中描述了 JVM 运行时内存区域结构可分为以下 6 个区。</p>
<p><strong>堆区（</strong><strong>Heap</strong><strong>）</strong><strong>：</strong>堆是存储类实例和数组的，通常是内存中最大的一块。实例很好理解，比如 new Object() 就会生成一个实例；而数组也是保存在堆上面的，因为在 Java 中，数组也是对象。</p>
<p><strong>虚拟机栈（</strong><strong>Java Virtual Machine Stacks</strong><strong>）</strong><strong>：</strong>它保存局部变量和部分结果，并在方法调用和返回中起作用。</p>
<p><strong>方法区（</strong><strong>Method Area</strong><strong>）</strong><strong>：</strong>它存储每个类的结构，例如运行时的常量池、字段和方法数据，以及方法和构造函数的代码，包括用于类初始化以及接口初始化的特殊方法。</p>
<p><strong>本地方法栈（</strong><strong>Native Method Stacks</strong><strong>）</strong><strong>：</strong>与虚拟机栈基本类似，区别在于虚拟机栈为虚拟机执行的 Java 方法服务，而本地方法栈则是为 Native 方法服务。</p>
<p><strong>程序计数器（</strong><strong>The PC Register</strong><strong>）</strong><strong>：</strong>是最小的一块内存区域，它的作用通常是保存当前正在执行的 JVM 指令地址。</p>
<p><strong>运行时常量池</strong><strong>（Run-Time Constant Pool）：</strong>是方法区的一部分，包含多种常量，范围从编译时已知的数字到必须在运行时解析的方法和字段引用。</p>
<p>注意，以上是 Java 虚拟机规范，不同的虚拟机实现会各有不同，一般会遵守规范。</p>
<p>这里总结一下，JVM 内存结构是由 Java 虚拟机规范定义的，描述的是在 Java 程序执行过程中，由 JVM 管理的不同数据区域，各个区域有其特定的功能。官方的<a href="https://docs.oracle.com/javase/specs/jvms/se8/html/jvms-2.html" target="_blank">规范地址</a><a href="https://docs.oracle.com/javase/specs/jvms/se8/html/jvms-2.html" target="_blank">请点击这里</a>查看。</p>
<h2 id="从-java-代码到-cpu-指令"><strong>从 Java 代码到 CPU 指令</strong></h2>
<p>看完了 JVM 内存结构，就让我们回到 Java 内存模型上来。我们都知道，编写的 Java 代码，最终还是要转化为 CPU 指令才能执行的。为了理解 Java 内存模型的作用，我们首先就来回顾一下从 Java 代码到最终执行的 CPU 指令的大致流程：</p>
<ul>
<li>最开始，我们编写的 Java 代码，是 *.java 文件；</li>
<li>在编译（包含词法分析、语义分析等步骤）后，在刚才的 <em>.java 文件之外，会多出一个新的 Java 字节码文件（</em>.class）；</li>
<li>JVM 会分析刚才生成的字节码文件（*.class），并根据平台等因素，把字节码文件转化为具体平台上的<strong>机器指令；</strong></li>
<li>机器指令则可以直接在 CPU 上运行，也就是最终的程序执行。</li>
</ul>
<h2 id="为什么需要-jmm-java-memory-model-java-内存模型"><strong>为什么需要 JMM</strong>（Java Memory Model，<strong>Java 内存模型）</strong></h2>
<p>在更早期的语言中，其实是不存在内存模型的概念的。</p>
<p>所以程序最终执行的效果会依赖于具体的处理器，而不同的处理器的规则又不一样，不同的处理器之间可能差异很大，因此同样的一段代码，可能在处理器 A 上运行正常，而在处理器 B 上运行的结果却不一致。同理，在没有 JMM 之前，不同的 JVM 的实现，也会带来不一样的“翻译”结果。</p>
<p>所以 Java 非常需要一个标准，来让 Java 开发者、编译器工程师和 JVM 工程师能够达成一致。达成一致后，我们就可以很清楚的知道什么样的代码最终可以达到什么样的运行效果，让多线程运行结果可以预期，这个标准就是 JMM<strong>，</strong>这就是需要 JMM 的原因。</p>
<p>我们本课时将突破 Java 代码的层次，开始往下钻研，研究从 Java 代码到 CPU 指令的这个转化过程要遵守哪些和并发相关的原则和规范，这就是 JMM 的重点内容。如果不加以规范，那么同样的 Java 代码，完全可能产生不一样的执行效果，那是不可接受的，这也违背了 Java “书写一次、到处运行”的特点。</p>
<h2 id="jmm-是什么"><strong>JMM</strong> <strong>是什么</strong></h2>
<p>有了上面的铺垫，下面我们就介绍一下究竟什么是 JMM。</p>
<h3 id="jmm-是规范"><strong>JMM 是规范</strong></h3>
<p>JMM 是和多线程相关的<strong>一组规范</strong>，需要各个 JVM 的实现来遵守 JMM 规范，以便于开发者可以利用这些规范，更方便地开发多线程程序。这样一来，即便同一个程序在不同的虚拟机上运行，得到的程序结果也是一致的。</p>
<p>如果没有 JMM 内存模型来规范，那么很可能在经过了不同 JVM 的“翻译”之后，导致在不同的虚拟机上运行的结果不一样，那是很大的问题。</p>
<p>因此，JMM 与处理器、缓存、并发、编译器有关。它解决了 CPU 多级缓存、处理器优化、指令重排等导致的结果不可预期的问题。</p>
<h3 id="jmm-是工具类和关键字的原理"><strong>JMM  是工具类和关键字的原理</strong></h3>
<p>之前我们使用了各种同步工具和关键字，包括 volatile、synchronized、Lock 等，其实它们的原理都涉及 JMM。正是 JMM 的参与和帮忙，才让各个同步工具和关键字能够发挥作用，帮我们开发出并发安全的程序。</p>
<p>比如我们写了关键字 synchronized，JVM 就会在 JMM 的规则下，“翻译”出合适的指令，包括限制指令之间的顺序，以便在即使发生了重排序的情况下，也能保证必要的“可见性”，这样一来，不同的 JVM 对于相同的代码的执行结果就变得可预期了，我们 Java 程序员就只需要用同步工具和关键字就可以开发出正确的并发程序了，这都要感谢 JMM。</p>
<p>JMM 里最重要 3 点内容，分别是：<strong>重排序、原子性、内存可见性</strong>。这三个部分的内容，后面我们会详细展开。</p>
<h2 id="总结">总结</h2>
<p>以上就是本课时的内容了。本课时，我们先对 JVM 内存结构和 Java 内存模型这两个容易混淆的概念进行了辨析，然后从宏观层面讲解了什么是 Java 内存模型，接下来，我们的脚步从 Java 代码逐渐往下探索，解释了为什么需要 JMM 以及什么是 JMM。</p>
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
<p>© 2019 - 2023 <a href="/cdn-cgi/l/email-protection#e38f8f8fdad7d2d2d3d4a3848e828a8fcd808c8e" target="_blank">Liangliang Lee</a>.
                    Powered by <a href="https://github.com/gin-gonic/gin" target="_blank">gin</a> and <a href="https://github.com/kaiiiz/hexo-theme-book" target="_blank">hexo-theme-book</a>.</p>
</div>
</div>
<a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script>(function(){function c(){var b=a.contentDocument||a.contentWindow.document;if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'8f0ae43dd88b8500',t:'MTczMzk3NjkwOC4wMDAwMDA='};var a=document.createElement('script');a.nonce='';a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();</script></body>

<script src="/static/index.js"></script>
</head></html>