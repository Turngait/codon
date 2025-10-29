import { Controller, Post, Headers, Body, Delete } from '@nestjs/common';
import { ClinicsService } from './clinics.service';
import { ClinicDTO, DeleteClinicDTO } from './clinics.dto';

@Controller('clinics')
export class ClinicsController {
  constructor(private readonly clinicsService: ClinicsService) {}

  @Post()
  async addClinic(@Body() addClinicDto: ClinicDTO, @Headers() headers) {
    return await this.clinicsService.addClinic(headers.user_id, addClinicDto);
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
