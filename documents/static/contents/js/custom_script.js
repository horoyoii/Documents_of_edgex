

$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });
});


function getPostList(){
    const query=`
        query {
              allPosts{ 
                  id
                  number
                  isMeta
                  slug
                  title
                  pubDate
              }
          }`;      
    
    const url = "/graphql";
    
    const opts = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ query}),
    };


    fetch(url, opts)
        .then(function(response){
            return response.json();
        })
        .then(function(myJson){
            var con_list= document.getElementById("contents_list");
            var sidebar_list = document.getElementById("main_sidebar");
            var main_li;

            $.each(myJson["data"]["allPosts"], function(key, value){

              
                // Make List in Main contents =============================
                var node = document.createElement("a");
                node.setAttribute("href", "/post/"+value["id"]);
                var text = document.createTextNode(value["number"]+" "+value["title"]);
                node.appendChild(text);
                con_list.appendChild(node);           
                con_list.appendChild(document.createElement("br"));
            

                // Make SideBar =============================
                
                if(value["isMeta"] == "true"){
 
                        main_li = document.createElement("li");
                        main_li.setAttribute("class", "activate");


                        var node = document.createElement("a");
                        node.setAttribute("href", "#"+value["slug"]);
                        node.setAttribute("class", "dropdown-toggle");
                        node.setAttribute("aria-expanded", "false");
                        node.setAttribute('data-toggle', "collapse");

                        node.appendChild(document.createTextNode(value["number"]+" "+value["title"]));
                        main_li.appendChild(node);

                        // make ul
                        var ul_node = document.createElement("ul");
                        ul_node.setAttribute("class", "collapse list-unstyled");
                        ul_node.setAttribute("id", value["slug"]);
                        
                        main_li.appendChild(ul_node);
                        sidebar_list.appendChild(main_li);
                }else{
                    var node = document.createElement("li");
                    var a_node = document.createElement("a");
                    a_node.setAttribute("href", "/post/"+value["id"]);
                    a_node.appendChild(document.createTextNode(value["number"]+" "+value["title"]));
                    node.appendChild(a_node);


                    document.getElementById(value["slug"]).appendChild(node);


                }


            });

            sidebar_list.appendChild(main_li);
            if(document.getElementById("con_main") != null){
                con_list.innerHTML="";
            }
        });

}


window.onload = function(){
    getPostList();
}   

