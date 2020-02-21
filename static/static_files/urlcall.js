function myFunction(num){
    // getting the click event
    $(document).click(function(event) {
    var text = $(event.target).text();
    if (text === "Call Entry" || text === "CDR" || text === "CALL PROGRESS" || text === "Call Entry And CDR" || text === "Call Entry Not Matched" || text === "CDR Not Matched"){
        localStorage.removeItem("sdate");
        localStorage.removeItem("edate");
        localStorage.removeItem("file");
        localStorage.removeItem("server");
        localStorage.setItem("filename", text);
        };
    });
    if (document.getElementById("sdate").value !== null){
        sdate = localStorage.getItem('sdate');
        edate = localStorage.getItem('edate');
        file = localStorage.getItem('file');
        server = localStorage.getItem('srvr');
//        page = document.getElementById("anchor").text;

       window.location.href = "http://127.0.0.1:8000/validation?page="+num+"&startdate="+sdate+"&enddate="+edate+"&server="+server+"&file="+file+"";
    }
    if (localStorage.getItem("filename") === "Call Entry"){
        var file = "call_entry";
        window.location.href = "http://127.0.0.1:8000/"+file+"?page="+num+"";
    }
    else if (localStorage.getItem("filename") === "CDR") {
        var file = "cdr";
        window.location.href = "http://127.0.0.1:8000/"+file+"?page="+num+"";
    }
    else if (localStorage.getItem("filename") === "CALL PROGRESS"){
        var file = "call_progress";
        window.location.href = "http://127.0.0.1:8000/"+file+"?page="+num+"";
    }
    else if (localStorage.getItem("filename") === "Call Entry And CDR"){
        var file = "call_entry_and_cdr";
        window.location.href = "http://127.0.0.1:8000/"+file+"?page="+num+"";
    }
    else if (localStorage.getItem("filename") === "Call Entry Not Matched"){
        var file = "call_entry_not_matched";
        window.location.href = "http://127.0.0.1:8000/"+file+"?page="+num+"";
    }
    else if (localStorage.getItem("filename") === "CDR Not Matched"){
        var file = "cdr_not_matched";
        window.location.href = "http://127.0.0.1:8000/"+file+"?page="+num+"";
    }
//        filename = document.getElementsByName("call_entry").name;
//
//
//        window.location.href = "http://127.0.0.1:8000/"+filename+"?page="+num+"";

   };
