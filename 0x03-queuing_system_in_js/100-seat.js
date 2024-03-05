const express = require('express');
const redis = require('redis');
const kue = require('kue');
const { promisify } = require('util');

// Create Redis client
const client = redis.createClient();

// Create Kue queue
const queue = kue.createQueue();

// Create express app
const app = express();
const port = 1245;

// Promisify Redis functions
const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

// Function to reserve seats
async function reserveSeat(number) {
  const stringNum = number.toString();
  await setAsync('available_seats', stringNum);
}

// Function to get current available seats
async function getCurrentAvailableSeats() {
  const availSeat = await getAsync('available_seats');
  return availSeat ? parseInt(availSeat) : 0;
}

// Initialize available seats to 50
reserveSeat(50);

// Initialize reservationEnabled to true
let reservationEnabled = true;

// Route to get available seats
app.get('/available_seats', async (req, res) => {
  const availableNumber = await getCurrentAvailableSeats();
  res.status(200).json({ numberOfAvailableSeats: availableNumber });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ "status": "Reservation are blocked" });
  }

  const job = queue.create('reserve_seat');

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err.message}`);
  });

  job.save();
  res.json({ "status": "Reservation in process" });
});

app.get('/process', async (req, res) => {
  res.json({ "status": "Queue processing" });

  queue.process('reserve_seat', async (job, done) => {
    const numOfSeats = await getCurrentAvailableSeats();
    if (numOfSeats === 0) {
      reservationEnabled = false;
      done(new Error('Not enough seats available'));
    } else if (numOfSeats >= 0) {
      reserveSeat(numOfSeats - 1);
      done();
    } else {
      done(new Error('Not enough seats available'));
    }
  });
});

// Start server
app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});
