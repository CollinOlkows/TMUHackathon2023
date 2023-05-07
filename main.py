import bottle
import json
import csv

@bottle.route("/")
def index():
    return bottle.static_file("index.html", root='.')
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







  




bottle.run(host="0.0.0.0", port=8080, debug=True)