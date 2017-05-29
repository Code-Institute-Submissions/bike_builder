/*code taken from https://stackoverflow.com/questions/11533542/twitter-bootstrap-add-active-class-to-li/12950620#12950620*/
$(function(){
    function removeEndSlash(str) {
        if(str.substr(-1) == '/') {
            return str.substr(0, str.length - 1);
        }
        return str;
    }

    var url = window.location.pathname;
    var activePage = removeEndSlash(url);

    $('.nav li a').each(function(){
        var currentPage = removeEndSlash($(this).attr('href'));

        if (activePage == currentPage) {
            $(this).parent().addClass('active');
        }
    });
});
