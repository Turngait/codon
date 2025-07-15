export class SignUpDto {
  email: string;
  pass: string;
  data: {
    sex: string;
    age: number;
    weight: number;
    height: number;
  };
  settings: {
    lang: string;
    theme: string;
  };
}
