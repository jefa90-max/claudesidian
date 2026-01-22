#API Key

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 #示例代码

curl https://openrouter.ai/api/v1/chat/completions \

-H "Content-Type: application/json" \

-H "Authorization: Bearer $OPENROUTER_API_KEY" \

-d '{

"model": "google/gemini-2.0-flash-001",

"messages": [

{

"role": "user",

"content": [

{

"type": "text",

"text": "What is in this image?"

},

{

"type": "image_url",

"image_url": {

"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"

}

}

]

}

]

}'

  

#示例输入

{

"model": "google/gemini-2.5-flash",

"messages": [

{

"role": "user",

"content": [

{

"type": "text",

"text": "这个图片画的是什么"

},

{

"type": "image_url",

"image_url": {

"url": "https://pic.vjshi.com/2022-08-27/5c612acf898d4e4abfce6e933bfcd91d/00002.jpg?x-oss-process=style/watermark"

}

}

]

}

]

}

  

#示例输出

{

"id": "gen-1750477210-xeofCQamjp7GJTdLPjBC",

"provider": "Google",

"model": "google/gemini-2.5-flash",

"object": "chat.completion",

"created": 1750477210,

"choices": [

{

"logprobs": null,

"finish_reason": "stop",

"native_finish_reason": "STOP",

"index": 0,

"message": {

"role": "assistant",

"content": "这张图片描绘的是一个美丽的夜景，主要特色是一个宏伟的**桥梁式建筑**横跨河流。\n\n以下是这张图片中包含的一些细节：\n\n* **建筑群和桥梁：** 画面中心是一个宏伟的桥梁，上面建有传统的中华风格建筑，屋檐飞翘，灯火通明，尤其屋顶和窗户透出橙黄色的暖光。桥本身有多个桥洞，其中一个主要桥洞下方宽敞，另外两侧还有更小的圆形桥洞。\n* **河流：** 画面的前景是平静的河流，映照着桥梁和岸边建筑的灯光。水面上的灯光反射呈现出橙黄色和蓝色，波光粼粼。\n* **船只：** 河流上可以看到至少两艘木船，船上挂着红色的灯笼，也有游客坐在船上。\n* **城市背景：** 河流两岸是城市景观，有高层建筑，其中一些楼房的窗户也亮着灯。远处的高楼上可以看到一些发光的中文文字，例如左侧楼顶的“大康”和右侧大楼上的“中海广场”。\n* **灯光：** 整个画面充满了各种灯光，除了桥梁上的暖色调灯光，岸边和高楼也有蓝白色的灯光，营造出夜晚的城市活力。\n\n综合来看，这很可能是一个中国的城市夜景，展示了传统的建筑风格与现代城市景观的结合，尤其是那座结构独特的桥梁，看起来像是著名的安顺廊桥或类似的建筑。",

"refusal": null,

"reasoning": null

}

}

],

"usage": {

"prompt_tokens": 2327,

"completion_tokens": 333,

"total_tokens": 2660

}

}