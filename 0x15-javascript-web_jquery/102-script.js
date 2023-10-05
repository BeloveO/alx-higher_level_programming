const $ = window.$;
window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    const lan = $('INPUT#language_code').val();
    $.getJSON('https://www.fourtonfish.com/hellosalut/hello/' + lan, function (data, textStatus) {
      $('DIV#hello').html(data.hello);
    });
  });
};
