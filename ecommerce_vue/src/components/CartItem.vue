<template>
	<tr>
		<td> <router-link :to='item.product.get_absolute_url'>  {{  item.product.name }} </router-link>   </td>

		<td> $ {{ item.product.price }} </td>

		<td> {{ item.quantity }} 
		<a @click='decremnentQuantity(item)'>-</a>
		<a @click='incrementQuantity(item)'>+</a>
		</td>


		<td> ${{ getItemTotal(item).toFixed(2) }} </td>
		<td> <button class='delete' @click='removeFormCart(item)'> </button></td>
	</tr>
</template>

<script>
export default {
	name: 'CartItem',
	props: {
		initialItem: Object
	},
	data() {
		return {
			item: this.initialItem
		}
	},
	methods: {
		getItemTotal(item) {
			return item.quantity * item.product.price
		},
		decremnentQuantity(item){
			item.quantity -= 1
			if (item.quantity === 0) {
				this.$emit('removeFormCart', item)
			}

		},
		incrementQuantity(item) {
			item.quantity += 1
			this.updateCart()
		},
		updateCart() {
			localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
		},
		removeFormCart(item) {
			this.$emit('removeFormCart' , item)

			this.updateCart()
		}

	}


}
	
</script>