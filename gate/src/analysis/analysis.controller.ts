import {
  Controller,
  Post,
  Body,
  Headers,
  Get,
  Delete,
  Put,
} from '@nestjs/common';
import { AnalysisService } from './analysis.service';
import {
  AnalysisDTO,
  DeleteAnalysisDTO,
  AnalysisGroupDTO,
  DeleteAnalysisGroupDTO,
  AddValueDTO,
  EditValueDTO,
  DeleteAnalysisValueDTO,
} from './analysis.dto';

@Controller('analysis')
export class AnalysisController {
  constructor(private readonly analysisService: AnalysisService) {}

  @Post()
  async addAnalysis(@Body() addAnalysisDto: AnalysisDTO, @Headers() headers) {
    return await this.analysisService.addAnalysis(
      headers.user_id,
      addAnalysisDto,
    );
  }

  @Get()
  async getAnalysisForUser(@Headers() headers) {
    return await this.analysisService.getAnalysis(headers.user_id);
  }

  @Delete()
  async deleteAnalysis(
    @Headers() headers,
    @Body() deleteAnalysisDTO: DeleteAnalysisDTO,
  ) {
    return await this.analysisService.deleteAnalysis(
      headers.user_id,
      deleteAnalysisDTO.id,
    );
  }

  @Put()
  async updateAnalysis(@Headers() headers, @Body() analysis: AnalysisDTO) {
    return await this.analysisService.updateAnalysis(headers.user_id, analysis);
  }

  @Post('/group')
  async addAnalysisGroup(
    @Body() addAnalysisGroupDto: AnalysisGroupDTO,
    @Headers() headers,
  ) {
    return await this.analysisService.addGroup(
      headers.user_id,
      addAnalysisGroupDto,
    );
  }

  @Delete('/group')
  async deleteAnalysisGroup(
    @Headers() headers,
    @Body() deleteAnalysisGroupDTO: DeleteAnalysisGroupDTO,
  ) {
    return await this.analysisService.delGroup(
      headers.user_id,
      deleteAnalysisGroupDTO.id,
    );
  }

  @Put('/group')
  async updateAnalysisGroup(
    @Headers() headers,
    @Body() analysisGroup: AnalysisGroupDTO,
  ) {
    console.log(analysisGroup);
    return await this.analysisService.updateGroup(
      headers.user_id,
      analysisGroup,
    );
  }

  @Post('/value')
  async addValueToAnalysis(
    @Body() addValueReq: AddValueDTO,
    @Headers() headers,
  ) {
    return await this.analysisService.addValueToAnalysis(
      headers.user_id,
      addValueReq,
    );
  }

  @Put('/value')
  async updateValueToAnalysis(
    @Body() updateValueReq: EditValueDTO,
    @Headers() headers,
  ) {
    return await this.analysisService.updateValueToAnalysis(
      headers.user_id,
      updateValueReq,
    );
  }

  @Delete('/value')
  async deleteValue(
    @Headers() headers,
    @Body() deleteAnalysisDTO: DeleteAnalysisValueDTO,
  ) {
    return await this.analysisService.deleteAnalysisValue(
      headers.user_id,
      deleteAnalysisDTO.id,
    );
  }
}
