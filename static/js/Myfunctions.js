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

function create_comment(){
    $.ajax({
        async: true,
        url: '/sun/createComment/',
        type: 'GET',
        data: {
            board_id: $('#post_id').text(),
            comment_author: $('#c_name').val(),
            comment_content: $('#c_content').val()
        },
        dataType: 'json',
        timeout: 3000,
        success: function (result){
            let tr = $('<tr></tr>').attr('id', 'comment_'+result['c_id'])
            let author_td = $('<td></td>').text(result['c_author'])
            let content_td = $('<td></td>').text(result['c_content'])
            let btn_td = $('<td></td>')
            let btn = $('<button></button>').text('삭제').addClass('btn btn-outline-danger')
            btn.on('click', function (){
                $.ajax({
                    async: true,
                    url: '/sun/commentDelete/',
                    type: 'GET',
                    data:{
                        comment_id: result['c_id']
                    },
                    dataType: 'json',
                    timeout: 3000,
                    success: function (){
                        $('#comment_'+result['c_id']).remove()
                    },
                    error: function (){
                        alert('삭제 실패')
                    }
                })
            })
            btn_td.append(btn)
            tr.append(author_td)
            tr.append(content_td)
            tr.append(btn_td)
            $('tbody').prepend(tr)
        },
        error: function (){
            alert('실패')
        }
    })
}


// function create_comment(){
//     $.ajax({
//         async: true,
//         url: '/sun/createComment/',
//         type: 'GET',
//         data: {
//             board_id: $('#post_id').text(),
//             comment_author: $('#c_name').val(),
//             comment_content: $('#c_content').val()
//         },
//         dataType: 'json',
//         timeout:3000,
//         success: function (result){
//             let tr = $('<tr></tr>').attr('id', 'comment_'+result['c_id'])
//             let author_td = $('<td></td>').text(result['c_author'])
//             let content_td = $('<td></td>').text(result['c_content'])
//             let btn_td = $('<td></td>')
//             let btn = $('<button></button>').text('삭제').addClass('btn btn-outline-danger')
//             btn.on('click', function (){
//                 $.ajax({
//                     async: true,
//                     url: '/sun/commentDelete/',
//                     type: 'GET',
//                     data: {
//                         comment_id: result['c_id']
//                     },
//                     dataType: 'json',
//                     timeout: 3000,
//                     success: function (){
//                         $('#comment_'+result['c_id']).remove()
//                     },
//                     error: function (){
//                         alert('Error1')
//                     }
//                 })
//             })
//             btn_td.append(btn)
//             tr.append(author_td)
//             tr.append(content_td)
//             tr.append(btn_td)
//             $('tbody').prepend(tr)
//         },
//         error: function (){
//             alert('Error2')
//         }
//     })
// }


function animal_list() {
    let my_date = $('#searchDate').val()

    if (my_date == ""){
        alert('검색을 위해 날짜를 선택해 주세요!')
    }

    else{

        let modified_date = my_date.replace(/-/g, '')

        $.ajax({
            async : true,
            url: 'http://openapi.animal.go.kr:80/openapi/service/rest/abandonmentPublicSrvc?_wadl&type=json',
            data : {
                serviceKey : 'NVk7m8SbanZW%2BtI9xjXbAL5fJqD56%2F3dzja%2FWCrt7VbEhAMec8CZLx91G%2FsZSLFEB6J6wqg8j252hdJ%2F76RJYA%3D%3D',
                bgnde : modified_date
            },
            method : 'GET',
            timeout : 3000,
            dataType : 'json',
            success : function(result) {
                $('tbody').empty()

                // <th scope="col">Rank</th>
                // <th scope="col">포스터 이미지</th>
                // <th scope="col">영화제목</th>
                // <th scope="col">개봉일</th>
                // <th scope="col">상세보기</th>

                for(i=0;i<10;i++) {
                    let tr = $('<tr></tr>')
                    let rankTd = $('<td></td>').text(result['boxOfficeResult']['dailyBoxOfficeList'][i]['rank'])
                    let imgTd = $('<td></td>>')
                    let searchTitle = result['boxOfficeResult']['dailyBoxOfficeList'][i]['movieNm'] + " 포스터 사진"
                    let img = $('<img />')
                    let imgUrl = result['']
                    img.attr('src', imgUrl)
                    imgTd.append(img)

                    let titleTd = $('<td></td>').text(result['boxOfficeResult']['dailyBoxOfficeList'][i]['movieNm'])
                    let openTd = $('<td></td>').text(result['boxOfficeResult']['dailyBoxOfficeList'][i]['openDt'])
                    let detailTd = $('<td></td>')
                    let detailBtn = $('<input/>').attr('type','button').attr('value','상세보기')

                    detailBtn.addClass('btn btn-warning')
                    detailBtn.on('click',function(){
                        alert('상세보기 버튼 눌림')
                    })

                    detailTd.append(detailBtn)
                    tr.append(rankTd)
                    tr.append(imgTd)
                    tr.append(titleTd)
                    tr.append(openTd)
                    tr.append(detailBtn)
                    $('tbody').append(tr)
                }

            },
            error : function (){
                alert('먼가 이상해요!')
            }

        });
    }
}