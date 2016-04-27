
horizon.mellanox_dashboard = {
    _getCookie: function(cname) {
        var name = cname + "=";
        var ca = document.cookie.split(';');
        for(var i=0; i<ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0)==' ') c = c.substring(1);
                if (c.indexOf(name) == 0) return c.substring(name.length,c.length);
        }
        return "";
    },
    prepareNEOPanel: function(){
        var val = this._getCookie("mellanox_neo_host");
        if(val != ""){/*
            // neo authentication
            var xhttp = new XMLHttpRequest();
            var url = "http://" + val + "/neo/login";
            var user = this._getCookie("mellanox_neo_host_user");
            var password = this._getCookie("mellanox_neo_host_password");
            var data = "username=" + user + "&password=" + password;
            xhttp.open("POST", url, true);
            xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

            xhttp.onreadystatechange = function() {
                alert("on");
                if (xhttp.readyState == 4 && xhttp.status == 200) {
                    alert("ready state");
                    //document.getElementById("neo_iframe").src = "http://" + val + "/neo";
                }
            };
            xhttp.send(data);*/
            document.getElementById("neo_iframe").src = "http://" + val + "/neo";
        }else{
            var msg = "<h5 style='margin:20px;'>NEO hostname/ip is not set, you can set it in Configurations panel</h5>";
            document.getElementsByClassName("col-xs-12")[0].innerHTML = msg;
        }
    },
    prepareUFMPanel: function(){
        var val = this._getCookie("mellanox_ufm_host");
        if(val != "")
            document.getElementById("ufm_iframe").src = "http://" + val + "/ufmui";
        else{
            var msg = "<h5 style='margin:20px;'>UFM hostname/ip is not set, you can set it in Configurations panel</h5>";
            document.getElementsByClassName("col-xs-12")[0].innerHTML = msg;
        }	
    },
    prepareSettingsPanel: function(){
        document.getElementById("id_neo_host").value = this._getCookie("mellanox_neo_host");
        document.getElementById("id_neo_host_user").value = this._getCookie("mellanox_neo_host_user");
        document.getElementById("id_neo_host_password").value = this._getCookie("mellanox_neo_host_password");
        document.getElementById("id_ufm_host").value = this._getCookie("mellanox_ufm_host");

    }
};
