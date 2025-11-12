from django import forms
from django.db.models import Sum
from datetime import date as date_cls, time as time_cls

from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'time', 'number_of_people']
        labels = {
            'date': 'Дата экскурсии',
            'time': 'Время экскурсии',
            'number_of_people': 'Количество человек',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control',
                'min': '10:00',
                'max': '22:00',
                'step': '7200',  
            }),
            'number_of_people': forms.NumberInput(attrs={
                'min': 1,
                'max': 20,
                'class': 'form-control',
                'placeholder': 'Введите количество участников',
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        excursion_date = cleaned_data.get('date')
        excursion_time = cleaned_data.get('time')
        people_count = cleaned_data.get('number_of_people')

        errors = {}

        
        if excursion_date and excursion_date < date_cls.today():
            errors['date'] = 'Нельзя выбрать прошедшую дату экскурсии.'

        
        if excursion_time:
            start = time_cls(10, 0)
            end = time_cls(22, 0)

            
            if excursion_time < start or excursion_time > end:
                errors['time'] = 'Экскурсии доступны только с 10:00 до 22:00.'
            else:
                
                if excursion_time.minute != 0 or ((excursion_time.hour - 10) % 2 != 0):
                    errors['time'] = (
                        'Экскурсии начинаются каждые 2 часа: '
                        '10:00, 12:00, 14:00, 16:00, 18:00, 20:00, 22:00.'
                    )

        
        if excursion_date and excursion_time and people_count:
            already = (
                Booking.objects
                .filter(date=excursion_date, time=excursion_time)
                .aggregate(total=Sum('number_of_people'))['total'] or 0
            )

            if already + people_count > 20:
                remaining = max(0, 20 - already)

                
                next_slot_time = None
                next_hour = excursion_time.hour + 2
                if next_hour <= 22:
                    next_slot_time = time_cls(next_hour, 0)

                if remaining > 0:
                    
                    msg = (
                        f'На это время осталось только {remaining} мест(а). '
                        
                    )
                else:
                    
                    msg = (
                        'На это время все 20 мест уже заняты.'
                    )

                if next_slot_time:
                    msg += f' Следующий доступный слот — {next_slot_time.strftime("%H:%M")}.'
                else:
                    msg += ' Попробуйте выбрать другое время или дату.'

                errors['number_of_people'] = msg

        if errors:
            
            raise forms.ValidationError(errors)

        return cleaned_data


