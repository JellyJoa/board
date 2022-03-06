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

function animal_list() {
    let my_date = $('#searchDate').val()

    if (my_date == ""){
        alert('검색을 위해 날짜를 선택해 주세요!')
    }

    else{

        let modified_date = my_date.replace(/-/g, '')

        $.ajax({
            async : true,
            url: 'http://openapi.animal.go.kr:80/openapi/service/rest/abandonmentPublicSrvc?_wadl&type=xml',
            data : {
                key : '5b015a49a0f1ae63cd63b5a1ba139a86',
                targetDt : modified_date
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
                    imgTd.append(img)
                    $.ajax({
                        async: true,
                        url: 'https://dapi.kakao.com/v2/search/image',
                        method: 'GET',
                        headers: {
                            Authorization: "KakaoAK " + 'cf0517506a09c39e970bb3cef7b670f9'
                        },
                        data: {
                            query: searchTitle
                        },
                        timeout: 4000,
                        dataType: 'json',
                        success: function(result) {
                            $('#myDiv').empty()
                            let imgUrl = result['documents'][0]['thumbnail_url']
                            img.attr('src',imgUrl)
                        },
                        error: function() {
                            alert('먼가 이상해요!')
                        }
                    })
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