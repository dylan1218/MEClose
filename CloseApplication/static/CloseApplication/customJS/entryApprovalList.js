$(document).ready(function() {
    $('#EntryApproval_ChecklistTable').DataTable();
});


function modal_display(clicked_id) {
    {
        var modal = $('#modal')
        underscore_Find = clicked_id.indexOf("_")
        crud_Type = clicked_id.substring(underscore_Find + 1, clicked_id.length)
        clicked_id = clicked_id.substring(0, underscore_Find)
        $.ajax({
            url: "/ClosePortal/entryapprovals/" + crud_Type + "/" + clicked_id,
            context: document.body
        }).done(function(response) {
            modal.html(response);
        });
    };
};