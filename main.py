import bottle
import json
import csv

@bottle.route("/")
def index():
    return bottle.static_file("Home.html", root='.')
@bottle.route("/instagram")
def instagram():
    return bottle.static_file("instagram.html", root='.')
@bottle.route("/icon1.png")
def icon1():
    return bottle.static_file("icon1.png", root='.')
@bottle.route("/Temp_image.png")
def Temp_image():
    return bottle.static_file("Temp_image.png", root='.')
@bottle.route("/play")
def play():
    return bottle.static_file("play_screen.html", root='.')
@bottle.route("/main.js")
def js():
    return bottle.static_file("main.js", root='.')
@bottle.route("/zoom")
def zoom():
    return bottle.static_file("image_zoomed.html", root='.')
@bottle.route('/data')
def data():
  o=[]
  with open('data.csv') as fp:
    reader=csv.reader(fp)
    next(reader)
    for lines in reader:
      o.append(lines)
    o = json.dumps(o)
    print(o)
    return o

@bottle.post('/save')
def save():
  stateInput = bottle.request.body.read().decode()
  state = json.loads(stateInput)
  with open('current.csv','w') as fp:
    writer=csv.writer(fp)
    writer.writerow(state)
    return
@bottle.route('/currentData')
def Cdata():
  o=[]
  with open('current.csv') as fp:
    reader=csv.reader(fp)
    for lines in reader:
      o.append(lines)
    o = json.dumps(o)
    print(o)
    return o



# not 1
@bottle.route('/Questions/Type 1 - Bot or Not/not - 1/pfp.jpg')
def pfp1():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 1/pfp.jpg",root='.')
@bottle.route('/Questions/Type 1 - Bot or Not/not - 1/post1.png')
def post11():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 1/post1.png",root='.')
@bottle.route('/Questions/Type 1 - Bot or Not/not - 1/post2.png')
def post12():
  return bottle.static_file("Questions/Type 1 - Bot or Not/not - 1/post2.png",root='.')
@bottle.route('/Questions/Type 1 - Bot or Not/not - 1/post3.png')
def post13():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 1/post3.png",root='.')
@bottle.route('/Questions/Type 1 - Bot or Not/not - 1/post4.png')
def post14():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 1/post4.png",root='.')
@bottle.route('/Questions/Type 1 - Bot or Not/not - 1/post5.png')
def post15():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 1/post5.png",root='.')
@bottle.route('/Questions/Type 1 - Bot or Not/not - 1/post6.png')
def post16():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 1/post6.png",root='.')

# not 2
@bottle.route('/Questions/Type 1 - Bot or Not/not - 2/post1.png')
def post17():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 2/post1.png",root='.')
@bottle.route('/Questions/Type 1 - Bot or Not/not - 2/post2.png')
def post18():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 2/post2.png",root='.')
@bottle.route('/Questions/Type 1 - Bot or Not/not - 2/post3.png')
def post19():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 2/post3.png",root='.')
@bottle.route('/Questions/Type 1 - Bot or Not/not - 2/post4.png')
def post20():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 2/post4.png",root='.')
@bottle.route('/Questions/Type 1 - Bot or Not/not - 2/post5.png')
def post21():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 2/post5.png",root='.')
@bottle.route('/Questions/Type 1 - Bot or Not/not - 2/post6.png')
def post22():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 2/post6.png",root='.')
@bottle.route('/Questions/Type 1 - Bot or Not/not - 2/pfp.jpg')
def post24():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 2/pfp.jpg",root='.')

# not 3
@bottle.route('/Questions/Type 1 - Bot or Not/not - 3/post1.png')
def post25():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 3/post1.png",root='.')
  
@bottle.route('/Questions/Type 1 - Bot or Not/not - 3/post2.png')
def post26():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 3/post2.png",root='.')
  
@bottle.route('/Questions/Type 1 - Bot or Not/not - 3/post3.png')
def post27():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 3/post3.png",root='.')
  
@bottle.route('/Questions/Type 1 - Bot or Not/not - 3/post4.png')
def post28():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 3/post4.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/not - 3/post5.png')
def post29():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 3/post5.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/not - 3/post6.png')
def post30():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 3/post6.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/not - 3/pfp.jpg')
def post31():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 3/pfp.jpg",root='.')

