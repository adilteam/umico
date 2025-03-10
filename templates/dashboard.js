document.addEventListener('DOMContentLoaded', () => {
    loadWidgets();
});

function loadWidgets() {
    const widgetsContainer = document.getElementById('widgets');
    // Burada widget-ların yüklənməsi və göstərilməsi təmin olunur
    fetchProductOffers();
}

function fetchProductOffers() {
    fetch('https://catalog-admin-web-stage.umico.az/api/v1/product_offers/upsert_collection', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'x-api-key': 'bc7cc0c7-d17c-420d-b838-ce63daaa6b7f'
        },
        body: JSON.stringify({
            product_offers: [
                {
                    payload: [
                        {
                            retail_price: 1854,
                            old_price: 2846,
                            quantity: 1,
                            maximum_installment_month: 18,
                            installment_enabled: true,
                            gtin: '194850877209',
                            discount_effective_start_date: '12.12.2024 0:00:00',
                            discount_effective_end_date: '12.12.2024 23:59:59'
                        }
                    ]
                }
            ]
        })
    })
    .then(response => response.json())
    .then(data => {
        // Məlumatları widget-lara əlavə edin
        console.log(data);
    })
    .catch(error => console.error('Error fetching product offers:', error));
}