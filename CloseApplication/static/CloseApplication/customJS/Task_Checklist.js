/*
***
Removed the DataTable method for now untill we can figure out how to only allow
filtering sorting on a parent row, not the sub rows.
***

$(document).ready( function () {
    $('#Task_ChecklistTable').DataTable();
} );
*/


function collapse_Button_Click() {
    console.log(document.getElementById("collapseButton").innerHTML);
    if (document.getElementById("collapseButton").innerHTML == "[+]") {
        document.getElementById("collapseButton").innerHTML = "[-]";
    } else {
        document.getElementById("collapseButton").innerHTML = "[+]"
    };
};

function modal_display(clicked_id) {
    {
        var modal = $('#modal')
        underscore_Find = clicked_id.indexOf("_")
        crud_Type = clicked_id.substring(underscore_Find + 1, clicked_id.length)
        clicked_id = clicked_id.substring(0, underscore_Find)
        $.ajax({
            url: "/ClosePortal/tasks/" + crud_Type + "/" + clicked_id,
            context: document.body
        }).done(function(response) {
            modal.html(response);
        });
    };
};