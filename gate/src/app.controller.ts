import { Controller, Get, Post, Headers } from '@nestjs/common';
import { AppService } from './app.service';

@Controller({
  version: '1',
})
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  getHello(): string {
    return this.appService.getHello();
  }

  @Post()
  getAllInfoForUser(@Headers() headers) {
    return this.appService.getAllInfoForUser(headers.user_id);
  }
}
