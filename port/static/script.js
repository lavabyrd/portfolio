$(".nav_btn").on("click", function () {
    $('.menu').toggleClass("show");
});

function scrollWin(id) {
    document.getElementById(id).scrollIntoView(true);
}