$(document).ready(function () {
  AWS.config.region = "us-east-1";
  AWS.config.credentials = new AWS.CognitoIdentityCredentials({
    IdentityPoolId: "us-east-1:f2f2e6d8-7cca-4b48-81f9-27e7a0ee65e9",
  });

  const lexruntimev2 = new AWS.LexRuntimeV2();
  const $messages = $(".messages-content");

  const botId = "5M9JOUG1ZG";
  const botAliasId = "7GZRAMSNT2";
  const localeId = "en_US";
  const sessionId = "User-" + Date.now();

  // Initial greeting
  $(window).on("load", function () {
    $messages.mCustomScrollbar();
    insertResponseMessage("👋 Welcome to CareConnect!", false);
  });

  function updateScrollbar() {
    $messages
      .mCustomScrollbar("update")
      .mCustomScrollbar("scrollTo", "bottom", { scrollInertia: 10, timeout: 0 });
  }

  function sendMessage() {
    const msg = $(".message-input").val().trim();
    if (msg === "") return false;

    $('<div class="message message-personal">' + msg + "</div>")
      .appendTo($(".mCSB_container"))
      .addClass("new");

    $(".message-input").val(null);
    updateScrollbar();

    const params = {
      botId,
      botAliasId,
      localeId,
      sessionId,
      text: msg,
    };

    lexruntimev2.recognizeText(params, function (err, data) {
      if (err) {
        console.error("Error:", err);
        insertResponseMessage("Oops, something went wrong. Please try again.");
      } else if (data && data.messages && data.messages.length > 0) {
        const responseText = data.messages.map((m) => m.content).join("\n");
        insertResponseMessage(responseText);
      } else {
        insertResponseMessage("Sorry, I didn’t quite get that.");
      }
    });
  }

  $(".message-submit").click(function () {
    sendMessage();
  });

  $(window).on("keydown", function (e) {
    if (e.which === 13) {
      sendMessage();
      return false;
    }
  });

    function insertResponseMessage(content) {
    const loadingDiv = $('<div class="message loading new"><span>Typing...</span></div>');
    loadingDiv.appendTo($(".mCSB_container"));
    updateScrollbar();

    setTimeout(function () {
      loadingDiv.remove();
      const botMsgDiv = $('<div class="message new">' + content + "</div>");
      if (content.length <= 5) {
        botMsgDiv.addClass("short"); // Add short class for tiny bot messages
      }
      botMsgDiv.appendTo($(".mCSB_container")).addClass("new");
      updateScrollbar();
    }, 500);
  }
});