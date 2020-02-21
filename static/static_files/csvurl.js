function getcsv(){
    if (localStorage.getItem('sdate')){
        var csv=document.getElementById("csv").value;
        if (typeof(Storage) !== "undefined") {
            // Store
            localStorage.setItem("csv", csv);
        };

        sdate = localStorage.getItem('sdate');
        edate = localStorage.getItem('edate');
        file = localStorage.getItem('file');
        server = localStorage.getItem('srvr');
        csv = localStorage.getItem('csv');
        num = document.getElementById("anchor").text;

        window.location.href = "http://127.0.0.1:8000/validation?page="+num+"&startdate="+sdate+"&enddate="+edate+"&server="+server+"&file="+file+"&csv="+csv+"";
    }else{

            var num = document.getElementById("anchor").text;
            var file = localStorage.getItem("filename");
            localStorage.clear()
            window.location.href = "http://127.0.0.1:8000/"+file+"?page="+num+"&csv="+csv+"";
    }

};
