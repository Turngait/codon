import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { VersioningType } from '@nestjs/common';
import mongoose from 'mongoose';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.enableVersioning({
    type: VersioningType.URI,
  });
  await app.listen(5000).then(() => {
    mongoose
      .connect(process.env.MONGOLINK)
      .then(() => console.log('MongoDB connected'));
  });
}
bootstrap();
