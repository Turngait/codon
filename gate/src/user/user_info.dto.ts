export class UpdateUserDataDTO {
  user_token: string;
  data: {
    sex: string;
    age: number;
    weight: number;
    height: number;
  };
}
