//textareaを定義
const chatarea_templete = document.getElementById('message');

//ボタンの定義
const buttons_templete = document.querySelectorAll('#templete1');

//ボタンのvalueを取得
buttons_templete.forEach(button => {
    button.addEventListener('click', () => {
        const value = button.value;
        chatarea_templete.value = value;
        modal_templete.style.display = 'none';
    });
});

//modalの表示
const modal_templete = document.getElementById('demo-modal-templete');
const btn_templete = document.getElementById('open-modal-templete');
const close_templete = document.getElementsByClassName('close-templete')[0];

//clickするとmodalを開く処理
btn_templete.onclick = function() {
    modal_templete.style.display = 'block';
};

//Xで閉じる処理
close_templete.onclick = function() {
    modal_templete.style.display = 'none';
};

