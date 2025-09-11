import { Controller, Body, Post, Put, Headers } from '@nestjs/common';
import { UserService } from './user.service';
import { UpdateUserDataDTO } from './user_info.dto';

@Controller('user')
export class UserController {
  constructor(private readonly userService: UserService) {}

  @Post()
  async getUserInfo(@Headers() headers) {
    return await this.userService.getUserInfo(
      headers.user_email,
      headers.user_id,
    );
  }

  @Put()
  async updateUserInfo(
    @Body() userInfoDTO: UpdateUserDataDTO,
    @Headers() headers,
  ) {
    return await this.userService.updateUserData(
      headers.user_email,
      userInfoDTO.data,
    );
  }
}
