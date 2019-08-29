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


function format() {
    // `d` is the original data object for the row
    return '<table cellpadding="5" cellspacing="0" border="0" style="padding-left:50px;">' +
        '<tr>' +
        '<td>Full name:</td>' +
        '<td>' + "TEST VAL" + '</td>' +
        '</tr>' +
        '<tr>' +
        '<td>Extension number:</td>' +
        '<td>' + "TEST VAL" + '</td>' +
        '</tr>' +
        '<tr>' +
        '<td>Extra info:</td>' +
        '<td>And any further details here (images etc)...</td>' +
        '</tr>' +
        '</table>';
}

$(document).ready(function() {
    $('#TaskChecklistTable').DataTable({
        "columns": [{
            "className": 'details-control',
            "orderable": false,
            "data": null,
            "defaultContent": ''
        }]
    });
    console.log("doc loaded")
    $('#TaskChecklistTable tbody tr').on('click', '.details-control', function() {
        var table = $('#Task_ChecklistTable').DataTable();
        console.log("clicked")
        var tr = $(this).closest('tr');
        console.log(tr)
        console.log(tr[0].getAttribute('id'));
        var row = table.row(tr);

        if (row.child.isShown()) {
            // This row is already open - close it
            row.child.hide();
            tr.removeClass('shown');
        } else {
            // Open this row
            console.log(row.child())
            row.child(format()).show();
            tr.addClass('shown');
        }
    });
});