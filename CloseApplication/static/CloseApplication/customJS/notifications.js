window.onload = function() {

    getSuccessOutput()

};

function binaryReadStatus(notifyPK) {
    var returnIndexOfDash;
    var notifyPK_Parse;
    returnIndexOfDash = notifyPK.indexOf("-")
    notifyPK_Parse = notifyPK.substr(returnIndexOfDash + 1, notifyPK.length);
    var readChangeData = {
        pk: notifyPK_Parse,
        unread: 'False'
    }
    var request = $.ajax({
        url: 'http://' + window.location.host + '/api/notifications/' + notifyPK_Parse + '/',
        type: "PATCH",
        data: JSON.stringify(readChangeData),
        dataType: "json",
        headers: {
            'Content-Type': 'application/json'
        }
    });
    request.done(function(msg) {
        console.log(msg);
    });

    request.fail(function(jqXHR, textStatus) {
        alert("Request failed: " + textStatus);
    });
}

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
            unreadCount = response.responseJSON.unread_list.length
            for (counter = 0; counter < unreadList.length; counter++) {
                htmlAppend += '<li onclick="binaryReadStatus(this.id)" class="list-group-item" id="notifyPK-' + unreadList[counter].id + '">' + unreadList[counter].verb + '</li>'
            }
            $('#notifications_container').html(htmlAppend);
            $('#span_notifications_counter').first().html(unreadCount);
            $('#strong_notifications_counter').first().html('You have ' + unreadCount + ' notifications');
            console.log(htmlAppend);
        },
        error: function() {
            $('#output').html('Bummer: there was an error!');
        },
    });

    setTimeout(getSuccessOutput, 5000);
}