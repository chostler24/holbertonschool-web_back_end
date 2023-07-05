// 2-redis_client.js module

import redis from 'redis';
import { promisify } from 'util';

// Configure Redis connection
const redisClient = redis.createClient();
const getAsync = promisify(redisClient.get).bind(redisClient);

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

async function displaySchoolValue(schoolName) {
    try {
      const value = await getAsync(schoolName);
      console.log(`Value for key '${schoolName}': ${value}`);
    } catch (error) {
      console.error('Error retrieving value from Redis:', error);
    }
  }

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
