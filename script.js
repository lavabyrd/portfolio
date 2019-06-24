$(".nav_btn").on("click", function () {
    $('.menu').toggleClass("show");
});


function scrollWin(id) {
    // document.location.hash = "#main-body";
    document.getElementById(id).scrollIntoView(true);
}