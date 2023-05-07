function ajaxGetRequest(path, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("GET", path);
    request.send();
}

function ajaxPostRequest(path, data, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("POST", path);
    request.send(data);
}




cycles=0
n=-1
profiles=[]
Image=0
score=0

function home(){
  
  //Reset all variables
  console.log('Done')
}

//making a guess its a real account
function real(){
  if(document.getElementById("Bot_Button").style.visibility == 'visible'){
    if(cycles<5){
    console.log('Guessed Real');
    cycles+=1;
      if(profiles[num][0]=='not '){
        score+=100
        console.log(score)
        console.log('here')
        document.getElementById("Score").innerHTML=score
      }
    let id=document.getElementById("Bot_Button");
    id.style.visibility="hidden";
    id=document.getElementById("Next");
    id.style.visibility="visible";
    id=document.getElementById("Exp");
      id=document.getElementById("Exp");
    document.getElementById("Exp").innerHTML=profiles[num][26]
    id.style.visibility="visible";
  }else{
    let id=document.getElementById("Leaderboards");
    id.style.visibility="visible"
      id=document.getElementById("Exp");
      id.style.visibility="visible"

  }
  }else{
    console.log('nahhhh')
  }
  
}

//making the guess its a fake account
function Bot(){
  if(document.getElementById("Real_Button").style.visibility == 'visible'){
    if(cycles<5){
    console.log('Guessed Bot');
    console.log(cycles)
      if(profiles[num][0]=='bot '){
        score+=100
        console.log(score)
        document.getElementById("Score").innerHTML=score
      }
    let id=document.getElementById("Real_Button");
    id.style.visibility="hidden"
    id=document.getElementById("Next");
    id.style.visibility="visible"
      ///if correct update score value else dont
    id=document.getElementById("Exp");
    document.getElementById("Exp").innerHTML=profiles[num][26]
    id.style.visibility="visible"
    cycles+=1;
  }else{
    let id=document.getElementById("Leaderboards");
    id.style.visibility="visible"
      id=document.getElementById("Exp");
      id.style.visibility="visible"
  }
  }else{
    console.log('nah')
  }
  
}

//update the leaderboard info
function Leaderboard(){

  
}

function Next(){
  let id=document.getElementById("Real_Button");
  id.style.visibility="visible";
  id=document.getElementById("Bot_Button");
  id.style.visibility="visible";
  id=document.getElementById("Exp");
  id.style.visibility="hidden";
  id=document.getElementById("Next");
  id.style.visibility="hidden";
  profiles.splice(n,1)
  SetupProfile()
}
function LoadData(){
  ajaxGetRequest('/data',Loaded)
}
function SetupProfile(){
  console.log(profiles)
  if(cycles<5){
    num=Math.floor(Math.random() * profiles.length);
  n=num
  console.log(n)
  id=document.getElementById("pfp");
  console.log(num)
  s=profiles[num]
  console.log(s)
  id.src=profiles[num][27]
  id=document.getElementById("Exp");
    document.getElementById("Exp").innerHTML=profiles[num][26]
  id=document.getElementById("Image1");
  id.src=profiles[num][8]
  id=document.getElementById("Image2");
  id.src=profiles[num][11]
  id=document.getElementById("Image3");
  id.src=profiles[num][14]
  id=document.getElementById("Image4");
  id.src=profiles[num][17]
  id=document.getElementById("Image5");
  id.src=profiles[num][20]
  id=document.getElementById("Image6");
  id.src=profiles[num][23]
  id=document.getElementById("Profile_Name").innerHTML='@'+profiles[num][1]
  id=document.getElementById("Name").innerHTML=profiles[num][2]
  id=document.getElementById("Bio").innerHTML=profiles[num][7]
  id=document.getElementById("Web").innerHTML=profiles[num][3]
  id=document.getElementById("Profile_Posts_Count").innerHTML=profiles[num][4]
  id=document.getElementById("Profile_Followers_Count").innerHTML=profiles[num][5]
  id=document.getElementById("Profile_Following_count").innerHTML=profiles[num][6]
  return
  }
  else{
    let id=document.getElementById("Leaderboards");
    id.style.visibility="visible"
      id=document.getElementById("Exp");
      id.style.visibility="visible"
  }
  if (n > -1) { 
    profiles.splice(n, 1); 
  }
  
  

}

function Zoom(){
  ajaxGetRequest('/currentData',LoadedC)
  
}

function LoadedC(response){
  let d = JSON.parse(response);
  let s = JSON.parse(response);
  console.log(d)
  id=document.getElementById("Img");
  if(s[0][0]=='1'){
    id.src=d[0][10];
    id.style.visibility="visible";
    document.getElementById("D").innerHTML=d[0][11]
    document.getElementById("Caption").innerHTML=d[0][10]
  }else if(s[0][0]=='2'){
    id.src=d[0][12];
    id.style.visibility="visible";
    document.getElementById("D").innerHTML=d[0][14]
    document.getElementById("Caption").innerHTML=d[0][13]
  }else if(s[0][0]=='3'){
    id.src=d[0][15];
    id.style.visibility="visible";
    document.getElementById("D").innerHTML=d[0][17]
    document.getElementById("Caption").innerHTML=d[0][16]
  }else if(s[0][0]=='4'){
    id.src=d[0][18];
    id.style.visibility="visible";
    document.getElementById("D").innerHTML=d[0][20]
    document.getElementById("Caption").innerHTML=d[0][19]
  }else if(s[0][0]=='5'){
    id.src=d[0][21];
    id.style.visibility="visible";
    document.getElementById("D").innerHTML=d[0][23]
    document.getElementById("Caption").innerHTML=d[0][22]
  }else if(s[0][0]=='6'){
    id.src=d[0][24];
    id.style.visibility="visible";
    document.getElementById("D").innerHTML=d[0][26]
    document.getElementById("Caption").innerHTML=d[0][25]
  }
}

function set_image(num) {
  Image=num
  l=[num]
  l=l.concat(profiles[n])
  l=JSON.stringify(l)
  ajaxPostRequest('/save',l,DONONE)
}
function DONONE(){
  console.log('none')
}

function Loaded(response){
  let data = JSON.parse(response);
  profiles=data
  SetupProfile()
}
