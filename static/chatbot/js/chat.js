// chatbot/static/chatbot/js/chat.js
$(document).ready(function() {
    function appendMessage(msg, sender = 'bot') {
      $('#chat-window').append(`<div><strong>${sender === 'bot' ? '🤖' : '🧑'}:</strong> ${msg}</div>`);
      $('#chat-window').scrollTop($('#chat-window')[0].scrollHeight);
    }
  
    function getNextQuestion(answer = null) {
      $.post('/get-next-question/', { answer: answer }, function(response) {
        appendMessage(response.message, 'bot');
        if (response.done) $('#user-input').prop('disabled', true);
      });
    }
  
    $('#user-input').keypress(function(e) {
      if (e.which === 13) {
        const answer = $(this).val();
        appendMessage(answer, 'user');
        $(this).val('');
        getNextQuestion(answer);
      }
    });
  
    // Initial question
    getNextQuestion();
  });
  