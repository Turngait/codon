export class ClinicDTO {
  id?: number;
  title: string;
  law_info?: string;
  main_site?: string;
  description: string;
  phone?: string;
}

export class AddClinicPhoneDTO {
  title: string;
  clinic_id: number;
  phone_number: string;
  is_main: boolean;
}

export class DeleteClinicDTO {
  id: number;
}

export class DeleteClinicPhoneDTO {
  id: number;
}
