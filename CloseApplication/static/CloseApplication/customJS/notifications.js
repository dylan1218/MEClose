window.onload = function() {

    getSuccessOutput()

};

function getSuccessOutput() {
    $.ajax({
        url: 'http://' + window.location.host + '/inbox/notifications/api/unread_list/',
        complete: function(response) {
            console.log(response);
            console.log(response.responseJSON.unread_list);
            var counter;
            var unreadList;
            var htmlAppend = '';
            unreadList = response.responseJSON.unread_list
            for (counter = 0; counter < unreadList.length; counter++) {
                htmlAppend += '<li class="list-group-item">' + unreadList[counter].verb + '</li>'
            }
            $('#notifications_container').html(htmlAppend);
            console.log(htmlAppend);
        },
        error: function() {
            $('#output').html('Bummer: there was an error!');
        },
    });
    return false;
}