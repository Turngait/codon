export class AnalysisDTO {
  id?: string;
  date: string;
  title: string;
  values: {
    title: string;
    volume: string;
    normal: string;
    description: string;
  }[];
  group_id: string;
  doctors: string[];
  clinic: string;
  equipment: string;
  description: string;
}

export class DeleteAnalysisDTO {
  id: string;
}

export class AnalysisGroupDTO {
  id?: string;
  title: string;
  description: string;
}

export class DeleteAnalysisGroupDTO {
  id: string;
}

export class AddValueDTO {
  analysis_id: string;
  value: {
    title: string;
    volume: string;
    normal: string;
    description: string;
  };
}

export class EditValueDTO {
  analysis_id: string;
  value: {
    id: string;
    title: string;
    volume: string;
    normal: string;
    description: string;
  };
}
