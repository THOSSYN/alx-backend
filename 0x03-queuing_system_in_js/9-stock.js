const listProducts = [
  {
    "id": 1,
    "name": "Suitcase 250",
    "price": 50,
    "stock": 4,
  },
  {
    "id": 2,
    "name": "Suitcase 450",
    "price": 100,
    "stock": 10,
  },
  {
    "id": 3,
    "name": "Suitcase 650",
    "price": 350,
    "stock": 2,
  },
  {
    "id": 4,
    "name": "Suitcase 1050",
    "price": 550,
    "stock": 5,
  }
];

const express = require('express');
const app = express();
const redis = require('redis');
const client = redis.createClient();
const { promisify } = require('util');

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);
const port = 1245;

function getItemById(id) {
  const itemById = listProducts.find((item) => item.id === parseInt(id));
  return itemById;
}

async function reserveStockById(itemId, stock) {
  console.log('Stock value:', stock); // Add this line to check the value of stock
  await setAsync(`item:${itemId}`, stock);
  await setAsync(`reserved_item:${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const reservedStock = await getAsync(`reserved_item:${itemId}`);
  return reservedStock ? parseInt(reservedStock) : 0;
}

app.get('/list_products', (req, res) => {
  res.status(200).json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const reservedStock = await getCurrentReservedStockById(itemId);
  const item = getItemById(itemId);
  if (item) {
    const productWithReservedStock = { ...item, reservedStock };
    res.status(200).json(productWithReservedStock);
  } else {
    res.status(404).json({ status: 'Product not found' });
  }
});

app.get('/reserve_product/:itemId', (req, res) => {
  const { itemId } = req.params;
  const item = getItemById(parseInt(itemId));

  if (!item) {
    res.status(404).json({ status: "Product not found" });
  } else {
    if (item.stock >= 1) {
      res.status(200).json({ status: "Reservation confirmed","itemId": `${itemId}` });
    } else {
      res.json({ status: "Not enough stock available", "itemId": `${itemId}` });
    }
  }
});

const server = app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});
