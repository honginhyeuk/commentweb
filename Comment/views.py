from django.http import JsonResponse,HttpResponseRedirect,Http404
from django.http import HttpResponse,HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import logging
logger = logging.getLogger(__name__)
from .models import Comment
from datetime import datetime
import json

@csrf_exempt  # CSRF 보안 예외
def comment_list(request):
    if request.method == "GET":  # 댓글 목록 조회
        comments = Comment.objects.all().order_by("-created_at")  # 최신순 정렬
        comment_list = [{"name": c.name, "content": c.content, "created_at": c.created_at} for c in comments]
        htmlfile = render(request,"comment_form.html" ,{"comments":comments})

        return htmlfile
       # return render(request,"comment_form.html" ,{"댓글":comment_list})
      #  if len(comment_list) > 0: 
       #     return JsonResponse( comment_list, safe=False)  # 목록 반환

    elif request.method == "POST":  # 새로운 댓글 작성
        try:
            data = json.loads(request.body)  # 요청 데이터 추출
            name = data.get("name")
            password = data.get("password")
            content = data.get("content")

            if not (name and password and content):
                return JsonResponse({"error": "필수 입력 사항을 모두 작성해주세요."}, status=400)
            
            Comment.objects.create(name=name, password=password, content=content)  # 댓글 저장
            return JsonResponse({"message": "댓글이 성공적으로 작성되었습니다."})
        except json.JSONDecodeError:
            name = request.POST.get("name")
            password = request.POST.get("password")
            content = request.POST.get("content")    
            Comment.objects.create(name=name, password=password, content=content)  # 댓글 저장


            return HttpResponseRedirect("/comments/")
           # return JsonResponse({"error": "유효하지 않은 JSON 데이터입니다."}, status=400)


def comment_edit(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)  # 수정할 댓글 가져오기
    
    if request.method == "POST":
        # 폼 데이터에서 비밀번호 가져오기
        password = request.POST.get("password")
        
        # 비밀번호가 일치하는지 확인
        if comment.password == password:
            # 폼에서 수정할 값 추출
            new_name = request.POST.get("name", comment.name)
            new_content = request.POST.get("content", comment.content)
            
            # 수정 사항 적용
            comment.name = new_name
            comment.content = new_content
            comment.save()  # 수정사항 저장
            
            return HttpResponseRedirect("/comments/")  # 목록으로 리다이렉트
        else:
            return JsonResponse({"error": "비밀번호가 일치하지 않습니다."}, status=403)
    
    return render(request, "comment_edit_form.html", {"comment": comment})  # 수정 폼

@csrf_exempt
def validate_password(request, comment_id):
    if request.method == "POST":
        data = json.loads(request.body)
        password = data.get("password")
        comment = get_object_or_404(Comment, id=comment_id)
        if comment.password == password:  # 비밀번호 확인
            return JsonResponse({"message": "비밀번호가 일치."}, status=200)
        else:
            return JsonResponse({"error": "비밀번호가 일치하지 않습니다."}, status=403)

def comment_detail(request, comment_id):  
    comment = get_object_or_404(Comment, id=comment_id)
    comment_data = {
        "name": comment.name,
        "content": comment.content,
    }
    return JsonResponse(comment_data)
def get_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)  # comment_id로 댓글 검색
    comment_data = {
        'name': comment.name,
        'content': comment.content,
        'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M')  # 날짜 형식 변환
    }
    return JsonResponse(comment_data)

def edit_comment(request, comment_id):
    try:
        logger.info("Comment ID: %s", comment_id)
        #
        if request.method == "POST":
            # 폼에서 전달된 데이터
            name = request.POST.get("name")
            content = request.POST.get("content")
            password = request.POST.get("password")
            id = comment_id
            try:
                comment = get_object_or_404(Comment,id=comment_id)
            except Http404:
                raise         
            comment.name = name
            comment.content = content
            comment.password = password
            comment.created_at = datetime.now()
            comment.save(update_fields=["name", "content", "password","created_at"])
            

            return JsonResponse({"status": "200", "refresh": True}, status=200)
        else:
                return JsonResponse({"error": "올바르지 않은 요청입니다."}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500) 
        return HttpResponse({})