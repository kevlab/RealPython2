$(function() {
    console.log("whee!")

    // event handler
    $("#btn-click").click(function() {
        if ($('input').val() !== '') {
            var input = $("input").val()
            console.log(input)
            // add value to DOM
            $('ol').append('<li><a href="">x</a> - ' + input + '</li>');
        }
        $('input').val('');
    });

});

// remove text from DOM
$(document).on('click', 'a', function (e) {
    // cancel defult action of clicking the link
    e.preventDefault();
    // this refers to the current object, a, and we’re removing the parent element, <li>.
    $(this).parent().remove();
});
