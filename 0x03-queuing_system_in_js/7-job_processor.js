const kue = require('kue');
const queue = kue.createQueue();

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notification
function sendNotification(phoneNumber, message, job, done) {
  // Track progress
  job.progress(0, 100);

  // If phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    // Fail the job
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Track progress
  job.progress(50, 100);

  // Log notification
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Complete the job
  done();
}

// Create queue to process jobs
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;

  // Call sendNotification function
  sendNotification(phoneNumber, message, job, done);
});
