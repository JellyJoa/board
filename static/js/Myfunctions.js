function list_func(){
    document.location.href='/sun/tip/'
}

function delete_post() {
    let result = confirm('삭제하시겠습니까?')
    if(result) {
        let queryString = "?post_id=" + $('#post_id').text()
        document.location.href = '/sun/delete/' + queryString
    }
}

function like_post() {
    let queryString = "?post_id=" + $('#post_id').text()
    document.location.href = 'sun/like/' + queryString
}