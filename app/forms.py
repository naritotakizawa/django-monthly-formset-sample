from django import forms
from .models import Monthly, Daily


DailyInlineFormset = forms.inlineformset_factory(
    Monthly, Daily, exclude=['day'],  # 日にちは編集できないようにする
    extra=0, can_delete=False
)

# 一般的にはclass MonthlyForm のように作りますが、ちょっとしたものなら関数で作ることもできます。
MonthlyForm = forms.modelform_factory(Monthly, fields=['comment'])
