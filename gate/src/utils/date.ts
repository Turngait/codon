import * as moment from 'moment';

export function getToday() {
  return moment().format('YYYY-MM-DD');
}

export function getTodayPlus30Days() {
  moment().add(60, 'day').format('YYYY-MM-DD');
}
