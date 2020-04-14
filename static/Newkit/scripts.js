//stores clicked team name
$(document).ready(function () {
    $('li').click(function () {
        var team_name = $(this).text() //take li text
        stored_var = localStorage.setItem("team_name", team_name);//store
    });
});

//retreives clicked team name
function getTextContent(x) {
    document.getElementById('page_title').innerHTML = x;
};