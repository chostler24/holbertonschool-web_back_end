// 0-redis_client.js module

import redis from 'redis';

// Configure Redis connection
const redisClient = redis.createClient();

// Listen for connection event
redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Listen for error event
redisClient.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

const setNewSchool = (schoolName, value) => {
  redisClient.set(schoolName, value, redis.print);
}

const displaySchoolValue = (schoolName) => {
  redisClient.get(schoolName, (err, reply) => {
    if (err) {
      console.error('Error retrieving value from Redis:', err);
    } else {
      console.log(`Value for key '${schoolName}': ${reply}`);
    }
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
