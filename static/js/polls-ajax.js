$(document).ready(function() {
    if(window.location.hash == '#voted') {
        window.location = '/poll/' + 'results/' + $('input[name="pk"]').val();
    }
    
    $('.poll.vote form').on('submit', function() {
        var form = $(this);
        
        $.post(form.attr('action'), form.serialize(), function(data) {
            var alert = $(data).find('.alerts');
            var source = $(data).find(form.attr('data-source'));
            
            $('.alerts').html(alert);
            $('.alerts').replaceWith(alert);
            
            if(source.length > 0) {
                $('.poll').replaceWith(source);
                window.location.hash = '#voted'
            }
        });
        
        
        return false;
    });
});