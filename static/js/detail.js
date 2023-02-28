// Enterキーが押された場合にsubmitを実行する（Shift + Enterは除外する）
document.addEventListener('keydown', function(event) {
    if (event.keyCode === 13 && !event.shiftKey) {
      event.preventDefault(); // デフォルトのEnterキーの動作をキャンセルする
      document.getElementById('add-message-btn').click(); // ボタンをクリックする
    }
  });