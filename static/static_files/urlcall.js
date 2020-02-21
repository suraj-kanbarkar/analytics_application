function myFunction(num){
    url = "http://127.0.0.1:8000/"

    // getting the click event
    $(document).click(function(event) {
    var text = $(event.target).text();
    if (text === "Call Entry" || text === "Call Progress" || text === "CDR" || text === "Call Entry And CDR"
    || text === "Call Entry Not Matched" || text === "CDR Not Matched"){
        localStorage.removeItem("sdate");
        localStorage.removeItem("edate");
        localStorage.setItem("filename", text);
        }
        if (localStorage.getItem("filename") === "Call Entry"){
            var file = "call_entry";
            window.location.href = url+file+"?page="+num+"";
        }
        else if (localStorage.getItem("filename") === "CDR"){
            var file = "cdr";
            window.location.href = url+file+"?page="+num+"";
        }
        else if (localStorage.getItem("filename") === "Call Progress"){
            var file = "call_progress";
            window.location.href = url+file+"?page="+num+"";
        }
        else if (localStorage.getItem("filename") === "Call Entry And CDR"){
            var file = "call_entry_and_cdr";
            window.location.href = url+file+"?page="+num+"";
        }
        else if (localStorage.getItem("filename") === "Call Entry Not Matched"){
            var file = "call_entry_not_matched";
            window.location.href = url+file+"?page="+num+"";
        }
        else if (localStorage.getItem("filename") === "CDR Not Matched"){
            var file = "cdr_not_matched";
            window.location.href = url+file+"?page="+num+"";
        }
    });


    if (localStorage.getItem('sdate') !== null){
        localStorage.removeItem("filename");
        sdate = localStorage.getItem('sdate');
        edate = localStorage.getItem('edate');
        file = localStorage.getItem('file');
        server = localStorage.getItem('srvr');
//        page = document.getElementById("anchor").text;

        window.location.href = url+"validation?page="+num+"&startdate="+sdate+"&enddate="+edate+"&server="+server+"&file="+file+"";
    }
   };
