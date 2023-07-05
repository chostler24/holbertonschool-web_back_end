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
