function BannerImgShift() {
    var img1 = document.getElementById("fig-1");
    var img2 = document.getElementById("fig-2");
    var img3 = document.getElementById("fig-3");
    img1.id = "fig-3";
    img2.id = "fig-1";
    img3.id = "fig-2";
}

setInterval(BannerImgShift , 7000);
