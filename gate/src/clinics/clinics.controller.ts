import { Controller, Post, Headers, Body, Delete } from '@nestjs/common';
import { ClinicsService } from './clinics.service';
import {
  ClinicDTO,
  DeleteClinicDTO,
  AddClinicPhoneDTO,
  DeleteClinicPhoneDTO,
  AddClinicAddressDTO,
} from './clinics.dto';

@Controller('clinics')
export class ClinicsController {
  constructor(private readonly clinicsService: ClinicsService) {}

  @Post()
  async addClinic(@Body() addClinicDto: ClinicDTO, @Headers() headers) {
    return await this.clinicsService.addClinic(headers.user_id, addClinicDto);
  }

  @Post('/phone')
  async addClinicPhone(
    @Body() addClinicPhoneDto: AddClinicPhoneDTO,
    @Headers() headers,
  ) {
    return await this.clinicsService.addClinicPhone(
      headers.user_id,
      addClinicPhoneDto,
    );
  }

  @Post('/address')
  async addClinicAddress(
    @Body() addClinicAddressDto: AddClinicAddressDTO,
    @Headers() headers,
  ) {
    return await this.clinicsService.addClinicAddress(
      headers.user_id,
      addClinicAddressDto,
    );
  }

  @Delete('/phone')
  async deleteClinicPhone(
    @Body() delClinicPhoneDto: DeleteClinicPhoneDTO,
    @Headers() headers,
  ) {
    return await this.clinicsService.deleteClinicPhone(
      headers.user_id,
      delClinicPhoneDto.id,
    );
  }

  @Delete()
  async DeleteClinicDTO(
    @Body() deleteClinicDTO: DeleteClinicDTO,
    @Headers() headers,
  ) {
    return await this.clinicsService.deleteClinic(
      headers.user_id,
      deleteClinicDTO.id,
    );
  }
}
