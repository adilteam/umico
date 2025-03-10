function loadProductOfferWidget(data) {
    const widget = document.createElement('div');
    widget.classList.add('widget');
    widget.innerHTML = `
        <h2>Product Offer</h2>
        <ul>
            <li>Retail Price: $<span class="retail-price">${data.retail_price}</span></li>
            <li>Old Price: $<span class="old-price">${data.old_price}</span></li>
            <li>Quantity: <span class="quantity">${data.quantity}</span></li>
            <li>Installment Enabled: <span class="installment-enabled">${data.installment_enabled}</span></li>
        </ul>
    `;
    document.getElementById('widgets').appendChild(widget);
}