# not 4
@bottle.route('/Questions/Type 1 - Bot or Not/not - 4/post1.png')
def post32():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 4/post1.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/not - 4/post2.png')
def post33():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 4/post2.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/not - 4/post3.png')
def post34():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 4/post3.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/not - 4/post4.png')
def post35():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 4/post4.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/not - 4/post5.png')
def post36():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 4/post5.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/not - 4/post6.png')
def post37():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 4/post6.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/not - 4/pfp.jpg')
def post38():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 4/pfp.jpg",root='.')

# not 5
@bottle.route('/Questions/Type 1 - Bot or Not/not - 5/post1.png')
def post39():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 5/post1.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/not - 5/post2.png')
def post40():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 5/post2.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/not - 5/post3.png')
def post41():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 5/post3.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/not - 5/post4.png')
def post42():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 5/post4.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/not - 5/post5.png')
def post43():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 5/post5.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/not - 5/post6.png')
def post44():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 5/post6.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/not - 5/pfp.jpg')
def post45():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/not - 5/pfp.jpg",root='.')

# bot 1
@bottle.route('/Questions/Type 1 - Bot or Not/bot - 1/post1.png')
def post46():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 1/post1.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 1/post2.png')
def post47():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 1/post2.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 1/post3.png')
def post48():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 1/post3.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 1/post4.png')
def post49():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 1/post4.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 1/post5.png')
def post50():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 1/post5.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 1/post6.png')
def post51():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 1/post6.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 1/pfp.jpg')
def post52():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 1/pfp.jpg",root='.')

# bot 2
@bottle.route('/Questions/Type 1 - Bot or Not/bot - 2/post1.png')
def post53():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 2/post1.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 2/post2.png')
def post54():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 2/post2.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 2/post3.png')
def post55():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 2/post3.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 2/post4.png')
def post56():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 2/post4.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 2/post5.png')
def post57():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 2/post5.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 2/post6.png')
def post58():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 2/post6.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 2/pfp.jpg')
def post59():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 2/pfp.jpg",root='.')

# bot 3
@bottle.route('/Questions/Type 1 - Bot or Not/bot - 3/post1.png')
def post60():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 3/post1.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 3/post2.png')
def post61():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 3/post2.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 3/post3.png')
def post62():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 3/post3.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 3/post4.png')
def post63():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 3/post4.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 3/post5.png')
def post64():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 3/post5.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 3/post6.png')
def post65():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 3/post6.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 3/pfp.jpg')
def post66():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 3/pfp.jpg",root='.')

# bot 4
@bottle.route('/Questions/Type 1 - Bot or Not/bot - 4/post1.png')
def post67():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 4/post1.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 4/post2.png')
def post68():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 4/post2.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 4/post3.png')
def post69():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 4/post3.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 4/post4.png')
def post70():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 4/post4.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 4/post5.png')
def post71():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 4/post5.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 4/post6.png')
def post72():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 4/post6.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 4/pfp.jpg')
def post73():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 4/pfp.jpg",root='.')

