export class ClinicDTO {
  id?: number;
  title: string;
  law_info?: string;
  main_site?: string;
  description: string;
  phone?: string;
}

export class UpdateClinicDTO {
  id: number;
  title: string;
  law_info: string;
  main_site: string;
  description: string;
}

export class DeleteClinicDTO {
  id: number;
}

export class AddClinicPhoneDTO {
  title: string;
  clinic_id: number;
  phone_number: string;
  is_main: boolean;
}

export class UpdateClinicPhoneDTO {
  id: number;
  title: string;
  phone_number: string;
  is_main: boolean;
  clinic_id: number;
}

export class DeleteClinicPhoneDTO {
  id: number;
}

export class AddClinicAddressDTO {
  title: string;
  clinic_id: number;
  address: string;
  is_main: boolean;
}

export class UpdateClinicAddressDTO {
  id: number;
  title: string;
  address: string;
  is_main: boolean;
  clinic_id: number;
}

export class DeleteClinicAddressDTO {
  id: number;
}
