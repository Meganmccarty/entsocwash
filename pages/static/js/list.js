// Courtesy List.js
// https://listjs.com/

// Membership Gallery
var options = {
    valueNames: ['name'],
    page: 50,
    pagination: true
}

var galleryList = new List('members', options);

// Pagination buttoms
$('.next').on('click' , function(){
    $('.pagination').find('.active').next().trigger( "click" );
});

$('.previous').on('click' , function(){
     $('.pagination').find('.active').prev().trigger( "click" );
});