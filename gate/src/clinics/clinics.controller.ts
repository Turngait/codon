import { Controller, Post, Headers, Body, Delete, Put } from '@nestjs/common';
import { ClinicsService } from './clinics.service';
import {
  ClinicDTO,
  DeleteClinicDTO,
  AddClinicPhoneDTO,
  DeleteClinicPhoneDTO,
  AddClinicAddressDTO,
  DeleteClinicAddressDTO,
  UpdateClinicDTO,
  UpdateClinicAddressDTO,
  UpdateClinicPhoneDTO,
} from './clinics.dto';

@Controller('clinics')
export class ClinicsController {
  constructor(private readonly clinicsService: ClinicsService) {}

  @Post()
  async addClinic(@Body() addClinicDto: ClinicDTO, @Headers() headers) {
    return await this.clinicsService.addClinic(headers.user_id, addClinicDto);
  }

  @Put()
  async UpdateClinic(
    @Body() updateClinicDTO: UpdateClinicDTO,
    @Headers() headers,
  ) {
    return await this.clinicsService.updateClinic(
      headers.user_id,
      updateClinicDTO,
    );
  }

  @Delete()
  async DeleteClinic(
    @Body() deleteClinicDTO: DeleteClinicDTO,
    @Headers() headers,
  ) {
    return await this.clinicsService.deleteClinic(
      headers.user_id,
      deleteClinicDTO.id,
    );
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

  @Put('/phone')
  async updateClinicPhone(
    @Body() updateClinicPhone: UpdateClinicPhoneDTO,
    @Headers() headers,
  ) {
    return await this.clinicsService.updateClinicPhone(
      headers.user_id,
      updateClinicPhone,
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

  @Put('/address')
  async updateClinicAddress(
    @Body() updateClinicAddress: UpdateClinicAddressDTO,
    @Headers() headers,
  ) {
    return await this.clinicsService.updateClinicAddress(
      headers.user_id,
      updateClinicAddress,
    );
  }

  @Delete('/address')
  async deleteClinicAddress(
    @Body() delClinicAddressDto: DeleteClinicAddressDTO,
    @Headers() headers,
  ) {
    return await this.clinicsService.deleteClinicAddress(
      headers.user_id,
      delClinicAddressDto.id,
    );
  }
}
