// 6-job_creator module

const kue = require('kue');
const queue = kue.createQueue();

const jobData = {
  phoneNumber: '1234567890',
  message: "Hello, we have been trying to reach you regarding your car's extended warranty!",
};

const pushNotificationQueue = queue.create('push_notification_code', jobData);

pushNotificationQueue.save(function (error) {
  if (error) {
    console.error('Failed to save job:', error);
  } else {
    console.log(`Notification job created: ${pushNotificationQueue.id}`);
  }
});
