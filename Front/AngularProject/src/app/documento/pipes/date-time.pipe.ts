import { DatePipe } from '@angular/common';
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'dateTime'
})

export class DateTimePipe implements PipeTransform {

  transform(value: string, format = 'dd/MM/yyyy HH:mm'): string {
    if (!value || value === '' || value === '0001-01-01T00:00:00') {
      return '-';
    }

    const date = new DatePipe('en-US');
    const formattedDate = date.transform(value, format);

    return formattedDate !== null ? formattedDate : '-';
  }

}
