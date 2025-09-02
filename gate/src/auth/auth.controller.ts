import { Controller, Post, Body, HttpCode } from '@nestjs/common';
import { AuthService } from './auth.service';
import { SignUpDto } from './signup-auth.dto';
import { SignInDTO } from './signin-auth.dto';

@Controller('auth')
export class AuthController {
  constructor(private readonly authService: AuthService) {}

  @Post('signup')
  signUp(@Body() signUpDTO: SignUpDto) {
    return this.authService.signUp(
      signUpDTO.email,
      signUpDTO.pass,
      signUpDTO.data,
      signUpDTO.settings,
    );
  }

  @Post('signin')
  @HttpCode(200)
  signIn(@Body() signInDTO: SignInDTO) {
    return this.authService.signIn(signInDTO.email, signInDTO.pass);
  }
}
