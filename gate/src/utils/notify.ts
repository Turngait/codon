import fetch from 'node-fetch';

import URI from '../config/uri';
import { NotifyTypes } from '../interfaces/common';

interface INotifyData {
  to: string;
  name: string;
  pass?: string;
  msg?: string;
  type: NotifyTypes;
}

export async function sendNotificationByMail(
  data: INotifyData,
): Promise<{ status: number; msg: string }> {
  try {
    await fetch(URI.NOTIFY_URL + 'mail/send', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    }).then((res) => res.json());

    return { status: 200, msg: '' };
  } catch (error) {
    console.log(error);
    return { status: 500, msg: error };
  }
}
