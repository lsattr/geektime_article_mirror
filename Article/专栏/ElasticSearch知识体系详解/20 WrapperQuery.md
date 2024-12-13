<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
<meta content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no" name="viewport"/>
<meta content="zh-cn" http-equiv="content-language"/>
<meta content="20 WrapperQuery" name="description"/>
<link href="/static/favicon.png" rel="icon"/>
<title>20 WrapperQuery </title>
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
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/ElasticSearch%e7%9f%a5%e8%af%86%e4%bd%93%e7%b3%bb%e8%af%a6%e8%a7%a3/01%20%e8%ae%a4%e7%9f%a5%ef%bc%9aElasticSearch%e5%9f%ba%e7%a1%80%e6%a6%82%e5%bf%b5.md" id="01 认知：ElasticSearch基础概念.md">01 认知：ElasticSearch基础概念.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/ElasticSearch%e7%9f%a5%e8%af%86%e4%bd%93%e7%b3%bb%e8%af%a6%e8%a7%a3/02%20%e8%ae%a4%e7%9f%a5%ef%bc%9aElastic%20Stack%e7%94%9f%e6%80%81%e5%92%8c%e5%9c%ba%e6%99%af%e6%96%b9%e6%a1%88.md" id="02 认知：Elastic Stack生态和场景方案.md">02 认知：Elastic Stack生态和场景方案.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/ElasticSearch%e7%9f%a5%e8%af%86%e4%bd%93%e7%b3%bb%e8%af%a6%e8%a7%a3/03%20%e5%ae%89%e8%a3%85%ef%bc%9aElasticSearch%e5%92%8cKibana%e5%ae%89%e8%a3%85.md" id="03 安装：ElasticSearch和Kibana安装.md">03 安装：ElasticSearch和Kibana安装.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/ElasticSearch%e7%9f%a5%e8%af%86%e4%bd%93%e7%b3%bb%e8%af%a6%e8%a7%a3/04%20%e5%85%a5%e9%97%a8%ef%bc%9a%e6%9f%a5%e8%af%a2%e5%92%8c%e8%81%9a%e5%90%88%e7%9a%84%e5%9f%ba%e7%a1%80%e4%bd%bf%e7%94%a8.md" id="04 入门：查询和聚合的基础使用.md">04 入门：查询和聚合的基础使用.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/ElasticSearch%e7%9f%a5%e8%af%86%e4%bd%93%e7%b3%bb%e8%af%a6%e8%a7%a3/05%20%e7%b4%a2%e5%bc%95%ef%bc%9a%e7%b4%a2%e5%bc%95%e7%ae%a1%e7%90%86%e8%af%a6%e8%a7%a3.md" id="05 索引：索引管理详解.md">05 索引：索引管理详解.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/ElasticSearch%e7%9f%a5%e8%af%86%e4%bd%93%e7%b3%bb%e8%af%a6%e8%a7%a3/06%20%e7%b4%a2%e5%bc%95%ef%bc%9a%e7%b4%a2%e5%bc%95%e6%a8%a1%e6%9d%bf%28Index%20Template%29%e8%af%a6%e8%a7%a3.md" id="06 索引：索引模板(Index Template)详解.md">06 索引：索引模板(Index Template)详解.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/ElasticSearch%e7%9f%a5%e8%af%86%e4%bd%93%e7%b3%bb%e8%af%a6%e8%a7%a3/07%20%e6%9f%a5%e8%af%a2%ef%bc%9aDSL%e6%9f%a5%e8%af%a2%e4%b9%8b%e5%a4%8d%e5%90%88%e6%9f%a5%e8%af%a2%e8%af%a6%e8%a7%a3.md" id="07 查询：DSL查询之复合查询详解.md">07 查询：DSL查询之复合查询详解.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/ElasticSearch%e7%9f%a5%e8%af%86%e4%bd%93%e7%b3%bb%e8%af%a6%e8%a7%a3/08%20%e6%9f%a5%e8%af%a2%ef%bc%9aDSL%e6%9f%a5%e8%af%a2%e4%b9%8b%e5%85%a8%e6%96%87%e6%90%9c%e7%b4%a2%e8%af%a6%e8%a7%a3.md" id="08 查询：DSL查询之全文搜索详解.md">08 查询：DSL查询之全文搜索详解.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/ElasticSearch%e7%9f%a5%e8%af%86%e4%bd%93%e7%b3%bb%e8%af%a6%e8%a7%a3/09%20%e6%9f%a5%e8%af%a2%ef%bc%9aDSL%e6%9f%a5%e8%af%a2%e4%b9%8bTerm%e8%af%a6%e8%a7%a3.md" id="09 查询：DSL查询之Term详解.md">09 查询：DSL查询之Term详解.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/ElasticSearch%e7%9f%a5%e8%af%86%e4%bd%93%e7%b3%bb%e8%af%a6%e8%a7%a3/10%20%e8%81%9a%e5%90%88%ef%bc%9a%e8%81%9a%e5%90%88%e6%9f%a5%e8%af%a2%e4%b9%8bBucket%e8%81%9a%e5%90%88%e8%af%a6%e8%a7%a3.md" id="10 聚合：聚合查询之Bucket聚合详解.md">10 聚合：聚合查询之Bucket聚合详解.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/ElasticSearch%e7%9f%a5%e8%af%86%e4%bd%93%e7%b3%bb%e8%af%a6%e8%a7%a3/11%20%e8%81%9a%e5%90%88%ef%bc%9a%e8%81%9a%e5%90%88%e6%9f%a5%e8%af%a2%e4%b9%8bMetric%e8%81%9a%e5%90%88%e8%af%a6%e8%a7%a3.md" id="11 聚合：聚合查询之Metric聚合详解.md">11 聚合：聚合查询之Metric聚合详解.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/ElasticSearch%e7%9f%a5%e8%af%86%e4%bd%93%e7%b3%bb%e8%af%a6%e8%a7%a3/12%20%e8%81%9a%e5%90%88%ef%bc%9a%e8%81%9a%e5%90%88%e6%9f%a5%e8%af%a2%e4%b9%8bPipline%e8%81%9a%e5%90%88%e8%af%a6%e8%a7%a3.md" id="12 聚合：聚合查询之Pipline聚合详解.md">12 聚合：聚合查询之Pipline聚合详解.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/ElasticSearch%e7%9f%a5%e8%af%86%e4%bd%93%e7%b3%bb%e8%af%a6%e8%a7%a3/13%20%e5%8e%9f%e7%90%86%ef%bc%9a%e4%bb%8e%e5%9b%be%e8%a7%a3%e6%9e%84%e7%ad%91%e5%af%b9ES%e5%8e%9f%e7%90%86%e7%9a%84%e5%88%9d%e6%ad%a5%e8%ae%a4%e7%9f%a5.md" id="13 原理：从图解构筑对ES原理的初步认知.md">13 原理：从图解构筑对ES原理的初步认知.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/ElasticSearch%e7%9f%a5%e8%af%86%e4%bd%93%e7%b3%bb%e8%af%a6%e8%a7%a3/14%20%e5%8e%9f%e7%90%86%ef%bc%9aES%e5%8e%9f%e7%90%86%e7%9f%a5%e8%af%86%e7%82%b9%e8%a1%a5%e5%85%85%e5%92%8c%e6%95%b4%e4%bd%93%e7%bb%93%e6%9e%84.md" id="14 原理：ES原理知识点补充和整体结构.md">14 原理：ES原理知识点补充和整体结构.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/ElasticSearch%e7%9f%a5%e8%af%86%e4%bd%93%e7%b3%bb%e8%af%a6%e8%a7%a3/15%20%e5%8e%9f%e7%90%86%ef%bc%9aES%e5%8e%9f%e7%90%86%e4%b9%8b%e7%b4%a2%e5%bc%95%e6%96%87%e6%a1%a3%e6%b5%81%e7%a8%8b%e8%af%a6%e8%a7%a3.md" id="15 原理：ES原理之索引文档流程详解.md">15 原理：ES原理之索引文档流程详解.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/ElasticSearch%e7%9f%a5%e8%af%86%e4%bd%93%e7%b3%bb%e8%af%a6%e8%a7%a3/16%20%e5%8e%9f%e7%90%86%ef%bc%9aES%e5%8e%9f%e7%90%86%e4%b9%8b%e8%af%bb%e5%8f%96%e6%96%87%e6%a1%a3%e6%b5%81%e7%a8%8b%e8%af%a6%e8%a7%a3.md" id="16 原理：ES原理之读取文档流程详解.md">16 原理：ES原理之读取文档流程详解.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/ElasticSearch%e7%9f%a5%e8%af%86%e4%bd%93%e7%b3%bb%e8%af%a6%e8%a7%a3/17%20%e4%bc%98%e5%8c%96%ef%bc%9aElasticSearch%e6%80%a7%e8%83%bd%e4%bc%98%e5%8c%96%e8%af%a6%e8%a7%a3.md" id="17 优化：ElasticSearch性能优化详解.md">17 优化：ElasticSearch性能优化详解.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/ElasticSearch%e7%9f%a5%e8%af%86%e4%bd%93%e7%b3%bb%e8%af%a6%e8%a7%a3/18%20%e5%a4%a7%e5%8e%82%e5%ae%9e%e8%b7%b5%ef%bc%9a%e8%85%be%e8%ae%af%e4%b8%87%e4%ba%bf%e7%ba%a7%20Elasticsearch%20%e6%8a%80%e6%9c%af%e5%ae%9e%e8%b7%b5.md" id="18 大厂实践：腾讯万亿级 Elasticsearch 技术实践.md">18 大厂实践：腾讯万亿级 Elasticsearch 技术实践.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/ElasticSearch%e7%9f%a5%e8%af%86%e4%bd%93%e7%b3%bb%e8%af%a6%e8%a7%a3/19%20%e8%b5%84%e6%96%99%ef%bc%9aAwesome%20Elasticsearch.md" id="19 资料：Awesome Elasticsearch.md">19 资料：Awesome Elasticsearch.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/ElasticSearch%e7%9f%a5%e8%af%86%e4%bd%93%e7%b3%bb%e8%af%a6%e8%a7%a3/20%20WrapperQuery.md" id="20 WrapperQuery.md">20 WrapperQuery.md</a>
</li>
<li>
<a class="menu-item" href="/%e4%b8%93%e6%a0%8f/ElasticSearch%e7%9f%a5%e8%af%86%e4%bd%93%e7%b3%bb%e8%af%a6%e8%a7%a3/21%20%e5%a4%87%e4%bb%bd%e5%92%8c%e8%bf%81%e7%a7%bb.md" id="21 备份和迁移.md">21 备份和迁移.md</a>
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
<h1 class="title" data-id="20 WrapperQuery" id="title">20 WrapperQuery</h1>
<div><h2 id="实现方式理论基础">实现方式理论基础</h2>
<ul>
<li>Wrapper Query 官网说明</li>
</ul>
<p><a href="https://www.elastic.co/guide/en/elasticsearch/reference/6.4/query-dsl-wrapper-query.html" target="_blank">https://www.elastic.co/guide/en/elasticsearch/reference/6.4/query-dsl-wrapper-query.html</a></p>
<blockquote>
<p>This query is more useful in the context of the Java high-level REST client or transport client to also accept queries as json formatted string. In these cases queries can be specified as a json or yaml formatted string or as a query builder (which is a available in the Java high-level REST client).</p>
</blockquote>
<pre><code class="language-json">GET /_search
{
    "query" : {
        "wrapper": {
            "query" : "eyJ0ZXJtIiA6IHsgInVzZXIiIDogIktpbWNoeSIgfX0=" // Base64 encoded string: {"term" : { "user" : "Kimchy" }}
        }
    }
}
</code></pre>
<ul>
<li>将DSL JSON语句 转成 map</li>
</ul>
<p><a href="https://blog.csdn.net/qq_41370896/article/details/83658948" target="_blank">https://blog.csdn.net/qq_41370896/article/details/83658948</a></p>
<pre><code class="language-java">String dsl = "";
Map maps = (Map)JSON.parse(dsl);  
maps.get("query");// dsl query string
</code></pre>
<ul>
<li>Java 代码</li>
</ul>
<p><a href="https://blog.csdn.net/tcyzhyx/article/details/84566734" target="_blank">https://blog.csdn.net/tcyzhyx/article/details/84566734</a></p>
<p><a href="https://www.jianshu.com/p/216ca70d9e62" target="_blank">https://www.jianshu.com/p/216ca70d9e62</a></p>
<pre><code class="language-java">StringBuffer dsl = new StringBuffer();
dsl.append("{\"bool\": {");
dsl.append("      \"must\": [");
dsl.append("        {");
dsl.append("          \"term\": {");
dsl.append("            \"mdid.keyword\": {");
dsl.append("              \"value\": \"2fa9d41e1af460e0d47ce36ca8a98737\"");
dsl.append("            }");
dsl.append("          }");
dsl.append("        }");
dsl.append("      ]");
dsl.append("    }");
dsl.append("}");
WrapperQueryBuilder wqb = QueryBuilders.wrapperQuery(dsl.toString());
SearchResponse searchResponse = client.prepareSearch(basicsysCodeManager.getYjzxYjxxIndex())
.setTypes(basicsysCodeManager.getYjzxYjxxType()).setQuery(wqb).setSize(10).get();
SearchHit[] hits = searchResponse.getHits().getHits();
for(SearchHit hit : hits){
	String content = hit.getSourceAsString();
	System.out.println(content);
}
</code></pre>
<ul>
<li>query + agg 应该怎么写</li>
</ul>
<p><a href="http://www.itkeyword.com/doc/1009692843717298639/wrapperquerybuilder-aggs-query-throwing-query-malformed-exception" target="_blank">http://www.itkeyword.com/doc/1009692843717298639/wrapperquerybuilder-aggs-query-throwing-query-malformed-exception</a></p>
<pre><code class="language-json">"{\"query\":{\"match_all\": {}},\"aggs\":{\"avg1\":{\"avg\":{\"field\":\"age\"}}}}"
SearchSourceBuilder ssb = new SearchSourceBuilder();

// add the query part
String query ="{\"match_all\": {}}";
WrapperQueryBuilder wrapQB = new WrapperQueryBuilder(query);
ssb.query(wrapQB);

// add the aggregation part
AvgBuilder avgAgg = AggregationBuilders.avg("avg1").field("age");
ssb.aggregation(avgAgg);
</code></pre>
<h2 id="实现示例">实现示例</h2>
<p>略</p>
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
<p>© 2019 - 2023 <a href="/cdn-cgi/l/email-protection#660a0a0a5f525757565126010b070f0a4805090b" target="_blank">Liangliang Lee</a>.
                    Powered by <a href="https://github.com/gin-gonic/gin" target="_blank">gin</a> and <a href="https://github.com/kaiiiz/hexo-theme-book" target="_blank">hexo-theme-book</a>.</p>
</div>
</div>
<a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script>(function(){function c(){var b=a.contentDocument||a.contentWindow.document;if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'8f0a83d228d51fb0',t:'MTczMzk3Mjk1OS4wMDAwMDA='};var a=document.createElement('script');a.nonce='';a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();</script></body>

<script src="/static/index.js"></script>
</head></html>