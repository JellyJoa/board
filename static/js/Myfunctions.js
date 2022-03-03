function list_func(){
    document.location.href='/sun/tip/'
}

function delete_post(id) {
    let result = confirm('삭제하시겠습니까?')
    if(result) {
        document.location.href = '/sun/'+id+'/delete/'
    }
}

function like_post(id) {
    document.location.href = '/sun/'+id+'/like/'
}