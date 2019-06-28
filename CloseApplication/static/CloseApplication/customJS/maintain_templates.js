$(document).ready(function() {
    //to update for relavent table ids
    $('#accountRecListTable').DataTable();

});

function modal_display(clicked_id) {
    {
        var modal = $('#modal')
            //finds the CRUD method that is appended to the HTML element's id
        underscore_Find = clicked_id.indexOf("_")
        crud_Type = clicked_id.substring(underscore_Find + 1, clicked_id.length)
        clicked_id = clicked_id.substring(0, underscore_Find)
            //finds current relative path to pass to URL string. This allows us to have one maintain_templates file instead of individual ones
        relative_URL = window.location.pathname
        relative_IndexBegin = relative_URL.indexOf("/", 1)
        relative_IndexEnd = relative_URL.indexOf("/", relative_IndexBegin + 1)
        relative_URL = relative_URL.substring(relative_IndexBegin + 1, relative_IndexEnd)


        $.ajax({
            url: "/ClosePortal/" + relative_URL + "/" + crud_Type + "/" + clicked_id,
            context: document.body
        }).done(function(response) {
            modal.html(response);
        });
    };
};