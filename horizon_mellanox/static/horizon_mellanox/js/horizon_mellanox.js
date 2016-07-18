
horizon.horizon_mellanox = {
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
        if(val != ""){
            var url = "http://" + val + "/neo/login?next=%2Fneo%2F#";
            var user = this._getCookie("mellanox_neo_host_user");
            var password = this._getCookie("mellanox_neo_host_password");

            var form_html = '<form id="neo_login" action="' + url + '" method="post" style="display:none;">' +
                                '<div class="form-group">' +
                                    '<input id="username" class="form-control" placeholder="Username" name="username" type="username" value="">' +
                                '</div>' +
                                '<div class="form-group">' +
                                    '<input id="password" class="form-control" placeholder="Password" name="password" type="password" value="">' +
                                '</div>' +
                                '<input id="auto-id-app-login-btn" type="submit" value="Login" class="btn btn-primary">' +
                                '<input type="hidden" name="redirect" value="true">' +
                            '</form>' ;
            var $frame = $('#neo_iframe');
            setTimeout( function() {
                var doc = $frame[0].contentWindow.document;
                var $body = $('body', doc);
                $body.html(form_html);
                $body.find('#username').val(user);
                $body.find('#password').val(password);
                $body.find('#neo_login').submit();
            }, 1 );
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
