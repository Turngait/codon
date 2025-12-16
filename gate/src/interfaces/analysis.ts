export interface IAnalysis {
  id?: number;
  date: string;
  title: string;
  group_id: string;
  doctors: string[];
  clinic_id: string;
  equipment: string;
  description: string;
}

export interface IValues {
  id?: number;
  title: string;
  volume: string;
  normal: string;
  description: string;
}
