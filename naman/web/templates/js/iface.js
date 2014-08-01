function cancel_iface_edition(machine_id){

    load_url("#iface_div", "{%url 'ifaces_by_machine' %}" + machine_id)

}
function fill_free_ip(vlan){

    $("#link_free_ip").attr("onclick", "get_ip("+vlan+")")
}

function get_ip(vlan_id){
  $.getJSON( "{%url 'get_free_ip_by_vlan' %}" + vlan_id, function( data ) {
        var items = [];
        $.each( data, function( key, val ) {
            $("#id_ip").val(val)
        });
        $("#id_dhcp").attr("checked", false)
    })
}
function del_iface(id){
  send_url("{%url 'delete_iface' %}" + id, function(data){
    if(data == "OK") $("tr[i=" + id+"]").fadeOut()
    toggle_nvlanc_btn()
    });
}

function del_iface_form(id) {
  send_url("{%url 'delete_iface' %}" + id, function(data){

    window.location="{%url 'home'%}"
    });
}

function edit_iface(id) {
  $("#glyphicon").fadeOut();$(".glyphicon").remove()
  send_url("{%url 'iface_by_machine' %}" + id, function(data){$("tr[i=" + id+"]").replaceWith(data);$("#niface_btn").fadeOut()});
}

function iface_short_form() {
  var id = $("#obj_id").attr("i")
  send_url(
    "{%url 'iface_by_machine' %}",
    function(data){
      $("#iface_tbl .glyphicon").remove()
      if(data) $('#iface_tbl tr:last').after(data)
    },
    "machines=" + id
    );
  $("#niface_btn").fadeOut()
  delete id;
}

function save_iface(id) {
  init_progress();
  machine = $("#obj_id").attr("i")
  $.ajax({
    url: "{%url 'iface_by_machine'%}" + id,
    method: "POST",
    data: {
      "vlan": $("#id_vlan").val(),
      "ip": $("#id_ip").val(),
      "mac": $("#id_mac").val(),
      "dhcp": $("#id_dhcp").is(":checked"),
      "machines": machine
    },
    beforeSend: function(){progress(30)},
    success: function(data, ts, xhr){
      if (xhr.getResponseHeader("FORM_VALIDATE") == "false") {
        $("#iface_tbl tr[role=form]").replaceWith(data)
        show_msg(xhr.getResponseHeader("FORM_MSGS"))
      }else{
        $("#iface_tbl").replaceWith(data)
      }

      if (xhr.status == 200) show_niface_btn(machine)
      toggle_nvlanc_btn(machine)

    },
    complete: function(){$("[title!=undefined]").tooltip({"animation": "true"});progress(100)},
    error: function(ob){show_msg(ob.responseText)}
  });
   drop_progress();
}
