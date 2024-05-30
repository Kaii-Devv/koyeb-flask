from flask import Flask, send_file, request, jsonify, render_template, Response
import uuid
import requests
import random
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello from Koyeb'
@app.route('/api/image')
def hello_world():
    prompt = request.args.get('prompt')
    if prompt:
        result = generateImagev2(prompt)
        return result

def generateImagev2(prompt,style='0',size='1:1'):
    ids=str(uuid.uuid4())
    label = {"0":"Custom","1":"Sketch General 1","10":"Comic Book 1","100":"3D Portrait 1","101":"Product Concept Art 1","102":"Line Art 2","103":"Illustration Art 1","104":"Illustration Art 2","105":"Cute Art 1","107":"Portrait Anime 1","108":"Portrait Anime 2","109":"Portrait Anime 3","11":"Comic Book 2","110":"Portrait Anime 4","113":"Portrait Game 4","114":"Photo Fashion 1","115":"Portrait Gothic 2","116":"Logo Illustration 1","117":"Psychedelic 1","118":"Illustration General 4","119":"Icon Minimal 1","12":"Comic Book 3","120":"Icon Black White 2","121":"Icon 3D 1","122":"Icon Cute 1","123":"Illustration General 2","124":"Isometric 1","125":"Isometric 2","126":"Concept Art 6","127":"Illustration General 5","128":"Concept Art 5","129":"Portrait Game 5","13":"Doom 1","130":"Illustration Art 3","131":"Portrait 6","132":"Portrait 5","133":"Portrait Game  6","134":"Portrait Anime 5","135":"Portrait 4","136":"Portrait 8","137":"Portrait 9","138":"Portrait 10","139":"Hotpot Art 8","14":"Doom 2","140":"Hotpot Art 9","141":"Portrait Concept Art 1","142":"Portrait Concept Art 2","143":"Portrait Game 7","144":"Portrait Concept Art 3","145":"Hotpot Art 10","146":"Concept Art 7","147":"Oil Painting 2","148":"Cyberpunk 1","149":"Cyberpunk 2","15":"Watercolor 1","150":"Chinese Art 1","151":"Chinese Art 2","152":"Chinese Art 3","153":"Japanese Art 2","154":"Photo Moody 1","155":"Watercolor 2","156":"Watercolor 3","158":"Anime Cute 1","159":"Fractal Pattern 1","16":"Japanese Art","160":"Painting Fusion 1","161":"Photo Cinematic 1","162":"Painting Fusion 3","163":"Sculpture Glass 1","164":"Photo Dystopian 1","165":"Painting Black White 1","166":"Painting Fusion 4","167":"Painting Fusion 5","168":"Painting Geometric 1","169":"Illustration Palette 1","17":"Acrylic Art","170":"Watercolor Black White 1","171":"Photo Dystopian 2","172":"Poster War Zone 1","173":"Animation 5","174":"Portrait Anime 6","175":"Portrait Anime 7","178":"Hotpot Art 11","179":"Hotpot Art 12","18":"Graffiti","180":"Photo General 2","181":"Hotpot Ephemeral Wisp 1","182":"Game Art 1","183":"Comic Book 6","184":"Bacon Art 1","185":"Anime Fantasy 1","186":"Anime 2","187":"Anime 3","188":"Portrait Anime 8","189":"Anime 4","19":"Hotpot Art 1","190":"Anime Realistic 1","191":"Anime 5","192":"Anime Van Gogh 1","193":"Photo Black White 1","194":"Photo Cinematic 2","195":"Demon Black White 1","196":"Iridescent Marble 1","197":"Photo Fashion 2","198":"Logo Minimal 1","199":"Anime 6","20":"Hotpot Art 2","200":"Doom 3","201":"Fast Blur 1","202":"Bioluminescence 1","203":"Iridescent Metal 1","204":"3D Toy 1","205":"Pizza Art 1","206":"Halftone Dystopian 1 ","207":"Cyberorganic 1","21":"Hotpot Art 3","22":"Hotpot Art 5","24":"Pixel Art","25":"Sculpture General 1","26":"Fantasy 1","27":"Fantasy 2","28":"Fantasy 3","29":"Anime 1","3":"Sketch General 3","30":"Anime Black White","31":"Anime Berserk","32":"Anime Korean 1","33":"Portrait 1","34":"Portrait 2","35":"Portrait 3","36":"Portrait Mugshot","37":"Portrait Marble","38":"Portrait Gothic","39":"Oil Painting 1","4":"Sketch Scribble Black White 1","40":"3D Black White","41":"3D General 1","42":"3D Print 1","43":"3D General 2","44":"3D General 3","45":"3D Voxel 1","46":"3D Minecraft 1","47":"3D Roblox 1","48":"Photo General Volumetric Lighting 1","49":"Photo General 1","5":"Sketch Scribble Color 1","53":"Illustration General 1","54":"Charcoal 1","55":"Charcoal 2","56":"Charcoal 3","57":"Steampunk","58":"Line Art","59":"Gothic","6":"Icon Black White","60":"Animation 1","61":"Animation 2","62":"Architecture Interior Modern 1","63":"Architecture General 1","64":"Sci-fi 1","65":"Logo Detailed 1","66":"Logo Draft 1","67":"Logo Clean 1","68":"Logo Hipster 1","69":"Illustration Flat","7":"Icon Flat","70":"Animation 3","71":"Concept Art 2","72":"Cartoon 1","73":"Comic Book 4","74":"Architecture Interior 1","75":"Architecture Exterior 1","76":"Comic Book 5","77":"Concept Art 3","78":"Stained Glass 1","79":"Animation 4","8":"Icon Sticker Black White","80":"Retro Art","81":"Pop Art","82":"Illustration Smooth","83":"Portrait Game 1","84":"Concept Art 4","85":"Sci-fi 2","86":"Sci-fi 3","87":"Logo Sticker 1","88":"Painting Huang Gongwang 1","89":"Painting Claude Monet 1","9":"Icon Sticker","90":"Painting Pablo Picasso 1","91":"Painting Paul Cezanne 1","92":"Painting Salvador Dali 1","93":"Painting Vincent Van Gogh 1","95":"Portrait Figurine 1","96":"Low Poly 1","97":"Low Poly 2","98":"Portrait Game 2","99":"Portrait Game 3"}
    data = {'seedValue':'null','inputText':prompt, 'width':'512','max':'512','height':'512', 'styleId':style,'styleLabel':label[style],'isPrivate':'true','price':'0','requestId':ids,'resultUrl':'https://hotpotmedia.s3.us-east-2.amazonaws.com/'+ids+'.png'}
    headers = {
      'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
      'sec-ch-ua': "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
      'Api-Token': "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MTA3NzE4MDQsImV4cCI6MTc0MTkzOTk1M30.HTJNdJgCMhOwP08NRIan_qI3AbRWz33MqnALrU2RdU8",
      'sec-ch-ua-mobile': "?0",
      'Authorization': "hotpot-t2mJbCr8292aQzp8CnEPaK",
      'sec-ch-ua-platform': "\"Linux\"",
      'Origin': "https://hotpot.ai",
      'Sec-Fetch-Site': "same-site",
      'Sec-Fetch-Mode': "cors",
      'Sec-Fetch-Dest': "empty",
      'Referer': "https://hotpot.ai/",
      'Accept-Language': "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,su;q=0.6"
    }
    response = requests.post("https://api.hotpot.ai/art-premium-test1", data=data, headers=headers)
    try:
        return eval(response.text)
    except Exception as e:print(e);print(response.text);raise(e)

if __name__ == "__main__":
    app.run()