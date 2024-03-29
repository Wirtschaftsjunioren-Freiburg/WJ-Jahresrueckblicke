
$(document).ready(function() {
    var myFullpage = new fullpage('#fullpage', {
        licenseKey: 'gplv3-license',
        navigation: true,
        anchors: anchors,
        navigationPosition: 'right',
        navigationTooltips: slides,
        showActiveTooltip: true,
        responsiveWidth: 900,
        onLeave: function(origin,destination,direction,trigger){
            if($(destination.item).hasClass('even')){
                $('#fp-nav').removeClass('odd');
                $('#fp-nav').addClass('even');
            } else {
                $('#fp-nav').removeClass('even');
                $('#fp-nav').addClass('odd');
            };
        }
    });
});

function showMore(el){
    var parent = $(el).parent().parent();
    parent.find('.long').removeClass('d-none');
    parent.find('.short').addClass('d-none');
    $(el).hide();
}