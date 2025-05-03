---
layout: page
title: AI Papers
permalink: /papers/
---

<div class="page" lang="en">
    <div class="container content">
        <h1>Seminal AI Papers</h1>
        <p>Analysis and notes on foundational papers in artificial intelligence.</p>
        
        <ul class="paper-list">
            {% for paper in site.papers %}
            <li class="paper-item">
                <h2>
                    <a href="{{ paper.url }}">{{ paper.title }}</a>
                </h2>
                <p class="paper-meta">
                    {{ paper.authors }} ({{ paper.year }})
                </p>
                <p class="paper-excerpt">{{ paper.excerpt }}</p>
            </li>
            {% endfor %}
        </ul>
    </div>
</div>

<style>
.paper-list {
    list-style: none;
    padding: 0;
}

.paper-item {
    margin-bottom: 2em;
    padding-bottom: 2em;
    border-bottom: 1px solid #eee;
}

.paper-item:last-child {
    border-bottom: none;
}

.paper-meta {
    color: #666;
    font-style: italic;
    margin: 0.5em 0;
}

.paper-excerpt {
    margin: 0.5em 0;
}
</style> 