const API_BASE = "http://localhost:8003/api/v1/orders";
const output = document.getElementById("output");

function show(data) {
  output.textContent = JSON.stringify(data, null, 2);
}

/* CREATE ORDER */
async function createOrder() {
  const userId = document.getElementById("userId").value;
  const productId = document.getElementById("productId").value;
  const quantity = document.getElementById("quantity").value;

  try {
    const res = await fetch(API_BASE, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        userId: Number(userId),
        productId: Number(productId),
        quantity: Number(quantity),
      }),
    });

    const data = await res.json();
    show(data);
  } catch (err) {
    show({ error: err.message });
  }
}

/* LIST ORDERS BY USER */
async function listOrders() {
  const userId = document.getElementById("listUserId").value;

  try {
    const res = await fetch(`${API_BASE}/user/${userId}`);
    const data = await res.json();
    show(data);
  } catch (err) {
    show({ error: err.message });
  }
}
