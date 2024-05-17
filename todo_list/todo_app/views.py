from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .models import Todo
from .forms import TodoForm


# 할 일 목록을 보여주는 뷰
# 사용자가 웹 사이트에서 할 일 목록을 요청할 때, 이 함수가 호출되어 할 일 목록 페이지를 보여줌
# Todo 모델에서 모든 할 일 객체를 우선순위 순으로 정렬하여 가져온 후, todo_list.html 템플릿에 전달함
def todo_list(request):
    todos = Todo.objects.all().order_by('priority')  # 우선순위에 따라 할 일 목록을 정렬
    return render(request, 'todo_app/todo_list.html', {'todo_list': todos})

# 할 일을 추가하는 뷰
# 사용자가 할 일 추가 페이지에서 할 일을 추가하고자 할 때, 이 함수가 호출됨
# 사용자가 제출한 폼 데이터가 유효하다면, 폼을 저장하여 새로운 할 일을 추가하고 할 일 목록 페이지로 리다이렉트함
# GET 요청인 경우 또는 폼이 유효하지 않은 경우, 빈 폼 또는 유효하지 않은 폼을 사용자에게 다시 보여줌
def todo_add(request):
    if request.method == "POST":
        form = TodoForm(request.POST)  # POST 요청으로 받은 데이터로 폼 인스턴스 생성
        if form.is_valid():  # 폼 데이터의 유효성 검사
            form.save()  # 폼 데이터를 데이터베이스에 저장
            return redirect('todo_list')  # 할 일 목록 페이지로 리다이렉트
        else: print(form.errors)
    else:
        form = TodoForm()  # GET 요청인 경우 빈 폼 생성
    return render(request, 'todo_app/todo_add.html', {'form': form})  # 폼을 템플릿에 전달
    
# 할 일을 수정하는 뷰
# 사용자가 특정 할 일을 수정하고자 할 때, 이 함수가 호출됨
# 주어진 pk(기본 키)를 가진 Todo 객체를 데이터베이스에서 찾고, 없으면 404 에러를 반환함
# POST 요청인 경우, 제출된 폼 데이터로 Todo 객체를 업데이트하고 할 일 목록 페이지로 리다이렉트
# GET 요청 또는 폼이 유효하지 않은 경우, 기존 데이터로 채워진 폼을 사용자에게 다시 보여줌
def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
        else: print(form.errors)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo_app/todo_edit.html', {'form': form})

# 할 일을 삭제하는 뷰
# 사용자가 특정 할 일을 삭제하고자 할 때, 이 함수가 호출됨
# 주어진 pk(기본 키)를 가진 Todo 객체를 데이터베이스에서 찾고, 없으면 404 에러를 반환함
# Todo 객체를 데이터베이스에서 삭제하고 할 일 목록 페이지로 리다이렉트
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todo_list')
