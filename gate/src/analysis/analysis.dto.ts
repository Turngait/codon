export class AnalysisDTO {
  id?: number;
  date: string;
  title: string;
  values: {
    title: string;
    volume: string;
    normal: string;
    description: string;
  }[];
  group_id: number;
  doctors: string;
  clinic: string;
  equipment: string;
  description: string;
}

export class DeleteAnalysisDTO {
  id: number;
}

export class DeleteAnalysisValueDTO {
  id: number;
}

export class AnalysisGroupDTO {
  id?: number;
  title: string;
  description: string;
}

export class DeleteAnalysisGroupDTO {
  id: number;
}

export class AddValueDTO {
  analysis_id: number;
  values: [
    {
      title: string;
      volume: string;
      normal: string;
      description: string;
    },
  ];
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
