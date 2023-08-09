import { MessageService } from 'primeng/api';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ToastService {

  constructor(private messageService: MessageService) { }

  showSuccess(summary: string, detail: string) {
    this.messageService.add({ severity: 'success', summary: summary, detail: detail });
  }

  showInfo(summary: string, detail: string) {
    this.messageService.add({ severity: 'info', summary: summary, detail: detail });
  }

  showWarn(summary: string, detail: string) {
    this.messageService.add({ severity: 'warn', summary: summary, detail: detail });
  }

  showError(summary: string, detail: string) {
    this.messageService.add({ severity: 'error', summary: summary, detail: detail });
  }
}
