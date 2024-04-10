import { firebase } from '../../config';
import 'firebase/database';

const database = firebase.database();

const deleteOrderById = (orderId) => {
  const orderRef = database.ref('Orders').child(orderId);
  orderRef.remove()
    .then(() => {
      console.log(`Order with ID ${orderId} deleted successfully.`);
    })
    .catch((error) => {
      console.error('Error removing order:', error);
    });
};

// Usage: Call this function with the ID of the order you want to delete
// deleteOrderById('your_order_id_here');
