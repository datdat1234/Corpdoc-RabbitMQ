import amqplib from 'amqplib';
import { protocol, username, password, hostname, vhost } from './config.js';

const amqpUrl = `${protocol}://${username}:${password}@${hostname}/${vhost}`;

const receiveQueue = async () => {
  try {
    const conn = await amqplib.connect(amqpUrl);
    const channel = await conn.createChannel();
    const nameQueue = 'q1';
    await channel.assertQueue(nameQueue, { durable: false });
    await channel.consume(
      nameQueue,
      (msg) => {
        console.log('Received', msg.content.toString());
      },
      { noAck: true }
    );
  } catch (err) {
    console.log('Error', err);
  }
};

receiveQueue();
