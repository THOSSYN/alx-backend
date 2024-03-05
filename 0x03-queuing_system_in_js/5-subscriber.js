import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.subscribe('holberton school channel');

client.on('message', (channel, message) => {
  if (message === 'KILL_SERVER') {
    // console.log('Received KILL_SERVER command. Unsubscribing and quitting...');
    console.log('KILL_SERVER');
    client.unsubscribe('holberton school channel');
    client.quit();
  } else {
    // console.log(`Received message on channel ${channel}: ${message}`);
    console.log(message);
  }
});
