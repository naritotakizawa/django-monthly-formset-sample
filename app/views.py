import calendar
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .forms import MonthlyForm, DailyInlineFormset
from .models import Monthly, Daily


class MonthlyList(generic.ListView):
    model = Monthly
    queryset = Monthly.objects.order_by('-year', '-month')  # 新しい月次から表示する


class MonthlyAdd(generic.CreateView):
    model = Monthly
    fields = '__all__'
    success_url = reverse_lazy('app:monthly_list')

    def form_valid(self, form):
        monthly = form.save()

        # その月が何日あるか取得
        days = calendar.monthlen(monthly.year, monthly.month)

        # 日付の数だけ日のデータを作成しておく
        for day in range(1, days+1):
            Daily.objects.create(month=monthly, day=day)

        return redirect('app:monthly_update', pk=monthly.pk)


def monthly_update(request, pk):
    monthly = get_object_or_404(Monthly, pk=pk)

    form = MonthlyForm(request.POST or None, instance=monthly)
    formset = DailyInlineFormset(request.POST or None, instance=monthly)

    if request.method == 'POST' and formset.is_valid() and form.is_valid():
        form.save()
        formset.save()
        # 編集ページを再度表示
        return redirect('app:monthly_list')

    context = {
        'form': form,
        'formset': formset
    }

    return render(request, 'app/monthly_form.html', context)
