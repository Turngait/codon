import { createHash } from 'crypto';

const SALT = process.env.SALT || '';
const SALT2 = process.env.SALT2 || '';

export function createPassword(pass: string, paper: string): string {
  console.log(pass, paper)

  const newPass = createHash('sha256').update(pass).digest('hex');
  return paper + newPass + SALT;
}

export function createPaper(): string {
  return createHash('sha256').update(String(Date.now())).digest('hex');
}

export function createToken(): string {
  return createHash('sha256').update(String(Date.now())).digest('hex');
}

export function createHashForRecovery(email: string): string {
  return createHash('sha256')
    .update(email + SALT2)
    .digest('hex');
}
