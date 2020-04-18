//stores clicked team name
$(document).ready(function () {
    $('li').click(function () {
        var team_name = $(this).text() //take li text
        stored_var = localStorage.setItem("team_name", team_name);//store
    });
});

//retreives clicked team name
function getTextContent(x) {
    var sup = "Supporting";
    document.getElementById('page_title').innerHTML = sup + x;
};

$(document).ready(function () {
    $(function () {
        $('#id_team__icontains').attr("placeholder", "Search Team");
      
       $('#id_league__icontains').hide();
       $('[for=id_league__icontains]').hide();
       $('[for=id_team__icontains]').hide();
        

        var open = false;
        $('#menuSlideButton').click(function () {
            if (open === false) {
                $('#menuSlideContent').animate({ height: '300px' });
                $(this).css('backgroundPosition', 'bottom left');
                open = true;
            } else {
                $('#menuSlideContent').animate({ height: '0px' });
                $(this).css('backgroundPosition', 'top left');
                open = false;
            }
        });
    });
});

/* button logic */
$(document).ready(function() {
         $('#submit').hide();

    });

    function showerz() {
            $('#submit_value').click(function () {
               $('#submit_value').hide();
               $('#submit').show(); 
            });
       };

