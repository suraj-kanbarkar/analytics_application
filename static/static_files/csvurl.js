function getcsv(){
    url = window.location.href
    sdate = localStorage.getItem('sdate');
    edate = localStorage.getItem('edate');
    file = localStorage.getItem('file');
    server = localStorage.getItem('srvr');
    csv = localStorage.getItem('csv');
    filename = localStorage.getItem('filename');
    num = document.getElementById("anchor").text;

    if (localStorage.getItem('sdate')){
        var csv=document.getElementById("csv").value;
        if (typeof(Storage) !== "undefined") {
            // Store
            localStorage.setItem("csv", csv);
        };
        window.location.href = url+"validation?page="+num+"&startdate="+sdate+"&enddate="+edate+"&server="+server+"&file="+file+"&csv="+csv+"";
    }else{
        if (filename === "Call Entry"){
            filename = "call_entry";
            window.location.href = url+filename+"?page="+num+"&csv="+csv+"";
        }
        else if (filename === "Call Progress"){
            filename = "call_progress";
            window.location.href = url+filename+"?page="+num+"&csv="+csv+"";
        }
        else if (filename === "CDR"){
            filename = "cdr";
            window.location.href = url+filename+"?page="+num+"&csv="+csv+"";
        }
        else if (filename === "Call Entry And CDR"){
            filename = "call_entry_and_cdr";
            window.location.href = url+filename+"?page="+num+"&csv="+csv+"";
        }
        else if (filename === "Call Entry Not Matched"){
            filename = "call_entry_not_matched";
            window.location.href = url+filename+"?page="+num+"&csv="+csv+"";
        }
        else if (filename === "CDR Not Matched"){
            filename = "cdr_not_matched";
            window.location.href = url+filename+"?page="+num+"&csv="+csv+"";
        }
        else if (filename === "LifeStyle CDR"){
            filename = "lifestyle_cdr";
            window.location.href = url+filename+"?page="+num+"&csv="+csv+"";
        }
    }

};
