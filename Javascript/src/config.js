import { config } from 'dotenv';
config();

const {
  AMQP_PROTOCOL,
  AMQP_USERNAME,
  AMQP_PASSWORD,
  AMQP_HOSTNAME,
  AMQP_VHOST,
} = process.env;

export const protocol = AMQP_PROTOCOL;
export const username = AMQP_USERNAME;
export const password = AMQP_PASSWORD;
export const hostname = AMQP_HOSTNAME;
export const vhost = AMQP_VHOST;
