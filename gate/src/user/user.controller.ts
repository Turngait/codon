import { Controller, Body, Post, Put, Headers } from '@nestjs/common';
import { UserService } from './user.service';
import { UpdateUserDataDTO } from './user_info.dto';

@Controller('user')
export class UserController {
  constructor(private readonly userService: UserService) {}

  @Post()
  async getUserInfo(@Headers() headers) {
    return await this.userService.getUserInfo(headers.user_id);
  }

  @Put()
  async updateUserInfo(
    @Body() userInfoDTO: UpdateUserDataDTO,
    @Headers() headers,
  ) {
    return await this.userService.updateUserData(
      headers.user_id,
      userInfoDTO.biological_gender,
      userInfoDTO.data_birth,
      userInfoDTO.weight,
      userInfoDTO.height,
    );
  }

  @Put()
  async changeUserTimeZone(@Body() userTimeZone: string, @Headers() headers) {
    return await this.userService.changeTimeZone(headers.user_id, userTimeZone);
  }
}
