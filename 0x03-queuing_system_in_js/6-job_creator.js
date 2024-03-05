const kue = require('kue');
const queue = kue.createQueue();
// import createQueue from 'kue';

// const queue = createQueue();

// Object containing job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'This is a notification message',
};

// Create a job and add it to the queue
const job = queue.create('push_notification_code', jobData);

// When the job is created
job.on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
});

// When the job is completed
job.on('complete', () => {
  console.log('Notification job completed');
});

// When the job fails
job.on('failed', () => {
  console.log('Notification job failed');
});

// Save the job to the queue
job.save();
