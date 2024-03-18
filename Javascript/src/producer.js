import amqplib from 'amqplib';
import { protocol, username, password, hostname, vhost } from './config.js';

const amqpUrl = `${protocol}://${username}:${password}@${hostname}/${vhost}`;

const sendQueue = async ({ msg }) => {
  try {
    const conn = await amqplib.connect(amqpUrl);
    const channel = await conn.createChannel();
    const nameQueue = 'q1';
    await channel.assertQueue(nameQueue, { durable: false });
    await channel.sendToQueue(nameQueue, Buffer.from(msg));
  } catch (err) {
    console.log('Error', err);
  }
};

sendQueue({ msg: 'Hello World' });
