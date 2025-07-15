import { Module } from '@nestjs/common';
import { ApiauthController } from './apiauth.controller';
import { ApiauthService } from './apiauth.service';

@Module({
  controllers: [ApiauthController],
  providers: [ApiauthService],
})
export class ApiauthModule {}
