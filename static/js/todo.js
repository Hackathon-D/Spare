'use strict';
let num =0;
//各要素のエレメントを取得
const table = document.querySelector('table'); //表
const todo = document.getElementsByName('tkna'); //todo
const priority = document.getElementsByName('level'); //優先度
const deadline = document.querySelector('input[type="date"]'); //期日
const submit = document.getElementById('submit'); //登録ボタン

//todo登録ボタン
submit.addEventListener('click', () => {
    //処理。ここにDBに投げる処理を書く？
    const item = {}; //入力値を一時的に保存

    //タスク名が未入力の際に処理を停止
    if (todo.value != '') {
        item.todo = todo.value;
    } else {
        window.alert('タスク名が未入力です')
        return;
    }

    //radioボタンで選択されている値を取得
    for ( var a="", i=priority.length; i--; ) {
        if ( priority[i].checked ) {
            item.priority = priority[i].value;
            break;
        }
    }

    //カレンダーを今日の日付にする
    const formatDate = (date, sep="") => date.getFullYear() + sep + ('00' + (date.getMonth()+1)).slice(-2) + sep +('00' + date.getDate()).slice(-2);
    const dateTime = new Date();
    const date = new Date(dateTime.getFullYear(), dateTime.getMonth(), dateTime.getDate());

    if (deadline.value != '') {
        item.deadline = deadline.value;
    } else {
        const date = new Date;
        item.deadline = formatDate(date, "-");
    }

    item.done = false;
    item.delete = false;
    
    todo.value = '';
    priority.value = '';
    deadline.value = formatDate(date, "-");

    const tr = document.createElement('tr'); //tr要素を生成

    for (const prop in item) {
        const td = document.createElement('td'); //tdを生成
        if (prop == 'done'){
            const done_btn = document.createElement('button');
            //done_btnというクラスを付与
            done_btn.className = 'done_btn'
            //methodを付与
            //処理
            td.appendChild(done_btn);
        } else if (prop == 'delete') {
            const delete_btn = document.createElement('button');
            delete_btn.className = 'delete_btn'
            td.appendChild(delete_btn);
        } else {
            td.textContent = item[prop];
        }
        tr.appendChild(td); //tdをtrに追加
    }

    table.append(tr); //trをtableに追加
});