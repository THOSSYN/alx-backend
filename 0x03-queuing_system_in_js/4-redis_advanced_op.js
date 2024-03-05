import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.error(`Redis client error: ${err}`);
});

client.on('connect', () => {
  console.error('Redis client connected to the server');
});

client.hset('HolbertonSchools', 'Portland', 50, (err, reply) => {
  console.log(`Reply: ${reply}`);
});
client.hset('HolbertonSchools', 'Seattle', 80, (err, reply) => {
  console.log(`Reply: ${reply}`);
});
client.hset('HolbertonSchools', 'New York', 20, (err, reply) => {
  console.log(`Reply: ${reply}`);
});
client.hset('HolbertonSchools', 'Bogota', 20, (err, reply) => {
  console.log(`Reply: ${reply}`);
});
client.hset('HolbertonSchools', 'Cali', 40, (err, reply) => {
  console.log(`Reply: ${reply}`);
});
client.hset('HolbertonSchools', 'Paris', 2, (err, reply) => {
  console.log(`Reply: ${reply}`);
});

// Display the hash
client.hgetall('HolbertonSchools', (err, result) => {
  if (err) {
    console.error(`Error getting hash: ${err}`);
  } else {
    console.log('Hash:');
    console.log(result);
  }
});

// Close the connection after displaying the hash
client.quit();
