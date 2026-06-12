// ecommerce/static/js/cart.js

function getCSRFToken() {
    const cookieValue = document.cookie.match('(^|;)\\s*csrftoken\\s*=\\s*([^;]+)');
    return cookieValue ? cookieValue.pop() : '';
}

// Add to Cart
async function addToCart(productId, quantity = 1) {
    try {
        const response = await fetch('/cart/add/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken(),
            },
            body: JSON.stringify({
                product_id: productId,
                quantity: quantity
            })
        });

        const data = await response.json();

        if (data.success) {
            showToast(data.message || 'Added to cart', 'success');
            updateCartCount(data.cart_count);
        } else {
            showToast(data.error || 'Failed to add item', 'error');
        }

    } catch (error) {
        console.error(error);
        showToast('Error adding to cart', 'error');
    }
}

// Update / Remove Cart Item
async function updateCartItem(itemId, action, quantity = null) {
    try {
        const response = await fetch('/cart/update/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken(),
            },
            body: JSON.stringify({
                item_id: itemId,
                action: action,
                quantity: quantity
            })
        });

        // Debugging
        const responseText = await response.text();
        console.log('Server Response:', responseText);

        let data;

        try {
            data = JSON.parse(responseText);
        } catch (e) {
            console.error('Invalid JSON:', responseText);
            showToast('Server returned invalid response', 'error');
            return;
        }

        if (!response.ok) {
            showToast(data.error || 'Server Error', 'error');
            return;
        }

        if (data.success) {

            updateCartCount(data.cart_count);

            if (action === 'remove') {
                const row = document.getElementById(`cart-item-${itemId}`);
                if (row) {
                    row.remove();
                }
                showToast('Item removed from cart', 'success');
            } else {
                showToast('Cart updated', 'success');
            }

            const totalElement = document.getElementById('cart-total');
            if (totalElement) {
                totalElement.innerHTML = `<strong>₹${data.total_price}</strong>`;
            }

            if (data.cart_empty) {
                location.reload();
            }

        } else {
            showToast(data.error || 'Update failed', 'error');
        }

    } catch (error) {
        console.error(error);
        showToast('Error updating cart', 'error');
    }
}

// Event Listeners
document.addEventListener('DOMContentLoaded', () => {

    // Add To Cart Buttons
    document.querySelectorAll('.add-to-cart-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();

            const productId = btn.dataset.productId;
            const quantity = btn.dataset.quantity
                ? parseInt(btn.dataset.quantity)
                : 1;

            addToCart(productId, quantity);
        });
    });

    // Increase Quantity
    document.querySelectorAll('.increment-qty').forEach(btn => {
        btn.addEventListener('click', () => {

            const itemId = btn.dataset.itemId;
            const input = document.getElementById(`qty-${itemId}`);

            let qty = parseInt(input.value);
            qty++;

            input.value = qty;

            updateCartItem(itemId, 'update', qty);
        });
    });

    // Decrease Quantity
    document.querySelectorAll('.decrement-qty').forEach(btn => {
        btn.addEventListener('click', () => {

            const itemId = btn.dataset.itemId;
            const input = document.getElementById(`qty-${itemId}`);

            let qty = parseInt(input.value);
            qty--;

            if (qty > 0) {
                input.value = qty;
                updateCartItem(itemId, 'update', qty);
            } else {
                updateCartItem(itemId, 'remove');
            }
        });
    });

    // Remove Button
    document.querySelectorAll('.remove-item').forEach(btn => {
        btn.addEventListener('click', () => {

            const itemId = btn.dataset.itemId;

            if (confirm('Remove this item from cart?')) {
                updateCartItem(itemId, 'remove');
            }
        });
    });

});