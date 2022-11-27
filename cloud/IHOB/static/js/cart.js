console.log("Cart Javascript loaded")
var updateButtons = document.getElementsByClassName('update-cart')

for (let i = 0; i < updateButtons.length; i++) {
	updateButtons[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log()
		console.log(productId, 'Action:', action)
		console.log('User',user)
			showProductPage(productId, action)
		})}


function showProductPage(productId, action){
	console.log('User is authenticated, transferring data')

		var url = '/bid_click/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				//token from main page
				'X-CSRFToken':csrftoken,
			},
			body:JSON.stringify({'productId':productId, 'action':action})
		})

		.then((response) => {
		   return response.json();

		})
		.then((data) => {
			console.log('data',data)
			location.reload()
		});
}
