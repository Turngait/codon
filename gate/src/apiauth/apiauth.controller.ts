import { Controller, Post, Body } from '@nestjs/common';
import { ApiauthService } from './apiauth.service';
import { AuthTokenDTO } from './auth_token.dto';
import { ApiTokenDTO } from './api_token.dto';

@Controller('apiauth')
export class ApiauthController {
  constructor(private readonly apiAuthService: ApiauthService) {}

  @Post('/authtoken')
  generateAuthToken(@Body() authTokenDTO: AuthTokenDTO) {
    return this.apiAuthService.generateAuthToken(
      authTokenDTO.contactEmail,
      authTokenDTO.clientName,
    );
  }

  @Post('/apitoken')
  generateApiToken(@Body() apiTokenDTO: ApiTokenDTO) {
    return this.apiAuthService.generateApiToken(
      apiTokenDTO.authToken,
      apiTokenDTO.contactEmail,
    );
  }
}
