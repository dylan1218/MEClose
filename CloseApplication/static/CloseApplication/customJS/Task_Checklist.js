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