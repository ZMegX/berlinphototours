function headerImage (){
    let img = document.createElement('img');
    img.src = "https://picsum.photos/200/300";
    document.getElementById('header').appendChild(img);
    res.innerHTML = "Image Element added.";

} 