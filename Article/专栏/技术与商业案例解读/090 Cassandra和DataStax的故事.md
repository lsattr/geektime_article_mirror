<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
<meta content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no" name="viewport"/>
<meta content="zh-cn" http-equiv="content-language"/>
<meta content="090 Cassandra和DataStax的故事" name="description"/>
<link href="/static/favicon.png" rel="icon"/>
<title>090 Cassandra和DataStax的故事 </title>
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
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/000%20%e5%bc%80%e7%af%87%e8%af%8d%20%e7%aa%81%e7%a0%b4%e6%8a%80%e6%9c%af%e6%80%9d%e7%bb%b4%ef%bc%8c%e7%ab%99%e5%9c%a8%e5%95%86%e4%b8%9a%e7%9a%84%e8%a7%92%e5%ba%a6%e7%9c%8b%e9%97%ae%e9%a2%98.md" id="000 开篇词 突破技术思维，站在商业的角度看问题.md">000 开篇词 突破技术思维，站在商业的角度看问题.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/001%20%e8%a5%bf%e9%9b%85%e5%9b%beIT%e5%85%ac%e5%8f%b8%e4%b9%8bRealNetworks%ef%bc%9a%e4%b8%80%e4%b8%aa%e5%b8%9d%e5%9b%bd%e7%9a%84%e5%85%b4%e8%a1%b0%ef%bc%88%e4%b8%8a%ef%bc%89.md" id="001 西雅图IT公司之RealNetworks：一个帝国的兴衰（上）.md">001 西雅图IT公司之RealNetworks：一个帝国的兴衰（上）.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/002%20%e8%a5%bf%e9%9b%85%e5%9b%beIT%e5%85%ac%e5%8f%b8%e4%b9%8bRealNetworks%ef%bc%9a%e4%b8%80%e4%b8%aa%e5%b8%9d%e5%9b%bd%e7%9a%84%e5%85%b4%e8%a1%b0%ef%bc%88%e4%b8%8b%ef%bc%89.md" id="002 西雅图IT公司之RealNetworks：一个帝国的兴衰（下）.md">002 西雅图IT公司之RealNetworks：一个帝国的兴衰（下）.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/003%20%e4%bb%a5RealNetworks%e4%b8%ba%e4%be%8b%ef%bc%8c%e8%b0%88%e8%b0%88%e5%88%9d%e5%88%9b%e5%85%ac%e5%8f%b8%e5%a6%82%e4%bd%95%e5%ba%94%e5%af%b9%e5%b7%a8%e5%a4%b4%e7%a2%be%e5%8e%8b.md" id="003 以RealNetworks为例，谈谈初创公司如何应对巨头碾压.md">003 以RealNetworks为例，谈谈初创公司如何应对巨头碾压.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/004%20%e5%8f%af%e8%a7%86%e5%8c%96%e5%88%86%e6%9e%90%e9%bc%bb%e7%a5%96Tableau.md" id="004 可视化分析鼻祖Tableau.md">004 可视化分析鼻祖Tableau.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/005%20%e4%bb%8eTableau%e4%b8%8a%e5%b8%82%ef%bc%8c%e7%9c%8b%e5%ad%a6%e6%9c%af%e7%95%8c%e5%92%8c%e5%b7%a5%e4%b8%9a%e7%95%8c%e4%ba%ba%e5%a3%ab%e5%88%9b%e4%b8%9a.md" id="005 从Tableau上市，看学术界和工业界人士创业.md">005 从Tableau上市，看学术界和工业界人士创业.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/006%20%e5%9c%a8%e7%ba%bf%e6%97%85%e6%b8%b8%e5%b8%9d%e5%9b%bdExpedia%e5%b4%9b%e8%b5%b7%e7%9a%84%e8%83%8c%e5%90%8e.md" id="006 在线旅游帝国Expedia崛起的背后.md">006 在线旅游帝国Expedia崛起的背后.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/007%20%e6%88%bf%e4%ba%a7%e7%bb%8f%e7%ba%aa%e7%9a%84%e9%a2%a0%e8%a6%86%e8%80%85Redfin%ef%bc%9a%e5%9c%a8%e2%80%9c%e4%bc%a0%e7%bb%9f%e2%80%9d%e4%b8%8e%e2%80%9c%e7%8e%b0%e4%bb%a3%e2%80%9d%e9%97%b4%e5%be%98%e5%be%8a.md" id="007 房产经纪的颠覆者Redfin：在“传统”与“现代”间徘徊.md">007 房产经纪的颠覆者Redfin：在“传统”与“现代”间徘徊.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/008%20%e6%88%bf%e4%ba%a7%e7%bb%8f%e7%ba%aa%e7%9a%84%e2%80%9c%e5%8d%8f%e4%bd%9c%e8%80%85%e2%80%9dZillow%ef%bc%9a%e4%b8%80%e4%b8%aa%e5%9c%b0%e4%ba%a7%e6%95%b0%e6%8d%ae%e5%b9%b3%e5%8f%b0.md" id="008 房产经纪的“协作者”Zillow：一个地产数据平台.md">008 房产经纪的“协作者”Zillow：一个地产数据平台.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/009%20%e9%a2%a0%e8%a6%86%e8%bf%98%e6%98%af%e5%8d%8f%e4%bd%9c%ef%bc%8c%e6%88%bf%e5%9c%b0%e4%ba%a7%e5%b8%82%e5%9c%ba%e4%b8%8aRedfin%e5%92%8cZillow%e7%9a%84%e6%8a%89%e6%8b%a9.md" id="009 颠覆还是协作，房地产市场上Redfin和Zillow的抉择.md">009 颠覆还是协作，房地产市场上Redfin和Zillow的抉择.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/010%20%e5%ba%94%e7%94%a8%e4%ba%a4%e4%bb%98%e7%bd%91%e7%bb%9c%e5%a4%a7%e5%8e%82F5%ef%bc%9a%e2%80%9c%e4%b8%80%e6%8b%9b%e9%b2%9c%e2%80%9d%e4%b9%8b%e6%ae%87.md" id="010 应用交付网络大厂F5：“一招鲜”之殇.md">010 应用交付网络大厂F5：“一招鲜”之殇.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/011%20%e5%9c%a8%e7%ba%bf%e5%b7%ae%e6%97%85%e6%8a%a5%e9%94%80%e9%bc%bb%e7%a5%96Concur%ef%bc%9a%e5%9c%a8%e8%bd%ac%e5%9e%8b%e4%b8%ad%e8%8e%b7%e5%be%97%e5%8f%91%e5%b1%95.md" id="011 在线差旅报销鼻祖Concur：在转型中获得发展.md">011 在线差旅报销鼻祖Concur：在转型中获得发展.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/012%20%e6%bc%ab%e8%b0%88%e4%bc%81%e4%b8%9a%e8%bd%ac%e5%9e%8b%ef%bc%9a%e5%9c%a8%e5%b8%82%e5%9c%ba%e5%8f%98%e8%bf%81%e4%b8%ad%e5%af%bb%e6%89%be%e7%94%9f%e6%9c%ba.md" id="012 漫谈企业转型：在市场变迁中寻找生机.md">012 漫谈企业转型：在市场变迁中寻找生机.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/013%20%e5%85%8b%e9%9b%b7%e5%85%ac%e5%8f%b8%e6%b2%89%e6%b5%ae%e5%bd%95%ef%bc%9a%e8%a1%8c%e8%b5%b0%e5%9c%a8%e8%b6%85%e7%ba%a7%e8%ae%a1%e7%ae%97%e6%9c%ba%e5%b8%82%e5%9c%ba.md" id="013 克雷公司沉浮录：行走在超级计算机市场.md">013 克雷公司沉浮录：行走在超级计算机市场.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/014%20%e2%80%9c%e5%8d%95%e4%b8%80%e5%8c%96%e2%80%9d%e7%9a%84%e9%9a%90%e5%bf%a7%ef%bc%9a%e4%bb%8e%e5%85%8b%e9%9b%b7%e5%85%ac%e5%8f%b8%e7%9c%8b%e2%80%9c%e4%b8%80%e6%9d%a1%e8%85%bf%e8%b5%b0%e8%b7%af%e2%80%9d.md" id="014 “单一化”的隐忧：从克雷公司看“一条腿走路”.md">014 “单一化”的隐忧：从克雷公司看“一条腿走路”.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/015%20Halo%e7%9a%84%e5%bc%80%e5%8f%91%e8%80%85Bungie%ef%bc%9a%e4%b8%8e%e5%be%ae%e8%bd%af%e7%9a%84%e8%81%9a%e6%95%a3.md" id="015 Halo的开发者Bungie：与微软的聚散.md">015 Halo的开发者Bungie：与微软的聚散.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/016%20%e2%80%9c%e5%8d%96%e8%ba%ab%e2%80%9d%e9%a1%bb%e8%b0%a8%e6%85%8e%ef%bc%9a%e5%88%9b%e4%b8%9a%e5%85%ac%e5%8f%b8%e9%9d%a2%e4%b8%b4%e7%9a%84%e6%8a%89%e6%8b%a9.md" id="016 “卖身”须谨慎：创业公司面临的抉择.md">016 “卖身”须谨慎：创业公司面临的抉择.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/017%20%e4%ba%9a%e9%a9%ac%e9%80%8a%e9%a2%86%e5%af%bc%e5%8a%9b%e5%87%86%e5%88%99%e4%b9%8b%e8%a6%81%e6%9c%89%e7%a1%ac%e9%aa%a8%e5%a4%b4.md" id="017 亚马逊领导力准则之要有硬骨头.md">017 亚马逊领导力准则之要有硬骨头.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/018%20%e4%ba%9a%e9%a9%ac%e9%80%8a%e9%a2%86%e5%af%bc%e5%8a%9b%e5%87%86%e5%88%99%e4%b9%8b%e5%86%b3%e7%ad%96%e6%ad%a3%e7%a1%ae.md" id="018 亚马逊领导力准则之决策正确.md">018 亚马逊领导力准则之决策正确.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/019%20%e4%ba%9a%e9%a9%ac%e9%80%8a%e9%a2%86%e5%af%bc%e5%8a%9b%e5%87%86%e5%88%99%e4%b9%8b%e5%ae%a2%e6%88%b7%e8%87%b3%e5%b0%9a.md" id="019 亚马逊领导力准则之客户至尚.md">019 亚马逊领导力准则之客户至尚.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/020%20%e4%ba%9a%e9%a9%ac%e9%80%8a%e9%a2%86%e5%af%bc%e5%8a%9b%e5%87%86%e5%88%99%e4%b9%8b%e5%8b%a4%e4%bf%ad%e8%8a%82%e7%ba%a6.md" id="020 亚马逊领导力准则之勤俭节约.md">020 亚马逊领导力准则之勤俭节约.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/021%20%e4%ba%9a%e9%a9%ac%e9%80%8a%e9%a2%86%e5%af%bc%e5%8a%9b%e5%87%86%e5%88%99%e4%b9%8b%e4%b8%bb%e4%ba%ba%e7%bf%81%e7%b2%be%e7%a5%9e.md" id="021 亚马逊领导力准则之主人翁精神.md">021 亚马逊领导力准则之主人翁精神.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/022%20%e4%ba%9a%e9%a9%ac%e9%80%8a%e9%a2%86%e5%af%bc%e5%8a%9b%e5%87%86%e5%88%99%e4%b9%8b%e9%80%89%e8%b4%a4%e8%82%b2%e8%83%bd.md" id="022 亚马逊领导力准则之选贤育能.md">022 亚马逊领导力准则之选贤育能.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/023%20%e4%ba%9a%e9%a9%ac%e9%80%8a%e9%a2%86%e5%af%bc%e5%8a%9b%e5%87%86%e5%88%99%e4%b9%8b%e6%9c%80%e9%ab%98%e6%a0%87%e5%87%86.md" id="023 亚马逊领导力准则之最高标准.md">023 亚马逊领导力准则之最高标准.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/024%20%e4%ba%9a%e9%a9%ac%e9%80%8a%e9%a2%86%e5%af%bc%e5%8a%9b%e5%87%86%e5%88%99%e4%b9%8b%e5%88%9b%e6%96%b0%e7%ae%80%e5%8c%96.md" id="024 亚马逊领导力准则之创新简化.md">024 亚马逊领导力准则之创新简化.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/025%20%e4%ba%9a%e9%a9%ac%e9%80%8a%e9%a2%86%e5%af%bc%e5%8a%9b%e5%87%86%e5%88%99%e4%b9%8b%e5%b4%87%e5%b0%9a%e8%a1%8c%e5%8a%a8.md" id="025 亚马逊领导力准则之崇尚行动.md">025 亚马逊领导力准则之崇尚行动.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/026%20%e4%ba%9a%e9%a9%ac%e9%80%8a%e9%a2%86%e5%af%bc%e5%8a%9b%e5%87%86%e5%88%99%e4%b9%8b%e8%bf%9c%e8%a7%81%e5%8d%93%e8%af%86.md" id="026 亚马逊领导力准则之远见卓识.md">026 亚马逊领导力准则之远见卓识.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/027%20%e4%ba%9a%e9%a9%ac%e9%80%8a%e9%a2%86%e5%af%bc%e5%8a%9b%e5%87%86%e5%88%99%e4%b9%8b%e5%a5%bd%e5%a5%87%e6%b1%82%e7%9f%a5%e4%b8%8e%e8%b5%a2%e5%be%97%e4%bf%a1%e4%bb%bb.md" id="027 亚马逊领导力准则之好奇求知与赢得信任.md">027 亚马逊领导力准则之好奇求知与赢得信任.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/028%20%e4%ba%9a%e9%a9%ac%e9%80%8a%e9%a2%86%e5%af%bc%e5%8a%9b%e5%87%86%e5%88%99%e4%b9%8b%e5%88%a8%e6%a0%b9%e9%97%ae%e5%ba%95%e4%b8%8e%e8%be%be%e6%88%90%e4%b8%9a%e7%bb%a9.md" id="028 亚马逊领导力准则之刨根问底与达成业绩.md">028 亚马逊领导力准则之刨根问底与达成业绩.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/029%20%e6%99%ba%e8%83%bd%e9%9f%b3%e7%ae%b1%e7%9a%84%e6%88%98%e6%96%97%ef%bc%9a%e4%ba%9a%e9%a9%ac%e9%80%8a%e7%9a%84%e7%a1%ac%e4%bb%b6%e8%b7%af.md" id="029 智能音箱的战斗：亚马逊的硬件路.md">029 智能音箱的战斗：亚马逊的硬件路.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/030%20%e6%99%ba%e8%83%bd%e9%9f%b3%e7%ae%b1%e7%9a%84%e6%88%98%e6%96%97%ef%bc%9aEcho%e6%94%bb%e5%9f%8e%e7%95%a5%e5%9c%b0.md" id="030 智能音箱的战斗：Echo攻城略地.md">030 智能音箱的战斗：Echo攻城略地.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/031%20%e6%99%ba%e8%83%bd%e9%9f%b3%e7%ae%b1%e7%9a%84%e6%88%98%e6%96%97%ef%bc%9a%e8%af%ad%e9%9f%b3%e5%8a%a9%e6%89%8bAlexa.md" id="031 智能音箱的战斗：语音助手Alexa.md">031 智能音箱的战斗：语音助手Alexa.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/032%20%e6%99%ba%e8%83%bd%e9%9f%b3%e7%ae%b1%e7%9a%84%e6%88%98%e6%96%97%ef%bc%9a%e8%b0%b7%e6%ad%8c%e7%9a%84%e6%9d%80%e5%85%a5.md" id="032 智能音箱的战斗：谷歌的杀入.md">032 智能音箱的战斗：谷歌的杀入.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/033%20%e6%99%ba%e8%83%bd%e9%9f%b3%e7%ae%b1%e7%9a%84%e6%88%98%e6%96%97%ef%bc%9a%e4%ba%9a%e9%a9%ac%e9%80%8a%e7%9a%84%e6%88%98%e7%95%a5%e5%b8%83%e5%b1%80.md" id="033 智能音箱的战斗：亚马逊的战略布局.md">033 智能音箱的战斗：亚马逊的战略布局.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/034%20%e6%99%ba%e8%83%bd%e9%9f%b3%e7%ae%b1%e7%9a%84%e6%88%98%e6%96%97%ef%bc%9a%e5%b7%a8%e5%a4%b4%e7%ba%b7%e7%ba%b7%e5%85%a5%e5%9c%ba.md" id="034 智能音箱的战斗：巨头纷纷入场.md">034 智能音箱的战斗：巨头纷纷入场.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/035%20%e6%99%ba%e8%83%bd%e9%9f%b3%e7%ae%b1%e7%9a%84%e6%88%98%e6%96%97%ef%bc%9a%e7%99%bd%e9%a9%ac%e9%9d%9e%e9%a9%ac.md" id="035 智能音箱的战斗：白马非马.md">035 智能音箱的战斗：白马非马.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/036%20%e5%a6%82%e4%bd%95%e9%80%8f%e8%bf%87%e4%b8%80%e4%b8%aa%e9%a2%86%e5%9f%9f%e5%8e%bb%e8%81%94%e5%90%88%e5%88%86%e6%9e%90%e5%a4%9a%e5%ae%b6%e4%bc%81%e4%b8%9a%ef%bc%9f.md" id="036 如何透过一个领域去联合分析多家企业？.md">036 如何透过一个领域去联合分析多家企业？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/037%20%e7%ae%a1%e4%b8%ad%e7%aa%a5%e8%b1%b9%e4%b9%8b%e4%bb%8e%e9%9d%a2%e8%af%95%e7%9c%8b%e4%bc%81%e4%b8%9a%e6%96%87%e5%8c%96%ef%bc%9a%e5%be%ae%e8%bd%af.md" id="037 管中窥豹之从面试看企业文化：微软.md">037 管中窥豹之从面试看企业文化：微软.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/038%20%e7%ae%a1%e4%b8%ad%e7%aa%a5%e8%b1%b9%e4%b9%8b%e4%bb%8e%e9%9d%a2%e8%af%95%e7%9c%8b%e4%bc%81%e4%b8%9a%e6%96%87%e5%8c%96%ef%bc%9a%e4%ba%9a%e9%a9%ac%e9%80%8a.md" id="038 管中窥豹之从面试看企业文化：亚马逊.md">038 管中窥豹之从面试看企业文化：亚马逊.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/039%20%e7%ae%a1%e4%b8%ad%e7%aa%a5%e8%b1%b9%e4%b9%8b%e4%bb%8e%e9%9d%a2%e8%af%95%e7%9c%8b%e4%bc%81%e4%b8%9a%e6%96%87%e5%8c%96%ef%bc%9a%e8%b0%b7%e6%ad%8c.md" id="039 管中窥豹之从面试看企业文化：谷歌.md">039 管中窥豹之从面试看企业文化：谷歌.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/040%20%e7%ae%a1%e4%b8%ad%e7%aa%a5%e8%b1%b9%e4%b9%8b%e4%bb%8e%e9%9d%a2%e8%af%95%e7%9c%8b%e4%bc%81%e4%b8%9a%e6%96%87%e5%8c%96%ef%bc%9a%e7%94%b2%e9%aa%a8%e6%96%87.md" id="040 管中窥豹之从面试看企业文化：甲骨文.md">040 管中窥豹之从面试看企业文化：甲骨文.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/041%20%e7%ae%a1%e4%b8%ad%e7%aa%a5%e8%b1%b9%e4%b9%8b%e4%bb%8e%e9%9d%a2%e8%af%95%e7%9c%8b%e4%bc%81%e4%b8%9a%e6%96%87%e5%8c%96%ef%bc%9aFacebook.md" id="041 管中窥豹之从面试看企业文化：Facebook.md">041 管中窥豹之从面试看企业文化：Facebook.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/042%20%e9%80%8f%e8%bf%87%e4%bc%81%e4%b8%9a%e7%94%a8%e4%ba%ba%e4%b9%8b%e9%81%93%e7%9c%8b%e4%bc%81%e4%b8%9a%e5%8f%91%e5%b1%95.md" id="042 透过企业用人之道看企业发展.md">042 透过企业用人之道看企业发展.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/043%20%e5%8a%9e%e5%85%ac%e8%bd%af%e4%bb%b6%e7%9a%84%e6%88%98%e6%96%97%ef%bc%9a%e5%bc%80%e7%af%87.md" id="043 办公软件的战斗：开篇.md">043 办公软件的战斗：开篇.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/044%20VisiCalc%ef%bc%9a%e7%ac%ac%e4%b8%80%e4%b8%aa%e7%94%b5%e5%ad%90%e8%a1%a8%e6%a0%bc%e8%bd%af%e4%bb%b6%e7%9a%84%e8%af%9e%e7%94%9f.md" id="044 VisiCalc：第一个电子表格软件的诞生.md">044 VisiCalc：第一个电子表格软件的诞生.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/045%20WordStar%ef%bc%9a%e7%ac%ac%e4%b8%80%e4%b8%aa%e5%ad%97%e5%a4%84%e7%90%86%e8%bd%af%e4%bb%b6%e7%9a%84%e6%95%85%e4%ba%8b.md" id="045 WordStar：第一个字处理软件的故事.md">045 WordStar：第一个字处理软件的故事.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/046%20%e5%be%ae%e8%bd%af%ef%bc%9a%e5%8a%9e%e5%85%ac%e8%bd%af%e4%bb%b6%e6%88%98%e5%9c%ba%e7%9a%84%e8%9e%b3%e8%9e%82.md" id="046 微软：办公软件战场的螳螂.md">046 微软：办公软件战场的螳螂.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/047%20WordPerfect%ef%bc%9a%e5%ad%97%e5%a4%84%e7%90%86%e8%bd%af%e4%bb%b6%e7%9a%84%e6%96%b0%e7%a7%80.md" id="047 WordPerfect：字处理软件的新秀.md">047 WordPerfect：字处理软件的新秀.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/048%20Lotus%201-2-3%ef%bc%9a%e8%8e%b2%e8%8a%b1%e5%85%ac%e5%8f%b8%e7%9a%84%e7%94%b5%e5%ad%90%e8%a1%a8%e6%a0%bc%e5%b8%9d%e5%9b%bd.md" id="048 Lotus 1-2-3：莲花公司的电子表格帝国.md">048 Lotus 1-2-3：莲花公司的电子表格帝国.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/049%20%e7%ba%a2%e7%8b%ae%e4%bc%9a%e6%88%98%ef%bc%9a%e5%be%ae%e8%bd%af%e7%9a%84%e5%8f%8d%e5%87%bb.md" id="049 红狮会战：微软的反击.md">049 红狮会战：微软的反击.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/050%20%e5%a4%a7%e6%9d%80%e5%99%a8Lotus%20Notes%20%e5%92%8c%e8%a2%ab%e6%94%b6%e8%b4%ad%e7%9a%84%e8%8e%b2%e8%8a%b1%e5%85%ac%e5%8f%b8.md" id="050 大杀器Lotus Notes 和被收购的莲花公司.md">050 大杀器Lotus Notes 和被收购的莲花公司.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/051%20%e6%97%a0%e6%95%8c%e5%af%82%e5%af%9e%e7%9a%84%e5%be%ae%e8%bd%af%e4%b9%8b%e4%b8%ba%e5%88%9b%e6%96%b0%e8%80%8c%e5%88%9b%e6%96%b0.md" id="051 无敌寂寞的微软之为创新而创新.md">051 无敌寂寞的微软之为创新而创新.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/052%20%e5%8a%9e%e5%85%ac%e8%bd%af%e4%bb%b6%e7%9a%84%e6%96%b0%e6%97%b6%e4%bb%a3%ef%bc%9a%e5%be%ae%e8%bd%af%e5%92%8c%e8%b0%b7%e6%ad%8c%e7%9a%84%e6%88%98%e6%96%97.md" id="052 办公软件的新时代：微软和谷歌的战斗.md">052 办公软件的新时代：微软和谷歌的战斗.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/053%20%e5%bc%82%e5%86%9b%e7%aa%81%e8%b5%b7%e7%9a%84Slack.md" id="053 异军突起的Slack.md">053 异军突起的Slack.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/054%20%e5%8a%9e%e5%85%ac%e8%bd%af%e4%bb%b6%e6%88%98%e6%96%97%e7%9a%84%e5%90%af%e7%a4%ba%ef%bc%9a%e5%86%85%e5%bf%a7%e6%80%bb%e6%98%af%e5%bc%ba%e4%ba%8e%e5%a4%96%e6%82%a3.md" id="054 办公软件战斗的启示：内忧总是强于外患.md">054 办公软件战斗的启示：内忧总是强于外患.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/055%20%e5%8a%9e%e5%85%ac%e8%bd%af%e4%bb%b6%e6%88%98%e6%96%97%e7%9a%84%e5%90%af%e7%a4%ba%ef%bc%9a%e6%95%8c%e4%ba%ba%e7%9a%84%e5%87%ba%e7%8e%b0%e5%b8%b8%e5%b8%b8%e5%87%ba%e5%85%b6%e4%b8%8d%e6%84%8f.md" id="055 办公软件战斗的启示：敌人的出现常常出其不意.md">055 办公软件战斗的启示：敌人的出现常常出其不意.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/056%20%e5%8d%8a%e6%9d%a1%e5%91%bd%e7%9a%84Dota%e5%b8%9d%e5%9b%bdValve%ef%bc%9a%e5%8d%8a%e6%9d%a1%e5%91%bd.md" id="056 半条命的Dota帝国Valve：半条命.md">056 半条命的Dota帝国Valve：半条命.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/057%20%e5%8d%8a%e6%9d%a1%e5%91%bd%e7%9a%84Dota%e5%b8%9d%e5%9b%bdValve%ef%bc%9aSteam%e5%b9%b3%e5%8f%b0.md" id="057 半条命的Dota帝国Valve：Steam平台.md">057 半条命的Dota帝国Valve：Steam平台.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/058%20%e5%8d%8a%e6%9d%a1%e5%91%bd%e7%9a%84Dota%e5%b8%9d%e5%9b%bdValve%ef%bc%9aDota%202.md" id="058 半条命的Dota帝国Valve：Dota 2.md">058 半条命的Dota帝国Valve：Dota 2.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/059%20%e5%8d%8a%e6%9d%a1%e5%91%bd%e7%9a%84Dota%e5%b8%9d%e5%9b%bdValve%ef%bc%9a%e6%97%a0%e9%a2%86%e5%af%bc%e7%ae%a1%e7%90%86.md" id="059 半条命的Dota帝国Valve：无领导管理.md">059 半条命的Dota帝国Valve：无领导管理.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/060%20%e5%8d%8a%e6%9d%a1%e5%91%bd%e7%9a%84Dota%e5%b8%9d%e5%9b%bdValve%ef%bc%9a%e8%99%9a%e6%8b%9f%e7%8e%b0%e5%ae%9e.md" id="060 半条命的Dota帝国Valve：虚拟现实.md">060 半条命的Dota帝国Valve：虚拟现实.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/061%20Gabe%20Newell%ef%bc%9aValve%e5%b8%9d%e5%9b%bd%e5%88%b6%e5%ba%a6%e7%9a%84%e5%88%a9%e5%bc%8a.md" id="061 Gabe Newell：Valve帝国制度的利弊.md">061 Gabe Newell：Valve帝国制度的利弊.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/062%20%e6%96%87%e6%a1%a3%e6%95%b0%e6%8d%ae%e5%ba%93%e7%9a%84%e7%bc%94%e9%80%a0%e8%80%85MongoDB%ef%bc%88%e4%b8%8a%ef%bc%89.md" id="062 文档数据库的缔造者MongoDB（上）.md">062 文档数据库的缔造者MongoDB（上）.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/063%20%e6%96%87%e6%a1%a3%e6%95%b0%e6%8d%ae%e5%ba%93%e7%9a%84%e7%bc%94%e9%80%a0%e8%80%85MongoDB%ef%bc%88%e4%b8%8b%ef%bc%89.md" id="063 文档数据库的缔造者MongoDB（下）.md">063 文档数据库的缔造者MongoDB（下）.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/064%20%e4%bb%a5MongoDB%e4%b8%ba%e4%be%8b%ef%bc%8c%e7%9c%8b%e5%9f%ba%e7%a1%80%e6%9e%b6%e6%9e%84%e7%b1%bb%e4%ba%a7%e5%93%81%e5%88%9b%e4%b8%9a.md" id="064 以MongoDB为例，看基础架构类产品创业.md">064 以MongoDB为例，看基础架构类产品创业.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/065%20%e7%9b%b4%e9%9d%a2MongoDB%ef%bc%8c%e8%b0%88%e5%be%ae%e8%bd%af%e7%9a%84NoSQL%e6%88%98%e7%95%a5.md" id="065 直面MongoDB，谈微软的NoSQL战略.md">065 直面MongoDB，谈微软的NoSQL战略.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/066%20Hadoop%e4%b8%89%e5%9b%bd%e4%b9%8b%e9%ad%8f%e5%9b%bdCloudera.md" id="066 Hadoop三国之魏国Cloudera.md">066 Hadoop三国之魏国Cloudera.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/067%20Hadoop%e4%b8%89%e5%9b%bd%e4%b9%8b%e5%90%b4%e5%9b%bdMapR.md" id="067 Hadoop三国之吴国MapR.md">067 Hadoop三国之吴国MapR.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/068%20Hadoop%e4%b8%89%e5%9b%bd%e4%b9%8b%e8%9c%80%e5%9b%bdHortonworks.md" id="068 Hadoop三国之蜀国Hortonworks.md">068 Hadoop三国之蜀国Hortonworks.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/069%20Hadoop%e5%8f%8a%e5%85%b6%e5%8f%91%e8%a1%8c%e5%95%86%e7%9a%84%e6%9c%aa%e6%9d%a5.md" id="069 Hadoop及其发行商的未来.md">069 Hadoop及其发行商的未来.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/070%20%e8%b0%b7%e6%ad%8c%e7%9a%84%e5%a4%a7%e6%95%b0%e6%8d%ae%e8%b7%af%ef%bc%9a%e4%bb%8e%e2%80%9c%e4%b8%89%e9%a9%be%e9%a9%ac%e8%bd%a6%e2%80%9d%e5%88%b0%e4%b8%80%e6%97%a0%e6%89%80%e6%9c%89.md" id="070 谷歌的大数据路：从“三驾马车”到一无所有.md">070 谷歌的大数据路：从“三驾马车”到一无所有.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/071%20%e8%b0%b7%e6%ad%8c%e7%9a%84%e5%a4%a7%e6%95%b0%e6%8d%ae%e8%b7%af%ef%bc%9a%e4%b8%80%e5%9c%ba%e5%bd%b1%e5%93%8d%e6%b7%b1%e8%bf%9c%e7%9a%84%e8%ae%ba%e6%88%98.md" id="071 谷歌的大数据路：一场影响深远的论战.md">071 谷歌的大数据路：一场影响深远的论战.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/072%20%e8%b0%b7%e6%ad%8c%e7%9a%84%e5%a4%a7%e6%95%b0%e6%8d%ae%e8%b7%af%ef%bc%9a%e8%b0%b7%e6%ad%8c%e7%9a%84%e2%80%9c%e9%bb%91%e7%a7%91%e6%8a%80%e2%80%9d.md" id="072 谷歌的大数据路：谷歌的“黑科技”.md">072 谷歌的大数据路：谷歌的“黑科技”.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/073%20%e5%a6%82%e4%bd%95%e8%af%bb%e6%87%82%e7%b1%bb%e4%bc%bc%e8%b0%b7%e6%ad%8c%e2%80%9c%e4%b8%89%e9%a9%be%e9%a9%ac%e8%bd%a6%e2%80%9d%e8%bf%99%e6%a0%b7%e7%9a%84%e6%8a%80%e6%9c%af%e8%ae%ba%e6%96%87%ef%bc%9f.md" id="073 如何读懂类似谷歌“三驾马车”这样的技术论文？.md">073 如何读懂类似谷歌“三驾马车”这样的技术论文？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/074%20%e9%9b%85%e8%99%8e%ef%bc%9a%e5%a4%a7%e6%95%b0%e6%8d%ae%e9%a2%86%e5%9f%9f%e7%9a%84%e2%80%9c%e6%b4%bb%e9%9b%b7%e9%94%8b%e2%80%9d.md" id="074 雅虎：大数据领域的“活雷锋”.md">074 雅虎：大数据领域的“活雷锋”.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/075%20IBM%e7%9a%84%e5%a4%a7%e6%95%b0%e6%8d%ae%e8%b7%af%e4%b9%8b%e8%b5%b7%e6%97%a9%e8%b4%aa%e9%bb%91%e8%b5%b6%e4%ba%86%e6%99%9a%e9%9b%86.md" id="075 IBM的大数据路之起早贪黑赶了晚集.md">075 IBM的大数据路之起早贪黑赶了晚集.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/076%20%e7%a4%be%e4%ba%a4%e5%85%ac%e5%8f%b8%e4%bb%ac%e7%9a%84%e5%a4%a7%e6%95%b0%e6%8d%ae%e8%b4%a1%e7%8c%ae.md" id="076 社交公司们的大数据贡献.md">076 社交公司们的大数据贡献.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/077%20%e5%be%ae%e8%bd%af%e7%9a%84%e5%a4%a7%e6%95%b0%e6%8d%ae%e5%8f%91%e5%b1%95%e5%8f%b2%ef%bc%9a%e5%be%ae%e8%bd%af%e7%a1%85%e8%b0%b7%e7%a0%94%e7%a9%b6%e9%99%a2.md" id="077 微软的大数据发展史：微软硅谷研究院.md">077 微软的大数据发展史：微软硅谷研究院.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/078%20%e5%be%ae%e8%bd%af%e7%9a%84%e5%a4%a7%e6%95%b0%e6%8d%ae%e5%8f%91%e5%b1%95%e5%8f%b2%ef%bc%9a%e5%bf%85%e5%ba%94%e7%9a%84Cosmos.md" id="078 微软的大数据发展史：必应的Cosmos.md">078 微软的大数据发展史：必应的Cosmos.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/079%20%e5%be%ae%e8%bd%af%e7%9a%84%e5%a4%a7%e6%95%b0%e6%8d%ae%e5%8f%91%e5%b1%95%e5%8f%b2%ef%bc%9aAzure%e7%9a%84%e5%a4%a7%e6%95%b0%e6%8d%ae%e5%8f%91%e5%b1%95.md" id="079 微软的大数据发展史：Azure的大数据发展.md">079 微软的大数据发展史：Azure的大数据发展.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/080%20%e4%ba%9a%e9%a9%ac%e9%80%8a%e7%9a%84%e5%a4%a7%e6%95%b0%e6%8d%ae%e6%95%85%e4%ba%8b%ef%bc%9a%e4%bb%8e%e5%85%88%e9%a9%b1%e8%80%85%e5%88%b0%e6%8f%92%e7%ae%a1%e5%90%b8%e8%a1%80%e5%bc%80%e6%ba%90.md" id="080 亚马逊的大数据故事：从先驱者到插管吸血开源.md">080 亚马逊的大数据故事：从先驱者到插管吸血开源.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/081%20%e4%ba%9a%e9%a9%ac%e9%80%8a%e7%9a%84%e5%a4%a7%e6%95%b0%e6%8d%ae%e6%95%85%e4%ba%8b%ef%bc%9a%e5%88%9b%e6%96%b0%e5%92%8c%e6%8b%bf%e6%9d%a5%e5%b9%b6%e5%ad%98%e7%9a%84%e4%ba%91%e6%9c%8d%e5%8a%a1.md" id="081 亚马逊的大数据故事：创新和拿来并存的云服务.md">081 亚马逊的大数据故事：创新和拿来并存的云服务.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/082%20%e9%98%bf%e9%87%8c%e5%b7%b4%e5%b7%b4%e7%9a%84%e5%a4%a7%e6%95%b0%e6%8d%ae%e6%95%85%e4%ba%8b%ef%bc%9a%e6%95%b0%e6%8d%ae%e5%88%86%e6%9e%90%e5%b9%b3%e5%8f%b0%e5%8f%91%e5%b1%95%e5%8f%b2.md" id="082 阿里巴巴的大数据故事：数据分析平台发展史.md">082 阿里巴巴的大数据故事：数据分析平台发展史.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/083%20%e9%98%bf%e9%87%8c%e5%b7%b4%e5%b7%b4%e7%9a%84%e5%a4%a7%e6%95%b0%e6%8d%ae%e6%95%85%e4%ba%8b%ef%bc%9a%e6%b5%81%e8%ae%a1%e7%ae%97%e5%bc%95%e6%93%8e%e5%8f%91%e5%b1%95%e5%8f%b2.md" id="083 阿里巴巴的大数据故事：流计算引擎发展史.md">083 阿里巴巴的大数据故事：流计算引擎发展史.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/084%20%e5%a4%a7%e5%85%ac%e5%8f%b8%e7%9a%84%e5%a4%a7%e6%95%b0%e6%8d%ae%e6%88%98%e7%95%a5%e5%be%97%e5%a4%b1%ef%bc%9a%e8%87%aa%e5%bb%ba%e8%bd%ae%e5%ad%90%e6%88%90%e6%9c%ac%e9%ab%98.md" id="084 大公司的大数据战略得失：自建轮子成本高.md">084 大公司的大数据战略得失：自建轮子成本高.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/085%20%e5%a4%a7%e5%85%ac%e5%8f%b8%e7%9a%84%e5%a4%a7%e6%95%b0%e6%8d%ae%e6%88%98%e7%95%a5%e5%be%97%e5%a4%b1%ef%bc%9a%e6%8a%b1%e5%9b%a2%e5%8f%96%e6%9a%96%e9%9a%be%e6%95%8c%e6%8f%92%e7%ae%a1%e5%90%b8%e8%a1%80%e8%80%85.md" id="085 大公司的大数据战略得失：抱团取暖难敌插管吸血者.md">085 大公司的大数据战略得失：抱团取暖难敌插管吸血者.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/086%20Palantir%ef%bc%9a%e7%a5%9e%e7%a7%98%e7%9a%84%e5%a4%a7%e6%95%b0%e6%8d%ae%e7%8b%ac%e8%a7%92%e5%85%bd.md" id="086 Palantir：神秘的大数据独角兽.md">086 Palantir：神秘的大数据独角兽.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/087Splunk%ef%bc%9a%e6%9c%ba%e5%99%a8%e5%a4%a7%e6%95%b0%e6%8d%ae%e7%9a%84%e5%88%86%e6%9e%90%e5%b8%9d%e5%9b%bd.md" id="087Splunk：机器大数据的分析帝国.md">087Splunk：机器大数据的分析帝国.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/088%20Confluent%ef%bc%9a%e5%9c%a8Kafka%e4%b8%8a%e9%a3%9e%e9%a9%b0%e7%9a%84%e6%95%b0%e6%8d%ae%e4%ba%a4%e6%8d%a2%e8%80%85.md" id="088 Confluent：在Kafka上飞驰的数据交换者.md">088 Confluent：在Kafka上飞驰的数据交换者.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/089%20Powerset%ef%bc%9aHBase%e7%9a%84%e8%80%81%e4%b8%9c%e5%ae%b6.md" id="089 Powerset：HBase的老东家.md">089 Powerset：HBase的老东家.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/090%20Cassandra%e5%92%8cDataStax%e7%9a%84%e6%95%85%e4%ba%8b.md" id="090 Cassandra和DataStax的故事.md">090 Cassandra和DataStax的故事.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/091%20Databricks%e4%b9%8bSpark%e7%9a%84%e6%95%b0%e6%8d%ae%e9%87%91%e7%a0%96%e7%8e%8b%e5%9b%bd.md" id="091 Databricks之Spark的数据金砖王国.md">091 Databricks之Spark的数据金砖王国.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/092%20Data%20Artisans%ef%bc%9a%e6%b5%b4%e7%81%ab%e9%87%8d%e7%94%9f%e7%9a%84%e6%96%b0%e4%b8%80%e4%bb%a3%e5%a4%a7%e6%95%b0%e6%8d%ae%e8%ae%a1%e7%ae%97%e5%bc%95%e6%93%8eFlink.md" id="092 Data Artisans：浴火重生的新一代大数据计算引擎Flink.md">092 Data Artisans：浴火重生的新一代大数据计算引擎Flink.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/093%20Dremio_%e5%9c%a8Drill%e5%92%8cArrow%e4%b8%8a%e7%9a%84%e5%a4%a7%e6%95%b0%e6%8d%ae%e5%85%ac%e5%8f%b8.md" id="093 Dremio_在Drill和Arrow上的大数据公司.md">093 Dremio_在Drill和Arrow上的大数据公司.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/094%20Imply%ef%bc%9a%e5%9f%ba%e4%ba%8eDruid%e7%9a%84%e5%a4%a7%e6%95%b0%e6%8d%ae%e5%88%86%e6%9e%90%e5%85%ac%e5%8f%b8.md" id="094 Imply：基于Druid的大数据分析公司.md">094 Imply：基于Druid的大数据分析公司.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/095%20Kyligence%ef%bc%9a%e9%98%bf%e5%b8%95%e5%a5%87%e9%ba%92%e9%ba%9f%e8%83%8c%e5%90%8e%e7%9a%84%e5%a4%a7%e6%95%b0%e6%8d%ae%e5%85%ac%e5%8f%b8.md" id="095 Kyligence：阿帕奇麒麟背后的大数据公司.md">095 Kyligence：阿帕奇麒麟背后的大数据公司.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/096%20Snowflake_%e4%ba%91%e7%ab%af%e7%9a%84%e5%bc%b9%e6%80%a7%e6%95%b0%e6%8d%ae%e4%bb%93%e5%ba%93.md" id="096 Snowflake_云端的弹性数据仓库.md">096 Snowflake_云端的弹性数据仓库.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/097%20TiDB%ef%bc%9a%e4%b8%80%e4%b8%aa%e5%9b%bd%e4%ba%a7%e6%96%b0%e6%95%b0%e6%8d%ae%e5%ba%93%e7%9a%84%e5%88%9b%e4%b8%9a%e6%95%85%e4%ba%8b.md" id="097 TiDB：一个国产新数据库的创业故事.md">097 TiDB：一个国产新数据库的创业故事.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/098%20%e5%a4%a7%e6%95%b0%e6%8d%ae%e5%88%9b%e4%b8%9a%e5%85%ac%e5%8f%b8%e7%9a%84%e5%89%8d%e6%99%af%ef%bc%9a%e7%ba%a2%e6%b5%b7%e5%88%9b%e4%b8%9a%e5%a4%9a%e8%89%b0%e8%be%9b.md" id="098 大数据创业公司的前景：红海创业多艰辛.md">098 大数据创业公司的前景：红海创业多艰辛.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/099%20%e5%a6%82%e4%bd%95%e9%80%9a%e8%bf%87%e4%bc%81%e4%b8%9a%e6%8a%80%e6%9c%af%e7%a7%af%e7%b4%af%e5%8e%bb%e5%88%86%e6%9e%90%e4%b8%80%e5%ae%b6%e4%bc%81%e4%b8%9a%ef%bc%9f.md" id="099 如何通过企业技术积累去分析一家企业？.md">099 如何通过企业技术积累去分析一家企业？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/100%20%e4%bb%81%e7%a7%91%ef%bc%9a%e8%a2%ab%e8%bf%ab%e5%86%8d%e5%88%9b%e4%b8%9a%e7%9a%84David%20Duffield.md" id="100 仁科：被迫再创业的David Duffield.md">100 仁科：被迫再创业的David Duffield.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/101%20%e4%bb%81%e7%a7%91%ef%bc%9a%e9%a3%9e%e8%b7%83%e5%8f%91%e5%b1%95%e7%9a%84%e4%bc%81%e4%b8%9a%e7%ba%a7%e8%bd%af%e4%bb%b6%e5%b8%9d%e5%9b%bd.md" id="101 仁科：飞跃发展的企业级软件帝国.md">101 仁科：飞跃发展的企业级软件帝国.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/102%20%e4%bb%81%e7%a7%91%ef%bc%9a%e6%94%b6%e8%b4%ad%e5%92%8c%e8%a2%ab%e6%94%b6%e8%b4%ad.md" id="102 仁科：收购和被收购.md">102 仁科：收购和被收购.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/103%20%e4%bb%81%e7%a7%91%e7%9a%84%e6%88%90%e4%b8%8e%e8%b4%a5.md" id="103 仁科的成与败.md">103 仁科的成与败.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/104%20WorkDay%ef%bc%9a%e6%9d%9c%e8%8f%b2%e5%b0%94%e5%be%b7%e5%a4%8d%e4%bb%87%e8%ae%b0.md" id="104 WorkDay：杜菲尔德复仇记.md">104 WorkDay：杜菲尔德复仇记.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/105%20David%20Duffield%e7%9a%84%e7%9c%bc%e7%95%8c%e5%92%8c%e6%88%90%e8%b4%a5.md" id="105 David Duffield的眼界和成败.md">105 David Duffield的眼界和成败.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/106%20%e5%88%86%e6%9e%90%e4%bc%81%e4%b8%9a%e7%9a%84%e4%b8%a4%e8%a6%81%e7%b4%a0%ef%bc%9a%e8%bf%9c%e8%a7%81%e5%92%8c%e6%89%a7%e8%a1%8c%e5%8a%9b.md" id="106 分析企业的两要素：远见和执行力.md">106 分析企业的两要素：远见和执行力.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/107%20Zenefits%ef%bc%9a%e4%b8%80%e4%b8%aa%e5%8d%96%e4%bf%9d%e9%99%a9%e7%9a%84%e5%88%9b%e4%b8%9a%e5%85%ac%e5%8f%b8.md" id="107 Zenefits：一个卖保险的创业公司.md">107 Zenefits：一个卖保险的创业公司.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/108%20Glassdoor%ef%bc%9a%e8%ae%a9%e5%85%ac%e5%8f%b8%e4%bf%a1%e6%81%af%e5%af%b9%e4%b8%aa%e4%ba%ba%e9%80%8f%e6%98%8e.md" id="108 Glassdoor：让公司信息对个人透明.md">108 Glassdoor：让公司信息对个人透明.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/109%20%e4%bb%8e%e5%b7%b4%e9%a1%bf%e7%9a%84%e5%88%9b%e4%b8%9a%e5%8f%b2%e7%9c%8b%e5%b7%b4%e9%a1%bf.md" id="109 从巴顿的创业史看巴顿.md">109 从巴顿的创业史看巴顿.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/110%20%e5%85%8d%e8%b4%b9%e8%bf%98%e6%98%af%e6%94%b6%e8%b4%b9%ef%bc%9fWinRAR%e7%9a%84%e7%94%9f%e6%84%8f%e7%bb%8f.md" id="110 免费还是收费？WinRAR的生意经.md">110 免费还是收费？WinRAR的生意经.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/111%20%e5%91%a8%e9%b8%bf%e7%a5%8e%e5%92%8cBAT%e7%9a%84%e6%b2%89%e6%b5%ae%e5%bd%95%ef%bc%88%e4%b8%8a%ef%bc%89.md" id="111 周鸿祎和BAT的沉浮录（上）.md">111 周鸿祎和BAT的沉浮录（上）.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/112%20%e5%91%a8%e9%b8%bf%e7%a5%8e%e5%92%8cBAT%e7%9a%84%e6%b2%89%e6%b5%ae%e5%bd%95%ef%bc%88%e4%b8%ad%ef%bc%89.md" id="112 周鸿祎和BAT的沉浮录（中）.md">112 周鸿祎和BAT的沉浮录（中）.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/113%20%e5%91%a8%e9%b8%bf%e7%a5%8e%e5%92%8cBAT%e7%9a%84%e6%b2%89%e6%b5%ae%e5%bd%95%ef%bc%88%e4%b8%8b%ef%bc%89.md" id="113 周鸿祎和BAT的沉浮录（下）.md">113 周鸿祎和BAT的沉浮录（下）.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/114%20%e5%91%a8%e9%b8%bf%e7%a5%8e%e5%92%8cBAT%e7%9a%84%e6%b2%89%e6%b5%ae%e5%bd%95%ef%bc%88%e5%90%8e%e8%ae%b0%ef%bc%89.md" id="114 周鸿祎和BAT的沉浮录（后记）.md">114 周鸿祎和BAT的沉浮录（后记）.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/115%20%e4%ba%92%e8%81%94%e7%bd%91%e7%ac%ac%e4%b8%80%e8%82%a1%e9%9b%85%e8%99%8e%e7%9a%84%e5%85%b4%e8%a1%b0%ef%bc%9a%e9%9c%b8%e4%b8%bb%e7%9a%84%e8%af%9e%e7%94%9f.md" id="115 互联网第一股雅虎的兴衰：霸主的诞生.md">115 互联网第一股雅虎的兴衰：霸主的诞生.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/116%20%e4%ba%92%e8%81%94%e7%bd%91%e7%ac%ac%e4%b8%80%e8%82%a1%e9%9b%85%e8%99%8e%e7%9a%84%e5%85%b4%e8%a1%b0%ef%bc%9a%e8%bf%90%e6%b0%94%e4%b8%8d%e6%95%8c%e6%8a%80%e6%9c%af.md" id="116 互联网第一股雅虎的兴衰：运气不敌技术.md">116 互联网第一股雅虎的兴衰：运气不敌技术.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/117%20%e4%ba%92%e8%81%94%e7%bd%91%e7%ac%ac%e4%b8%80%e8%82%a1%e9%9b%85%e8%99%8e%e7%9a%84%e5%85%b4%e8%a1%b0%ef%bc%9a%e6%b2%a1%e6%9c%89%e6%95%91%e4%b8%96%e4%b8%bb.md" id="117 互联网第一股雅虎的兴衰：没有救世主.md">117 互联网第一股雅虎的兴衰：没有救世主.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/118%20%e6%88%90%e4%b9%9f%e6%9d%a8%e8%87%b4%e8%bf%9c%ef%bc%8c%e8%b4%a5%e4%b9%9f%e6%9d%a8%e8%87%b4%e8%bf%9c.md" id="118 成也杨致远，败也杨致远.md">118 成也杨致远，败也杨致远.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/119%20%e4%bc%81%e4%b8%9a%e5%9b%a0%e4%ba%ba%e6%88%90%e4%ba%8b%ef%bc%8c%e9%a2%86%e5%af%bc%e4%ba%ba%e5%be%88%e9%87%8d%e8%a6%81.md" id="119 企业因人成事，领导人很重要.md">119 企业因人成事，领导人很重要.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/120%20%e5%bd%bc%e5%be%97%20%c2%b7%20%e8%92%82%e5%b0%94%e7%9a%84%e6%8a%95%e8%b5%84%e4%ba%ba%e7%94%9f.md" id="120 彼得 · 蒂尔的投资人生.md">120 彼得 · 蒂尔的投资人生.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/121%20%e5%95%86%e4%b8%9a%e4%b9%8b%e5%a4%96%e7%9a%84%e5%bd%bc%e5%be%97%20%c2%b7%20%e8%92%82%e5%b0%94.md" id="121 商业之外的彼得 · 蒂尔.md">121 商业之外的彼得 · 蒂尔.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/122%20%e5%88%9b%e4%b8%9a%e7%9a%84%e6%99%ba%e6%85%a7%ef%bc%9a%e4%bb%8e%e5%bd%bc%e5%be%97%c2%b7%e8%92%82%e5%b0%94%e7%9a%84%e5%88%9b%e6%8a%95%e5%93%b2%e5%ad%a6%e8%af%b4%e8%b5%b7.md" id="122 创业的智慧：从彼得·蒂尔的创投哲学说起.md">122 创业的智慧：从彼得·蒂尔的创投哲学说起.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/123%20%e8%b0%b7%e6%ad%8c%e7%9a%84%e5%88%9b%e6%96%b0%e7%b2%be%e7%a5%9e%ef%bc%9a%e5%a5%bd%e7%9a%84%e3%80%81%e5%9d%8f%e7%9a%84%e5%92%8c%e4%b8%91%e9%99%8b%e7%9a%84%ef%bc%88%e4%b8%8a%ef%bc%89.md" id="123 谷歌的创新精神：好的、坏的和丑陋的（上）.md">123 谷歌的创新精神：好的、坏的和丑陋的（上）.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/124%20%e8%b0%b7%e6%ad%8c%e7%9a%84%e5%88%9b%e6%96%b0%e7%b2%be%e7%a5%9e%ef%bc%9a%e5%a5%bd%e7%9a%84%e3%80%81%e5%9d%8f%e7%9a%84%e5%92%8c%e4%b8%91%e9%99%8b%e7%9a%84%ef%bc%88%e4%b8%8b%ef%bc%89.md" id="124 谷歌的创新精神：好的、坏的和丑陋的（下）.md">124 谷歌的创新精神：好的、坏的和丑陋的（下）.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/125%20Facebook%e7%9a%84%e9%bb%91%e5%ae%a2%e7%b2%be%e7%a5%9e.md" id="125 Facebook的黑客精神.md">125 Facebook的黑客精神.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/126%20Twitter%ef%bc%9a%e8%93%9d%e8%89%b2%e5%b0%8f%e9%b8%9f%e8%bf%98%e8%83%bd%e9%a3%9e%e5%a4%9a%e4%b9%85%ef%bc%88%e4%b8%8a%ef%bc%89.md" id="126 Twitter：蓝色小鸟还能飞多久（上）.md">126 Twitter：蓝色小鸟还能飞多久（上）.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/127%20Twitter%ef%bc%9a%e8%93%9d%e8%89%b2%e5%b0%8f%e9%b8%9f%e8%bf%98%e8%83%bd%e9%a3%9e%e5%a4%9a%e4%b9%85%ef%bc%88%e4%b8%8b%ef%bc%89.md" id="127 Twitter：蓝色小鸟还能飞多久（下）.md">127 Twitter：蓝色小鸟还能飞多久（下）.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/128%20%e8%b5%9a%e9%92%b1%e6%98%af%e6%a0%b9%e6%9c%ac%ef%bc%8c%e6%8d%a2CEO%e4%b9%9f%e6%b2%a1%e6%95%91.md" id="128 赚钱是根本，换CEO也没救.md">128 赚钱是根本，换CEO也没救.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/129%20Square%ef%bc%9a%e6%89%8b%e6%9c%baPOS%e6%9c%ba%e5%92%8c%e6%af%94%e7%89%b9%e5%b8%81%e4%ba%a4%e6%98%93.md" id="129 Square：手机POS机和比特币交易.md">129 Square：手机POS机和比特币交易.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/130%20%e5%88%9b%e6%84%8f%e5%be%88%e9%87%8d%e8%a6%81%ef%bc%8c%e4%bd%86%e4%b8%8d%e6%98%af%e4%b8%80%e5%88%87.md" id="130 创意很重要，但不是一切.md">130 创意很重要，但不是一切.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/131%20%e6%9d%b0%e5%85%8b%c2%b7%e5%a4%9a%e8%a5%bf%ef%bc%9a%e5%88%86%e8%ba%ab%e6%9c%89%e6%9c%af%e4%b9%8b%e5%85%bc%e4%bb%bb%e4%b8%a4%e5%ae%b6%e4%b8%8a%e5%b8%82%e5%85%ac%e5%8f%b8CEO.md" id="131 杰克·多西：分身有术之兼任两家上市公司CEO.md">131 杰克·多西：分身有术之兼任两家上市公司CEO.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/132%20Groupon%ef%bc%9a%e5%9b%a2%e8%b4%ad%e9%bc%bb%e7%a5%96%e7%9a%84%e5%85%b4%e8%a1%b0.md" id="132 Groupon：团购鼻祖的兴衰.md">132 Groupon：团购鼻祖的兴衰.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/133%20%e5%8d%96%e6%8e%89%e8%87%aa%e5%b7%b1%e6%98%af%e4%b8%8d%e6%98%af%e6%9b%b4%e5%a5%bd.md" id="133 卖掉自己是不是更好.md">133 卖掉自己是不是更好.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/134%20%e4%bc%81%e4%b8%9a%e5%9c%a8%e7%ba%bf%e5%ad%98%e5%82%a8Box.md" id="134 企业在线存储Box.md">134 企业在线存储Box.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/135%20%e4%b8%aa%e4%ba%ba%e5%9c%a8%e7%ba%bf%e5%ad%98%e5%82%a8%20Dropbox.md" id="135 个人在线存储 Dropbox.md">135 个人在线存储 Dropbox.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/136%20%e5%81%9a%e4%ba%a7%e5%93%81%e5%85%88%e5%81%9a%e6%b6%88%e8%b4%b9%e8%80%85%e5%b8%82%e5%9c%ba%ef%bc%8c%e8%bf%98%e6%98%af%e5%85%88%e5%81%9a%e4%bc%81%e4%b8%9a%e5%b8%82%e5%9c%ba.md" id="136 做产品先做消费者市场，还是先做企业市场.md">136 做产品先做消费者市场，还是先做企业市场.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/137%20%e4%bb%8a%e5%a4%a9%e6%88%91%e4%bb%ac%e9%83%bd%e6%9d%a5Pin%e5%9b%be%e7%89%87%e4%b9%8bPinterest%e7%9a%84%e5%9b%be%e7%89%87%e7%a4%be%e4%ba%a4%e8%b7%af.md" id="137 今天我们都来Pin图片之Pinterest的图片社交路.md">137 今天我们都来Pin图片之Pinterest的图片社交路.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/138%20%e4%bc%81%e4%b8%9a%e4%b8%8d%e4%b8%8a%e5%b8%82%e4%b8%ba%e5%93%aa%e8%88%ac.md" id="138 企业不上市为哪般.md">138 企业不上市为哪般.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/139%20%e5%be%ae%e8%bd%af%e7%9a%84%e7%bb%bc%e5%90%88%e5%b7%a5%e7%a8%8b%e5%b8%88%e6%94%b9%e9%9d%a9.md" id="139 微软的综合工程师改革.md">139 微软的综合工程师改革.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/140%20SaaS%e5%85%88%e9%a9%b1Salesforce.md" id="140 SaaS先驱Salesforce.md">140 SaaS先驱Salesforce.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/141%20%e5%a4%aa%e8%b6%85%e5%89%8d%e5%a5%bd%e4%b8%8d%e5%a5%bd.md" id="141 太超前好不好.md">141 太超前好不好.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/142%20Sun%ef%bc%9a%e5%a4%aa%e9%98%b3%e7%9a%84%e5%8d%87%e8%b5%b7.md" id="142 Sun：太阳的升起.md">142 Sun：太阳的升起.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/143%20Sun%ef%bc%9a%e5%a4%aa%e9%98%b3%e7%9a%84%e9%99%a8%e8%90%bd.md" id="143 Sun：太阳的陨落.md">143 Sun：太阳的陨落.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/144%20%e7%9c%8b%e9%94%99%e6%95%8c%e4%ba%ba%e5%a4%9a%e5%8f%af%e6%80%95.md" id="144 看错敌人多可怕.md">144 看错敌人多可怕.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/145%20SAP%e7%9a%84HANA%e6%88%98%e7%95%a5%ef%bc%88%e4%b8%8a%ef%bc%89.md" id="145 SAP的HANA战略（上）.md">145 SAP的HANA战略（上）.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/146%20SAP%e7%9a%84HANA%e6%88%98%e7%95%a5%ef%bc%88%e4%b8%8b%ef%bc%89.md" id="146 SAP的HANA战略（下）.md">146 SAP的HANA战略（下）.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/147%20%e6%88%90%e5%8a%9f%e7%9a%84%e5%bf%bd%e6%82%a0%20%e5%8a%a0%20%e6%88%90%e5%8a%9f%e7%9a%84%e6%89%a7%e8%a1%8c%20%e7%ad%89%e4%ba%8e%20%e6%88%90%e5%8a%9f%e7%9a%84%e4%ba%a7%e5%93%81.md" id="147 成功的忽悠 加 成功的执行 等于 成功的产品.md">147 成功的忽悠 加 成功的执行 等于 成功的产品.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/148%20SQL%20Server%e5%8f%91%e5%b1%95%e5%8f%b2.md" id="148 SQL Server发展史.md">148 SQL Server发展史.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/149%20%e7%9c%bc%e5%85%89%e5%86%b3%e5%ae%9a%e4%b8%80%e5%88%87.md" id="149 眼光决定一切.md">149 眼光决定一切.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/150%20Ashton-Tate%ef%bc%9a%e6%a1%8c%e9%9d%a2%e6%95%b0%e6%8d%ae%e5%ba%93%e7%8e%8b%e8%80%85%e7%9a%84%e5%85%b4%e8%a1%b0.md" id="150 Ashton-Tate：桌面数据库王者的兴衰.md">150 Ashton-Tate：桌面数据库王者的兴衰.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/151%20%e6%97%a0%e6%95%8c%e4%b8%8d%e5%8f%af%e4%bb%a5%e8%82%86%e6%84%8f%e5%a6%84%e4%b8%ba.md" id="151 无敌不可以肆意妄为.md">151 无敌不可以肆意妄为.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/152%20Reddit%ef%bc%9a%e5%a4%a9%e6%b6%af%e8%ae%ba%e5%9d%9b%e7%be%8e%e5%9b%bd%e7%89%88.md" id="152 Reddit：天涯论坛美国版.md">152 Reddit：天涯论坛美国版.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/153%20Hacker%20News%ef%bc%9a%e5%88%9b%e4%b8%9a%e7%a4%be%e4%ba%a4%e4%b8%a4%e4%b8%8d%e8%af%af.md" id="153 Hacker News：创业社交两不误.md">153 Hacker News：创业社交两不误.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/154%20Y%20Combinator%ef%bc%9a%e5%ad%b5%e5%8c%96%e5%99%a8%e8%bf%98%e6%98%af%e5%9f%b9%e8%ae%ad%e7%8f%ad%ef%bc%9f.md" id="154 Y Combinator：孵化器还是培训班？.md">154 Y Combinator：孵化器还是培训班？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/155%20%e5%88%9b%e4%b8%9a%e5%85%ac%e5%8f%b8%e8%bf%9b%e5%ad%b5%e5%8c%96%e5%99%a8%e7%9c%9f%e7%9a%84%e5%80%bc%e5%be%97%e5%90%97%ef%bc%9f.md" id="155 创业公司进孵化器真的值得吗？.md">155 创业公司进孵化器真的值得吗？.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/156%20Paul%20Graham%ef%bc%9a%e7%a1%85%e8%b0%b7%e5%88%9b%e4%b8%9a%e6%95%99%e7%88%b6.md" id="156 Paul Graham：硅谷创业教父.md">156 Paul Graham：硅谷创业教父.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/157%20Zynga%ef%bc%9a%e5%8f%91%e5%ae%b6%e4%bb%8e%e5%86%9c%e5%9c%ba%e5%bc%80%e5%a7%8b.md" id="157 Zynga：发家从农场开始.md">157 Zynga：发家从农场开始.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/158%20%e8%ae%baZynga%e7%9a%84%e5%80%92%e5%8f%b0.md" id="158 论Zynga的倒台.md">158 论Zynga的倒台.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/159%20%e4%bc%81%e4%b8%9a%e5%88%86%e6%9e%90%e8%a6%81%e6%b1%82%e7%bb%bc%e5%90%88%e7%b4%a0%e8%b4%a8.md" id="159 企业分析要求综合素质.md">159 企业分析要求综合素质.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/%e6%8a%80%e6%9c%af%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a1%88%e4%be%8b%e8%a7%a3%e8%af%bb/%e7%bb%93%e6%9d%9f%e8%af%ad%20%e7%a7%af%e8%b7%ac%e6%ad%a5%ef%bc%8c%e8%80%8c%e7%bb%88%e8%87%b3%e5%8d%83%e9%87%8c.md" id="结束语 积跬步，而终至千里.md">结束语 积跬步，而终至千里.md</a>
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
<h1 class="title" data-id="090 Cassandra和DataStax的故事" id="title">090 Cassandra和DataStax的故事</h1>
<div><p>Cassandra是大数据时代中非常具有影响力的一个开源项目，DataStax则是背后支持开源Cassandra并将其商业化的公司。今天我们就来聊一下Cassandra和Datatax的故事。</p>
<p>我们都知道，在大数据发展历史上，谷歌的“三驾马车”：谷歌文件系统、 MapReduce、 BigTable。三者都曾经扮演了非常重要的角色，Hadoop开源生态圈里也有对应的Hadoop文件系统，Hadoop MapReduce和HBase。</p>
<p>但是在大数据发展史上，还有一篇影响力几乎等同于谷歌“三驾马车”的论文。它讲的就是亚马逊发布的Dynamo系统。</p>
<p>2008年，Dynamo系统的作者之一阿维纳什·拉克希曼（Avinash Lakshman），跳槽去了Facebook。跳槽的阿维纳（Avinash）和Facebook网站的另外一个工程师普拉桑特·马利克（Prashant Malik），一起开发了Cassandra，一个Dynamo的开源山寨版。</p>
<p>Cassandra开发出来之后很快就被开源了。早期Facebook对于开源这件事还是非常支持的，但是它开源的Cassandra很快就受到了一次重大的打击，这个打击可以说是十分致命的。</p>
<p>早年的Facebook对于谷歌技术非常崇拜，但对于亚马逊的技术却缺乏信心。于是Facebook准备开发移动App“Messenger”的时候，决定使用谷歌的技术架构。更明确一点说就是，Facebook抛弃了自己开发的Cassandra，选择了当时在Hadoop系统里山寨了BigTable的HBase。</p>
<p>亲儿子被自己的公司抛弃，开发人员也没什么兴趣继续开发了。与被众心捧月的HBase状态比起来，Cassandra当时就是一种被众人嫌弃的状态，不过，如果故事到此为止的话，那么Cassandra估计也就不会活到今天了。</p>
<p>我们把时光回溯到2010年，当时在Rackspace工作的乔纳森·艾利斯（Jonathan Ellis）和马特·皮菲尔（Matt Pfeil），这两个和Cassandra无关的人，决定离开Rackspace，自己创业。</p>
<p>Rackspace在工业界里最为著名的是OpenStack那一套体系，做的是数据中心云计算的基础架构。算起来和Cassandra这套NoSQL的东西多少也有点关系。</p>
<p>他们创业的故事非常有意思，同时也跟Cassandra有着千丝万缕的联系，公开的说法是这样的。</p>
<blockquote>
<p>乔纳森是个很牛的工程师，决定结束碌碌无为的工作状态，辞职创业去。马特代表公司去挽留这个人才，于是两个人约了去吃午餐；然而结局却颇为戏剧化，马特没有说服乔纳森继续为Rackspace工作，而杰纳森却说服了马特和他一起创业，并让他出任自己公司的CEO。<br/>
公司同年成立，最初公司的名字叫Riptano。创业需要有方向，乔纳森和马特看好开源社区商业化的模式，但是他们并没有打算成为Hadoop的发行商，所以环顾四周之后他们挑中了Cassandra，并打算将它做为核心，开启他们的创业之旅。<br/>
大概就是因为选取了Cassandra，公司的定位就比较明确了，也就是选择了云端数据处理的方向。于是他们觉得Riptano这个公司的名字不太适合公司的定位，就把公司名字改成了DataStax。这个故事就是DataStax的由来。</p>
</blockquote>
<p>自从2010年选中了Cassandra之后，DataStax就开始了全力以赴开发Cassandra的历程。在很长一段时间里，DataStax对Cassandra贡献的代码量，占据了整个代码提交量的85%以上。</p>
<p>可以说，正是因为DataStax的介入，才最终让Cassandra活了下来，并且在2011年成为了Apache基金会的顶级开源项目。DataStax推出的主打产品，是一个叫做DataStax Enterprise的东西。这是一个以Cassandra为核心，整合了诸多开源项目的产品。</p>
<p>DataStax Enterprise提供了两种模式，一种是卖软件和服务给企业，企业再装到自己的机器上去运行。另外一种是托管云服务“DataStax Managed Cloud”，这是一个运行在亚马逊云服务（AWS）上的云托管服务，用户无需购买和维护自己的机器。</p>
<p>从产品完整性和盈利模式来看，DataStax提供的是相对来说比较完整的一套产品体系。但是以Cassandra为核心的主要问题是，Cassandra的技术相对冷门，优点和缺点也都很明显，这导致的结果是：适用于Cassandra的应用也是有一定限制的。</p>
<p>DataStax的产品也因为选择了Cassandra作为核心，和其他公司的同类产品就有很明显的不一样。</p>
<p>具体来说，Cassandra是一个写入非常快、吞吐量很大、延时很低的系统；同时，这个系统的处理能力伴随容量的增长，也呈现出线性的增强。这些都是Cassandra的优势。尤其是做云端部署时，这个系统可以很灵活地根据工作负载来加减机器。</p>
<p>2012年，多伦多大学一篇论文比较研究了6个不同的NoSQL数据库的优劣，得出的结论是Cassandra是当之无愧的赢家。这篇论文被DataStax广泛引用，以此来证明这个系统比其他更为优质。</p>
<p>但是凡事都有两面性，Cassandra的缺点也很明显。首先是Cassandra有一个十分令人讨厌的问题：这个系统没办法保证一条记录行级别的一致性。</p>
<p>简单来说，如果A操作改变了行里面的一个列，B操作改变了同一行里面的另外一列，那么很有可能就得到了一条四不像的行。</p>
<p>这对应用程序来说是一件非常糟糕的事，虽然现实来说这种错误的概率不是特别高，但是只要不是0概率的话，很多应用程序都不可能使用这样的系统。</p>
<p>还有一个缺点是Cassandra普遍适用的场景非常有限，Cassandra虽然对于单行操作非常快，但是对于多行操作就会非常慢；而且不仅仅慢，很可能同时消耗的资源也会很高。</p>
<p>Cassandra对范围查询的能力比起HBase要差了很多。因此，通常来说Cassandra应用的场景适合只访问单行记录的，但是在单行记录的时候却不能保证行级别的一致性。这就是Cassandra适用场景的瓶颈所在。</p>
<p>不过，DataStax发展到了今天，它的主打产品DataStax Enterprise也是经过了多年的演进，并且在以Cassandra为核心的基础上，进行了全面的整合。</p>
<p>例如它通过对Spark和Solr的整合，提供了数据分析和搜索的功能。它还在自我完善中提供了对多种语言和开发平台的支持，比如说Java、Python、Ruby、 C++、Javascript等等。</p>
<p>此外，DataStax Enterprise还提供了给管理员用来做系统监控和操作的OpsCenter，以及给开发者提供的IDE环境 DataStax Studio。</p>
<p>从产品的完善程度来讲，DataStax Enterprise是非常完善的，它是一套整合了开源以及自主开发产品的系统，并提供了开发、运行、部署和监控几乎全方位的支持。这些都是这套系统的优势。</p>
<p>然而，DataStax的发展相对来说不温不火，在业界也只是名气平平。我想，它选择了Cassandra，既给了DataStax足够多的辨识度和区分度，也让DataStax的产品受到了各种限制。至于这样的选择到底是好是坏，对DataStax的发展是否有利，可能只有时间才能说清楚了。</p>
<p>不管怎么样，Cassandra仍然需要感谢DataStax的救命之恩和鼎力支持。可以说没有DataStax，就不会有今天的Cassandra。</p>
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
<p>© 2019 - 2023 <a href="/cdn-cgi/l/email-protection#c9a5a5a5f0fdf8f8f9fe89aea4a8a0a5e7aaa6a4" target="_blank">Liangliang Lee</a>.
                    Powered by <a href="https://github.com/gin-gonic/gin" target="_blank">gin</a> and <a href="https://github.com/kaiiiz/hexo-theme-book" target="_blank">hexo-theme-book</a>.</p>
</div>
</div>
<a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script>(function(){function c(){var b=a.contentDocument||a.contentWindow.document;if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'8f0cf3fcada685bb',t:'MTczMzk5ODUyNS4wMDAwMDA='};var a=document.createElement('script');a.nonce='';a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();</script></body>

<script src="/static/index.js"></script>
</head></html>