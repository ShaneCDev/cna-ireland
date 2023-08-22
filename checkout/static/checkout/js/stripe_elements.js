// var stripePublicKey = document.getElementById('id_stripe_public_key').textContent.slice(1, -1);
// var clientSecret = document.getElementById('id_client_secret').textContent.slice(1, -1);
// var stripe = Stripe(stripePublicKey);
// var elements = stripe.elements();
// var style = {
//     base: {
//         color: '#000',
//         fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
//         fontSmoothing: 'antialiased',
//         fontSize: '16px',
//         '::placeholder': {
//             color: '#aab7c4'
//         }
//     },
//     invalid: {
//         color: '#dc3545',
//         iconColor: '#dc3545'
//     }
// };
// var card = elements.create('card', { style: style });
// card.mount('#card-element');

// card.addEventListener('change', function(event) {
//     var errorDiv = document.getElementById('card-errors');
//     if (event.error) {
//         var html = `
//             <span class="icon" role="alert">
//                 <i class="fas fa-times"></i>
//             </span>
//             <span>${event.error.message}</span>
//         `;
//         errorDiv.innerHTML = html;
//     } else {
//         errorDiv.textContent = '';
//     }
// });

// var form = document.getElementById('payment-form');

// form.addEventListener('submit', function(ev) {
//     console.log(clientSecret);
//     ev.preventDefault();
//     card.update({ 'disabled': true });
//     document.getElementById('submit-button').setAttribute('disabled', true);
//     document.getElementById('payment-form').style.display = 'none';
//     document.getElementById('loading-overlay').style.display = 'block';

//     var saveInfo = document.getElementById('id-save-info').checked;
//     // var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
//     // var csrfToken = "{{ csrf_token }}";
//     console.log("CSRF:", csrfToken);
//     var postData = {
//         'csrfmiddlewaretoken': csrfToken,
//         'client_secret': clientSecret,
//         'save_info': saveInfo,
//     };
//     var url = '/checkout/cache_checkout_data/';
//     console.log(JSON.stringify(postData));
//     fetch(url, {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRFToken': csrfToken,
//         },
//         body: JSON.stringify(postData),
//     }).then(function () {
//         return stripe.confirmCardPayment(clientSecret, {
//             payment_method: {
//                 card: card,
//                 billing_details: {
//                     name: form.full_name.value.trim(),
//                     phone: form.phone_number.value.trim(),
//                     email: form.email.value.trim(),
//                     address: {
//                         line1: form.street_address1.value.trim(),
//                         line2: form.street_address2.value.trim(),
//                         city: form.town_or_city.value.trim(),
//                         country: form.country.value.trim(),
//                         state: form.county.value.trim(),
//                     }
//                 }
//             },
//             shipping: {
//                 name: form.full_name.value.trim(),
//                 phone: form.phone_number.value.trim(),
//                 address: {
//                     line1: form.street_address1.value.trim(),
//                     line2: form.street_address2.value.trim(),
//                     city: form.town_or_city.value.trim(),
//                     country: form.country.value.trim(),
//                     postal_code: form.postcode.value.trim(),
//                     state: form.county.value.trim(),
//                 }
//             },
//         });
//     }).then(function (result) {
//         if (result.error) {
//             var errorDiv = document.getElementById('card-errors');
//             var html = `
//                 <span class="icon" role="alert">
//                 <i class="fas fa-times"></i>
//                 </span>
//                 <span>${result.error.message}</span>
//             `;
//             errorDiv.innerHTML = html
//             document.getElementById('payment-form').style.display = 'block';
//             document.getElementById('loading-overlay').style.display = 'none';
//             card.update({ 'disabled': false });
//             document.getElementById('submit-button').removeAttribute('disabled');
//         } else {
//             if (result.paymentIntent.status === 'succeeded') {
//                 form.submit();
//             }
//         }
//     }).catch(function () {
//         location.reload();
//     });
// });

var stripePublicKey = document.getElementById('id_stripe_public_key').innerText;
var clientSecret = document.getElementById('id_client_secret').innerText;
console.log(stripePublicKey);
var stripe = Stripe(stripePublicKey);

var elements = stripe.elements();

var card = elements.create('card');
card.mount('#card-element');

card.addEventListener('change', function(event) {
    if (event.error) {
        document.getElementById('card-errors').innerHTML = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
    } else {
        document.getElementById('card-errors').innerHTML = '';
    }
});

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();

    var saveInfo = Boolean(document.getElementById('id-save-info').checked);

    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    }
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function() {
        var paymentIntent = stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: document.getElementById('full_name').value,
                    phone: document.getElementById('phone_number').value,
                    email: document.getElementById('email').value,
                    address: {
                        line1: document.getElementById('street_address1').value,
                        line2: document.getElementById('street_address2').value,
                        city: document.getElementById('town_or_city').value,
                        country: document.getElementById('country').value,
                        state: document.getElementById('county').value,
                    }
                }
            },
            shipping: {
                name: document.getElementById('full_name').value,
                phone: document.getElementById('phone_number').value,
                address: {
                    line1: document.getElementById('street_address1').value,
                    line2: document.getElementById('street_address2').value,
                    city: document.getElementById('town_or_city').value,
                    country: document.getElementById('country').value,
                    postal_code: document.getElementById('postcode').value,
                    state: document.getElementById('county').value,
                }
            },
        });

        paymentIntent.then(function(result) {
            if (result.error) {
                document.getElementById('card-errors').innerHTML = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>
                `;
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        location.reload();
    });
});