# ----- bot 5 -------
@bottle.route('/Questions/Type 1 - Bot or Not/bot - 5/post1.png')
def post74():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 5/post1.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 5/post2.png')
def post75():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 5/post2.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 5/post3.png')
def post76():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 5/post3.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 5/post4.png')
def post77():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 5/post4.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 5/post5.png')
def post78():
  return bottle.static_file("Questions/Type 1 - Bot or Not/bot - 5/post5.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 5/post6.png')
def post79():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 5/post6.png",root='.')

@bottle.route('/Questions/Type 1 - Bot or Not/bot - 5/pfp.jpg')
def post80():
  return bottle.static_file("/Questions/Type 1 - Bot or Not/bot - 5/pfp.jpg",root='.')


@bottle.route('/Team.html')
def idc1():
  return bottle.static_file("/Team.html",root='.')
@bottle.route('/Returning Players.html')
def idc2():
  return bottle.static_file("/Returning Players.html",root='.')
@bottle.route('/Our Mission and Goals.html')
def idc3():
  return bottle.static_file("/Our Mission and Goals.html",root='.')
@bottle.route('/Leader Board.html')
def idc4():
  return bottle.static_file("/Leader Board.html",root='.')
@bottle.route('/Home.html')
def idc5():
  return bottle.static_file("/Home.html",root='.')
@bottle.route('/Game.html')
def idc6():
  return bottle.static_file("/Game.html",root='.')
@bottle.route('/Blank 1.html')
def idc7():
  return bottle.static_file("/Blank 1.html",root='.')
@bottle.route('/Blank 2.html')
def idc8():
  return bottle.static_file("/Blank 2.html",root='.')
@bottle.route('/About.html')
def idc9():
  return bottle.static_file("/About.html",root='.')
@bottle.route('/Play Now.html')
def idc10():
  return bottle.static_file("/Play Now.html",root='.')

@bottle.route('/Team/917d6f86a9afc3640bf04951cd61f707.jpg')
def idc11():
  return bottle.static_file("/Team/917d6f86a9afc3640bf04951cd61f707.jpg",root='.')

@bottle.route('/Team/27d54c0ecc85dc46c2333716da274549.jpg')
def idc12():
  return bottle.static_file("/Team/27d54c0ecc85dc46c2333716da274549.jpg",root='.')

@bottle.route('/Team/b81a05c8d45ae618dc194660b1bdcd84.jpg')
def idc13():
  return bottle.static_file("/Team/b81a05c8d45ae618dc194660b1bdcd84.jpg",root='.')
  
@bottle.route('/Team/c1ae1504910fb5ab862e70044e8b31d3.jpg')
def idc14():
  return bottle.static_file("/Team/c1ae1504910fb5ab862e70044e8b31d3.jpg",root='.')
  
@bottle.route('/Team/dd31e5de947b8893eafd0af61db4a2a6.jpg')
def idc15():
  return bottle.static_file("/Team/dd31e5de947b8893eafd0af61db4a2a6.jpg",root='.')
  
@bottle.route('/Team/eceb2e1af111094ba6c1cbfde153eadf.jpg')
def idc16():
  return bottle.static_file("/Team/eceb2e1af111094ba6c1cbfde153eadf.jpg",root='.')

@bottle.route('/Our Mission and Goals/277cdd526e6ceaea1ada061fb0e30ba5.jpg')
def idc17():
  return bottle.static_file("/Our Mission and Goals/277cdd526e6ceaea1ada061fb0e30ba5.jpg",root='.')

@bottle.route('/Our Mission and Goals/4926316e7e4022ec70ba41d45bad5131.jpg')
def idc18():
  return bottle.static_file("/Our Mission and Goals/4926316e7e4022ec70ba41d45bad5131.jpg",root='.')

@bottle.route('/Our Mission and Goals/aebfde07b6ae86654fbc11ed12775cf5.jpg')
def idc19():
  return bottle.static_file("/Our Mission and Goals/aebfde07b6ae86654fbc11ed12775cf5.jpg",root='.')

@bottle.route('/Our Mission and Goals/f05eda15ec48f71715ffce669c5a1114.jpg')
def idc20():
  return bottle.static_file("/Our Mission and Goals/f05eda15ec48f71715ffce669c5a1114.jpg",root='.')


@bottle.route('/Home/1b6d85e6ebeee04ac69ce8b9f700cf2a.jpg')
def idc21():
  return bottle.static_file("/Home/1b6d85e6ebeee04ac69ce8b9f700cf2a.jpg",root='.')

@bottle.route('/Home/6dd435f5031b34febd41b2cce9a1ab8b.jpg')
def idc22():
  return bottle.static_file("/Home/6dd435f5031b34febd41b2cce9a1ab8b.jpg",root='.')

@bottle.route('/Home/054d44ff114c768607d9b138176b5f04.jpg')
def idc23():
  return bottle.static_file("/Home/054d44ff114c768607d9b138176b5f04.jpg",root='.')

@bottle.route('/Home/224a76b350745e2098a09a13f8d06bb6.jpg')
def idc24():
  return bottle.static_file("/Home/224a76b350745e2098a09a13f8d06bb6.jpg",root='.')

@bottle.route('/Home/788b04872c8999e6f07c2baefac14506.jpg')
def idc25():
  return bottle.static_file("/Home/788b04872c8999e6f07c2baefac14506.jpg",root='.')

@bottle.route('/About/8ecf02110c866da69bf9423681b470bf.jpg')
def idc26():
  return bottle.static_file("/About/8ecf02110c866da69bf9423681b470bf.jpg",root='.')

@bottle.route('/About/238720247980ea5459e3f6318a811fd3.jpg')
def idc27():
  return bottle.static_file("/About/238720247980ea5459e3f6318a811fd3.jpg",root='.')
@bottle.route('/917d6f86a9afc3640bf04951cd61f707.jpg')
def idc27():
  return bottle.static_file("/917d6f86a9afc3640bf04951cd61f707.jpg",root='.')


  
  
  
  
  




  




bottle.run(host="0.0.0.0", port=8080, debug=True)