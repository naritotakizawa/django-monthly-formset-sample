from django.db import models


class Monthly(models.Model):
    year = models.IntegerField('年')
    month = models.IntegerField('月')
    comment = models.TextField('月次に関するコメント', blank=True, null=True)

    class Meta:
        # 年と月の組み合わせは一意になるように。
        unique_together = ('year', 'month')

    def __str__(self):
        return f'{self.year}年{self.month}月'


class Daily(models.Model):
    day = models.IntegerField('日')
    month = models.ForeignKey(Monthly, verbose_name='紐づく年月', on_delete=models.PROTECT)

    # 予測値など、いろいろ作ってください。
    value = models.IntegerField('値', blank=True, null=True)
