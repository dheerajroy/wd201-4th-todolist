from django.shortcuts import redirect, render


class Views:
    def __init__(self):
        self._tasks, self._completed_tasks = [], []

    def all_tasks(self, request):
        return render(request, 'index.html', {'tasks': self._tasks, 'completed_tasks': self._completed_tasks})

    def tasks(self, request):
        return render(request, "tasks.html", {"tasks": self._tasks})

    def completed_tasks(self, request):
        return render(request, "completed_tasks.html", {"completed_tasks": self._completed_tasks})

    def add_task(self, request):
        task = request.GET.get("task")
        if task:
            self._tasks.append(task)
        return redirect("/all_tasks")

    def delete_task(self, request, index):
        if index:
            del self._tasks[index - 1]
        return redirect("/all_tasks")

    def complete_task(self, request, index):
        if index:
            self._completed_tasks.append(self._tasks.pop(index - 1))
        return redirect("/all_tasks")

    def delete_completed_task(self, request, index):
        if index:
            del self._completed_tasks[index - 1]
        return redirect("/all_tasks")