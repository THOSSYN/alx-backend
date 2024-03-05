import { createPushNotificationsJobs } from './8-job.js';
const kue = require('kue');
const expect = require('chai').expect;

describe('createPushNotificationsJobs', function() {
  let queue;

  before(function() {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  after(function() {
    queue.testMode.exit();
  });

  afterEach(function() {
    queue.testMode.clear();
  });

  it('Logs information about created job', function() {
    const jobs = [
      {
        phoneNumber: '4151234567',
        message: 'Test message 1'
      },
      {
        phoneNumber: '4157654321',
        message: 'Test message 2'
      }
    ];

    createPushNotificationsJobs(jobs, queue);

    const createdJobs = queue.testMode.jobs;

    // Assert that jobs were created with correct data
    expect(createdJobs.length).to.equal(jobs.length);

    createdJobs.forEach((job, index) => {
      const expectedJobData = jobs[index];
      expect(job.type).to.equal('push_notification_code_3');
      expect(job.data).to.deep.equal(expectedJobData);
    });
  });
});
