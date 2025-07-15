import { MiddlewareConsumer, Module, NestModule } from '@nestjs/common';

import { AppController } from './app.controller';
import { AppService } from './app.service';
import { AuthModule } from './auth/auth.module';
import { ApiauthModule } from './apiauth/apiauth.module';
import { CheckTokenMiddleware } from './middlewares/checkToken.middleware';
import { UserModule } from './user/user.module';
import { AnalysisModule } from './analysis/analysis.module';
import { CheckUserTokenMiddleware } from './middlewares/checkUserToken.middleware';

@Module({
  imports: [AuthModule, ApiauthModule, UserModule, AnalysisModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule implements NestModule {
  configure(consumer: MiddlewareConsumer) {
    consumer.apply(CheckTokenMiddleware).forRoutes('auth', 'user', 'analysis');
    consumer.apply(CheckUserTokenMiddleware).forRoutes('analysis', 'user');
  }
}
