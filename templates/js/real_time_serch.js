window.onload = function (){	  
    var word = new Array();
    //객체 가져오기
    var ranking = document.getElementById("ranking");
    //Ajax객체 생성
    var request = new XMLHttpRequest();					
    //요청준비
    request.open("get","",true);
    //데이터 요청
    request.send();
    //데이터 수신
    request.onreadystatechange = function(){
        if(request.readyState==4){
            if(request.status==200){
                var obj = JSON.parse(request.responseText); //json객체로 변환
                var str="";
                for(var i=0; i<4; i++){
                    str = "["+(i+1)+"]"+obj.search_word[i].name;
                    word[i] = str;		//str을 순서대로 배열 형태로 저장
                }
            }
        }	
    }
    var i=0;	
    var interval = setInterval(function(){	
        if(i>3){		//i가 3이상이되면 반복이 종료되므로 
            i=0;		//다시 i를 0으로 초기화
        }
         ranking.innerHTML = "<h3>" + word[i] + "</h3>";
          i++;	  
      }, 2000);			//2초마다 갱신
      
      setTimeout(function(){
              clearInterval(interval);
      }, 20000); 		//20초후 정지	
}